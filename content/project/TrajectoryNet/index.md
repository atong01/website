---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Modeling Cellular Dynamics from Single-cell Data"
summary: ""
authors:
  [
    "Alexander Tong",
    "Jessie Huang",
    "Guy Wolf",
    "David van Dijk",
    "Smita Krishnaswamy",
  ]
tags: []
categories: []
date: 2020-07-13T10:07:43-04:00

# Optional external URL for project (replaces project detail page).
external_link: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

links:
  - name: Arxiv
    url: https://arxiv.org/abs/2002.04461
url_code: https://github.com/KrishnaswamyLab/TrajectoryNet
url_video: https://youtu.be/uEEbC3KI8RM
url_slides: "TrajectoryNet ICML 2020.pdf"

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
---

Single-cell transcriptomics is a powerful technology that allows for high resolution understanding of cell state, however, this measurement also destroys the cell. We therefore only have access to population-level measurements of cell state over time. The task of _trajectory inference_ tries to recover individual cell trajectories from these population-level measurements.
