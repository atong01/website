---
# Documentation: https://docs.hugoblox.com/managing-content/

title: "Foundations of Diffusion Models in General State Spaces: A Self-Contained Introduction"
subtitle: ''
summary: ''
authors:
- Vincent Pauline
- Tobias Höppe
- Kirill Neklyudov
- admin
- Stefan Bauer
- Andrea Dittadi
author_notes: []
tags: []
date: '2025-12-04'
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
abstract: "Although diffusion models now occupy a central place in generative modeling, introductory treatments commonly assume Euclidean data and seldom clarify their connection to discrete-state analogues. This article is a self-contained primer on diffusion over general state spaces, unifying continuous domains and discrete/categorical structures under one lens. We develop the discrete-time view (forward noising via Markov kernels and learned reverse dynamics) alongside its continuous-time limits -- stochastic differential equations (SDEs) in ℝᵈ and continuous-time Markov chains (CTMCs) on finite alphabets -- and derive the associated Fokker--Planck and master equations. A common variational treatment yields the ELBO that underpins standard training losses. We make explicit how forward corruption choices -- Gaussian processes in continuous spaces and structured categorical transition kernels (uniform, masking/absorbing and more) in discrete spaces -- shape reverse dynamics and the ELBO. The presentation is layered for three audiences: newcomers seeking a self-contained intuitive introduction; diffusion practitioners wanting a global theoretical synthesis; and continuous-diffusion experts looking for an analogy-first path into discrete diffusion. The result is a unified roadmap to modern diffusion methodology across continuous domains and discrete sequences, highlighting a compact set of reusable proofs, identities, and core theoretical principles."
publication: '*arXiv preprint*'
publication_short: '*arXiv*'
links:
url_pdf: https://arxiv.org/abs/2512.05092
---
