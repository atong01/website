---
# Documentation: https://docs.hugoblox.com/managing-content/

title: "OXtal: An All-Atom Diffusion Model for Organic Crystal Structure Prediction"
subtitle: ''
summary: ''
authors:
- Emily Jin
- Andrei Cristian Nica
- Mikhail Galkin
- Jarrid Rector-Brooks
- Kin Long Kelvin Lee
- Santiago Miret
- Frances H. Arnold
- Michael Bronstein
- Avishek Joey Bose
- admin
- Chenghao Liu
author_notes:
- Equal Contribution
- Equal Contribution
tags: []
date: '2025-12-10'
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
- 'article'
categories: ["preprint"]
projects: [flow-matching]
abstract: "Accurately predicting experimentally-realizable 3D molecular crystal structures from their 2D chemical graphs is a long-standing open challenge in computational chemistry called crystal structure prediction (CSP). Efficiently solving this problem has implications ranging from pharmaceuticals to organic semiconductors, as crystal packing directly governs the physical and chemical properties of organic solids. In this paper, we introduce OXtal, a large-scale 100M parameter all-atom diffusion model that directly learns the conditional joint distribution over intramolecular conformations and periodic packing. To efficiently scale OXtal, we abandon explicit equivariant architectures imposing inductive bias arising from crystal symmetries in favor of data augmentation strategies. We further propose a novel crystallization-inspired lattice-free training scheme, Stoichiometric Stochastic Shell Sampling (S⁴), that efficiently captures long-range interactions while sidestepping explicit lattice parametrization -- thus enabling more scalable architectural choices at all-atom resolution. By leveraging a large dataset of 600K experimentally validated crystal structures (including rigid and flexible molecules, co-crystals, and solvates), OXtal achieves orders-of-magnitude improvements over prior ab initio machine learning CSP methods, while remaining orders of magnitude cheaper than traditional quantum-chemical approaches. Specifically, OXtal recovers experimental structures with conformer RMSD₁<0.5 Å and attains over 80% packing similarity rate, demonstrating its ability to model both thermodynamic and kinetic regularities of molecular crystallization."
publication: '*arXiv preprint*'
publication_short: '*arXiv*'
links:
- name: Blog
  url: https://oxtal.github.io/
url_pdf: https://arxiv.org/abs/2512.06987
---
