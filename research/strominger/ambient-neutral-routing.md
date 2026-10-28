# Ambient neutral routing versus structure-dependent response

## Controlled comparison

The edge-seven opposite-edge routing trial produces 294 reversible N channels. To determine whether these are localized by the P/E structure, embed the observation region in a larger native carrier lattice and remove the P/E occupancy in the reference. Retain the N carrier geometry and the same opposite-edge routing rule.

Trace the larger reference paths, restrict each trace to the original observation window, and compare the complete local pass sequence (up to reversal). Do not compare raw whole-domain counts: the larger lattice contains additional routes that never enter the object window.

The hypothesis being tested is limited: a neutral fibre skeleton persists in the absence of occupied P/E cells. This is not an independently derived vacuum field.

## Actual result

For edge seven:

- Actual occupied P/E cells: 448; reference occupied P/E cells: zero.
- Local channels compared: **294**.
- Exact ambient matches: **294**.
- Added/changed channels: **0**; removed/changed channels: **0**.
- Local passes compared: **1,386**, all retained.
- Every channel extends beyond **both** observation-window endpoints in the surrounding carrier.
- No closed strands occur under this routing rule.
- Enlarging the ambient sector by a second shell leaves the restricted comparison unchanged.

All tested sizes 1, 3, 5 and 7 give the same identity-response conclusion. The test confirms what the current algorithm implies: its routing reads N geometry but never reads P/E occupancy.

## Interpretation

The 294 routes are **ambient-matched neutral channels under this reference**, not evidence for 294 localized neutrons. Conversely, zero detected response is **not a claim of zero physical neutrons**. The model still lacks a P/E-dependent neutral routing or state-coupling law; `localizedNeutronCount` is explicitly null.

No routes, cells, modes or voids are deleted from their source inventories. There remain 231 geometric N cells and 85 enclosed filler voids under the separate occupancy/positive-area connectivity convention. A future P/E-dependent law must be compared against the same ambient reference and preserve strand multiplicity; its parameters must not be chosen merely to yield 126.

## Viewer

In the single-octahedron **N tube routing trial**, the new **Structure-dependent routes only** overlay filters out exact ambient matches. It is empty for the current rule. The panel and table show 294 ambient-matched and zero changed/new routes, while stating that localized neutron content remains undefined. The existing all-directions and single-direction overlays remain available for comparison.

## Verification

`tests/ambient-neutral-routing.test.mjs` checks all four sizes, complete trace coverage, extension beyond both window ends, two ambient shell sizes, reversal invariance, detection of a changed trace, duplicate-channel rejection and preservation of the cell/void inventories. The viewer browser tests verify the response-only filter and explicit unresolved neutron count.

Sources: `research/strominger/ambient-neutral-routing.mjs`, `research/realization-tower/single-octahedral-process.mjs`.
