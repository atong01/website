---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Iterated Denoising Energy Matching for Sampling from Boltzmann Densities
subtitle: ''
summary: ''
authors:
- Tara Akhound-Sadegh
- Jarrid Rector-Brooks
- Avishek Joey Bose
- Sarthak Mittal
- Pablo Lemos
- Cheng-Hao Liu
- Marcin Sendera
- Siamak Ravanbakhsh
- Gauthier Gidel
- Yoshua Bengio
- Nikolay Malkin
- admin
author_notes:
- Equal Contribution
- Equal Contribution
- Equal Contribution
tags: []
categories: ["archival"]
date: '2024-07-21'
lastmod: 2024-02-13T17:16:03-05:00
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
publishDate: '2024-02-13T22:16:02.239246Z'
publication_types:
- paper-conference
abstract: 'Efficiently generating statistically independent samples from an unnormalized probability distribution, such as equilibrium samples of many-body systems, is a foundational problem in science. In this paper, we propose Iterated Denoising Energy Matching (iDEM), an iterative algorithm that uses a novel stochastic score matching objective leveraging solely the energy function and its gradient -- and no data samples -- to train a diffusion-based sampler. Specifically, iDEM alternates between (I) sampling regions of high model density from a diffusion-based sampler and (II) using these samples in our stochastic matching objective to further improve the sampler. iDEM is scalable to high dimensions as the inner matching objective, is simulation-free, and requires no MCMC samples. Moreover, by leveraging the fast mode mixing behavior of diffusion, iDEM smooths out the energy landscape enabling efficient exploration and learning of an amortized sampler. We evaluate iDEM on a suite of tasks ranging from standard synthetic energy functions to invariant n-body particle systems. We show that the proposed approach achieves state-of-the-art performance on all metrics and trains 2−5× faster, which allows it to be the first method to train using energy on the challenging 55-particle Lennard-Jones system.'
publication: 'In *ICML*'
url_pdf: https://arxiv.org/abs/2402.06121
url_code: https://github.com/jarridrb/dem
---
