---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: about.biography
    id: about
    content:
      title: About Me
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
      count: 4
    design:
      columns: '2'
      view: card
  - block: collection
    id: preprints
    content:
      title: Preprints
      filters:
        folders:
          - publication
        publication_type: article
        exclude_featured: false
      count: 0
    design:
      columns: '2'
      view: citation
  - block: collection
    id: publications
    content:
      title: Publications
      filters:
        folders:
          - publication
        category: archival
        exclude_featured: false
      count: 0
    design:
      columns: '2'
      view: citation
---
