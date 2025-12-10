---
# Documentation: https://docs.hugoblox.com/managing-content/

title: Curly Flow Matching for Learning Non-gradient Field Dynamics
subtitle: ''
summary: ''
authors:
- Katarina Petrović
- Lazar Atanackovic
- Viggo Moro
- Kacper Kapuśniak
- İsmail İlkan Ceylan
- Michael Bronstein
- Avishek Joey Bose
- admin
author_notes:
-
-
-
-
-
-
- Equal Contribution
- Equal Contribution
tags: []
date: '2025-12-04'
lastmod: 2025-12-10T00:00:00-04:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
publishDate: '2025-12-10T00:00:00.000000Z'
publication_types:
- 'paper-conference'
categories: ["archival"]
projects: [flow-matching]
abstract: "Modeling the transport dynamics of natural processes from population-level observations is a ubiquitous problem in the natural sciences. Such models rely on key assumptions about the underlying process in order to enable faithful learning of governing dynamics that mimic the actual system behavior. The de facto assumption in current approaches relies on the principle of least action that results in gradient field dynamics and leads to trajectories minimizing an energy functional between two probability measures. However, many real-world systems, such as cell cycles in single-cell RNA, are known to exhibit non-gradient, periodic behavior, which fundamentally cannot be captured by current state-of-the-art methods such as flow and bridge matching. In this paper, we introduce Curly Flow Matching (Curly-FM), a novel approach that is capable of learning non-gradient field dynamics by designing and solving a Schrödinger bridge problem with a non-zero drift reference process -- in stark contrast to typical zero-drift reference processes -- which is constructed using inferred velocities in addition to population snapshot data. We showcase Curly-FM by solving the trajectory inference problems for single cells, computational fluid dynamics, and ocean currents with approximate velocities. We demonstrate that Curly-FM can learn trajectories that better match both the reference process and population marginals. Curly-FM expands flow matching models beyond the modeling of populations and towards the modeling of known periodic behavior in physical systems."
publication: 'In *NeurIPS*'
publication_short: 'In *NeurIPS*'
links:
url_pdf: https://arxiv.org/abs/2510.26645
url_code: https://github.com/kpetrovicc/curly-flow-matching
---
