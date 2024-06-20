---
layout: archive
title: "Research Overview"
permalink: /research/
author_profile: true
---

I am an observational astronomer and an observational cosmologist by training. My academic research interests can be broadly classified into two categories: understanding and constraining physics from large cosmological datasets and developing statistical models to analyze such datasets. During my Ph.D. I mostly focused on understanding how a novel tracer of the Large-Scale Structures, the Emisison-Line Galaxies (ELGs), can be used to [constrain cosmological models]({{ site.baseurl }}{% link _research/elgs.md %}) in the context of the [Dark Energy Spectroscopic Instrument (DESI)](https://www.desi.lbl.gov/).

Currently, I am co-leading the Lyman-Break Galaxies Topical Team within the [Dark Energy Science Collaboration](https://lsstdesc.org/). Our goal is to constrain cosmological models using data from the 2 < z < 5 redshift Universe.

Additionally, I have worked on various Milky Way-related observational projects such as [characterizing the high-velocity clouds in the Milky Way halo]({{ site.baseurl }}{% link _research/fermi-bubbles.md %}), [characterizing T Tauri stars in the Orion OB1 association]({{ site.baseurl }}{% link _research/t-tauri.md %}), and [measuring the height of the Sun above the Milky Way plane]({{ site.baseurl }}{% link _research/solar-height.md %}). 

As a new postdoc, I am now excited to venture into Machine Learning and Artificial Intelligence-driven projects and to understand how we can use these powerful techniques to study our Universe with unprecedented precision. I am also interested in exploring the bridge between theory and observation - how do we know that we have learned something new about a model from data? If you are interested in collaborating, please reach out! 

{% include base_path %}

{% assign ordered_pages = site.research | sort:"order_number" %}

{% for post in ordered_pages %}
  {% include archive-single.html type="grid" %}
{% endfor %}