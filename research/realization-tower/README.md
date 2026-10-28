# Realization Tower — research home

This is the home and prior-work index for the **Realization Tower**. Established
constructions and the operator's proposed geometric synthesis are distinguished
in [definition.md](definition.md). Original owner files remain authoritative;
this directory indexes them rather than copying or moving them.

## Recursive interface realization — working proposal

[Approach and experimental status](../strominger/recursive-interface-realization-approach.md):
retain the central P and revised P,E,N,N boundary, insert coherence between them,
then turn each new interface into a layer (3→5→9→17 radial levels).
Records the proposed two-cycle interpretation and stage-relative attachment rules.
Geometric probes retain identities and consistent seams; native typing, directed
edge transport, unit-length growth and the esd7 binding remain open.

## Space viewer

[Realization lattice — space-only Three.js viewer](../../examples/realization-lattice/README.md)
constructs the four repeated plane families, equal-length intersection edges and
inspectable local neighbour stars. Run `pnpm lattice:dev`; the generated website
route is `/experiments/realization-lattice/index.html`. No coherence search or
particle assignment is included.

## Four-channel P–E rod study

[Open the interactive rod study](four-channel-rod.html), served from the repository
root over HTTP. Process 3 also links to it. This separate view retains four
labelled center-to-vertex channels at k=1..7, marks the V1 P–E rod, and switches
between center-fixed and E-vertex-fixed reference frames. Drag to rotate.

It uses the existing envelope and center-containment geometry, including the
k=1 shared seed and even-size multiple center pieces. Straight channels are
schematic endpoint relations: no lattice paths, transport laws, N fillers or
particle assignments are derived. Changing size is a geometric family, not yet
a witnessed growth operation. Other boundary vertices are not assigned E.

Verification: `node --test tests/four-channel-rod.test.mjs` and
`node scripts/test-four-channel-rod.mjs` (prints screenshots/audit directory).

## Coherence pyramid / esd7: full layout and seven-stage transport

**Start here for the existing coherence pyramid**, also named
`esd_7(Delta^3)`: a tetrahedron with seven elementary intervals per edge.
Its full incidence census is already available; do not replace it with an
unrelated square or infer its coherence from matching counts.

| Resource | What to reuse |
|---|---|
| [Explicit esd7 analytical-prototype bridge](../strominger/esd7-analytical-binding-v1.md) | 343 source registry entries bound by a finite sorting construction;588 shared faces retain both contexts, including294 H123/H234 comparisons.24 checks pass; no analytical filler or global field operator is inferred. |
| [Source-generated full esd7 geometry](../strominger/esd7-attachment-channel-v1.md) | 345 source-rule records reconstruct all1807 labelled geometric cells and shared signed incidence without reading the census;25 checks pass. The114-record convention and analytical/field witnesses remain open. |
| [Executable native channel and assembler](../strominger/native-retained-channel-v1.md) | 23 typed records derive14 packet presentations and18 interfaces; history/context recovery and all44-channel readout squares pass. Bounded fixture, not yet the full114-record/esd7 construction. |
| [Single-channel esd7 assembly conjecture](../strominger/single-channel-esd7-assembly-conjecture.md) | Serialize the retained1+4×28+1 construction into one ordered channel; conjecture an operator reconstructing the full esd7 incidence and coherence presentation. |
| [Native joint-field assembly sewing](../strominger/joint-field-assembly-sewing-v1.md) | Positive exact extension of the prior44-channel candidate over14 retained packets and18 interfaces; native readout squares and both E exits pass, with histories and all five coefficients retained. |
| [Executable whole-FCC evolution candidate](../strominger/global-fcc-evolution-candidate-v1.md) | One120-site dynamical update plus lossless whole-complex fibration; all1807 source rows retained;28 steps executed. Coherence/norm checks pass, but the independently defined native E endpoint fails. |
| [Task-relative selector test](../strominger/task-relative-retained-transport-conjecture.md) | Same state and broad realization-advance task still admit two continuations at8 N markings. Fixed-carrier versus cross-face requirements distinguish them where available;16 N markings admit neither. |
| [Intrinsic-selector conjecture and native falsifier](../strominger/intrinsic-retained-selector-conjecture.md) | 96 identical retained-source forks with192 certified E continuations. Native admissibility, history and exit coherence do not uniquely select the next operation kind. |
| [Native P/N/E end-to-end binding test](../strominger/native-fcc-end-to-end-binding.md) | Actual T184→T242→T256 replay and retained coefficients; seven native views disagree with the quarter-rotated flag at the final two positions. Central duality is not required by this replay. |
| [Central cell-to-dual-vertex handoff](../strominger/central-dual-cell-handoff-v1.md) | Explicit complementary-degree cellular duality on T184; four equal dual volumes; all15 coefficients retained; signed S4 covariance and24 dual descending windows. |
| [Route-face and central chain/dual binding](../strominger/fcc-face-flag-binding-v1.md) | 224 actual route-comparison faces, 24 seven-presentation flags; ascending chain inclusions and descending dual restrictions; central representation-change interface isolated. |
| [FCC-first transport and carried subdivisions](../strominger/fcc-first-sector-transport-v1.md) | Twelve sector-labelled root moves; all24 S4 frames; 119 tetrahedra and56 octahedra; three frame-related esd7 splits; 224 retained diagonal-route comparison faces. |
| [Seven-stage extraction and central flags](../strominger/esd7-seven-stage-handoff-v1.md) | Fresh all-cell signed rotation audit; central cell T184; 24 actual flags with profile 1,2,3,4,3,2,1; separates central passage from outer conductor paths. |
| [Recovered coherence-layout guide](../strominger/esd7-coherence-layout-recovery.md) | Prior-source map, face equations, analytical prototypes, and the distinction between seven stages per chart and four stages per cycle. |
| [Full geometric census](../voevodsky/results/esd7_explicit_analytical_census.json) / [builder](../voevodsky/checkers/check_esd7_explicit_analytical_census.py) | Stable IDs for 120 vertices, 560 edges, 784 faces and 343 tetrahedra, with shared boundaries. |
| [Analytical coverage ledger](../voevodsky/eight-node-lattice-analytical-form-coverage-ledger.md) | Full geometric/semantic registry and its verification scopes; operation dependencies and residual-carrying face/filler data. |
| [First tetrahedron's coherence equations](../voevodsky/the-first-elementary-conductor-tetrahedron-has-four-transfer-equations-and-one-higher-coherence-equation.md) | Six transfers, four face comparisons, one tetrahedral comparison-of-comparisons, with polarity. |
| [Four-chart suspension helix](../voevodsky/a-clean-universal-category-for-the-eight-lattice-four-chart-suspension-system.md) | Typed chart handoff `q u = rho(u) q`, `rho^4=1`, `q^4=Sigma`; retained grade versus visible orientation. |
| [Full esd7 graded realization](../nima/full-esd7-graded-tate-torus-realization.md) | All-cell realization under the stated maximal designation profile. |
| [Global 28-stage P/E conjecture](../strominger/global-28-stage-pe-fibration-conjecture.md) | Current four-seven-stage-block proposal and contextual-window endpoint binding; not yet a derived evolution. |

**Maintained net recommendation (revision73):**
The [131-node typing review](../strominger/persistent-seam-pe-node-typing-review-v28.md) restores the existing signed parent H234 as input. Construct K on parent presentations/arrows/cell, with its compositor and actual native boundary identifications; retain the finite representative and then form the inverse mate and both coupled completions. The kernel/current proposals are deferred pending typed parent-model functors. Scalar reconstruction and additive defect calculus are not substitutes for this transport. No native realization or positive/Pb completion is claimed.

Historical revision72 recommendation (superseded):
[Two OPEN mechanisms](../strominger/f736-two-witness-lift-conjectures-v27.md) now address the hard witness gap: canonical polarized-kernel realization, and actual cutoff-current transgression. Start with the finite-regulator derivative and its boundary terms; the independent alternative tests an explicit kernel-to-witness map. Neither is verified, neither is a joint prerequisite for the broader task, and neither follows from scalar remainder decay. Both have concrete first tests and falsifiers. Full K and both coupled fillers remain open.

Previous recommendation context:
The [representative-bearing readout comparison](../strominger/f736-prior-representative-bearing-boundary-target-v26.md) records the actual T,V,E boundary families on the grid and a scalar comparison-groupoid presentation of the existing rapid quotient. The OPEN lift must identify the parent natural arrows and H234 in the intended native presentation enhancement. Response-chart inversion, scalar comparison and relative-feature isometry have different types; full K and both coupled fillers remain open.

Previous recommendation context:
The [six-object native/word retained grid](../strominger/f736-prior-native-word-retained-comparison-grid-v25.md) is now a conditional derived result: its mixed squares retain the native field and admitted analytical coordinate records on the frozen packet. The OPEN witness-record lift is narrowed to the parent natural-arrow/modification interpretation on that grid, not another decoder or generic covariance construction. Full K and both dependent bottom/filler pairs over one H736 remain open. No all-observer surjectivity or external positive metric follows.

Previous recommendation context:
The [actual-constructor search](../strominger/f736-prior-actual-native-constructor-binding-v24.md) traces native NE15 and the already verified finite-packet equation `D15 U_NE=D5`. Its decoded source action is identity; fixed-cutoff physical covariance is available. The earlier mandatory recentering interpretation is withdrawn. The OPEN witness-record lift must compare native incident contexts with the fine-edge triangle and retained analytical modification, not re-prove readout covariance. Full K and both coupled fillers over one H736 remain open. Existing results are enriched without duplicate counting.

Earlier search context, subject to the correction above:
The [action-type search](../strominger/f736-prior-recentering-action-types-v23.md) records the explicit one-sector half-density/response dilation square and its endpoint/density laws. The OPEN native lift must distinguish fixed-observer cutoff-frame change, retained-label translation and simultaneous pair translation before identifying a constructor. Fine word edges preserve the recovered label; neither their existence nor the response square supplies the full ordered-boundary comparison K.
The [constructor-square search](../strominger/f736-prior-constructor-naturality-squares-v22.md) records actual relative-rigged successor, difference-row recentering and canonical/dual place-cutoff squares, plus the exact finite-step left-placement defect. The OPEN F736 lift must identify one native generator and compare its independently intended target action on the full centered record. Relative covariance does not erase left placement, volume/calibration or endpoints; neither vanishing nor nonvanishing of the placement defect is claimed.
The [centered-boundary search](../strominger/f736-prior-centered-cutoff-boundary-comparison-v21.md) adds three scoped conditional results: exact centered/relative/calibration decomposition, regulated H124 feature-plus-volume readout, and an external signed defect-augmented presentation comparison. The OPEN witness-record lift starts with K(eta24): account for finite reference calibration and prove one native naturality square with the actual transported regulator. No positive centered form, erased commutator, rapid-decay upgrade or native filler follows.
The [parent-signature search](../strominger/f736-prior-parent-modification-signature-v20.md) is attached to existing verified imports without duplicate result nodes. The recommended OPEN `f736-boundary-witness-record-graph-lift` now requires K on the actual Q_i presentation functors, eta_ij arrows and retained H234 modification, with native boundary identifications. Graph-set inverses are not presentation-functor comparisons. The signed parent signature and finite remainder exist; the native witness comparison remains unconstructed.
The [net's prior-research imports](../strominger/persistent-seam-pe-conjecture.md) now include seventy-three scoped conditionally verified research results, including an actual witness-preserving rigged graph lift on its own source, restricted prepared-sector output equivalence and formal stable enhancement. The OPEN `f736-boundary-witness-record-graph-lift` task is recommended: extend the carrier map to the actual H234 record and prove boundary/composition compatibility, rather than infer it from graph recovery. The OPEN comparison task explicitly distinguishes a source-retaining modification enhancement from actual output-defect maps; scalar remainders are not identified with operator defects without a typed realization. Candidate source round trips are available; native spectral-domain and modification identifications remain open. The common-target modification comparison remains the broader open task. These one-sector components are recorded in the still-open carrier/normalization tasks; operator-family, all-sector and native witness claims are not promoted. The frozen log2/PV component is recorded as established without promoting it to all-domain or native witness equality. Carrier instantiation and general native normalization retain their separate acceptance gates. The compact-physical half-density dictionary fixes endpoint/volume response observations at that sector's declared strength; general semilocal and native witness identifications remain open. Their fixed-cutoff, placement and source-bound qualifications remain explicit; the family and native witness bindings are not inferred. The OPEN `f736-response-cutoff-joint-graph-instantiation` task remains available; the separate modification-level `f736-source-retaining-common-target-comparison` remains open, with actual analytical boundary maps and both coupled bottom/filler pairs as its acceptance—not scalar observation inversion. The newly imported right-adjoint compositor-mate rule fixes F736's candidate direction as the inverse mate `C32 C43=>C42`; actual same-target analytical boundaries and the finite representative still need identification. These preserve the distinction between chart inversion, source-star polarity reversal and a modification mate; no completed native F736 reversal is inferred. The explicit conditional word-image remainder formula is available; its boundary/reverse-mate identification with the geometric F736 triangle remains open. These support an explicit five-word candidate table, not a verified analytical F736 binding; the remaining comparison must transport the actual face modification and its finite remainder. The target is their typed identification with actual F736 words and edges, preserving normalization, source authority limits and dependent bottom/filler witnesses. The formal presentation bridge preserves shared faces; it does not itself construct the analytical response-to-cutoff interpretation. The paired constructor is available; its actual analytical F736 instantiation remains open. The current target is the package `(H736,H745,H760,Theta324,Theta325)` with one shared F736 witness, not independent bottom and filler choices. Internal polarized-cell closure remains distinct from external physical volume/Green identification and the physical Schur bound. The parent analytical filler is available; its explicit binding to the retained F736 presentations remains open. These imports do not establish finite-cutoff equality or the external Green endpoint comparison.
[Attempt the actual retained P/N/E construction of Pb-208](../strominger/pb208-retained-construction-obligation-v1.md). The operator rejected preassembled-target transformations and untyped geometric filling as substitutes. Return a source-bound construction or a concrete failed attachment exposing the missing rule. The [first native batch attempt](../strominger/native-retained-batch-attempt-v1.md) now records a concrete NE/NN species conflict on one shared primitive, with valid separate continuations and15 checks. The [NE/NN comparison](../strominger/native-reader-comparison-v1.md) now has an exact five-slot intertwiner and12 checks, but does not preserve the current composition reader or supply native occurrence/context identification. A [pre-registered retained-total inventory test](../strominger/pb208-inventory-fibration-result-v1.md) now rejects that candidate as sufficient: it preserves the incompatible supplied inventories rather than supplying their comparison.22 checks pass, but no bridge or Pb construction is established. The [registered native-whole test](../strominger/native-whole-inventory-fixture-result-v1.md) now establishes a grounded chart-independent inventory but fails admission of the actual NE/NN pair across7 marked-root frames. The original18 field checks and9 new checks pass; neither pair binding nor Pb construction is inferred. The [prior-led N-reader atlas](../strominger/octahedral-reader-atlas-result-v1.md) now excludes an external port only under fixed-root N-only rules. The [registered screw-growth sewing test](../strominger/screw-field-sewing-result-v1.md) now passes19 checks on66 packets and all95 native interfaces of that24-body patch, with unchanged44-channel generators. The [registered geometric attachment test](../strominger/screw-esd7-geometric-attachment-result-v1.md) finds40 exact occupied embeddings, but no fully internalized reference embedding in its map family. Eleven checks identify a single external C0 shared by NE packets5 and15 in a diagnostic frame. The [registered relative attachment](../strominger/screw-esd7-relative-attachment-result-v1.md) now passes10 checks: native completion and all95 transfers validate on24 occupied target primitives while retaining the external reference and one unoccupied reference-only primitive. The [external-C0 finite trace](../strominger/external-c0-finite-trace-result-v1.md) now passes109 checks with the frozen encoder: C0 is the calibrated flux2A B_f(4), not recoverable from Mellin endpoints alone. The [actual NE fine-face lookup](../strominger/native-ne-fine-face-result-v1.md) now passes13 checks: the complete343-primitive coordinate bridge identifies F736, H134 in both T325 and T324, with E514/E539 versus E515. The [F736 physical readout comparison](../strominger/f736-physical-readout-result-v1.md) now passes47 checks:75 source entry enclosures at three cutoffs, both Hermitian/skew channels, and25 exact native matrix-unit squares. The [correlated-word realization](../strominger/f736-correlated-word-edges-result-v1.md) now passes31 checks and supplies conditional fine-edge maps while rejecting flattened-program composition. Its H234 component triangle is distinct from the unchanged local H134 registry roles. Next compare the intended witnesses across these presentations; strict cancellation and readout covariance do not supply the analytical filler. Any reader/carrier extension requires source support and prior registration. The esd7 attachment/analytical comparison remains a separate supporting frontier.
The [net](../strominger/contracts/persistent-seam-pe-conjecture-net.v1.json) records the native assembler, complete geometric attachment complex and explicit analytical-prototype bridge as conditionally verified. The [F006 comparison gate](../strominger/esd7-retained-face-comparison-v1.md) now passes12 synthetic implementation controls; actual face verification is blocked on source-bound operators/domains, frames and endpoint transport. The [source-binding audit](../strominger/esd7-parent-chart-binding-v1.md) now shows why bare parent-chart substitution cannot provide it:116 fine vertices have conflicting incident types. That [structural fine-vertex refinement is now constructed](../strominger/esd7-simplicial-refinement-v1.md) on all1807 cells with20 checks. Its [conditional strict-parent evaluation](../strominger/esd7-strict-parent-evaluation-v1.md) now passes21 checks, including F006 and5421 retained readout squares. The [native comparison side](../strominger/strict-native-comparison-v1.md) now has196 exact pairwise squares and2744 triangles, with coefficient witnesses retained. An [explicit compact five-packet encoder](../strominger/finite-observer-encoder-v1.md) now passes17 endpoint/flux reconstruction and native transport checks. The [signed endpoint term](../strominger/finite-packet-endpoint-form-v1.md) is now evaluated on all25 packet pairs and matched to the native readout, with18 checks. A [weighted Volterra/value-flux trace subproblem](../strominger/finite-packet-green-trace-v1.md) now also passes17 checks and detects a nonzero pairing between endpoint-invisible packets. A [finite cutoff-placement audit](../strominger/cutoff-regulator-placement-v1.md) now corrects an observer-leg rewrite that fails without extra commutation. The [actual archimedean even-sector cutoff kernel](../strominger/archimedean-cutoff-entry-v1.md) now bounds all20 off-diagonal packet entries at three cutoffs, with23 checks. The [common diagonal finite part](../strominger/archimedean-diagonal-limit-v1.md) now has an explicit representation and convergence bound, with19 checks controlling the entire centered packet-matrix limit. Its supporting frontier is witness-preserving analytical/native comparison; neither positivity nor a higher filler follows from that convergence. The114-record convention, full analytical/field binding and assembler/evolution synthesis remain open. This is an explicit work-plan recommendation, not a proof or automatic ranking.

**Latest channel implementation:**
`node research/strominger/checkers/check_native_retained_channel.mjs`.
See [reproduction](../strominger/native-retained-channel-v1.md) for the separate full-field replay on its reconstructed output.

**Current native gluing result:**
`node research/strominger/checkers/export_joint_field_sewing_fixture.mjs`, then
`python research/strominger/checkers/check_joint_field_assembly_sewing.py`.
The prior native joint-field candidate sews on a certified five-body assembly;
this is not yet an autonomous global clock.

**Earlier global dynamical candidate:**
`python research/strominger/checkers/check_global_fcc_evolution.py`.
This executes a nontrivial whole-field candidate, not another local uniqueness test.
Its native E endpoint comparison fails; the action/readout assumptions are explicit.

**Earlier task-selection gate:**
`node research/strominger/checkers/check_retained_transport_task_selection.mjs`.
Broad task specification does not ensure uniqueness; geometric task refinements are checked explicitly.

**State-only selection gate:**
`node research/strominger/checkers/check_intrinsic_retained_selector.mjs`.
The tested native uniqueness claim is falsified; the common evolution-step meaning remains to be specified.

**Native binding test:**
`node research/strominger/checkers/check_native_fcc_end_to_end.mjs`.
It distinguishes successful native transport from an unbound geometric analogy.

Geometry replay: `python research/strominger/checkers/check_fcc_first_transport.py`
for the ambient transport, then
`python research/strominger/checkers/check_esd7_seven_stage_handoff.py`
for the selected presentation, then
`python research/strominger/checkers/check_fcc_face_flag_binding.py`
for the actual route faces and chain/dual flag maps, then
`python research/strominger/checkers/check_central_dual_cell_handoff.py`
for the central complementary-degree dual-cell handoff.
The geometric extraction does not modify the original census. The shared-center
flag has seven cell presentations and six incidence transitions; the boundary
conductor has seven edges and does not pass through the center. Keep those
objects distinct when binding a stage law.

## Working diagram

```text
12 --9--> 6
 |        |
11 --8--> 5
 |        |
10 --7--> 4
```

The existing diagram has six object presentations and three horizontal transport
roles. The geometric proposal adds empty-simplex generation, source selection,
decorated join/link interpretation, forward/reverse realization, and boundary
quotients. It does not silently turn all nine numbers into serial state dimensions.

## Primary tower definitions and atlases

| Material | What to reuse |
|---|---|
| [Confirmed diagram and fixed reference](../nima/rung-transport-diagram-and-fixed-reference.md) | Labelled -> source-indexed -> target-indexed presentations; commuting squares; specified rung4 reference locus. Historical software-selection statements have the pinned successor below. |
| [Full nine-position atlas v2](../strominger/rung-symmetry-atlas-v2.md) | Object/map table, sectors, components, comparison leaves and symmetries of the candidate field-slot diagram. |
| [Atlas JSON](../strominger/rung-symmetry-atlas-v2.json) | Per-position roles, recovery, maps, numerical counterparts and gaps. |
| [Grading and orientation](../strominger/wg-grading-orientation-v1.md) | Typed rung/count/rank table; both endpoint quotients; histories and direction reversal. |
| [Earlier label/from/to recurrence](../nima/label-from-to-fibration-tower.md) | Retained-total recurrence and historical gauge assignments; a different schedule from the confirmed diagram. |
| [Pinned T9 software contract](../nima/pinned-T9-software-contract.md) | Selected inherited-key two-round incoming promotion, retained leaves, T8/T7 views and exact composition domain. |
| [Generating horizontal schedule](../strominger/generating-horizontal-schedule-v1.md) | Twelve primitive arrows to generated 137 comparison slots; explicit adapter to the numerical layer. |

## Geometric origin and current operator conjectures

| Material | What it supplies |
|---|---|
| [Ledger 4329: Joins and Cones as a Candidate Source Space](../../src/ledger/20261020-4329%20Joins%20and%20Cones%20as%20a%20Candidate%20Source%20Space.md) | Empty-simplex/join/cone proposal, fixed-base lift versus sections, exact geometric checks and source-incidence boundary. |
| [Join/cone checker](../voevodsky/checkers/check_join_cone_source_space.py) | Existing finite simplex and affine-cone checks; not a proof of native WG identification. |
| [Plane lattice and witnessing conjectures](../strominger/tetrahedral-plane-lattice-universal-witness-conjectures-v1.md) | Plane arrangement, self-witnessed reference, twelve-endpoint comparison, domain–codomain–witness projection, Hamiltonian dictionary and GR propagation proposal. |
| [Retained plane viewer](../../examples/tetrahedral-planes/) | Repository visualization context. |
| [Field comparison preparation](../strominger/field-comparison-preparation-v1.md) | Precise S5/U(1)=CP2 quotient versus distinct four-dimensional fixed-defect leaves. Not assigned to numbered rung4. |
| [Toroidal rung12 encoding](../strominger/toroidal-rung12-v1.md) | Earlier checked field encoding; not the definition of the proposed underlying space. |

The operator's local working reference is
`C:/Users/andrey/Downloads/tetrahedron_planes_free_rotation.html`. Its repeated
planes and intersections specify the discussed arrangement; the shaded solid
is a visual prop. The local file and repository viewer are pointers, not an
assertion that their current contents are identical.

## Quotients, reversal, continuation and reconstruction

| Material | What to reuse |
|---|---|
| [Retained square reversal](../nima/retained-square-reversal.md) | Actual reflected backward section, double-reflection identity and retained forward histories. |
| [Full-cycle reconciliation](../nima/full-cycle-prior-work-reconciliation.md) | Prior return, promotion, feedback and reconstruction inventory; distinguishes candidate generators. Read historical selection claims with the pinned T9 successor. |
| [Reconstruction-aware tower](../strominger/reconstruction-aware-tower-v1.md) | Retained transport, conditional field recovery, explicit operator fallback and separation from scalar averages. |
| [WG rehydration correction](../strominger/wg-I-squared-rehydration-correction.md) | Terminal quotient S/I, relation products and attachments; reusable package retains witnesses. No automatic rung-location assignment. |
| [Contextual equivalence](../nima/contextual-equivalence-needs-stabilized-congruence.md) | A lawful quotient must preserve authorized future continuations, not only present readout. |
| [Retained assembly](../strominger/wg-retained-assembly-v1.md) | Conditional common-source assembly with complete generation, comparison/filler and predecessor records. |
| [Staged factorization / half-step test](../strominger/wg-half-step-binding-v1.md) | Actual heterogeneous factorization of the generator; failed specific triangle-root binding. |

## Hamiltonian and Postnikov comparisons

| Material | Scope |
|---|---|
| [Deeper Postnikov/rung prior search](../strominger/postnikov-rung-deeper-prior-search-v1.md) | Separates presentation rung, coherence degree, realization and physical readout. |
| [Hamiltonian-compatible WG and Postnikov clues](../strominger/hamiltonian-descent-wg-and-postnikov-clues.md) | Conditional reducing interfaces and reconstruction; distinguishes actual Postnikov data from numerical labels. |
| [Top-down Hamiltonian descent](../strominger/source-arrow-hamiltonian-top-down-descent.md) | Independently constructed source-arrow generator and reducing schedule at its declared scope. |
| [Fixed-carrier Gram restriction tower](../nima/carrier-gram-restriction-tower.md) | Separate dimension-reducing model with explicit metric projections; not the retained presentation tower. |
| [Coherence-extension fibres](../nima/coherence-realization-depth-is-a-dependent-filler-tower-not-a-source-cutoff.md) | Dependent filler tower; coherence degree is not automatically rung number or time. |

## Join-factor transfer candidate

[Join-factor apex transfer](join-factor-apex-transfer-conjecture-v1.md) records
 the combined picture: A * (v * B) -> (A * v) * B, linking the output factor
and coning the input factor while retaining the whole. It realizes the proposed
3/12 through 11/4 arithmetic on marked simplex vertices. Its lattice-channel
and rung-diagram identification remains open; the transfer is not a quotient.

## Local tests

- [Actual seed and four-channel binding](seed-channel-binding-v1.md): reads the
  formal six-occurrence seed, distinguishes four target-indexed path families
  from primitive outgoing ports, retains a nontrivial return boundary, and
  reproduces the existing Boolean face-obstruction probe without adding a face.

- [Two assembly approaches](assembly-approaches-v1.md): compares marked A4
  interface/ridge completion with the current He-4 transport graph. Local star
  closure is unique in the fixed honeycomb; the derived electron comparison
  closes a coefficient square but lacks a native reader/history lift. The two
  fourfold structures are not identified by their count.

- [Neutron pullback prototype](neutron-pullback-v1.md): 36 local compatibility
  tests on actual PN/NE maps, retaining five coefficients and endpoint histories.
  Formal leg-exchange passes; native species duality remains unconstructed.

- [Current native phase lift audit](native-phase-lift-audit-v1.md): recovered the
  newer phase-first six-carrier coverage and checked its 18 transitions. Two
  advances restore coefficients but not phase/history. Geometric-chain-to-native
  cross-branch lifting remains an explicit missing adapter.

- [Cross-branch cellular coherence](cross-branch-coherence-v1.md): all 400 six-step
  routes connected through 1,200 local comparisons; exact face witnesses and
  volume fillers verified. This compares recovered geometric routes, not yet
  their full native WG/reader data.

- [Recursive branch descent/re-probing](recursive-branch-descent-v1.md): existing
  retained relation promotion tested on 36 four-step and 400 six-step branches.
  New-level connectivity reaches shared records; cross-branch coherence and
  numerical rung identification remain separate.

- [Extended-region closure and carriers](extended-region-closure-and-carriers-v1.md):
  oriented cell boundaries close; all 192 marked local P–N–E trials complete,
  128 stay inside, but none spans the two poles under the explicit incidence test.

- [Extended probe diagonal](extended-probe-diagonal-v1.md): poles separated by
  four nearest-neighbour steps first match at depth two per side. The 144 slots
  yield nine meeting vertices and 36 shortest paths, recovering grades 1,4,9,4,1.

- [Compare-first codomain pilot](codomain-compare-first-pilot-v1.md): 144 directed-
  edge comparisons per pair, then witnessed face-chain completion in the six-
  carrier pool. Recovers P1–N1–E1 and P2–N1–E2; not full WG closure or a global
  completion search.

- [Helium ring and role test](helium-ring-role-test-v1.md): subdivision along
  the polar diagonal gives four equal-volume wedges sharing an edge. Alternation
  gives 2+2 with two choices; ordered endpoints alone do not select species.
  The wedges are not regular primitive honeycomb tetrahedra.

- [Small octahedron / helium candidate](helium-small-octahedron-candidate-v1.md):
  two-step interval with grades 1,4,1; four equatorial vertices between the poles.
  Exact small-size comparison executed; particle-role assignment remains open.

- [Six-step graded octahedron](six-step-graded-octahedron-v1.md): a six-edge
  graph interval along an octahedral axis gives grades 1,4,9,16,9,4,1;
  44 vertices, 32 tetrahedra and 19 octahedra. Straight root-axis steps instead
  give a line. Pb-208 role/readout identification remains open.

- [Witnessed output-to-input reuse](witnessed-transfer-test-v1.md): freshly runs
  the actual generating WG schedule and checks that first-stage constructed
  families become second-stage inputs, retaining all 137 witnessed slots.
  Five hostile controls are rejected. This supports staged reuse, not the
  fifteen-token/single-apex accounting. Dependency receipts stay in this home.
- [Channel trade versus coning](channel-trade-test-v1.md): exact simplex/link
  and plane-direction audit. Ordinary coning does not yield the proposed
  (3,12)->(4,11) trade. A separate retained fifteen-token role transfer does;
  no decorated-cone identification is established. Includes executable checker
  and receipt.

## Questions to settle before merging interpretations

1. Derive the decorated twelve-sector source from join/cone generation, rather
   than only its tetrahedral support.
2. Relate source indexing, selecting one source fibre, and taking a decorated
   vertex link by explicit maps. These are three different operations.
3. Identify which return construction realizes the intended 12–4 circulation
   and what witness data it requires.
4. Specify each quotient's equivalence and observer. Endpoint quotient,
   common-phase quotient and terminal source quotient are distinct.
5. Locate the proposed boundary where the operator's 4D representations meet.
   Rung8, rung4 and the return seam are not interchangeable candidate locations;
   no location was established by this bounded prior search.
6. Keep geometric dimensions, field components, sector counts, independent
   ranks and term counts in separate columns.

## Registration and verification

Glossary canonical name: **Realization Tower** (`marici:concept`).
Definition version: **1**. Home: `research/realization-tower/`.

This index records inspected prior work; it does not rerun scientific checkers,
change their outcomes, or admit new research tasks. Registration details are
recorded in [glossary-registration.md](glossary-registration.md).
