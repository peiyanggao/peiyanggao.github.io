---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---


You can also find my articles on <a href="{{author.googlescholar}}">my Google Scholar profile</a>.


{% include base_path %}

<style>
.archive__subtitle {
  color: #1a1a1a !important;
  font-weight: 700 !important;
  font-size: 1.5em !important;
  margin-top: 1.5em !important;
  margin-bottom: 0.6em !important;
  padding-bottom: 0.3em !important;
  border-bottom: 1px solid #e5e5e5 !important;
}
</style>

{% assign ordered_pubs = site.publications | sort: "date" | reverse %}

{% for category in site.publication_category %}
{% assign category_slug = category[0] %}
{% assign category_title = category[1].title %}
{% assign cat_pubs = ordered_pubs | where: "category", category_slug %}
{% if cat_pubs.size > 0 %}

<h2 class="archive__subtitle">{{ category_title }}</h2>

{% for post in cat_pubs %}
{% include archive-single.html %}
{% endfor %}

{% endif %}
{% endfor %}
