---
# Documentation: https://docs.hugoblox.com/managing-content/

title: Amortized Sampling with Transferable Normalizing Flows
subtitle: ''
summary: ''
authors:
- Charlie B. Tan
- Majdi Hassan
- Leon Klein
- Saifuddin Syed
- Dominique Beaini
- Michael M. Bronstein
- admin
- Kirill Neklyudov
author_notes:
- Equal Contribution
- Equal Contribution
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
abstract: 'Efficient equilibrium sampling of molecular conformations remains a core challenge in computational chemistry and statistical inference. Classical approaches such as molecular dynamics or Markov chain Monte Carlo inherently lack amortization; the computational cost of sampling must be paid in full for each system of interest. The widespread success of generative models has inspired interest towards overcoming this limitation through learning sampling algorithms. Despite performing competitively with conventional methods when trained on a single system, learned samplers have so far demonstrated limited ability to transfer across systems. We demonstrate that deep learning enables the design of scalable and transferable samplers by introducing Prose, a 285 million parameter all-atom transferable normalizing flow trained on a corpus of peptide molecular dynamics trajectories up to 8 residues in length. Prose draws zero-shot uncorrelated proposal samples for arbitrary peptide systems, achieving the previously intractable transferability across sequence length, whilst retaining the efficient likelihood evaluation of normalizing flows. Through extensive empirical evaluation we demonstrate the efficacy of Prose as a proposal for a variety of sampling algorithms, finding a simple importance sampling-based finetuning procedure to achieve competitive performance to established methods such as sequential Monte Carlo. We open-source the Prose codebase, model weights, and training dataset, to further stimulate research into amortized sampling methods and finetuning objectives.'
publication: 'In *NeurIPS*'
publication_short: 'In *NeurIPS*'
links:
- name: Data
  url: https://huggingface.co/datasets/transferable-samplers/many-peptides-md
url_pdf: https://arxiv.org/abs/2508.18175
url_code: https://github.com/transferable-samplers/transferable-samplers

---
