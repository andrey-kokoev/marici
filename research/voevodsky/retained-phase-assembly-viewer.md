# Retained phase links in the assembly viewer

Source: `papers/witness-generators/proton-neutron-assembly.html`.
Generated site asset: `website/public/experiments/proton-neutron-assembly.html`.

Stages 7–8 add optional coefficient-plane guides at facet centroids, with an integer source-phase control and play/pause/reset. Earlier exploded geometry stages remain unchanged. The pair-comparison view keeps its existing, separately labelled conjugate-coefficient illustration.

## Display contract

- Existing spatial edges remain solid, including projected fourth-dimensional edges. Projection is not a complex-edge classifier.
- Nonzero nontrivial order-3/order-5 Fourier channels are dotted. Their classification persists through return and does not depend on the instantaneous imaginary component.
- Each ray depicts the phase of a representative nonzero coordinate of a vector Fourier coefficient, with normalized display length. It is not a spatial displacement, occupied bond, energy or amplitude scale.
- The source geometry supplies the facet-centroid orbits; their DFT is computed in the browser. The proton uses the first supplied order-3 generator that moves each facet (not a single global trajectory). The belt uses its C3 action; the electron uses the five-cycle on the unprojected regular 4-simplex.
- Moving facet counts are 4 / 6 / 5. Two fixed neutron cap-centroid channels remain as real, solid guides, without adding cap solids to the belt.
- The guide census is **not** the native triangle-mode census. Recovering 12 proton and 18 belt modes, and 21 belt seam projectors, requires ordered geometry and native adapters. The page explains this distinction.
- Five-cell electron spinor/energy transport remains open. No particle mass, binding, isotope stability, charge-conjugation or autonomous-storage result is inferred.

## Verification

```sh
python research/voevodsky/checkers/prepare_assembly_ledger_asset.py
node research/voevodsky/checkers/check_unified_assembly_page.mjs
```

The browser checker exercises both source and generated asset, all existing stages, focus modes, pair comparison, isotope arrangements and mobile layouts. Added checks cover dotted materials and line-distance attributes, 4/6/5 moving facets and two fixed caps, exact centroid decoding and metric preservation at all fifteen return steps, phase-return guide positions, visibility and playback/reset.

Receipts: `results/assembly_ledger_asset.json`, `results/unified_assembly_browser.json`. Visual inspection snapshots: `results/retained_phase_assembly.png`, `results/retained_phase_neutron.png`.

Related research: [relative geometry mode motion](relative-geometric-reversible-mode-motion.md), [phase / energy bridge](geometric-phase-energy-bridge.md), [persistence frontier](phase-occupation-persistence-frontier.md).
