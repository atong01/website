---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Time-Inhomogeneous Diffusion Geometry and Topology
subtitle: ''
summary: ''
authors:
- Guillaume Huguet
- Alexander Tong
- Bastian Rieck
- Jessie Huang
- Manik Kuchroo
- Matthew Hirn
- Guy Wolf
- Smita Krishnaswamy
tags:
- Computer Science - Machine Learning
- Statistics - Machine Learning
categories: ["Journal"]
date: '2023-05-01'
lastmod: 2023-05-10T21:28:42-04:00
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
publishDate: '2023-05-11T01:28:42.304977Z'
publication_types:
- '1'
abstract: Diffusion condensation is a dynamic process that yields a sequence of multiscale
  data representations that aim to encode meaningful abstractions. It has proven effective
  for manifold learning, denoising, clustering, and visualization of high-dimensional
  data. Diffusion condensation is constructed as a time-inhomogeneous process where
  each step first computes and then applies a diffusion operator to the data. We theoretically
  analyze the convergence and evolution of this process from geometric, spectral,
  and topological perspectives. From a geometric perspective, we obtain convergence
  bounds based on the smallest transition probability and the radius of the data,
  whereas from a spectral perspective, our bounds are based on the eigenspectrum of
  the diffusion kernel. Our spectral results are of particular interest since most
  of the literature on data diffusion is focused on homogeneous processes. From a
  topological perspective, we show diffusion condensation generalizes centroidbased
  hierarchical clustering. We use this perspective to obtain a bound based on the
  number of data points, independent of their location. To understand the evolution
  of the data geometry beyond convergence, we use topological data analysis. We show
  that the condensation process itself defines an intrinsic diffusion homology. We
  use this intrinsic topology as well as an ambient topology to study how the data
  changes over diffusion time. We demonstrate both homologies in well-understood toy
  examples. Our work gives theoretical insights into the convergence of diffusion
  condensation, and shows that it provides a link between topological and geometric
  data analysis.
publication: 'In *SIMODS*: SIAM Journal on the Mathematics of Data Science'
links:
- name: SIMODS
  url: https://epubs.siam.org/doi/abs/10.1137/21M1462945
url_pdf: https://arxiv.org/abs/2203.14860

---
