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
#  - block: collection
#    id: news
#    content:
#      title: Recent News
#      subtitle: ''
#      text: ''
#      # Page type to display. E.g. post, talk, publication...
#      page_type: post
#      # Choose how many pages you would like to display (0 = all pages)
#      count: 5
#      # Filter on criteria
#      filters:
#        author: ""
#        category: ""
#        tag: ""
#        exclude_featured: false
#        exclude_future: false
#        exclude_past: false
#        publication_type: ""
#      # Choose how many pages you would like to offset by
#      offset: 0
#      # Page order: descending (desc) or ascending (asc) date.
#      order: desc
#    design:
#      # Choose a layout view
#      columns: '2'
#      view: community/date-title-summary
#      # Reduce spacing
#      spacing:
#        padding: [0, 0, 0, 0]
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
---
