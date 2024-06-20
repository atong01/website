---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Improving and Generalizing Flow-Based Generative Models with Minibatch Optimal Transport'
subtitle: ''
summary: 'We present methods for learning simple flows over R^d with optimal transport conditional flow matching (OT-CFM). Training with this objective leads to imprved results on a variety of conditional and unconditional generation tasks, such as inferring single cell dynamics, unsupervised image translation, and Schrodinger bridge inference.'
authors:
- admin
- Nikolay Malkin
- Guillaume Huguet
- Yanlei Zhang
- Jarrid Rector-Brooks
- Kilian Fatras
- Guy Wolf
- Yoshua Bengio
tags: []
categories: ["archival"]
date: '2023-02-01'
lastmod: 2023-05-31T06:34:38-04:00
featured: true
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
publishDate: '2023-05-31T10:34:38.480754Z'
publication_types:
- paper-conference
abstract: 'Continuous normalizing flows (CNFs) are an attractive generative modeling technique, but they have been held back by limitations in their simulation-based maximum likelihood training. We introduce the generalized conditional flow matching (CFM) technique, a family of simulation-free training objectives for CNFs. CFM features a stable regression objective like that used to train the stochastic flow in diffusion models but enjoys the efficient inference of deterministic flow models. In contrast to both diffusion models and prior CNF training algorithms, CFM does not require the source distribution to be Gaussian or require evaluation of its density. A variant of our objective is optimal transport CFM (OT-CFM), which creates simpler flows that are more stable to train and lead to faster inference, as evaluated in our experiments. Furthermore, OT-CFM is the first method to compute dynamic OT in a simulation-free way. Training CNFs with CFM improves results on a variety of conditional and unconditional generation tasks, such as inferring single cell dynamics, unsupervised image translation, and Schrödinger bridge inference.'
publication: 'In *TMLR* <br> Also presented at Frontiers4LCD Workshop @ ICML 2023'
url_pdf: https://arxiv.org/abs/2302.00482
url_code: https://github.com/atong01/conditional-flow-matching
url_video: https://www.youtube.com/watch?v=UhDtH7Ia9Ag
---
