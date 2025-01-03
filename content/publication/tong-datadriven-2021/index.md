---
title: "Data-Driven Learning of Geometric Scattering Networks"
date: 2021-08-15
# date: 2020-10-08
publishDate: 2021-08-15
summary: "A geometric scattering based network with learnable scale parameters"
authors:
  [
    admin,
    "Frederik Wenkel",
    "Kincaid MacDonald",
    "Smita Krishnaswamy",
    "Guy Wolf",
  ]
author_notes:
  - Equal Contribution
  - Equal Contribution
publication_types: ["paper-conference"]
categories: [archival]
abstract: "Graph neural networks (GNNs) in general, and graph convolutional networks (GCN) in particular, often rely on low-pass graph filters to incorporate geometric information in the form of local smoothness over neighboring nodes. While this approach performs well on a surprising number of standard benchmarks, the efficacy of such models does not translate consistently to more complex domains, such as graph data in the biochemistry domain. We argue that these more complex domains require priors that encourage learning of band-pass and high-pass features rather than oversmoothed signals of standard GCN architectures. Here, we propose an alternative GNN architecture, based on a relaxation of recently proposed geometric scattering transforms, which consists of a cascade of graph wavelet filters. Our learned geometric scattering (LEGS) architecture adaptively tunes these wavelets and their scales to encourage band-pass features to emerge in learned representations. This results in a simplified GNN with significantly fewer learned parameters compared to competing methods. We demonstrate the predictive performance of our method on several biochemistry graph classification benchmarks, as well as the descriptive quality of its learned features in biochemical graph data exploration tasks. Our results show that the proposed LEGS network matches or outperforms popular GNNs, as well as the original geometric scattering construction, while also retaining certain mathematical properties of its handcrafted (nonlearned) design."
featured: false
publication: "In *IEEE Machine Learning for Signal Processing Workshop 2021*. <br> Also presented at ML4M Workshop @ NeurIPS 2020"
publication_short: "In *IEEE MLSP*. <br> Also presented at ML4M Workshop @ NeurIPS 2020"

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "Trainable parameters for the learnable geometric scattering network"
  focal_point: "Smart"
  preview_only: false

links:
  - name: ArXiv
    url: https://arxiv.org/abs/2010.02415
  - name: Tweetorial
    url: https://twitter.com/KrishnaswamyLab/status/1454845639171379205?s=20&t=sxgkKOqRneKIf3AmEpJJBA
url_pdf: https://arxiv.org/pdf/2010.02415.pdf
url_code: https://github.com/KrishnaswamyLab/LearnableScattering
url_video: https://youtu.be/GsNlHHvN6p4
url_slides: "LEGS_MLSP_2021.pdf"

tags: ["Graph Signal Processing", "Scattering", "Graph Neural Network"]
---
