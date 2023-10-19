---
title: "MURAL: An Unsupervised Random Forest-Based Embedding for Electronic Health Record Data"
date: 2021-12-13
publishDate: 2021-12-13
summary: "A unsupervised random tree distance for missing data in EHR"
authors: ["Michal Gerasimiuk", "Dennis L. Shung", "Alexander Tong", "Adrian J. Stanley", "Machael Shultz", "Jeffrey Ngu", "Loren Laine", "Guy Wolf", "Smita Krishnaswamy"]
author_notes:
- Equal Contribution
- Equal Contribution

categories: ["archival"]
publication_types: ["paper-conference"]
abstract: "A major challenge in embedding or visualizing clinical patient data is the heterogeneity of variable types including continuous lab values, categorical diagnostic codes, as well as missing or incomplete data. In particular, in EHR data, some variables are {\em missing not at random (MNAR)} but deliberately not collected and thus are a source of information. For example, lab tests may be deemed necessary for some patients on the basis of suspected diagnosis, but not for others. Here we present the MURAL forest -- an unsupervised random forest for representing data with disparate variable types (e.g., categorical, continuous, MNAR). MURAL forests consist of a set of decision trees where node-splitting variables are chosen at random, such that the marginal entropy of all other variables is minimized by the split. This allows us to also split on MNAR variables and discrete variables in a way that is consistent with the continuous variables. The end goal is to learn the MURAL embedding of patients using average tree distances between those patients. These distances can be fed to nonlinear dimensionality reduction method like PHATE to derive visualizable embeddings. While such methods are ubiquitous in continuous-valued datasets (like single cell RNA-sequencing) they have not been used extensively in mixed variable data. We showcase the use of our method on one artificial and two clinical datasets. We show that using our approach, we can visualize and classify data more accurately than competing approaches. Finally, we show that MURAL can also be used to compare cohorts of patients via the recently proposed tree-sliced Wasserstein distances."
featured: false
publication: In *IEEE International Conference on Big Data*
publication_short: In *IEEE Big Data*


# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
#image:
#  caption: "Embedding Distributions based on Diffusion EMD"
#  focal_point: "Top"
#  preview_only: false

links:
- name: Arxiv
  url: https://arxiv.org/abs/2111.10452
- name: Tweetorial
  url: https://twitter.com/KrishnaswamyLab/status/1471852935428689920?s=20&t=sxgkKOqRneKIf3AmEpJJBA
url_code: https://github.com/KrishnaswamyLab/MURAL
tags: ["OT", "Trees", "EHR"]
---

