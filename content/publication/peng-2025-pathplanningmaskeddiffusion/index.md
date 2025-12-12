---
# Documentation: https://docs.hugoblox.com/managing-content/

title: Path Planning for Masked Diffusion Model Sampling
subtitle: ''
summary: ''
authors:
- Fred Zhangzhi Peng
- Zachary Bezemek
- Sawan Patel
- Jarrid Rector-Brooks
- Sherwood Yao
- admin
- Pranam Chatterjee
author_notes:
- Equal Contribution
- Equal Contribution
- ""
- ""
- ""
- Equal Contribution
- Equal Contribution

tags: []
categories: []
date: '2025-02-05'
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
projects: [flow-matching]
publishDate: '2025-03-06T11:12:40.166848Z'
publication_types:
- article
abstract: "Any order generation of discrete data using masked diffusion models (MDMs) offers a compelling alternative to traditional autoregressive models, especially in domains that lack a natural causal ordering of data. However, current popular MDMs depart from their successful continuous diffusion model counterparts with simplified masked inference wherein unmasked tokens cannot be iteratively refined -- even if there is a mistake. In this paper, we extract the full power of MDMs by introducing a novel inference sampling strategy termed Path Planning (P2) that decomposes each generation step into two sub-stages: planning and denoising. Under P2, the planner at every step selects appropriate tokens that are marked to be updated, which can then be sampled using the denoiser. We demonstrate that P2 generalizes all existing sampling strategies for MDMs and critically enhances generative quality through the new capability of refining and updating existing unmasked tokens. We theoretically prove that P2 establishes a (new) expanded evidence lower bound (ELBO) on the log marginal likelihood of data. We instantiate P2 with a family of planners including: 1.) Self-Planning, 2.) BERT-Planning, and 3.) Trained-Planning with a learned planner leading to SOTA generative performance for MDMs on a suite of domains. Specifically, solely using P2 inference, we observe relative improvements of 22% in protein sequence foldability, 8% in RNA sequence pLDDT, 4% in math reasoning, 68% in story generation (ROUGE score), and 33% in code generation for the challenging pass@1 metric."
publication: ''
links:
- name: arXiv
  url: https://arxiv.org/abs/2502.03540
url_pdf: https://arxiv.org/pdf/2502.03540
url_code: https://github.com/pengzhangzhi/Path-Planning
---
