---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Graph Fourier MMD for signals on data graphs
subtitle: ''
summary: ''
authors:
- Sam Leone
- admin
- Guillaume Huguet
- Guy Wolf
- Smita Krishnaswamy
tags: []
categories: [archival]
date: '2023-01-01'
lastmod: 2023-05-31T06:35:54-04:00
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
publishDate: '2023-05-31T10:35:54.045924Z'
publication_types:
- paper-conference
abstract: 'While numerous methods have been proposed for computing distances between probability distributions in Euclidean space, relatively little attention has been given to computing such distances for distributions on graphs. However, there has been a marked increase in data that either lies on graph (such as protein interaction networks) or can be modeled as a graph (single cell data), particularly in the biomedical sciences. Thus, it becomes important to find ways to compare signals defined on such graphs. Here, we propose Graph Fourier MMD (GFMMD), a novel distance between distributions and signals on graphs. GFMMD is defined via an optimal witness function that is both smooth on the graph and maximizes difference in expectation between the pair of distributions on the graph. We find an analytical solution to this optimization problem as well as an embedding of distributions that results from this method.  We also prove several properties of this method including scale invariance and applicability to disconnected graphs. We showcase it on graph benchmark datasets as well on single cell RNA-sequencing data analysis. In the latter, we use the GFMMD-based gene embeddings to find meaningful gene clusters. We also propose a novel type of score for gene selection called {\em gene localization score} which helps select genes for cellular state space characterization.'
publication: '*SAMPTA: Sampling Theory and Applications Conference*'
publication_short: 'In *SAMPTA*'
url_pdf: https://arxiv.org/abs/2306.02508
---
