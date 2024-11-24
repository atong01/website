---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Metric Flow Matching for Smooth Interpolations on the Data Manifold
subtitle: ''
summary: ''
authors:
- Kacper Kapusniak
- Peter Potaptchik
- Teodora Reu
- Leo Zhang
- admin
- Michael Bronstein
- Avishek Joey Bose
- Francesco Di Giovanni
tags: [flow-matching]
categories: ["archival"]
date: '2024-12-08'
lastmod: 2024-06-20T09:20:28-04:00
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
publishDate: '2024-05-23T13:20:26.987462Z'
publication_types:
- paper-conference
abstract: 'Matching objectives underpin the success of modern generative models and rely on constructing conditional paths that transform a source distribution into a target distribution. Despite being a fundamental building block, conditional paths have been designed principally under the assumption of Euclidean geometry, resulting in straight interpolations. However, this can be particularly restrictive for tasks such as trajectory inference, where straight paths might lie outside the data manifold, thus failing to capture the underlying dynamics giving rise to the observed marginals. In this paper, we propose Metric Flow Matching (MFM), a novel simulation-free framework for conditional flow matching where interpolants are approximate geodesics learned by minimizing the kinetic energy of a data-induced Riemannian metric. This way, the generative model matches vector fields on the data manifold, which corresponds to lower uncertainty and more meaningful interpolations. We prescribe general metrics to instantiate MFM, independent of the task, and test it on a suite of challenging problems including LiDAR navigation, unpaired image translation, and modeling cellular dynamics. We observe that MFM outperforms the Euclidean baselines, particularly achieving SOTA on single-cell trajectory prediction.'
publication: 'In *NeurIPS*'
url_pdf: https://arxiv.org/abs/2405.14780
url_code: https://github.com/kksniak/metric-flow-matching
---
