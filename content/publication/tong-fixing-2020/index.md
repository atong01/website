---
title: "Fixing Bias in Reconstruction-based Anomaly Detection with Lipschitz Discriminators"
date: 2020-09-21
publishDate: 2020-07-04T22:16:45.026157Z
authors: ["Alexander Tong", "Guy Wolf", "Smita Krishnaswamy"]
publication_types: ["1"]
catagories: ["Conference"]
abstract: "Anomaly detection is of great interest in fields where abnormalities need to be identified and corrected (e.g., medicine and finance). Deep learning methods for this task often rely on autoencoder reconstruction error, sometimes in conjunction with other errors. We show that this approach exhibits intrinsic biases that lead to undesirable results. Reconstruction-based methods are sensitive to training-data outliers and simple-to-reconstruct points. Instead, we introduce a new unsupervised Lipschitz anomaly discriminator that does not suffer from these biases. Our anomaly discriminator is trained, similar to the ones used in GANs, to detect the difference between the training data and corruptions of the training data. We show that this procedure successfully detects unseen anomalies with guarantees on those that have a certain Wasserstein distance from the data or corrupted training set. These additions allow us to show improved performance on MNIST, CIFAR10, and health record data."
featured: true
publication: In *30th IEEE International Workshop on Machine Learning for Signal Processing*
publication_short: In *IEEE MLSP*
categories: ["Conference"]

links:
- name: Arxiv
  url: https://arxiv.org/abs/1905.10710
url_code: https://github.com/KrishnaswamyLab/LAD
url_video: https://youtu.be/142Pgj0m2lU
url_slides: "LAD MLSP 2020.pdf"
---
