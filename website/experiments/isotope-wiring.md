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

Choose an isotope and select a cell. Use **Add / Remove** to edit, or **Try another placement** to compare an alternative.

**Research model—not established nuclear geometry.** [Validation and export limits](/experiments/isotope-wiring-limitations).

<p><a id="wiring-full-window" href="/experiments/isotope-wiring-standalone.html" target="_blank" rel="noopener">Open full-window editor</a> · <a id="wiring-download" href="/experiments/isotope-wiring-standalone.html" download="isotope-wiring.html" target="_self">Download standalone HTML</a></p>

<ClientOnly><IsotopeWiring /></ClientOnly>

<details class="editor-help"><summary>Using checks, alternatives, and saved work</summary>

The catalog includes all 13 stable isotopes before oxygen: H-1/2, He-3/4, Li-6/7, Be-9, B-10/11, C-12/13 and N-14/15. Their inventories are established; their diagram placements are illustrative seeds and explicitly unresolved.

**Counts** shows structural checks and record differences. Expand a finding and choose **Inspect** to locate its cell. Question marks identify unresolved placement; passing checks do not remove that uncertainty.

**Try another placement** offers EP and neutron-line alternatives within a shell. Configure a destination, then **Review comparison** before keeping a separate alternative. **Test placement alternatives** checks other destinations in small batches without choosing a physical placement.

Applied graph edits are saved in this browser when storage is available. Unapplied Wiring text is retained separately; **Download text draft** preserves it as a file. Export a project through **File** before moving applied work to a downloaded editor. Browser storage does not travel with the HTML file, and project exports do not include unapplied text drafts.

Hosted and direct-file editors use the same structural core. Storage and basic editing still use the legacy engine; passing checks do not certify full-definition replay or physical adequacy. See also the [isotope / R-space viewer](/experiments/isotope-space).

</details>

</div>

<style>
.isotope-wiring-page { max-width: 1440px; margin: 0 auto; padding: 32px 24px; }
.isotope-wiring-page h1 { margin: 0 0 12px; font-size: 28px; font-weight: 600; letter-spacing: -.035em; }
.isotope-wiring-page p { margin: 16px 0; color: var(--vp-c-text-2); line-height: 1.7; }
.isotope-wiring-page a { color: var(--vp-c-brand-1); text-decoration: underline; }
@media (max-width: 600px) { .isotope-wiring-page { padding: 24px 12px; } }
</style>
