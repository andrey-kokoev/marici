# Prior-research clues for the missing source-admitted role transition

## Search scope and evidence status

Read prior research and implementation sources across Strominger, realization-tower, Nima and related notes, emphasizing actual role-changing mechanisms rather than extending the recent Voevodsky comparison chain. The prior scientific suites were **not** freshly replayed during this search. Counts below are either reported by those notes or explicitly identified as fresh inspection of saved data.

The main correction in emphasis is that fixed-coordinate role-changing **reader transformations already exist in prior research**. Their missing admission into the forward generator is a concrete boundary; they should not be dismissed as if the only available candidate were a spatial vertex permutation.

## 1. Strongest lead: context-aware reverse reading

Sources:

- `research/strominger/deuterium-reverse-reading-v1.md`
- `research/strominger/checkers/probe_deuterium_reverse_reading.mjs`
- `research/strominger/isotope-reversal-v1.md`

The implementation keeps each occurrence's vertex coordinate, swaps M/C roles, reflects indices by `i -> 2-i` in the deuterium case (sample-dependent K in isotope cases), swaps P/E reader species, and reorders the active window together with its context:

- P to E: `[w2, context, w1 ; w0]`;
- N to N: `[context, w2, w1 ; w0]`;
- E to P: `[context, w2, w0 ; w1]`.

It reverses boundary/path order and inverts the full coefficient permutations. The note reports involution and local PN/NE phase compatibility for all24 deuterium markings. This is a role-changing operation on descriptions at fixed coordinates, not a coordinate half-turn.

**Admission limitations are explicit:** inverse NE and inverse readers are not registered outgoing operations of the original forward generator. P/E reader exchange can conflict with its regular/split body convention. The transformation changes the entry/exit boundary, and isotope reversal generally needs all old exits, not one new root. Reversed NN face counts also fail the unchanged guard.

This is not yet the parent's regular-P-chart transition: it also swaps P/E readers. The full outside reference and target species/shape must be tested, not merely the active frame.

## 2. Existing coherence for that reader transformation

Source: `research/strominger/deuterium-coherence-square-v1.md`.

The prior checker compares complete decorated states under geometric half-turn G and fixed-coordinate reading reversal B. It reports24 commuting squares,96 local corner audits and48 hostile controls, with `G²=B²=1` and `BGBG=1`.

The coefficient convention carries the fixed five-slot reference basis. It is not derived from the six-vertex geometric interchange. The note explicitly withholds unchanged forward-generator admission and notes the regular-P shape restriction.

**Use:** there is already a coherence candidate for B; the useful next task is admission/type binding, not another abstract coherence filler.

## 3. Fresh saved-data inspection narrows the shape test

Read `research/strominger/results/hydrogen-edge-attachment/verification.json` without regenerating it. Among its24 saved markings,8 have `electronGeometry = proton` (regular) and16 have `electronGeometry = split`.

The default marking `[0,1,2,3]` is in the split group. Examples in the regular group include `[0,2,1,3]` and `[0,2,3,1]`.

Thus the old-E-to-new-P shape obstacle is not uniform across all markings. The8 regular cases are candidates for a sharper admission test, not proof that reversal is admitted there. Their availability also does not show reachability from the default fixed-role seed.

## 4. An already implemented role XOR with unchanged geometry

Sources:

- `research/strominger/vacuum-space-typed-R-v2.md`
- `research/strominger/vacuum-space-alternating-R-v4.md`
- `research/strominger/demos/particle-overlap-tetrahedron/vacuum-model.mjs`

A global assignment switches MMC and CCM on three axis identities without changing positions. The later realization rule alternates these assignments by level parity. The code implements `effectiveAssignment` separately from directions and positions.

This is an operator-requested candidate rule in the vacuum model, not a derived particle operation. Its objects are axis roles, not the five/six named reference vertices of a PN chart. Its scope explicitly says no particle transitions. A typed axis-to-port interpretation is missing.

**Use:** fixed-geometry role exchange is not geometrically incoherent; but a pre-existing rule on another source type is not automatically admissible on PN packets.

## 5. The fixed C/M partition is not intrinsic to bare incidence

Source: `research/strominger/emergent-cm-incidence-audit-v1.md`.

All24 coordinate permutations preserve the untriangulated assembly. The fixed subdivision preserves8, with an invariant unordered2+2 partition whose blocks can exchange. Orientation and growth arrows do not name one block C and the other M. Roles on marked incidences, transported states or processes remain possible.

**Use:** the default local role-coloring invariant is an invariant of its chosen grammar/marking. It is not a theorem that every source interpretation must attach C/M permanently to ambient vertices. Do not confuse this observation with an admitted role-changing transition.

## 6. Additional clues and exclusions

- `cmc-mcm-identity-attachment.md`: explicit overlap-fixing swaps retain shared vertices and all five coefficients, but are declared adapters. The original fifth pentachoron mark differs from the glide chain's outer mark. A3-C/2-M full source has no global C/M-swapping bijection; facet duality must retain the fifth mark.
- `polarization-reversal-transport.md`: an actual dual/Riesz identification plus metric normalization yields an involutive mode reversal. Raw occurrence reversal alone is insufficient. Relevant if the reader reversal must lift to retained field data, but not itself a PN vertex-role operation.
- `rotation-realization-square-v1.md` and `tetrahedral-field-attachment-v1.md`: coarse projector-role exchange does not lift automatically to the independently specified geometric action or full neutron field. These L/G roles must not be identified with vertex C/M by name alone.
- `realization-seam-v1.md`: two ordinary reader advances restore geometry/aliases but increase origin by2; they do not implement M/C reflection or justify an origin reset.

## Recommended next test

Replay the existing fixed-coordinate B reversal on freshly generated full PNE packets. Attempt to bind each reversed frame to the existing complete chart constructors and transfer guards, retaining all outside references, species, coordinates, occurrence indices and the full boundary. Classify the first failure separately for the8 regular-E and16 split-E markings.

Then inspect whether an existing source-level reversed-boundary admission interface supplies the missing operation. Do not add B to the forward signature by fiat. Do not substitute the vacuum-axis XOR, spatial symmetry, package equality or independent target admission for that interface.

This is a candidate-directed source search and admission audit, not another proof that independently supplied contexts can be compared. No conjecture verdict or owning source was changed.
