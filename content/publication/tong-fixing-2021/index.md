---
title: "Fixing Bias in Reconstruction-based Anomaly Detection with Lipschitz Discriminators"
date: 2021-11-23
publishDate: 2021-11-23
authors: [admin, "Guy Wolf", "Smita Krishnaswamy"]
publication_types: [article-journal]
abstract: "Anomaly detection is of great interest in fields where abnormalities need to be identified and corrected (e.g., medicine and finance). Deep learning methods for this task often rely on autoencoder reconstruction error, sometimes in conjunction with other penalties. We show that this approach exhibits intrinsic biases that lead to undesirable results. Reconstruction-based methods can sometimes show low error on simple-to-reconstruct points that are not part of the training data, for example the all black image. Instead, we introduce a new unsupervised Lipschitz anomaly discriminator (LAD) that does not suffer from these biases. Our anomaly discriminator is trained, similar to the discriminator of a GAN, to detect the difference between the training data and corruptions of the training data. We show that this procedure successfully detects unseen anomalies with guarantees on those that have a certain Wasserstein distance from the data or corrupted training set. These additions allow us to show improved performance on MNIST, CIFAR10, and health record data. Further, LAD does not require decoding back to the original data space, which makes anomaly detection possible in domains where it is difficult to define a decoder, such as in irregular graph structured data. Empirically, we show this framework leads to improved performance on image, health record, and graph data."
summary: "We fix unwanted biases in standard deep anomaly detection with a new architecture. Extended from IEEE MLSP (2020) version."
featured: false
publication: In *Journal of Signal Processing Systems*

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: "Top"
  preview_only: false

url_pdf: https://arxiv.org/abs/1905.10710
url_code: https://github.com/KrishnaswamyLab/LAD
url_video: https://youtu.be/142Pgj0m2lU
url_slides: "LAD MLSP 2020.pdf"
---

