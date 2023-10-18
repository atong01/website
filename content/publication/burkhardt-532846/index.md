---
title: "Quantifying the effect of experimental perturbations in single-cell RNA-sequencing data using graph signal processing"
date: 2021-02-08
authors: ["Daniel B. Burkhardt", "Jay S. Stanley", admin, "Ana Luisa Perdigoto", "Scott A. Gigante", "Kevan C. Herold", "Guy Wolf", "Antonio J. Giraldez", "David van Dijk", "Smita Krishnaswamy"]
publication_types: ["article-journal"]
abstract: "Single-cell RNA-sequencing (scRNA-seq) is a powerful tool to quantify transcriptional states in thousands to millions of cells. It is increasingly common for scRNA-seq data to be collected in multiple conditions to measure the effect of an experimental perturbation. However, quantifying differences between scRNA-seq datasets remains an analytical challenge. Previous efforts at quantifying such differences focus on discrete regions of the transcriptional state space such as clusters of cells. Here, we describe a continuous measure of the effect of an experiment across the transcriptomic space with single cell resolution. First, we use the manifold assumption to model the cellular state space as a graph with cells as nodes and edges connecting cells with similar transcriptomic profiles. Next, we calculate an Enhanced Experimental Signal (EES) that estimates the likelihood of observing cells from each condition at every point in the manifold. We show that the EES has useful properties for analysis of single cell perturbation studies. We show that we can use the magnitude and frequency of the EES, using an algorithm we call vertex frequency clustering, to identify specific populations of cells that are or are not affected by an experimental treatment at the appropriate level of granularity. Using these selected populations we can derive gene signatures of affected populations of cells. We demonstrate both algorithms using a combination of biological and synthetic datasets. Implementations are provided in the MELD Python package, which is available at https://github.com/KrishnaswamyLab/MELD."
featured: false
publication: "In *Nature Biotechnology*"
links:
- name: BioRxiv
  url: "https://www.biorxiv.org/content/early/2020/08/01/532846"
url_code: https://github.com/KrishnaswamyLab/MELD
url_paper: https://doi.org/10.1038/s41587-020-00803-5
doi: "10.1101/532846"
---

