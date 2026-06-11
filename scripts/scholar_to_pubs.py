#!/usr/bin/env python3
"""Scrape recent publications from a Google Scholar profile and generate Hugo
Academic publication entries (index.md + cite.bib) for this website.

For each work on the Scholar profile that isn't already on the site, the script
looks the title up on arXiv (then OpenReview as a fallback) and uses *that*
canonical metadata -- full author list, abstract, date, stable link -- to build
the entry. Scholar is only used to discover the list of works.

Usage:
    python3 scripts/scholar_to_pubs.py                 # dry run, show what would be added
    python3 scripts/scholar_to_pubs.py --write         # actually create the folders
    python3 scripts/scholar_to_pubs.py --since 2025    # only works from 2025 onward
    python3 scripts/scholar_to_pubs.py --limit 5       # only the 5 most recent new works
    python3 scripts/scholar_to_pubs.py --user CS80pt4AAAAJ

Stdlib + beautifulsoup4 only (no requests/lxml needed).
"""

import argparse
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
DEFAULT_USER = "CS80pt4AAAAJ"

# Names that map to `admin` (the site owner) in author lists.
SELF_NAMES = {"alexander tong", "alex tong", "a tong", "tong, alexander", "tong, a"}

# Venue keywords that indicate an archival conference paper rather than a preprint.
CONFERENCE_KEYWORDS = [
    "conference", "proceedings", "symposium", "workshop", "neurips",
    "icml", "iclr", "aistats", "cvpr", "iccv", "eccv", "acl", "emnlp",
    "naacl", "kdd", "aaai", "ijcai", "uai", "tmlr", "journal", "transactions",
    "nature", "science", "cell", "bioinformatics", "plos",
]

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB_DIR = os.path.join(REPO_ROOT, "content", "publication")

ARXIV_NS = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"

_SSL = ssl.create_default_context()
_SSL.check_hostname = False
_SSL.verify_mode = ssl.CERT_NONE


# ---------------------------------------------------------------------------
# Small helpers
# ---------------------------------------------------------------------------
def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=timeout, context=_SSL).read()


def norm(text):
    """Normalize a title for fuzzy comparison."""
    return re.sub(r"[^a-z0-9]+", " ", (text or "").lower()).strip()


def clean_title(text):
    """Strip LaTeX artifacts Scholar leaves in titles (\\", \\^, {}, etc.) so
    they don't break the arXiv query or title matching."""
    text = re.sub(r'\\[\'"^`~=.]', "", text)  # accent escapes: \" \^ \' ...
    text = text.replace("{", "").replace("}", "").replace("\\", "")
    return re.sub(r"\s+", " ", text).strip()


def clean_venue(text):
    """Tidy the venue string Scholar provides: drop the trailing truncation
    ellipsis + redundant year, and convert LaTeX bits to plain text."""
    if not text:
        return ""
    text = text.replace("{\\&}", "&").replace("\\&", "&")
    text = text.replace("{", "").replace("}", "").replace("\\", "")
    text = re.sub(r"\s*[,]?\s*[…\.]{1,}\s*,?\s*\d{0,4}\s*$", "", text)  # "… , 2026"
    text = re.sub(r",\s*\d{4}\s*$", "", text)  # trailing ", 2026"
    return re.sub(r"\s+", " ", text).strip()


def jaccard(a, b):
    sa, sb = set(norm(a).split()), set(norm(b).split())
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / len(sa | sb)


def titles_match(a, b):
    """True if two titles refer to the same work. Loose enough to bridge
    Scholar/arXiv punctuation differences, strict enough to avoid matching an
    unrelated paper (guarded further by the author check at the call site)."""
    na, nb = norm(a), norm(b)
    if not na or not nb:
        return False
    if na == nb:
        return True
    # One fully contains the other (e.g. "SE(3)-Stochastic Flow..." vs "Stochastic Flow...").
    if (na in nb or nb in na) and jaccard(a, b) >= 0.5:
        return True
    return jaccard(a, b) >= 0.8


def last_name(full):
    """Best-effort surname extraction from 'First Last' or 'Last, First'."""
    full = full.strip()
    if "," in full:
        return full.split(",")[0].strip()
    parts = full.split()
    return parts[-1] if parts else full


def is_self(name):
    n = name.lower().strip()
    if n in SELF_NAMES:
        return True
    # Handle "A. Tong" / "Alexander G. Tong" style.
    parts = n.replace(".", "").split()
    return len(parts) >= 2 and parts[-1] == "tong" and parts[0][0] == "a"


def slugify_folder(authors, year, title):
    """lastname-YYYY-titlewords (academic-cli style: concatenated, alnum only)."""
    first = last_name(authors[0]) if authors else "anon"
    first = re.sub(r"[^a-z0-9]", "", first.lower())
    words = re.sub(r"[^a-z0-9 ]", " ", title.lower()).split()
    stop = {"a", "an", "the", "of", "for", "and", "to", "in", "on", "with", "via"}
    sig = [w for w in words if w not in stop][:6]
    slug = "".join(sig)[:40] or "untitled"
    return f"{first}-{year}-{slug}"


# ---------------------------------------------------------------------------
# Scholar profile parsing
# ---------------------------------------------------------------------------
def scholar_works(user):
    url = ("https://scholar.google.com/citations?" +
           urllib.parse.urlencode({"hl": "en", "user": user,
                                    "view_op": "list_works", "sortby": "pubdate",
                                    "cstart": 0, "pagesize": 100}))
    soup = BeautifulSoup(fetch(url), "html.parser")
    works = []
    for row in soup.select("tr.gsc_a_tr"):
        a = row.select_one(".gsc_a_at")
        if not a:
            continue
        grays = [g.get_text(strip=True) for g in row.select(".gs_gray")]
        yr = row.select_one(".gsc_a_y span")
        works.append({
            "title": a.get_text(strip=True),
            "authors_short": grays[0] if grays else "",
            "venue": grays[1] if len(grays) > 1 else "",
            "year": yr.get_text(strip=True) if yr else "",
        })
    return works


# ---------------------------------------------------------------------------
# arXiv / OpenReview lookups
# ---------------------------------------------------------------------------
def arxiv_lookup(title):
    url = ("https://export.arxiv.org/api/query?" +
           urllib.parse.urlencode({"search_query": 'ti:"%s"' % title, "max_results": 5}))
    root = ET.fromstring(fetch(url))
    for e in root.findall("a:entry", ARXIV_NS):
        t = (e.find("a:title", ARXIV_NS).text or "").strip()
        if not titles_match(t, title):
            continue
        abs_id = e.find("a:id", ARXIV_NS).text.strip()
        arxiv_id = re.sub(r"^https?://arxiv\.org/abs/", "", abs_id)
        arxiv_id = re.sub(r"v\d+$", "", arxiv_id)
        prim = e.find("arxiv:primary_category", ARXIV_NS)
        return {
            "source": "arxiv",
            "title": " ".join(t.split()),
            "authors": [a.find("a:name", ARXIV_NS).text.strip() for a in e.findall("a:author", ARXIV_NS)],
            "date": e.find("a:published", ARXIV_NS).text.strip()[:10],
            "abstract": " ".join((e.find("a:summary", ARXIV_NS).text or "").split()),
            "url": "https://arxiv.org/abs/%s" % arxiv_id,
            "arxiv_id": arxiv_id,
            "primary": prim.get("term", "") if prim is not None else "",
        }
    return None


def openreview_lookup(title):
    for api in ("https://api2.openreview.net", "https://api.openreview.net"):
        try:
            url = api + "/notes/search?" + urllib.parse.urlencode(
                {"term": title, "content": "all", "limit": 5})
            import json
            notes = json.loads(fetch(url)).get("notes", [])
        except Exception:
            continue
        for n in notes:
            c = n.get("content", {})

            def val(k):
                v = c.get(k)
                return v.get("value") if isinstance(v, dict) else v

            t = val("title") or ""
            if not titles_match(t, title):
                continue
            authors = val("authors") or []
            abstract = val("abstract") or ""
            cdate = n.get("cdate")
            date = ""
            if cdate:
                # cdate is epoch ms; format without Date.now-style helpers.
                date = time.strftime("%Y-%m-%d", time.gmtime(cdate / 1000))
            return {
                "source": "openreview",
                "title": " ".join(t.split()),
                "authors": authors,
                "date": date,
                "abstract": " ".join(abstract.split()),
                "url": "https://openreview.net/forum?id=%s" % n.get("id"),
                "arxiv_id": "",
                "primary": "",
            }
    return None


# ---------------------------------------------------------------------------
# Entry generation
# ---------------------------------------------------------------------------
def existing_index():
    """Scan the site once and return everything we need to dedupe against:
    a list of normalized titles and sets of arXiv / OpenReview ids already used."""
    titles, arxiv_ids, openreview_ids = [], set(), set()
    if not os.path.isdir(PUB_DIR):
        return titles, arxiv_ids, openreview_ids
    for name in os.listdir(PUB_DIR):
        idx = os.path.join(PUB_DIR, name, "index.md")
        if not os.path.isfile(idx):
            continue
        text = open(idx, encoding="utf-8").read()
        m = re.search(r'^title:\s*[\'"]?(.+?)[\'"]?\s*$', text, re.MULTILINE)
        if m:
            titles.append(norm(m.group(1)))
        for aid in re.findall(r"arxiv\.org/abs/([0-9]+\.[0-9]+)", text):
            arxiv_ids.add(aid)
        for oid in re.findall(r"openreview\.net/forum\?id=([\w-]+)", text):
            openreview_ids.add(oid)
    return titles, arxiv_ids, openreview_ids


def already_on_site(meta, ex_titles, ex_arxiv, ex_openreview):
    if meta.get("arxiv_id") and meta["arxiv_id"] in ex_arxiv:
        return True
    if meta["source"] == "openreview":
        oid = meta["url"].rsplit("=", 1)[-1]
        if oid in ex_openreview:
            return True
    return any(titles_match(meta["title"], t) for t in ex_titles)


def has_self_author(authors):
    return any(is_self(a) for a in authors)


def is_conference(venue):
    v = venue.lower()
    return any(k in v for k in CONFERENCE_KEYWORDS)


def map_authors(names):
    out = []
    for n in names:
        out.append("admin" if is_self(n) else n)
    return out


def yaml_author_list(authors):
    return "\n".join("- %s" % a for a in authors)


def build_entry(meta, venue):
    """Return (front_matter, cite_bib) strings."""
    venue = clean_venue(venue)
    conf = is_conference(venue)
    authors = map_authors(meta["authors"])
    year = meta["date"][:4] if meta["date"] else "2026"
    date = meta["date"] or "%s-01-01" % year

    if conf and venue:
        pub = "*%s*" % venue
        pub_short = pub
        pub_type = "paper-conference"
        category = "archival"
    else:
        pub = "*arXiv preprint*"
        pub_short = "*arXiv*"
        pub_type = "article"
        category = "preprint"

    # Escape for a YAML double-quoted scalar: backslash first, then quote.
    def yq(s):
        return s.replace("\\", "\\\\").replace('"', '\\"')

    abstract = yq(meta["abstract"])
    title = yq(meta["title"])

    links = ""
    if meta["source"] == "arxiv":
        links = ("links:\n- name: arXiv\n  url: %s\nurl_pdf: %s\n"
                 % (meta["url"], meta["url"]))
    else:
        links = ("links:\n- name: OpenReview\n  url: %s\nurl_pdf: %s\n"
                 % (meta["url"], meta["url"]))

    fm = f"""---
# Documentation: https://docs.hugoblox.com/managing-content/
# Generated by scripts/scholar_to_pubs.py -- review before publishing.

title: "{title}"
subtitle: ''
summary: ''
authors:
{yaml_author_list(authors)}
author_notes: []
tags: []
date: '{date}'
lastmod: '{date}'
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: ''
  focal_point: ''
  preview_only: false

publishDate: '{date}T00:00:00.000000Z'
publication_types:
- '{pub_type}'
categories: ["{category}"]
abstract: "{abstract}"
publication: '{pub}'
publication_short: '{pub_short}'
{links}---
"""

    # cite.bib
    key = "%s%s%s" % (
        re.sub(r"[^a-z]", "", (last_name(meta["authors"][0]) if meta["authors"] else "anon").lower()),
        year,
        re.sub(r"[^a-z0-9]", "", meta["title"].split()[0].lower()) if meta["title"] else "",
    )
    bib_authors = " and ".join(meta["authors"])
    if conf and venue:
        bib = (f"@inproceedings{{{key},\n"
               f"  title={{{meta['title']}}},\n"
               f"  author={{{bib_authors}}},\n"
               f"  booktitle={{{venue}}},\n"
               f"  year={{{year}}}\n}}\n")
    elif meta["source"] == "arxiv":
        bib = (f"@misc{{{key},\n"
               f"  title={{{meta['title']}}},\n"
               f"  author={{{bib_authors}}},\n"
               f"  year={{{year}}},\n"
               f"  eprint={{{meta['arxiv_id']}}},\n"
               f"  archivePrefix={{arXiv}},\n"
               + (f"  primaryClass={{{meta['primary']}}},\n" if meta["primary"] else "")
               + f"  url={{{meta['url']}}}\n}}\n")
    else:
        bib = (f"@misc{{{key},\n"
               f"  title={{{meta['title']}}},\n"
               f"  author={{{bib_authors}}},\n"
               f"  year={{{year}}},\n"
               f"  url={{{meta['url']}}}\n}}\n")
    return fm, bib


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--user", default=DEFAULT_USER, help="Google Scholar user id")
    ap.add_argument("--since", type=int, default=0, help="only works from this year onward")
    ap.add_argument("--limit", type=int, default=0, help="max number of new works to process")
    ap.add_argument("--write", action="store_true", help="actually create folders (default: dry run)")
    args = ap.parse_args()

    print("Fetching Scholar profile for %s ..." % args.user)
    try:
        works = scholar_works(args.user)
    except Exception as e:
        sys.exit("ERROR: could not fetch/parse Scholar profile: %s" % e)
    print("Found %d works on the profile.\n" % len(works))

    ex_titles, ex_arxiv, ex_openreview = existing_index()
    created, skipped_existing, skipped_old, not_found, no_self = 0, 0, 0, [], []

    for w in works:
        if args.limit and created >= args.limit:
            break
        title = clean_title(w["title"])

        # Pre-filter on Scholar's year (loose; it reflects activity, not the
        # real publication date). The authoritative date check happens after
        # lookup below.
        try:
            scholar_year = int(w["year"])
        except ValueError:
            scholar_year = 0
        if args.since and scholar_year and scholar_year < args.since - 1:
            continue

        # Skip works whose Scholar title already matches something on the site
        # before spending a network call.
        if any(titles_match(title, t) for t in ex_titles):
            skipped_existing += 1
            continue

        print("• %s [%s]" % (title, w["year"]))
        meta = None
        try:
            meta = arxiv_lookup(title)
            time.sleep(3)  # be polite to the arXiv API
        except Exception as e:
            print("    arXiv lookup error: %s" % e)
        if not meta:
            try:
                meta = openreview_lookup(title)
            except Exception as e:
                print("    OpenReview lookup error: %s" % e)
        if not meta:
            print("    -> not found on arXiv or OpenReview, skipping")
            not_found.append(title)
            continue

        # Guard: every entry on this site lists the owner as an author. If the
        # matched record doesn't, it's the wrong paper (false-positive match).
        if not has_self_author(meta["authors"]):
            print("    -> matched record has no '%s' author, skipping as false positive"
                  % "Tong")
            no_self.append(title)
            continue

        # Authoritative date filter, using the real publication date.
        real_year = int(meta["date"][:4]) if meta["date"][:4].isdigit() else 0
        if args.since and real_year and real_year < args.since:
            print("    -> published %s, before --since %d, skipping" % (meta["date"], args.since))
            skipped_old += 1
            continue

        # Robust dedup by arXiv / OpenReview id (and fuzzy title).
        if already_on_site(meta, ex_titles, ex_arxiv, ex_openreview):
            print("    -> already on site (%s), skipping" % meta["url"])
            skipped_existing += 1
            continue

        folder = slugify_folder(meta["authors"], (meta["date"][:4] or w["year"]), meta["title"])
        dest = os.path.join(PUB_DIR, folder)
        fm, bib = build_entry(meta, w["venue"])

        print("    source: %s | %s | %d authors | -> content/publication/%s/"
              % (meta["source"], meta["url"], len(meta["authors"]), folder))

        if args.write:
            if os.path.exists(dest):
                print("    !! folder already exists, skipping write")
            else:
                os.makedirs(dest)
                with open(os.path.join(dest, "index.md"), "w", encoding="utf-8") as fh:
                    fh.write(fm)
                with open(os.path.join(dest, "cite.bib"), "w", encoding="utf-8") as fh:
                    fh.write(bib)
                print("    written.")
        created += 1

    print("\n%s" % ("=" * 60))
    print("New entries %s: %d" % ("written" if args.write else "to add (dry run)", created))
    print("Skipped (already on site): %d" % skipped_existing)
    print("Skipped (older than --since): %d" % skipped_old)
    if no_self:
        print("Skipped (no matching author, likely false match): %d" % len(no_self))
        for t in no_self:
            print("   - %s" % t)
    if not_found:
        print("Not found on arXiv/OpenReview (%d):" % len(not_found))
        for t in not_found:
            print("   - %s" % t)
    if not args.write and created:
        print("\nRe-run with --write to create these folders.")
        print("Generated entries have featured:false and empty subtitle/summary -- review each one.")


if __name__ == "__main__":
    main()
