---
# Documentation: https://docs.hugoblox.com/managing-content/

title: 'FORT: Forward-Only Regression Training of Normalizing Flows'
subtitle: ''
summary: ''
authors:
- Danyal Rehman
- Oscar Davis
- Jiarui Lu
- Jian Tang
- Michael Bronstein
- Yoshua Bengio
- Alexander Tong
- Avishek Joey Bose
tags: []
categories: []
date: '2025-01-01'
lastmod: 2025-07-01T19:26:38-04:00
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
projects: [flow-matching]
publishDate: '2025-07-01T23:26:38.658506Z'
publication_types:
- 'article'
abstract: "Simulation-free training frameworks have been at the forefront of the generative modelling revolution in continuous spaces, leading to large-scale diffusion and flow matching models. However, such modern generative models suffer from expensive inference, inhibiting their use in numerous scientific applications like Boltzmann Generators (BGs) for molecular conformations that require fast likelihood evaluation. In this paper, we revisit classical normalizing flows in the context of BGs that offer efficient sampling and likelihoods, but whose training via maximum likelihood is often unstable and computationally challenging. We propose Regression Training of Normalizing Flows (RegFlow), a novel and scalable regression-based training objective that bypasses the numerical instability and computational challenge of conventional maximum likelihood training in favour of a simple ℓ2-regression objective. Specifically, RegFlow maps prior samples under our flow to targets computed using optimal transport couplings or a pre-trained continuous normalizing flow (CNF). To enhance numerical stability, RegFlow employs effective regularization strategies such as a new forward-backward self-consistency loss that enjoys painless implementation. Empirically, we demonstrate that RegFlow unlocks a broader class of architectures that were previously intractable to train for BGs with maximum likelihood. We also show RegFlow exceeds the performance, computational cost, and stability of maximum likelihood training in equilibrium sampling in Cartesian coordinates of alanine dipeptide, tripeptide, and tetrapeptide, showcasing its potential in molecular systems."
publication: '*ICML GenBio Best Paper Award 2025*'
links:
- name: arXiv
  url: https://arxiv.org/abs/2506.01158
- name: URL
  url: https://arxiv.org/abs/2506.01158
---
