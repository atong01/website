---
# Documentation: https://docs.hugoblox.com/managing-content/

title: 'geneRNIB: a living benchmark for gene regulatory network inference'
subtitle: ''
summary: ''
authors:
- Jalil Nourisa
- Antoine Passemiers
- Marco Stock
- Berit Zeller-Plumhoff
- Robrecht Cannoodt
- Christian Arnold
- Alexander Tong
- Jason Hartford
- Antonio Scialdone
- Yves Moreau
- Yang Li
- Malte D. Luecken
tags: []
categories: []
date: '2025-02-25'
lastmod: 2025-03-06T11:12:40Z
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
publishDate: '2025-03-06T11:12:39.027175Z'
publication_types:
- article
abstract: 'Gene regulatory networks (GRNs) underpin cellular identity and function,
  playing a key role in health and disease. Despite various benchmarking efforts,
  existing studies remain limited in the number of GRN inference methods, datasets,
  and evaluation metrics. The absence of a universally accepted ground truth further
  complicates the evaluation, requiring continuous refinement of benchmarking strategies.
  In addition, regulatory interactions are highly context-specific and vary between
  perturbations, cell types, tissues, and organisms. However, current benchmarks do
  not account for this complexity, limiting their applicability in personalized medicine.
  Here, we introduce geneRNIB, a comprehensive GRN bench-marking framework built on
  three key principles: context-specific evaluation, continuous integration, and holistic
  assessment in the absence of a true reference network. geneRNIB enables the seamless
  incorporation of new algorithms, datasets, and evaluation metrics to reflect ongoing
  developments. In the current version, we systematically integrated and assessed
  ten GRN inference methods, spanning single- and multiomics approaches across five
  diverse datasets including thousands of perturbation scenarios. We introduced eight
  novel metrics specifically designed to assess context-specific causal inference.
  Our findings indicate that simple models with fewer assumptions often outperformed
  more complex pipelines. Notably, gene expression-based correlation algorithms yielded
  better results than more advanced approaches incorporating prior datasets or pre-trained
  on large datasets. In addition, we identified several potential factors that influence
  the performance of GRN inference and offered actionable guidelines for the future
  development of the method. By addressing these critical limitations in existing
  benchmarks, geneRNIB advances GRN research and fosters progress toward personalized
  medicine.Competing Interest StatementThe authors have declared no competing interest.'
publication: '*bioRxiv*'
doi: 10.1101/2025.02.25.640181
links:
- url_pdf: https://www.biorxiv.org/content/early/2025/03/01/2025.02.25.640181
---
