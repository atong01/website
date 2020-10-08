---
title: "Uncovering the Folding Landscape of RNA Secondary Structure with Deep Graph Embeddings"
date: 2020-08-01
publishDate: 2020-10-08T13:56:06.782239Z
authors: ["Egbert Castro", "Andrew Benz", "Alexander Tong", "Guy Wolf", "Smita Krishnaswamy"]
publication_types: ["3"]
categories: ["Under Review"]
abstract: "Biomolecular graph analysis has recently gained much attention in the emerging field of geometric deep learning. While numerous approaches aim to train classifiers that accurately predict molecular properties from graphs that encode their structure, an equally important task is to organize biomolecular graphs in ways that expose meaningful relations and variations between them. We propose a geometric scattering autoencoder (GSAE) network for learning such graph embeddings. Our embedding network first extracts rich graph features using the recently proposed geometric scattering transform. Then, it leverages a semi-supervised variational autoencoder to extract a low-dimensional embedding that retains the information in these features that enable prediction of molecular properties as well as characterize graphs. Our approach is based on the intuition that geometric scattering generates multi-resolution features with in-built invariance to deformations, but as they are unsupervised, these features may not be tuned for optimally capturing relevant domain-specific properties. We demonstrate the effectiveness of our approach to data exploration of RNA foldings. Like proteins, RNA molecules can fold to create low energy functional structures such as hairpins, but the landscape of possible folds and fold sequences are not well visualized by existing methods. We show that GSAE organizes RNA graphs both by structure and energy, accurately reflecting bistable RNA structures. Furthermore, it enables interpolation of embedded molecule sequences mimicking folding trajectories. Finally, using an auxiliary inverse-scattering model, we demonstrate our ability to generate synthetic RNA graphs along the trajectory thus providing hypothetical folding sequences for further analysis."
featured: false
publication: "Under Review"

url_pdf: https://arxiv.org/abs/2006.06885

---

