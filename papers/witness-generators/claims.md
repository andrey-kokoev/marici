# Tutorial evidence map

The tutorial explains standard constructions; it does not claim a new construction principle. No Agda or checker code changed during the final editorial revision.

## Main example

| Claim | Source | Evidence boundary |
| --- | --- | --- |
| Selected-step interface | `research/nima/agda/TypedGeneratorLayers.agda` | `Layer1 ℓ` uses a common level for states and witnesses |
| Indexed refinement composition | `research/nima/agda/ComposableWitnessSpecialization.agda` | Supplied leaf refinements; dependent admission/edge pairs; source metadata retained separately |
| Full-step preservation | Same module, `Composite.correct` | State and complete-step isomorphisms, endpoint compatibility, selected-step preservation; no extra semantic naturality claim |
| Matched ordinary/WG behavior | `research/voevodsky/agda/WGRefinementComparison.agda` | Quantified state/edge/generator/map equalities; fixed source values |
| Matched library reuse | `research/voevodsky/agda/WGRefinementLibraryComparison.agda` | Same tests, identical except module/import names; all comparison proofs remain `refl` |
| Ordinary structural helper | `research/voevodsky/agda/SigmaReassociation.agda` | Generic dependent-sum reassociation; no WG-specific premise |
| Evidence-erasure rejection | `research/voevodsky/agda/negative/WGRefinement{Baseline,Library,Client}Bad.agda` | Each fails with the intended Boolean mismatch, exit 42 |

Fresh local checking and the independent internal rerun passed two positive compilations and three negative controls. The latter was performed in the existing checkout. See `matched-comparison.md` and `research/voevodsky/results/wg-refinement-comparison.json`.

## Wider library: historical evidence only

`research/nima/agda/CoherentWitnessSpecialization.agda` contains canonical pentagon and triangle results. `DisplayedWitnessSpecialization.agda` gives the displayed interpretation and conditional category bridge. Their earlier logs are under `research/voevodsky/results/wg-ucc-audit/`. Units and four-layer coherence were not independently rerun for this tutorial. Neither arbitrary higher coherence nor arbitrary refinement transport is inferred from those results.

The tutorial's `Source` field is auxiliary metadata at a higher universe, not part of the compiled complete-step type. The fixed-source comparisons do not constitute an arbitrary-source experiment.

## Disposition

The independent review found the fixed mathematics correct, the baseline fair for capability and structural-proof reuse, and the exposition useful as tutorial/library documentation. We adopted that scope. No standalone research-publication claim is pursued here.

Unverified matters remain limits, not a queue of required expansion: clean-checkout reproducibility, compiler builtin pinning, comprehensive related work, runtime performance and global minimality. The separate Wolfram note is outside the tutorial and has its own historical evidence.
