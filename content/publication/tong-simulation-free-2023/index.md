---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Simulation-Free Schrodinger Bridges via Score and Flow Matching
subtitle: ''
summary: ''
authors:
- admin
- Nikolay Malkin
- Kilian Fatras
- Lazar Atanackovic
- Yanlei Zhang
- Guillaume Huguet
- Guy Wolf
- Yoshua Bengio
author_notes:
- Equal Contribution
- Equal Contribution
- Equal Contribution
tags: []
categories: []
date: '2024-01-02'
lastmod: 2023-10-02T23:28:21-04:00
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
projects: ["flow-matching"]
publishDate: '2023-10-03T03:28:21.007796Z'
categories:
- archival
publication_types:
- paper-conference
abstract: 'We present simulation-free score and flow matching ([SF]2M), a simulation-free objective for inferring stochastic dynamics given unpaired source and target samples drawn from arbitrary distributions. Our method generalizes both the score-matching loss used in the training of diffusion models and the recently proposed flow matching loss used in the training of continuous normalizing flows. [SF]2M interprets continuous-time stochastic generative modeling as a Schrödinger bridge (SB) problem. It relies on static entropy-regularized optimal transport, or a minibatch approximation, to efficiently learn the SB without simulating the learned stochastic process. We find that [SF]2M is more efficient and gives more accurate solutions to the SB problem than simulation-based methods from prior work. Finally, we apply [SF]2M to the problem of learning cell dynamics from snapshot data. Notably, [SF]2M is the first method to accurately model cell dynamics in high dimensions and can recover known gene regulatory networks from simulated data.'
publication: 'In *AISTATS*. <br> Also presented at Frontiers4LCD Workshop @ ICML 2023'
url_pdf: https://arxiv.org/abs/2307.03672
url_code: https://github.com/atong01/conditional-flow-matching
---
