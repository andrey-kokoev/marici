---
layout: page
title: Isotope wiring
description: Edit working isotope definitions and review validation, delta replay, and export limitations.
---

<script setup>
import IsotopeWiring from '../.vitepress/components/IsotopeWiring.vue'
</script>

<div class="isotope-wiring-page">

# Isotope wiring

Select an isotope, inspect or edit its cells, and compare absolute or delta wiring definitions. Use **File** to import or export your work.

**Research model—not established nuclear geometry.** [Validation and export limits](/experiments/isotope-wiring-limitations).

<ClientOnly><IsotopeWiring /></ClientOnly>

These diagrams and counts describe working constructions, not established nuclear geometry or isotope stability. See also the [isotope / R-space viewer](/experiments/isotope-space).

</div>

<style>
.isotope-wiring-page { max-width: 1440px; margin: 0 auto; padding: 32px 24px; }
.isotope-wiring-page h1 { margin: 0 0 12px; font-size: 28px; font-weight: 600; letter-spacing: -.035em; }
.isotope-wiring-page p { margin: 16px 0; color: var(--vp-c-text-2); line-height: 1.7; }
.isotope-wiring-page a { color: var(--vp-c-brand-1); text-decoration: underline; }
@media (max-width: 600px) { .isotope-wiring-page { padding: 24px 12px; } }
</style>
