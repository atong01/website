---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Manifold Interpolating Optimal-Transport Flows for Trajectory Inference
subtitle: ''
summary: ''
authors:
- Guillaume Huguet
- D. S. Magruder
- Alexander Tong
- Oluwadamilola Fasina
- Manik Kuchroo
- Guy Wolf
- Smita Krishnaswamy
tags: []
categories: []
date: '2022-12-09'
lastmod: 2023-05-31T06:26:48-04:00
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
publishDate: '2022-12-09T10:26:48.511128Z'
publication_types:
- '1'
abstract: 'We present a method called Manifold Interpolating Optimal-Transport Flow (MIOFlow) that learns stochastic, continuous population dynamics from static snapshot samples taken at sporadic timepoints. MIOFlow combines dynamic models,  manifold learning, and optimal transport by training neural ordinary differential equations (Neural ODE) to interpolate between static population snapshots as penalized by optimal transport with manifold ground distance. Further, we ensure that the flow follows the geometry by operating in the latent space of an autoencoder that we call a geodesic autoencoder (GAE). In GAE the latent space distance between points is regularized to match a novel multiscale geodesic distance on the data manifold that we define. We show that this method is superior to normalizing flows, Schr\"odinger bridges and other generative models that are designed to flow from noise to data in terms of interpolating between populations. Theoretically, we link these trajectories with dynamic optimal transport. We evaluate our method on simulated data with bifurcations and merges, as well as scRNA-seq data from embryoid body differentiation, and acute myeloid leukemia treatment.'
publication: '*NeurIPS*'

links:
- name: NeurIPS
  url: https://proceedings.neurips.cc/paper_files/paper/2022/hash/bfc03f077688d8885c0a9389d77616d0-Abstract-Conference.html
- name: Arxiv
  url: https://arxiv.org/abs/2206.14928
url_pdf: https://arxiv.org/pdf/2206.14928.pdf
url_code: https://github.com/KrishnaswamyLab/MIOFlow
---
