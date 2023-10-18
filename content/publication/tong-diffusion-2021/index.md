---
title: "Diffusion Earth Mover's Distance and Distribution Embeddings"
date: 2021-07-22
publishDate: 2021-07-22
summary: "A fast diffusion-based earth mover's distance"
authors: [admin, "Guillaume Huguet", "Amine Natik", "Kincaid MacDonald", "Manik Kuchroo", "Ronald Coifman", "Guy Wolf", "Smita Krishnaswamy"]
author_notes:
- Equal Contribution
- Equal Contribution
- Equal Contribution
categories: [archival]
publication_types: ["paper-conference"]
abstract: "We propose a new fast method of measuring distances between large numbers of related high dimensional datasets called the Diffusion Earth Mover's Distance (EMD). We model the datasets as distributions supported on common data graph that is derived from the affinity matrix computed on the combined data. In such cases where the graph is a discretization of an underlying Riemannian closed manifold, we prove that Diffusion EMD is topologically equivalent to the standard EMD with a geodesic ground distance. Diffusion EMD can be computed in {{< math >}}$\tilde{O}(n)${{< /math >}} time and is more accurate than similarly fast algorithms such as tree-based EMDs. We also show Diffusion EMD is fully differentiable, making it amenable to future uses in gradient-descent frameworks such as deep neural networks. Finally, we demonstrate an application of Diffusion EMD to single cell data collected from 210 COVID-19 patient samples at Yale New Haven Hospital. Here, Diffusion EMD can derive distances between patients on the manifold of cells at least two orders of magnitude faster than equally accurate methods. This distance matrix between patients can be embedded into a higher level patient manifold which uncovers structure and heterogeneity in patients. More generally, Diffusion EMD is applicable to all datasets that are massively collected in parallel in many medical and biological systems."
featured: false
publication: In *Proceedings of the 38th International Conference on Machine Learning*. <br> Also presented at LMRL Workshop @ NeurIPS 2020
publication_short: In *ICML*. <br> Also presented at LMRL Workshop @ NeurIPS 2020


# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "Embedding Distributions based on Diffusion EMD"
  focal_point: "Top"
  preview_only: false

links:
- name: Arxiv
  url: https://arxiv.org/abs/2102.12833
- name: ICML Page
  url: http://proceedings.mlr.press/v139/tong21a.html
- name: Tweetorial
  url: https://twitter.com/KrishnaswamyLab/status/1394059986205040647?s=20&t=h5eFpIa32tuxT8HrUEmbng
- name: Workshop Poster
  url: "NeurIPS_LMRL_2020_Manifold.pdf"
url_pdf: http://proceedings.mlr.press/v139/tong21a/tong21a-supp.pdf
url_code: https://github.com/KrishnaswamyLab/DiffusionEMD
url_video: https://youtu.be/3Lwi_nYsmDs
url_slides: "DiffusionEMD_slides.pdf"
url_poster: "DiffusionEMD_poster.pdf"
tags: ["OT", "Optimal Transport", "Diffusion"]
---

