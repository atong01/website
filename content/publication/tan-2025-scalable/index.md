---
# Documentation: https://docs.hugoblox.com/managing-content/

title: Scalable Equilibrium Sampling with Sequential Boltzmann Generators
subtitle: ''
summary: ''
authors:
- Charlie B. Tan
- Avishek Joey Bose
- Chen Lin
- Leon Klein
- Michael M. Bronstein
- admin
author_notes:
- Equal Contribution
- Equal Contribution

tags: []
categories: ["archival"]
date: '2025-07-14'
lastmod: 2025-03-06T11:12:40Z
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
projects: [sampling]
publishDate: '2025-03-06T11:12:40.312058Z'
publication_types:
- paper-conference
abstract: "Scalable sampling of molecular states in thermodynamic equilibrium is a long-standing challenge in statistical physics. Boltzmann generators tackle this problem by pairing normalizing flows with importance sampling to obtain uncorrelated samples under the target distribution. In this paper, we extend the Boltzmann generator framework with two key contributions, denoting our framework Sequential Boltzmann Generators (SBG). The first is a highly efficient Transformer-based normalizing flow operating directly on all-atom Cartesian coordinates. In contrast to the equivariant continuous flows of prior methods, we leverage exactly invertible non-equivariant architectures which are highly efficient during both sample generation and likelihood evaluation. This efficiency unlocks more sophisticated inference strategies beyond standard importance sampling. In particular, we perform inference-time scaling of flow samples using a continuous-time variant of sequential Monte Carlo, in which flow samples are transported towards the target distribution with annealed Langevin dynamics. SBG achieves state-of-the-art performance w.r.t. all metrics on peptide systems, demonstrating the first equilibrium sampling in Cartesian coordinates of tri-, tetra- and hexa-peptides that were thus far intractable for prior Boltzmann generators."
publication: 'In *ICML*'
links:
url_pdf: https://arxiv.org/pdf/2502.18462
url_code: https://github.com/transferable-samplers/transferable-samplers
---
