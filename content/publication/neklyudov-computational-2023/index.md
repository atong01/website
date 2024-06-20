---
# Documentation: https://wowchemy.com/docs/managing-content/

title: A Computational Framework for Solving Wasserstein Lagrangian Flows
subtitle: ''
summary: ''
authors:
- Kirill Neklyudov
- Rob Brekelmans
- admin
- Lazar Atanackovic
- Qiang Liu
- Alireza Makhzani
author_notes:
- Equal Contribution
- Equal Contribution
tags: []
categories: [archival]
date: '2024-07-20'
lastmod: 2023-10-18T12:30:34-04:00
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
projects: []
publishDate: '2023-10-18T16:30:34.393570Z'
publication_types:
- paper-conference
abstract: 'The dynamical formulation of the optimal transport can be extended through various choices of the underlying geometry (kinetic energy), and the regularization of density paths (potential energy). These combinations yield different variational problems (Lagrangians), encompassing many variations of the optimal transport problem such as the Schro¨dinger bridge, unbalanced optimal transport, and optimal transport with physical constraints, among others. In general, the optimal density path is unknown, and solving these variational problems can be computationally challenging. Leveraging the dual formulation of the Lagrangians, we propose a novel deep learning based framework approaching all of these problems from a unified perspective. Our method does not require simulating or backpropagating through the trajectories of the learned dynamics, and does not need access to optimal couplings. We showcase the versatility of the proposed framework by outperforming previous approaches for the single-cell trajectory inference, where incorporating prior knowledge into the dynamics is crucial for correct predictions.'
publication: 'In *ICML*'
url_pdf: http://arxiv.org/abs/2310.10649
url_code: https://github.com/necludov/wl-mechanics
---
