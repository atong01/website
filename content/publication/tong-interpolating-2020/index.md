---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Interpolating Optimal Transport Barycenters of Patient Manifolds"
authors: [admin, "Smita Krishnaswamy"]
date: 2020-06-01
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2020-10-08T12:04:15-04:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: [abstract]

# Publication name and optional abbreviated publication name.
publication: "28th Conference on Intelligent Systems for Molecular Biology"
publication_short: "In *ISMB*"

abstract: "Single-cell data is now being collected across many patients in varying conditions. However, data is still relatively expensive. This opens up the opportunity for computational methods to decrease overall cost by inferring a single-cell measurement based on similarity to the meta-data of other similar samples. We examine this problem with an optimal transport perspective. This allows us to leverage a variant of the Sinkhorn algorithm for extremely computationally efficient approximations of transport along discrete manifolds. Our method first constructs the manifold between samples, then aligns this to the manifold of patients, and finally applies this to interpolate a barycenter sample along this manifold. We show first that we are able to better interpolate samples between timepoints than existing methods e.g. Waddington-OT (Schiebinger et al. 2019 Cell) by accounting for structure between multiple timepoints instead of pairs. We then show when the relationship between patients is an inferred manifold, how to impute a patient’s single-cell measurements based on other similar single-cell samples by aligning the manifold of patients with that of single-cell measurements. When the manifold of patients exhibits non-linear but intrinsically low-dimensional structure, we are able to more accurately infer a single-cell measurement."

# Summary. An optional shortened abstract.
summary: ""

tags: []
categories: []
featured: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_pdf:
url_code:
url_dataset:
url_poster: ISMB_2020.pdf
url_project:
url_slides: https://f1000research.com/slides/9-836
url_source:
url_video: https://youtu.be/oBPDV1pfqPg

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
