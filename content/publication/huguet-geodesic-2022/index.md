---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Geodesic Sinkhorn: Optimal Transport for High-Dimensional Datasets'
subtitle: ''
summary: ''
authors:
- Guillaume Huguet
- Alexander Tong
- María Ramos Zapatero
- Guy Wolf
- Smita Krishnaswamy
tags: []
categories: []
date: '2022-11-01'
lastmod: 2023-05-31T06:32:24-04:00
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
publishDate: '2023-05-31T10:32:24.609712Z'
publication_types:
- '3'
abstract: 'Efficient computation of optimal transport distance between distributions is of growing importance in data science. Sinkhorn-based methods are currently the state of the art for such computations, but require $O(n^2)$ computations. In addition, Sinkhorn-based methods commonly use an Euclidean ground distance between datapoints. However, with the prevalence of manifold structured scientific data, it is often desirable to consider geodesic ground distance. Here, we tackle both issues by proposing Geodesic Sinkhorn---based on diffusing a heat kernel on a manifold graph. Notably, Geodesic Sinkhorn requires only $O(n\log n)$ computation, as we approximate the heat kernel with Chebyshev polynomials based on the sparse graph Laplacian. We apply our method to the computation of barycenters of several distributions of high dimensional single cell data from patient samples undergoing chemotherapy. In particular we define the barycentric distance as the distance between two such barycenters. Using this definition, we identify an optimal transport distance and path associated with the effect of treatment on cellular data.'
publication: '*arXiv*'

url_pdf: https://arxiv.org/abs/2211.00805
---
