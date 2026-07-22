#!/usr/bin/env python3
"""Find publications missing a `url_code` link and auto-discover code repositories.

Scans every `content/publication/<slug>/index.md`, finds entries with no
`url_code:` front-matter field, and tries to discover the official code repo by:

  1. Papers With Code API  (most authoritative - paper -> repository mapping)
  2. arXiv listing          (arXiv exposes a `<code>` link on the abstract page)
  3. GitHub Search API     (fallback: title + first-author surname)

A report is printed.  Use --write to insert discovered `url_code:` lines into
the front matter of the index.md files (a backup .bak is created first).

Usage:
    python3 scripts/find_missing_code.py                 # dry run: scan + report
    python3 scripts/find_missing_code.py --write         # apply discoveries
    python3 scripts/find_missing_code.py --pub <slug>    # scope to one pub
    python3 scripts/find_missing_code.py --manual        # list only unresolved
    python3 scripts/find_missing_code.py --json          # machine-readable report

Stdlib + beautifulsoup4 only (mirrors scripts/scholar_to_pubs.py).
"""

import argparse
import json
import os
import re
import ssl
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB_DIR = os.path.join(REPO_ROOT, "content", "publication")

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
PWC_BASE = "https://paperswithcode.com/api/v1"
GITHUB_API = "https://api.github.com/search/repositories"
ARXIV_ABS = "https://arxiv.org/abs"

_SSL = ssl.create_default_context()
_SSL.check_hostname = False
_SSL.verify_mode = ssl.CERT_NONE

# Names that map to the site owner (so we can prefer their GitHub orgs).
SELF_NAMES = {"alexander tong", "alex tong", "a tong", "tong, alexander", "tong, a"}
SELF_GH_ORGS = {"KrishnaswamyLab", "atong01", "sophtang"}


# ---------------------------------------------------------------------------
# Network helpers
# ---------------------------------------------------------------------------
def fetch(url, timeout=30, headers=None):
    h = {"User-Agent": UA}
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, headers=h)
    return urllib.request.urlopen(req, timeout=timeout, context=_SSL).read()


def fetch_json(url, timeout=30, headers=None):
    raw = fetch(url, timeout=timeout, headers=headers)
    return json.loads(raw.decode("utf-8", "replace"))


# ---------------------------------------------------------------------------
# Front-matter helpers (no PyYAML - keep parity with scholar_to_pubs.py)
# ---------------------------------------------------------------------------
def parse_front_matter(text):
    """Return (fm_dict, fm_text, body_text). fm_dict is a flat best-effort dict."""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.S)
    if not m:
        return {}, "", text
    fm_text, body = m.group(1), m.group(2)
    d = {}
    for line in fm_text.splitlines():
        kv = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if kv:
            d[kv.group(1)] = kv.group(2).strip()
    return d, fm_text, body


def has_url_code(fm_text):
    return bool(re.search(r"^url_code:\s*\S+", fm_text, re.M))


def get_field(fm_text, key):
    m = re.search(r"^%s:\s*(.+)$" % re.escape(key), fm_text, re.M)
    return m.group(1).strip().strip('"').strip("'") if m else None


def extract_arxiv_id(url):
    """Pull an arXiv id (e.g. 2408.14608 or 1905.10710) out of a URL/string."""
    if not url:
        return None
    m = re.search(r"(\d{4}\.\d{4,5}(v\d+)?)", url)
    if m:
        return m.group(1)
    m = re.search(r"(cs|stat|math|physics|q-bio)\.[A-Z]{2}/\d{7}", url)
    if m:
        return m.group(0)
    return None


def first_author_lastname(fm_dict):
    """Best-effort first author surname from authors field."""
    authors = fm_dict.get("authors", "")
    # Could be flow style [a, b] or block style. Grab the first name.
    m = re.match(r"^\[?\"?([^,\"'\]]+)", authors)
    if not m:
        return None
    name = m.group(1).strip()
    parts = name.split()
    return parts[-1] if parts else None


# ---------------------------------------------------------------------------
# Discovery backends
# ---------------------------------------------------------------------------
def discover_paperswithcode(arxiv_id, title):
    """Query Papers With Code for an official repository."""
    candidates = []
    # Try by arXiv id first.
    if arxiv_id:
        try:
            data = fetch_json("%s/papers/arxiv:%s/" % (PWC_BASE, arxiv_id))
            if data.get("arxiv_id"):
                for repo in (data.get("official_repository") and [data["official_repository"]] or []):
                    candidates.append((repo.get("url"), "pwc-official", 0.95))
                # Also check 'repos' link if present (requires a second call).
                for repo in data.get("repositories", []) or []:
                    candidates.append((repo.get("url"), "pwc-listed", 0.7))
        except Exception:
            pass
    # Fallback: search PWC by title.
    if not candidates and title:
        try:
            q = urllib.parse.quote(title[:200])
            data = fetch_json("%s/search/?q=%s" % (PWC_BASE, q))
            for r in data.get("results", []) or []:
                if r.get("type") == "paper":
                    paper = r.get("paper", {})
                    for repo in paper.get("repositories", []) or []:
                        candidates.append((repo.get("url"), "pwc-search", 0.6))
        except Exception:
            pass
    return candidates


def discover_arxiv_page(arxiv_id):
    """Scrape the arXiv abstract page for a code link."""
    if not arxiv_id:
        return []
    try:
        html = fetch("%s/%s" % (ARXIV_ABS, arxiv_id)).decode("utf-8", "replace")
        soup = BeautifulSoup(html, "html.parser")
        out = []
        # arXiv wraps code link in a <a> whose text is "Code" or "Code, Software".
        for a in soup.find_all("a", string=re.compile(r"(?i)\bcode\b")):
            href = a.get("href")
            if href:
                out.append((href, "arxiv-page", 0.85))
        # Some pages have a meta tag / cite-as with a code URL.
        for a in soup.select("a[href*='github.com']"):
            href = a.get("href")
            if href and "github.com" in href:
                out.append((href, "arxiv-page-github", 0.75))
        return out
    except Exception:
        return []


def discover_github(title, lastname):
    """GitHub Search API by title + first author surname."""
    if not title:
        return []
    # Use a trimmed title for the query.
    q = title.strip()
    if lastname:
        q = "%s %s" % (q, lastname)
    # Prefer repos from the site owner's orgs when possible.
    params = urllib.parse.urlencode({"q": q, "sort": "stars", "order": "desc"})
    try:
        data = fetch_json("%s?%s" % (GITHUB_API, params),
                          headers={"Accept": "application/vnd.github+json"})
        out = []
        for item in (data.get("items") or [])[:5]:
            url = item.get("html_url")
            owner = (item.get("owner") or {}).get("login", "")
            score = 0.5
            if owner in SELF_GH_ORGS:
                score = 0.9
            out.append((url, "github-search(%s)" % owner, score))
        return out
    except Exception:
        return []


def discover(fm_text, fm_dict):
    """Return list of (url, source, confidence) candidates, best first."""
    title = get_field(fm_text, "title")
    title = title.strip('"').strip("'") if title else None
    arxiv_id = None
    for k in ("url_pdf", "url_slides"):
        v = get_field(fm_text, k)
        if v:
            arxiv_id = extract_arxiv_id(v)
            if arxiv_id:
                break
    # Also check the links block for an arXiv url.
    if not arxiv_id:
        for m in re.finditer(r"url:\s*(.+)$", fm_text, re.M):
            aid = extract_arxiv_id(m.group(1))
            if aid:
                arxiv_id = aid
                break
    lastname = first_author_lastname(fm_dict)

    candidates = []
    candidates += discover_paperswithcode(arxiv_id, title)
    candidates += discover_arxiv_page(arxiv_id)
    candidates += discover_github(title, lastname)
    # De-dup by url, keep best confidence.
    seen = {}
    for url, src, conf in candidates:
        if url and url not in seen:
            seen[url] = (url, src, conf)
    return sorted(seen.values(), key=lambda c: -c[2])


# ---------------------------------------------------------------------------
# Write helper
# ---------------------------------------------------------------------------
def insert_url_code(path, url):
    """Insert `url_code: <url>` into the front matter, before the closing ---."""
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    m = re.match(r"^(---\s*\n)(.*?)(\n---\s*\n)", text, re.S)
    if not m:
        raise RuntimeError("could not parse front matter in %s" % path)
    head, fm, tail = m.group(1), m.group(2), m.group(3)
    # Backup.
    bak = path + ".bak"
    with open(bak, "w", encoding="utf-8") as fh:
        fh.write(text)
    # Insert just before the closing delimiter.
    addition = "\nurl_code: %s" % url
    new_fm = fm.rstrip() + addition + "\n"
    new_text = head + new_fm + tail + text[m.end():]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(new_text)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def scan_publications():
    """Yield (slug, path, fm_text, fm_dict) for every publication index.md."""
    for name in sorted(os.listdir(PUB_DIR)):
        d = os.path.join(PUB_DIR, name)
        if not os.path.isdir(d):
            continue
        idx = os.path.join(d, "index.md")
        if not os.path.exists(idx):
            continue
        with open(idx, "r", encoding="utf-8") as fh:
            text = fh.read()
        fm_dict, fm_text, _ = parse_front_matter(text)
        yield name, idx, fm_text, fm_dict


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true",
                    help="apply discovered url_code links (default: dry run)")
    ap.add_argument("--pub", default=None,
                    help="scope to a single publication slug")
    ap.add_argument("--manual", action="store_true",
                    help="list only pubs the script could not resolve")
    ap.add_argument("--json", action="store_true",
                    help="emit machine-readable JSON instead of a text report")
    ap.add_argument("--max-rate", type=float, default=1.0,
                    help="seconds to sleep between API calls (default 1.0)")
    args = ap.parse_args()

    missing = []
    for slug, path, fm_text, fm_dict in scan_publications():
        if args.pub and slug != args.pub:
            continue
        if has_url_code(fm_text):
            continue
        missing.append((slug, path, fm_text, fm_dict))

    print("Found %d publication(s) missing url_code." % len(missing),
          file=sys.stderr)

    results = []
    for i, (slug, path, fm_text, fm_dict) in enumerate(missing):
        title = (get_field(fm_text, "title") or slug).strip('"').strip("'")
        cands = discover(fm_text, fm_dict)
        best = cands[0] if cands else None
        results.append({
            "slug": slug,
            "title": title,
            "candidates": [{"url": u, "source": s, "confidence": c}
                           for u, s, c in cands],
            "best": ({"url": best[0], "source": best[1], "confidence": best[2]}
                     if best else None),
            "path": path,
        })
        if i < len(missing) - 1 and args.max_rate > 0:
            time.sleep(args.max_rate)

    # ---- Reporting ----
    if args.json:
        print(json.dumps(results, indent=2))
        return

    found = [r for r in results if r["best"]]
    unresolved = [r for r in results if not r["best"]]

    if args.manual:
        print("\n=== Unresolved (%d) - need manual lookup ===" % len(unresolved))
        for r in unresolved:
            print("\n- %s" % r["slug"])
            print("    title: %s" % r["title"])
        return

    print("\n=== Auto-discovered (%d) ===" % len(found))
    for r in found:
        b = r["best"]
        print("\n- %s" % r["slug"])
        print("    title : %s" % r["title"])
        print("    url   : %s" % b["url"])
        print("    source: %s (confidence %.2f)" % (b["source"], b["confidence"]))
        if args.write:
            insert_url_code(r["path"], b["url"])
            print("    >> APPLIED to %s" % r["path"])

    print("\n=== Needs manual lookup (%d) ===" % len(unresolved))
    for r in unresolved:
        print("\n- %s" % r["slug"])
        print("    title: %s" % r["title"])

    if args.write:
        print("\nApplied %d link(s); %d still need manual lookup."
              % (len(found), len(unresolved)))
    else:
        print("\nDry run only. Re-run with --write to apply discovered links.")


if __name__ == "__main__":
    main()
