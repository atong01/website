---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: about.biography
    id: about
    content:
      title: Biography
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
  - block: collection
    id: featured
    content:
      title: Featured Publications
      filters:
        folders:
          - publication
        featured_only: true
    design:
      columns: '2'
      view: card
  - block: collection
    content:
      title: Publications
      filters:
        folders:
          - publication
        publication_types:
          - article-journal
        exclude_featured: false
      count: 0
    design:
      columns: '2'
      view: citation
  - block: collection
    content:
      title: Preprints
      filters:
        folders:
          - publication
        publication_types:
          - preprint
        exclude_featured: false
      count: 0
    design:
      columns: '2'
      view: citation
---
