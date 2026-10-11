# Tetrahedron presentation bridge: fixed-boundary equivalence proved

## Result and scope

`agda/TetrahedronPresentationBridge.agda` now supplies
`FixedBoundaryTarget.equivalence : FixedBoundaryTarget.Goal`.
For any type, four vertices, six fixed edges and four Cubical triangle witnesses,
it gives an equivalence between the Cubical tetrahedral filler and the earlier
concatenation-based tetrahedral filler, with **all four faces translated by the
same context-independent triangle comparison**.

`Bridge.Horn.route-naturality : RouteNaturality` and
`Bridge.Horn.face-naturality : FaceNaturality` are proved terms, not supplied
assumptions. The former horn-relative restriction on the tetrahedron bridge is
therefore removed. No truncation, proof irrelevance, postulates or holes are used.

The canonical `FourSimplexHorn.triangle-comparison` has been restored to its
original J-based definition (`triangle-comparison-J`). The temporary selection
of `triangle-comparison-by-pasting` was not needed: the original map admits a
sweep-coherence proof once the propositional J computation is handled explicitly.
The pasting-based alternative remains available, but equality between the two
choices is **not** claimed. This result is for the original J-based face map.

The theorem translates each fixed-boundary tetrahedron independently of the
surrounding horn, so shared triangles use the same map. A full equivalence of
4-dimensional filler presentations is not constructed in this module. The
follow-up [four-simplex equation bridge](four-simplex-equation-bridge.md) now
proves a fixed-five-tetrahedron four-cell equivalence to an induced equation
family, not an independently defined pentagon relation. Geometric
opposing-face-to-vertex maps also remain explicit input structure.

## Proof structure

1. **Horn-relative equivalence.** Transport in the family of triangles determined
   by faces 012 and 013, followed by the old route equivalences, gives
   `fourth-face`. `filler-equivalence` translates fillers over that derived map;
   `completion-equivalence` translates the complete fourth-face/filler pair.
   Both inverse laws retain the witnesses. Contractibility of completion spaces
   proves `complete-then-translate` and `translate-then-complete`.
2. **Comparison versus sweep.** `FourSimplexHorn.triangle-comparison-J-sweep`
   uses path induction, the explicit `JRefl` computation path, and
   `Square→compPath` applied to inverse left-unit naturality. Thus the selected
   comparison of a triangle `t` is homotopic to
   `sym (triangle-sweep p q r t) ∙ sym (lUnit r)`.
   `triangle-sweep-cancel` gives the corresponding cancellation law.
3. **Moving route.** `comparison-pathover` maps the transported triangle through
   the comparison family. `route-from-equation` whiskers by the moving initial
   segment and uses sweep tails and the associator to land in the fixed old
   route space. `transported-route-line` connects its endpoints.
4. **Terminal endpoint.** `route-line-end` removes two inserted left units with
   `sym (lUnit ...)`, identifying the terminal route with `route123`.
5. **Initial endpoint.** The sweep cancellation identifies the right boundary;
   `left-sweep-factor` handles the left boundary.
   `unit-whisker-normalize` proves the remaining unit naturality and cancellation.
   `route-start-from-unit-associativity` reduces the initial endpoint to
   `cong (_∙ q) (lUnit p) ∙ sym (assoc refl p q) ≡ lUnit (p ∙ q)`.
6. **Unit/associator coherence.** `agda/PathUnitCoherence.agda` proves that last
   equation as `left-unit-assoc`. In the reflexive case, write
   `h = rUnit refl`: the associator is the antidiagonal of the square obtained by
   composing `h` with itself. An explicit square, unit naturality and cancellation
   prove the base case; two path inductions extend it to all composable paths.
7. **Closure.** `unit-associativity` instantiates that theorem.
   `route-naturality` joins the endpoint proofs to the moving route;
   `from-route-naturality` gives `face-naturality`. The already established
   `fixed-face-equivalence` then yields `FixedBoundaryTarget.equivalence`.

Failed reflexivity and contractible-space projection probes were removed. They
were not evidence of inequality. In particular, the successful unit coherence
uses an explicit square, not an assumption that arbitrary higher paths are equal.

## Graded 2 → 1 → 0 projections and opposing incidence

`TriangleProjection` proves all three edge-package projection squares
and their six endpoint laws definitionally: translation retains the marked
vertices and edges.

`OpposingVertexProjection.Projection` supplies a function from triangle packages
to an omitted vertex together with its designated value. Transport through the
triangle equivalence preserves that value by the checked roundtrip.
`TetrahedralOpposingProjections.Projections` packages four such functions and
value laws. `recoverVertices` and `omitted-vertices-recovered` recover the full
vertex tuple; the corresponding old-face projections satisfy the same laws.

`OpposingFaceIncidence` separately gives the canonical slot-level incidence map:
012 ↦ 3, 123 ↦ 0, 013 ↦ 2, 023 ↦ 1. Its vertex recovery is definitional and
unchanged under triangle translation. This map uses a face slot **in its ambient
marked tetrahedron**. No recovery of an omitted vertex from a bare triangle is
asserted.

## Computation API for higher-dimensional clients

The exported `equivalence` implementation remains abstract. Its new
`equivalence-route-computation` and `equivalence-sweep-computation` theorems
identify its forward function with an explicit route formula and then a
corrected direct sweep of the supplied filler. Naturality of the inverse
section and transport in path families prove the first formula.
`PathSweepCoherence.mapped-pathover-pasting` proves the second using an explicit
square. These theorems describe the existing map; they do not replace it.
See the [pentagon bridge note](four-simplex-pentagon-bridge.md) for their use on
all five tetrahedra of a four-cell.

## Verification

The initial proof passed fresh checks of `PathUnitCoherence`, `FourSimplexHorn`
and `TetrahedronPresentationBridge`. After the computation API addition, fresh
checks of `PathSweepCoherence` and `TetrahedronPresentationBridge` passed;
the latter rechecks the complete dependency closure with ignored interfaces.

The current bridge receipt reports `passed: true`, `ignore_interfaces: true`,
and stable inputs, with its source SHA-256 independently matched. It finished at
2026-10-05T12:56:30Z with SHA-256
`140984c2dcd6fa9f70855b2bf8b8bd485dfa81ba25e95848ef3b034bea14817c`.
The theorem type and chosen equivalence are unchanged.
Logs and receipts are `results/agda-{Module}.{log,json}`.
Only the pre-existing `TypedGeneratorLayers` import warning remains.

The checked nonconstant `TypedFixture` includes
`independently-translated-filler` and `fixed-boundary-roundtrip`, in addition to
the earlier horn-relative completion tests.
`check_tetrahedron_presentation_bridge.py` passes its receipt audit with
classification `fixed_boundary_tetrahedron_bridge_checked`.

No SCC execution, graph admission, commit or ledger publication is claimed.
