---
# Documentation: https://docs.hugoblox.com/managing-content/

title: 'Meta Flow Matching: Integrating Vector Fields on the Wasserstein Manifold'
subtitle: ''
summary: ''
authors:
- Lazar Atanackovic
- Xi Zhang
- Brandon Amos
- Mathieu Blanchette
- Leo J. Lee
- Yoshua Bengio
- admin
- Kirill Neklyudov
author_notes:
- Equal Contribution
- Equal Contribution

tags: []
categories: ["archival"]
date: '2025-05-24'
lastmod: 2025-01-23T11:14:17Z
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
publishDate: '2025-01-23T11:14:16.859001Z'
publication_types:
- paper-conference
publication: 'In *ICLR*'
abstract: "Numerous biological and physical processes can be modeled as systems of interacting entities evolving continuously over time, e.g. the dynamics of communicating cells or physical particles. Learning the dynamics of such systems is essential for predicting the temporal evolution of populations across novel samples and unseen environments. Flow-based models allow for learning these dynamics at the population level - they model the evolution of the entire distribution of samples. However, current flow-based models are limited to a single initial population and a set of predefined conditions which describe different dynamics. We argue that multiple processes in natural sciences have to be represented as vector fields on the Wasserstein manifold of probability densities. That is, the change of the population at any moment in time depends on the population itself due to the interactions between samples. In particular, this is crucial for personalized medicine where the development of diseases and their respective treatment response depend on the microenvironment of cells specific to each patient. We propose Meta Flow Matching (MFM), a practical approach to integrate along these vector fields on the Wasserstein manifold by amortizing the flow model over the initial populations. Namely, we embed the population of samples using a Graph Neural Network (GNN) and use these embeddings to train a Flow Matching model. This gives MFM the ability to generalize over the initial distributions, unlike previously proposed methods. We demonstrate the ability of MFM to improve the prediction of individual treatment responses on a large-scale multi-patient single-cell drug screen dataset."
links:
- name: arXiv
  url: https://arxiv.org/abs/2408.14608
---
