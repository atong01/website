---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'DynGFN: Bayesian Dynamic Causal Discovery Using Generative Flow Networks'
subtitle: ''
summary: ''
authors:
- Lazar Atanackovic
- Alexander Tong
- Jason Hartford
- Leo J. Lee
- Bo Wang
- Yoshua Bengio
tags: []
categories: []
date: '2023-12-01'
lastmod: 2023-05-31T06:37:09-04:00
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
publishDate: '2023-05-31T10:37:09.593042Z'
publication_types:
- '1'
abstract: 'One of the grand challenges of cell biology is inferring the gene regulatory network (GRN) which describes interactions between genes and their products that control gene expression and cellular function. We can treat this as a causal discovery problem but with two non-standard challenges: (1) regulatory networks are inherently cyclic so we should not model a GRN as a directed acyclic graph (DAG), and (2) observations have significant measurement noise, so for typical sample sizes there will always be a large equivalence class of graphs that are likely given the data, and we want methods that capture this uncertainty. Existing methods either focus on challenge (1), identifying *cyclic* structure from dynamics, or on challenge (2) learning complex Bayesian *posteriors* over DAGs, but not both. In this paper we leverage the fact that it is possible to estimate the ``velocity'' of gene expression with *RNA velocity* techniques to develop an approach that addresses both challenges. Because we have access to velocity information, we can treat the Bayesian structure learning problem as a problem of sparse identification of a dynamical system, capturing cyclic feedback loops through time. Since our objective is to model uncertainty over discrete structures, we leverage Generative Flow Networks (GFlowNets) to estimate the posterior distribution over the combinatorial space of possible sparse dependencies. Our results indicate that our method learns posteriors that better encapsulate the distributions of cyclic structures compared to counterpart state-of-the-art Bayesian structure learning approaches.'
publication: 'NeurIPS'

url_pdf: https://arxiv.org/abs/2302.04178
url_code: https://github.com/lazaratan/dyn-gfn
---
