---
title: "Abstract 2839: Understanding the mesenchymal-to-epithelial transition and its drivers in triple-negative breast cancer with continuous normalizing flows"
date: 2021-01-01
publishDate: 2021-07-07T14:51:48.664228Z
authors: [admin, "Beatriz P. San Juan", "Brandon Zhu", "Christine L. Chaffer", "Smita Krishnaswamy"]
publication_types: ["abstract"]
abstract: "Here we focus on understanding mechanisms that
drive dynamic changes in gene expression and epigenetic marks that enable
triple negative breast cancer cells to change states, and to thereby invade
tissues and seed secondary tumors. The epithelial-to-mesenchymal transition
(EMT) facilitates invasion and migration away from the primary tumor site.
However, it is increasingly apparent that the reverse process, the
mesenchymal-to-epithelial transition (MET), enhances metastatic colonization
and growth via reacquisition of the epithelial phenotype. With no therapies
currently available to stop metastatic tumor growth, we aim to uncover the
mechanisms driving the MET towards identifying novel anti-metastatic therapies.
We use the 3D in vitro mammosphere model system where single tumor-initiating
cells residing in a partial-EMT state develop into a 3D organoid over 30 days.
We sampled cells at 5 time points and performed scRNA-seq and scATAC-seq to
analyze cell states. We develop a novel computational model of cellular
development based on the theory of dynamic optimal transport (OT) and
continuous normalizing flows. Our model TrajectoryNet is a neural ODE (ordinary
differential equation) network that models the gradient of cell state with
respect to time continuously over the input space and over time from
cross-sectional single-cell data. TrajectoryNet interpolates between collected
timepoints and learns a continuous realistic progression that describes
cellular evolution in terms of gene expression and chromatin accessibility. Key
to TrajectoryNet is a unique regularization to penalize the magnitude of the
gradient over the flow. We prove this results in dynamic OT, thereby
discouraging the neural network from taking circuitous or unrealistic paths. In
contrast to TrajectoryNet, pseudotime, and RNA velocity are best at analyzing
within a particular timepoint and do not handle large gaps in timepoints. We
compare TrajectoryNet to RNA velocity and static OT and show that TrajectoryNet
achieves better trajectories in terms of predicting withheld timepoints. Using
TrajectoryNet, we identify a continuous ordering of events that occur during
MET that show when and how the epithelial cell states begin to emerge. Such a
continuous ordering can give rise to causal associations that can be inhibited
to alter MET mechanisms. We also differentiate between trajectories that show
self-renewal and maintenance of the tumor-initiating cells, and trajectories
that revert to an epithelial state. Further we find that only ~10% of the
initial seeded cells develop into mammospheres and identify which initial cells
have the potential to seed secondary tumors. Hence, we can refine features
(gene and epigenetic states) that define aggressive tumor-initiating cells in
triple negative breast cancer, as well as their dynamics through the MET in
order to find therapeutic targets."
featured: false
publication: "American Association of Cancer Research"
publication_short: "AACR"
url_pdf: "https://cancerres.aacrjournals.org/content/81/13_Supplement/2839"
doi: "10.1158/1538-7445.AM2021-2839"
---

