---
layout: archive
title: "Photography"
permalink: /portfolio/
author_profile: true
---

A collection of film photographs I have taken over the years.

{% include base_path %}

{% for post in site.portfolio %}
  {% include archive-single.html %}
{% endfor %}

This is an item in your portfolio. It can be have images or nice text. If you name the file .md, it will be parsed as markdown. If you name the file .html, it will be parsed as HTML. 
