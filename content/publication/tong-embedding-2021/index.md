---
title: "Embedding Signals on Knowledge Graphs with Unbalanced Diffusion Earth Mover's Distance"
date: 2021-01-01
publishDate: 2021-07-27T13:56:12.593331Z
authors: ["Alexander Tong", "Guillaume Huguet", "Dennis Shung", "Amine Natik", "Manik Kuchroo", "Guillaume Lajoie", "Guy Wolf", "Smita Krishnaswamy"]
publication_types: ["3"]
abstract: "In modern relational machine learning it is common to encounter large graphs that arise via interactions or similarities between observations in many domains. Further, in many cases the target entities for analysis are actually signals on such graphs. We propose to compare and organize such datasets of graph signals by using an earth mover's distance (EMD) with a geodesic cost over the underlying graph. Typically, EMD is computed by optimizing over the cost of transporting one probability distribution to another over an underlying metric space. However, this is inefficient when computing the EMD between many signals. Here, we propose an unbalanced graph earth mover's distance that efficiently embeds the unbalanced EMD on an underlying graph into an L1 space, whose metric we call unbalanced diffusion earth mover's distance (UDEMD). This leads us to an efficient nearest neighbors kernel over many signals defined on a large graph. Next, we show how this gives distances between graph signals that are robust to noise. Finally, we apply this to organizing patients based on clinical notes who are modelled as signals on the SNOMED-CT medical knowledge graph, embedding lymphoblast cells modeled as signals on a gene graph, and organizing genes modeled as signals over a large peripheral blood mononuclear (PBMC) cell graph. In each case, we show that UDEMD-based embeddings find accurate distances that are highly efficient compared to other methods."
featured: false
publication: "arXiv"
tags: ["Computer Science - Machine Learning", "Electrical Engineering and Systems Science - Signal Processing"]

url_code: https://github.com/KrishnaswamyLab/DiffusionEMD
url_pdf: https://arxiv.org/pdf/2107.12334.pdf
links:
- name: Arxiv
  url: https://arxiv.org/abs/2107.12334

---

