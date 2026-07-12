---
layout: archive
title: "Research Overview"
permalink: /research/
author_profile: true
---

I am an observational cosmologist who uses the largest galaxy surveys to test our models of the Universe, and who builds the statistical and machine-learning methods that turn that data into physics. My work is anchored in the [Dark Energy Spectroscopic Instrument (DESI)](https://www.desi.lbl.gov/) — where I am a **builder** and **co-lead the Photo-z Topical Team** — and in the [Dark Energy Science Collaboration (DESC)](https://lsstdesc.org/), where I **co-lead the Lyman-Break Galaxies Topical Team**.

My research falls into a few connected themes, from cross-correlating galaxies with the cosmic microwave background, to pushing cosmology into the high-redshift Universe, to the inference methods that decide what we can actually learn from data. Explore them below.

I am increasingly excited about bringing Machine Learning and Artificial Intelligence to bear on these problems — using these techniques to study our Universe with unprecedented precision. I am also drawn to the bridge between theory and observation: how do we actually *know* that we have learned something new about a model from data? If you are interested in collaborating, please [reach out](mailto:tanveer.karim@utoronto.ca)!

{% include base_path %}

<div class="home-research" style="margin-top:2em;">
{% assign ordered_pages = site.research | sort:"order_number" %}
{% for post in ordered_pages %}
  {% assign img = post.card_image | default: post.header.og_image %}
  <a class="rcard rcard__link" href="{{ base_path }}{{ post.url }}">
    {% if img %}
    <div class="rcard__media"><img src="{{ img | prepend: '/images/' | prepend: base_path }}" alt="{{ post.title }}"></div>
    {% endif %}
    <div class="rcard__body">
      <h3 class="rcard__title">{{ post.title }}</h3>
      {% if post.blurb %}<p class="rcard__blurb">{{ post.blurb }}</p>{% endif %}
      <span class="rcard__more">Read more &rarr;</span>
    </div>
  </a>
{% endfor %}
</div>