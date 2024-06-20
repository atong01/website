---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Sequence-Augmented SE(3)-Flow Matching For Conditional Protein Backbone Generation
subtitle: ''
summary: ''
authors:
- Guillaume Huguet
- James Vuckovic
- Kilian Fatras
- Eric Thibodeau-Laufer
- Pablo Lemos
- Riashat Islam
- Cheng-Hao Liu
- Jarrid Rector-Brooks
- Tara Akhound-Sadegh
- Michael Bronstein
- admin
- Avishek Joey Bose
author_notes:
- Equal Contribution
- Equal Contribution
- ""
- ""
- ""
- ""
- ""
- ""
- ""
- ""
- Equal advising
- Equal advising
tags: []
categories: []
date: '2024-05-30'
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
projects: [flow-matching]
publishDate: '2024-06-20T13:20:28.098896Z'
publication_types:
- article
abstract: 'Proteins are essential for almost all biological processes and derive their diverse functions from complex 3D structures, which are in turn determined by their amino acid sequences. In this paper, we exploit the rich biological inductive bias of amino acid sequences and introduce FoldFlow-2, a novel sequence-conditioned SE(3)-equivariant flow matching model for protein structure generation. FoldFlow-2 presents substantial new architectural features over the previous FoldFlow family of models including a protein large language model to encode sequence, a new multi-modal fusion trunk that combines structure and sequence representations, and a geometric transformer based decoder. To increase diversity and novelty of generated samples -- crucial for de-novo drug design -- we train FoldFlow-2 at scale on a new dataset that is an order of magnitude larger than PDB datasets of prior works, containing both known proteins in PDB and high-quality synthetic structures achieved through filtering. We further demonstrate the ability to align FoldFlow-2 to arbitrary rewards, e.g. increasing secondary structures diversity, by introducing a Reinforced Finetuning (ReFT) objective. We empirically observe that FoldFlow-2 outperforms previous state-of-the-art protein structure-based generative models, improving over RFDiffusion in terms of unconditional generation across all metrics including designability, diversity, and novelty across all protein lengths, as well as exhibiting generalization on the task of equilibrium conformation sampling. Finally, we demonstrate that a fine-tuned FoldFlow-2 makes progress on challenging conditional design tasks such as designing scaffolds for the VHH nanobody.'
publication: 'arXiv'
links:
- name: arXiv
  url: https://arxiv.org/abs/2405.20313
---
