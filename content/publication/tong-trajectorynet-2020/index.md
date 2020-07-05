---
title: "TrajectoryNet: A Dynamic Optimal Transport Network for Modeling Cellular Dynamics"
date: 2020-07-12
publishDate: 2020-06-14T22:16:45.026157Z
authors: ["Alexander Tong", "Jessie Huang", "Guy Wolf", "David van Dijk", "Smita Krishnaswamy"]
publication_types: ["1"]
abstract: "It is increasingly common to encounter data from dynamic processes captured by static crosssectional measurements over time, particularly in biomedical settings. Recent attempts to model individual trajectories from this data use optimal transport to create pairwise matchings between time points. However, these methods cannot model continuous dynamics and non-linear paths that entities can take in these systems. To address this issue, we establish a link between continuous normalizing flows and dynamic optimal transport, that allows us to model the expected paths of points over time. Continuous normalizing flows are generally under constrained, as they are allowed to take an arbitrary path from the source to the target distribution. We present TrajectoryNet, which controls the continuous paths taken between distributions. We show how this is particularly applicable for studying cellular dynamics in data from single-cell RNA sequencing (scRNA-seq) technologies, and that TrajectoryNet improves upon recently proposed static optimal transport-based models that can be used for interpolating cellular distributions."
featured: true
publication: In *Proceedings of the 37th International Conference on Machine Learning*
publication_short: In *ICML*

links:
- name: Arxiv
  url: https://arxiv.org/abs/2002.04461
url_code: https://github.com/KrishnaswamyLab/TrajectoryNet
url_video: https://youtu.be/uEEbC3KI8RM
url_slides: "TrajectoryNet ICML 2020.pdf"
tags: ["Computer Science - Computer Vision and Pattern Recognition", "Computer Science - Machine Learning", "Quantitative Biology - Quantitative Methods", "Statistics - Machine Learning"]
---

