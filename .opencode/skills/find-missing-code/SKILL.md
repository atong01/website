---
name: find-missing-code
description: Find publications missing code links and auto-discover repositories via Papers With Code, arXiv, and GitHub
version: 1.0.0
author: opencode
type: skill
category: content
tags:
  - publications
  - code-links
  - hugo
  - discovery
---

# Find Missing Code Links

> **Purpose**: Scan Hugo publication entries for missing `url_code` front-matter
> fields and auto-discover the corresponding code repositories.

---

## What I Do

I find publication entries in `content/publication/` that are missing a `url_code:`
link and attempt to discover the official code repository for each one using three
discovery backends:

1. **Papers With Code API** — the most authoritative source (paper → repository mapping)
2. **arXiv abstract page** — scrapes the "Code" link that arXiv exposes
3. **GitHub Search API** — fallback search by paper title + first-author surname

I produce a report of auto-discovered links (with confidence scores) and a list of
publications that need **manual lookup**. Discovered links can be written directly
into the front matter with a single flag.

---

## How to Use Me

### Quick Start

```bash
# Dry run: scan all pubs, attempt discovery, print report
.venv/bin/python scripts/find_missing_code.py

# Apply discovered links (creates .bak backups)
.venv/bin/python scripts/find_missing_code.py --write

# Scope to a single publication
.venv/bin/python scripts/find_missing_code.py --pub <slug>

# List only pubs needing manual lookup
.venv/bin/python scripts/find_missing_code.py --manual

# Machine-readable JSON output
.venv/bin/python scripts/find_missing_code.py --json
```

### Command Reference

| Flag | Description |
|------|-------------|
| (none) | Dry run: scan + discover + report (no files changed) |
| `--write` | Apply discovered `url_code` links to index.md files |
| `--pub <slug>` | Scope to a single publication folder name |
| `--manual` | List only pubs the script could not resolve |
| `--json` | Emit JSON instead of text report |
| `--max-rate <sec>` | Seconds to sleep between API calls (default 1.0) |

---

## Confidence Scoring

Each discovered link carries a confidence score to help you decide what to trust:

| Score | Source | Meaning |
|-------|--------|---------|
| 0.95 | `pwc-official` | Papers With Code "official repository" badge |
| 0.90 | `github-search(<org>)` | GitHub repo owned by a known lab org (KrishnaswamyLab, atong01, sophtang) |
| 0.85 | `arxiv-page` | "Code" link scraped directly from the arXiv abstract page |
| 0.75 | `arxiv-page-github` | Any github.com link found on the arXiv abstract page |
| 0.70 | `pwc-listed` | Papers With Code community-listed (non-official) repository |
| 0.60 | `pwc-search` | Papers With Code title-search result |
| 0.50 | `github-search(<user>)` | GitHub Search API match (unknown owner) |

**Rule of thumb**: links at 0.75+ are usually correct. Links at 0.50 should be
verified before applying with `--write`.

---

## Workflow

### 1. Run discovery (dry run)

```bash
.venv/bin/python scripts/find_missing_code.py
```

Review the output:
- **Auto-discovered** section: links found automatically, sorted by confidence.
- **Needs manual lookup** section: pubs where no code repo was found.

### 2. Provide manual links

For pubs in the "needs manual lookup" section, find the code repo yourself
(e.g. check the paper PDF, ask the author) and apply with:

```bash
# Option A: edit the index.md directly, adding a url_code: line in the front matter
# Option B: use the script scoped to that pub (it will re-attempt discovery):
.venv/bin/python scripts/find_missing_code.py --pub <slug> --write
```

### 3. Apply discovered links

```bash
.venv/bin/python scripts/find_missing_code.py --write
```

This inserts `url_code: <url>` into the front matter of each index.md file where
a link was discovered. A `.bak` backup is created for every modified file.

### 4. Verify

```bash
git diff content/publication/
```

Review the changes, then commit when satisfied.

---

## When to Run

- **After adding new publications** via `scripts/scholar_to_pubs.py` — new entries
  won't have code links yet.
- **Periodic audit** — some older pubs may have acquired code repos since the last run.
- **After a new code release** — re-run for a specific pub to pick up newly available repos.

---

## Discovery Backends (Detail)

### 1. Papers With Code (`paperswithcode.com/api/v1`)

Queries the PWC API by arXiv id (preferred) or title search. Returns official and
community-listed repositories. This is the most reliable source when available.

### 2. arXiv Abstract Page

Scrapes `arxiv.org/abs/<id>` for links labeled "Code" or any `github.com` link.
Many papers list their code repo directly on the arXiv page.

### 3. GitHub Search API

Searches `api.github.com/search/repositories` by the paper title + first-author
surname. Repos owned by known lab orgs (KrishnaswamyLab, atong01, sophtang) get a
confidence boost. This is the least reliable backend — results should be verified.

---

## Architecture

```
scripts/
└── find_missing_code.py        # The script (run with the project venv)

.opencode/skills/find-missing-code/
└── SKILL.md                    # This documentation
```

### Dependencies

- **Python 3.11+** (use the project venv: `.venv/bin/python`)
- **beautifulsoup4** (already in the venv, shared with `scholar_to_pubs.py`)
- No other external packages — uses stdlib `urllib`, `json`, `re`, `ssl`

### Front-Matter Format

The script parses Hugo front matter without PyYAML (matching the convention in
`scholar_to_pubs.py`). It inserts `url_code:` just before the closing `---`:

```yaml
---
title: "..."
...
url_pdf: https://arxiv.org/abs/XXXX.XXXXX
url_code: https://github.com/OrgName/RepoName    # <-- inserted here
---
```

---

## Known Lab Orgs

The script boosts confidence for repos owned by these GitHub organizations
(associated with the site owner):

- `KrishnaswamyLab`
- `atong01`
- `sophtang`

To add more, edit `SELF_GH_ORGS` in `scripts/find_missing_code.py`.

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'bs4'"

Use the project venv: `.venv/bin/python scripts/find_missing_code.py`

### "Could not parse front matter"

The `index.md` file doesn't have standard `---` delimited front matter. Check the
file manually.

### GitHub API rate limit

The unauthenticated GitHub Search API allows 10 requests/minute. If you hit a
rate limit, increase `--max-rate` or run `--pub` for individual publications.

### Papers With Code returns nothing

Not all papers are indexed on PWC. The script falls through to arXiv and GitHub
backends automatically.

---

## Companion Script

`scripts/scholar_to_pubs.py` — discovers *new* publications from a Google Scholar
profile and creates Hugo entries. Run `find_missing_code.py` afterward to fill in
code links for any entries the scholar script created without them.

---

**Find Missing Code Skill** — Keep your publication code links up to date!
