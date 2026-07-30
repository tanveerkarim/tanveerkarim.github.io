---
title: "Robust Inference & Machine Learning for Cosmology"
layout: single-portfolio
excerpt: "<img src='/images/research/methods.svg' alt=''>"
collection: research
order_number: 30
card_image: "research/methods.svg"
blurb: "Building the statistical and machine-learning machinery — model selection, emulators, systematics control — that decides what we can actually learn from cosmological data."
header:
  og_image: "research/methods.svg"
tags:
  - cosmology
  - statistics
  - machine-learning
---

# From data to knowledge

A measurement is only as trustworthy as the method behind it. Much of my work sits on the
**bridge between theory and observation**: how do we know we have genuinely learned something
new about a model from data — rather than fooled ourselves with a systematic or an
over-flexible fit? This theme collects the statistical and machine-learning methods that make
the cosmology defensible.

# Selected threads

- **Observational systematics in large-scale structure.** In [Karim et al. (2023),
  *MNRAS*](https://arxiv.org/abs/2305.11956) — first author — I identified a new systematic:
  the bias introduced when *measuring* the imaging-systematics weights themselves distorts the
  galaxy power spectrum and, in turn, cosmological inference.
- **Model selection for dark energy.** Applying the expected log pointwise predictive density
  (**ELPD**) as a principled criterion in the $w_0 w_a$-versus-$\Lambda$CDM debate — asking
  which dark-energy model the data actually prefer, and by how much. Because ELPD decomposes
  point by point, it can also identify *which* measurements drive a preference:
  **[try the interactive DESI DR2 leave-one-tracer-out explorer]({{ site.baseurl }}/teaching/elpd/)**.
- **Faster inference with emulators** *(student-led).* Improving the
  [COSMOPOWER](https://github.com/alessiospuriomancini/cosmopower) emulator through
  hyper-parameter tuning, to accelerate cosmological likelihood evaluation.
- **Forecasting a redshift-evolving σ₈** *(student-led).* Forecasting how well an
  LSST-era analysis could constrain a **redshift-evolving $\sigma_8$** model — a direct handle
  on the growth-of-structure tension.
