---
# Documentation: https://docs.hugoblox.com/managing-content/

title: "FALCON: Few-step Accurate Likelihoods for Continuous Flows"
subtitle: ''
summary: ''
authors:
- Danyal Rehman
- Tara Akhound-Sadegh
- Artem Gazizov
- Yoshua Bengio
- admin
author_notes: []
tags: []
date: '2025-12-11'
lastmod: 2025-12-11T00:00:00-04:00
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
publishDate: '2025-12-11T00:00:00.000000Z'
publication_types:
- 'paper-conference'
categories: ["workshop"]
projects: [flow-matching]
abstract: "Scalable sampling of molecular states in thermodynamic equilibrium is a long-standing challenge in statistical physics. Boltzmann Generators tackle this problem by pairing a generative model, capable of exact likelihood computation, with importance sampling to obtain consistent samples under the target distribution. Current Boltzmann Generators primarily use continuous normalizing flows (CNFs) trained with flow matching for efficient training of powerful models. However, likelihood calculation for these models is extremely costly, requiring thousands of function evaluations per sample, severely limiting their adoption. In this work, we propose Few-step Accurate Likelihoods for Continuous Flows (FALCON), a method which allows for few-step sampling with a likelihood accurate enough for importance sampling applications by introducing a hybrid training objective that encourages invertibility. We show FALCON outperforms state-of-the-art normalizing flow models for molecular Boltzmann sampling and is two orders of magnitude faster than the equivalently performing CNF model."
publication: '*NeurIPS 2025 MLSB Workshop*'
publication_short: '*NeurIPS MLSB*'
links:
url_pdf: https://arxiv.org/abs/2512.09914
---
