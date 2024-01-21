---
# Documentation: https://wowchemy.com/docs/managing-content/

title: SE(3)-Stochastic Flow Matching for Protein Backbone Generation
subtitle: ''
summary: 'We present **FoldFlow** a novel flow matching model for protein design. We present theory and practical tricks for flow models over SE(3)^N. Empirically, we validate these models on protein backbone generation of up to 300 amino acids leading to high-quality designable, diverse, and novel samples.'
authors:
- Avishek Joey Bose
- Tara Akhound-Sadegh
- Kilian Fatras
- Guillaume Huguet
- Jarrid Rector-Brooks
- Cheng-Hao Liu
- Andrei Cristian Nica
- Maksym Korablyov
- Michael Bronstein
- admin
author_notes:
- Equal Contribution
- Equal Contribution
tags: ["flow-matching"]
categories: ["archival"]
date: '2024-01-20'
lastmod: 2023-10-18T12:30:34-04:00
featured: true
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: 'FoldFlow for protein backbone generation'
  focal_point: 'Right'
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: [flow-matching]
publishDate: '2023-10-18T16:30:34.273370Z'
publication_types:
- 'paper-conference'
abstract: 'The computational design of novel protein structures has the potential to impact numerous scientific disciplines greatly. Toward this goal, we introduce $\text{FoldFlow}$ a series of novel generative models of increasing modeling power based on the flow-matching paradigm over $3\text{D}$ rigid motions -- i.e. the group $\text{SE(3)}$ -- enabling accurate modeling of protein backbones. We first introduce $\text{FoldFlow-Base}$, a simulation-free approach to learning deterministic continuous-time dynamics and matching invariant target distributions on $\text{SE(3)}$. We next accelerate training by incorporating Riemannian optimal transport to create $\text{FoldFlow-OT}$, leading to the construction of both more simple and stable flows. Finally, we design $\text{FoldFlow-SFM}$ coupling both Riemannian OT and simulation-free training to learn stochastic continuous-time dynamics over $\text{SE(3)}$. Our family of $\text{FoldFlow}$ generative models offer several key advantages over previous approaches to the generative modeling of proteins: they are more stable and faster to train than diffusion-based approaches, and our models enjoy the ability to map any invariant source distribution to any invariant target distribution over $\text{SE(3)}$. Empirically, we validate our FoldFlow models on protein backbone generation of up to $300$ amino acids leading to high-quality designable, diverse, and novel samples.'
publication: 'To appear in *ICLR* (Spotlight)'
url_pdf: http://arxiv.org/abs/2310.02391
url_code: https://github.com/DreamFold/FoldFlow
url_video: https://www.youtube.com/watch?v=JqKzTdhW7fY
links:
- name: Logg Video
  url: https://www.youtube.com/watch?v=EPxDI0ytfQU
---
