---
# Documentation: https://docs.hugoblox.com/managing-content/

title: 'Feynman-Kac Correctors in Diffusion: Annealing, Guidance, and Product of Experts'
subtitle: ''
summary: ''
authors:
- Marta Skreta
- Tara Akhound-Sadegh
- Viktor Ohanesian
- Roberto Bondesan
- Alán Aspuru-Guzik
- Arnaud Doucet
- Rob Brekelmans
- admin
- Kirill Neklyudov
author_notes:
- Equal Contribution
- Equal Contribution
- Equal Contribution
-
-
-
-
- Equal Contribution
- Equal Contribution

tags: []
categories: ["archival"]
date: '2025-07-14'
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
publishDate: '2025-03-06T11:12:40.462037Z'
publication_types:
- paper-conference
abstract: "While score-based generative models are the model of choice across diverse domains, there are limited tools available for controlling inference-time behavior in a principled manner, e.g. for composing multiple pretrained models. Existing classifier-free guidance methods use a simple heuristic to mix conditional and unconditional scores to approximately sample from conditional distributions. However, such methods do not approximate the intermediate distributions, necessitating additional 'corrector' steps. In this work, we provide an efficient and principled method for sampling from a sequence of annealed, geometric-averaged, or product distributions derived from pretrained score-based models. We derive a weighted simulation scheme which we call Feynman-Kac Correctors (FKCs) based on the celebrated Feynman-Kac formula by carefully accounting for terms in the appropriate partial differential equations (PDEs). To simulate these PDEs, we propose Sequential Monte Carlo (SMC) resampling algorithms that leverage inference-time scaling to improve sampling quality. We empirically demonstrate the utility of our methods by proposing amortized sampling via inference-time temperature annealing, improving multi-objective molecule generation using pretrained models, and improving classifier-free guidance for text-to-image generation."
publication: 'In *ICML* (spotlight)'
links:
- name: arXiv
  url: https://arxiv.org/abs/2503.02819
url_pdf: https://arxiv.org/pdf/2503.02819
url_code: https://github.com/martaskrt/fkc-diffusion
---
