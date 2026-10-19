# Selected witnessed steps: a Cubical Agda tutorial

Read [the tutorial](main.md). It explains selected witnessed steps, proof-dependent refinement and complete-step preservation using standard dependent constructions.

The matched comparison shows that ordinary Cubical dependent-sum isomorphisms provide the same structural proof machinery. WG's remaining convenience is refinement assembly and certificate packaging—not new mathematics. Independent internal review found the fixed example correct and pedagogically useful, and recommended library/tutorial documentation rather than a standalone research paper. This package follows that recommendation.

## Particle assembly navigation

The proton/electron assembly pages in this directory are separate from this
tutorial. For their constructors, cycles and assembly measures, start with
[the arrow assembly guide](../../docs/arrow-assembly.md).

## Run the examples

From the repository root, with Python, Agda 2.8.0 and Cubical 0.9:

```text
python research/voevodsky/checkers/check_wg_refinement_comparison.py
```

Set `AGDA` and `CUBICAL_DIR` for another installation. Expect two positive compilations and three intended Boolean-mismatch rejections. The checker verifies independent ordinary imports and comparison tests identical except for module/import names.

Sources are under `research/voevodsky/agda/`: `WGRefinementBaseline`, `WGRefinementLibraryBaseline`, `SigmaReassociation`, `WGRefinementClient`, and the two comparison modules. Results and compiler logs are under `research/voevodsky/results/wg-refinement-*`.

The independent rerun used the existing checkout, not a clean installation. The known `TypedGeneratorLayers` import warning about `isPropIsContr` remains. This tutorial makes no performance or extracted-code correctness claim.

## Supporting material

- [Matched comparison](matched-comparison.md): implementation details, controls, counts and reproduction limits.
- [Evidence map](claims.md): tested scope and historical coherence pointers.
- [Contribution review](contribution-review.md): background literature and the comparison's development.
- [Review record](review-brief.md): independent review findings and applied corrections.
- `references/sources.json`: literature source provenance.

The older Wolfram example is retained separately in [its archived note](appendix-wolfram.md); it is not part of this tutorial.
