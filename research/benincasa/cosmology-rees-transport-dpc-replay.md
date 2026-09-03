# DPC replay for pole-order cokernel transport

## Problem

Determine whether an order-two reduced cokernel detector transports to pole order three, and separate target detection, operator annihilation, and degree persistence.

## Bold conjecture

There is an exact order-two reduced left-null functional that detects both target powers, and after normalization its difference from the order-three functional is a correction driven solely by the pole-shift term on every polynomial input degree.

## Named rivals

1. No order-two cokernel representative detects the order-three target.
2. A simultaneous detector exists, but only on bounded numerator caps.
3. The correction exists algebraically as a difference of representatives, but its interpretation through the pole-shift term fails when the base detector ceases to annihilate the extended order-two domain.
4. Modular existence does not lift over the rationals.

## Risky consequences

- A simultaneous detector must annihilate every declared order-two column and pair nontrivially with both target powers over the rationals.
- For `delta = mu3 - nu`, exact evaluation must give `delta M3 = -nu M3` on every declared order-three column.
- The stronger identity `delta M3 = nu T` requires `nu M2 = 0` at the same degree.
- Persistence requires testing every omitted degree that overlaps the functional's output support, not merely the first degree beyond the order-three caps.

## Strongest falsification attempt and exact residual

Dependency-free CRT reconstruction produced a 300-term order-two detector `nu`. Exact replay annihilates all 692 construction columns; its pairings with target powers `R^3` and `R^4` are respectively `8348485609619780297/45672560141036648371200` and `1`. The 344-term difference `delta = mu3 - nu` satisfies `delta M3 = -nu M3` on all 1308 tested order-three columns.

The stronger pole-shift interpretation fails outside the construction caps. Exact degree-local evaluation finds its first residual at level 1 degree 20, with 42 failing columns. Additional failures occur at level 1 degree 21 and level 0 degrees 16 through 19, for 218 failures total. The earlier `persistent: true` result tested the wrong boundary and was overwritten before graph admission.

## Disposition with surviving scope

A rational simultaneous-target representative exists at order two, and its exact difference from the chosen order-three detector repairs order-three annihilation on the tested 1308 columns. The claim that this correction is solely induced by the pole-shift term is rejected beyond the order-two construction caps. No canonical, persistent, or all-pole-order transport is established. The next admissible test is to reconstruct the simultaneous detector at caps `(21,19)` and retest every degree overlapping its support.

## Durable verification

- `research/benincasa/results/cosmology_rees_affine_transportable_representative.json`
- `research/benincasa/results/cosmology_rees_affine_dual_correction_order2_to3.json`
- `research/benincasa/results/cosmology_rees_affine_correction_driven_by_T.json`
- `research/benincasa/results/cosmology_rees_affine_localized_certificates_replay.json`
