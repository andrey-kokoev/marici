# Four-simplex bridge: induced equation-family presentation

## Checked result

`agda/FourSimplexEquationBridge.agda` extends the fixed-boundary tetrahedron
bridge to four-dimensional fillers while retaining all five independent
boundary tetrahedron maps.

For fixed vertices, ten edges, ten triangles, a supplied four-tetrahedron horn
`h` and fifth tetrahedron `t`, `Bridge.old-fourcell-equivalence` proves:

```agda
F.FourCell h t ≃ OldFourCell (to-equation-horn h) (equivFun e1234 t)
```

`filled-equivalence` lifts this to whole filled packages, including the horn,
missing tetrahedron and four-cell witness. Both roundtrips are proved.
`boundary-square` proves that translating a filled package and extracting its
five-tetrahedron boundary agrees with independently translating that boundary.
The supplied horn and fifth tetrahedron are preserved definitionally by the
forward package map.

## Important scope limit

This is an **induced equation-family presentation**, not a proof of equality
with a separately chosen pentagon equation. At the time this module was built,
there was no independent old-style four-cell definition. The follow-up
[marked pentagon construction](four-simplex-pentagon-bridge.md) now supplies
that definition and its completion theorem, but not the comparison coherence.

`OldFourCell` accepts only old tetrahedron witnesses, but its interval-indexed
family is constructed by decoding the first three supplied old tetrahedra to
Cubical ones and applying the proved tetrahedron comparison to each moving
slice. Its endpoint tetrahedra are the supplied old witnesses, not replacements
derived by solving a horn. Thus the theorem is a genuine fixed-boundary
four-cell equivalence, but the target family still depends on the chosen
Cubical presentation through that construction.

The remaining independent-presentation task is to compare the now-defined
concatenation-based pentagon relation to `OldFourCell`, including the higher
associator and whiskering coherence. `FourSimplexPentagonBridge` isolates a
necessary and sufficient `CenterCoherence` condition. No such identification
is claimed by this module or its receipt audit.

## Construction

- `e0123`, `e0124`, `e0134`, `e0234`, `e1234` instantiate the same proved
  `TetrahedronPresentationBridge.FixedBoundaryTarget.equivalence` on the five
  face slots. Shared triangles use the same J-based triangle map.
- `horn-equivalence` translates the four supplied tetrahedra componentwise;
  `boundary-equivalence` adds the independent fifth tetrahedron. Both boundary
  roundtrips are named explicitly.
- `moving-edges` and `moving-surface` exhibit each slice of a Cubical four-cell
  as a marked tetrahedron. `slice-equivalence` translates it to the old
  tetrahedron equation space. `slice-start` and `slice-end` identify its endpoint
  maps with `e0234` and `e1234` by reflexivity.
- `fourcell-equivalence` applies Cubical's `congPathEquiv` to the family of slice
  equivalences. `fourcell-map` identifies its forward function pointwise.
- To obtain a target indexed entirely by old horn data,
  `old-fourcell-equivalence` reindexes along `cubical-horn-recovered` **with the
  fifth tetrahedron held fixed**, then uses `correct-start-fiber` and the section
  law for `e0234`. This supplies the exact old initial endpoint.
- `old-completion-equivalence` and `filled-equivalence` use dependent-sum
  equivalences to retain all witnesses. `supplied-horn-preserved`,
  `old-fifth-tetrahedron-preserved` and `boundary-square` record boundary
  compatibility.
- `old-unique` proves contractibility of the induced completion space as a
  dependent singleton. `old-completion-square` compares the complete generated
  pairs, not merely their missing tetrahedra.

The tetrahedron equivalence's implementation is now `abstract`: higher clients
use its boundary-indexed type and equivalence laws without repeatedly unfolding
the full route proof. This changed no theorem statement or mathematical
assumption. All source modules remain `--safe --cubical --guardedness`.

## Verification

Fresh checks passed for `PathUnitCoherence`, `FourSimplexHorn`,
`TetrahedronPresentationBridge`, and `FourSimplexEquationBridge`, using
`check_cubical_agda.ps1 -Module <Module> -Fresh`.
All four receipts report `passed: true`, `ignore_interfaces: true`, stable inputs,
and source hashes independently matched to the files. Only the pre-existing
`TypedGeneratorLayers` import warning remains.

The new module's receipt finished at 2026-10-05T05:37:23Z, source SHA-256
`187fa4c53a884e0dc952cf7750a0ace87688fcb2dfff567204d3a340c8bccef5`.
The nonconstant `TypedFixture` checks both the fixed-horn and whole-package
roundtrips and the completion squares.

Both receipt audits passed against that source inventory (historical receipts;
new source additions require refreshed owner-inventory evidence):

- `check_tetrahedron_presentation_bridge.py`
- `check_four_simplex_equation_bridge.py`, classified as
  `induced_equation_family_fourcell_bridge_checked`.

No independent pentagon equivalence, SCC execution, graph admission, commit or
ledger publication is claimed.
