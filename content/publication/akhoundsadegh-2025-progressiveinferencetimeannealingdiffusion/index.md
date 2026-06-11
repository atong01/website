---
# Documentation: https://docs.hugoblox.com/managing-content/

title: Progressive Inference-Time Annealing of Diffusion Models for Sampling from
  Boltzmann Densities
subtitle: ''
summary: ''
authors:
- Tara Akhound-Sadegh
- Jungyoon Lee
- Avishek Joey Bose
- Valentin De Bortoli
- Arnaud Doucet
- Michael M. Bronstein
- Dominique Beaini
- Siamak Ravanbakhsh
- Kirill Neklyudov
- admin
author_notes:
- Equal Contribution
- Equal Contribution
-
-
-
-
-
-
- Equal Contribution
- Equal Contribution
tags: []
date: '2025-12-10'
lastmod: 2025-07-01T19:26:38-04:00
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
publishDate: '2025-07-01T23:26:38.446292Z'
publication_types:
- 'paper-conference'
categories: ["archival"]
projects: [flow-matching]
abstract: 'Sampling efficiently from a target unnormalized probability density remains a core challenge, with relevance across countless high-impact scientific applications. A promising approach towards this challenge is the design of amortized samplers that borrow key ideas, such as probability path design, from state-of-the-art generative diffusion models. However, all existing diffusion-based samplers remain unable to draw samples from distributions at the scale of even simple molecular systems. In this paper, we propose Progressive Inference-Time Annealing (PITA), a novel framework to learn diffusion-based samplers that combines two complementary interpolation techniques: I.) Annealing of the Boltzmann distribution and II.) Diffusion smoothing. PITA trains a sequence of diffusion models from high to low temperatures by sequentially training each model at progressively higher temperatures, leveraging engineered easy access to samples of the temperature-annealed target density. In the subsequent step, PITA enables simulating the trained diffusion model to procure training samples at a lower temperature for the next diffusion model through inference-time annealing using a novel Feynman-Kac PDE combined with Sequential Monte Carlo. Empirically, PITA enables, for the first time, equilibrium sampling of N-body particle systems, Alanine Dipeptide, and tripeptides in Cartesian coordinates with dramatically lower energy function evaluations. Code available at: https://github.com/taraak/pita'
publication: 'In *NeurIPS* (spotlight)'
publication_short: 'In *NeurIPS* (spotlight)'
links:
url_pdf: https://arxiv.org/abs/2506.16471
url_code: https://github.com/taraak/pita
---
