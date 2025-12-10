---
# Documentation: https://docs.hugoblox.com/managing-content/

title: Planner Aware Path Learning in Diffusion Language Models Training
subtitle: ''
summary: ''
authors:
- Fred Zhangzhi Peng
- Zachary Bezemek
- Jarrid Rector-Brooks
- Shuibai Zhang
- Anru R. Zhang
- Michael Bronstein
- Avishek Joey Bose
- admin
author_notes:
- Equal Contribution
- Equal Contribution
-
-
-
-
- Equal Contribution
- Equal Contribution
tags: []
date: '2025-09-27'
lastmod: 2025-12-10T00:00:00-04:00
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
publishDate: '2025-12-10T00:00:00.000000Z'
publication_types:
- 'article'
categories: ["preprint"]
projects: [flow-matching]
abstract: "Diffusion language models have emerged as a powerful alternative to autoregressive models, enabling fast inference through flexible and parallel generation paths. This flexibility is enabled by new sampling strategies, or planners, that iteratively choose where to denoise along the sequence rather than sampling uniformly at random. However, by modifying reverse paths, planners introduce a mismatch between the uniformly random denoising paths used during training and the planning-based paths used at inference. In this work, we systematically investigate this mismatch and theoretically show that the standard discrete diffusion training evidence lower bound (ELBO) does not accurately describe a denoiser under non-uniform planning. To bridge this gap, we derive a new Planned Evidence Lower Bound (P-ELBO) that directly incorporates planner-based reverse dynamics into the training objective. Building on this, we propose Planner Aware Path Learning (PAPL), a simple and effective modification of the standard masked discrete diffusion loss that aligns training and inference under planned denoisers. Empirically, PAPL delivers consistent improvements across domains, including a 40% relative gain in protein sequence modeling, up to a 4x improvement in MAUVE for text generation, and a 23% relative gain in HumanEval pass@10 for code generation."
publication: '*arXiv preprint*'
publication_short: '*arXiv*'
links:
url_pdf: https://arxiv.org/abs/2509.23405
---
