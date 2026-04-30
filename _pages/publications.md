---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
You can also find my articles on <a href="{{author.googlescholar}}">my Google Scholar profile</a>.
{% endif %}

{% include base_path %}

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
