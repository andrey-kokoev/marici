# Polarity pair experiment — PP → N, PE → octahedral P

**Superseded experiment:** removed from the active process and viewer at the user's request. The module and standalone tests are retained as research history only. The following describes the former trial; its previews are no longer available. Current work is [complementary layer 1](cell-fibration-v1.md#complementary-layer-1).

At layer 5 of **Cell-level fibration**, expand **Polarity pair experiment**. Choose one of two alternative wireframe previews. No assigned cells, counts, geometry, or previous rules are overwritten. Cut mode disables the preview; the vertex/depth cut still inspects the existing same-orientation sector.

This tests the user's proposed pair rules without assuming which geometric objects form the pair. E is allowed: no P > N > E resolution is applied to experimental results. The existing 84-cell input construction is left intact, including its earlier priority rule.

## Explicit trial assumptions

- PP → N.
- PE and EP → P, with the octahedron as the prospective carrier. Treating PE as unordered is a trial assumption.
- NN, PN/NP and EE have no supplied rule; they remain unspecified, not rejected or guessed.
- In the independent-neighbor trial, all six source pairs are inspected. A whole octahedron is called covered only if all six have a defined, agreeing result. No distinguished pair is silently chosen. Failure of this all-pairs criterion is not a refutation of a future rule selecting one particular pair.
- Results from different pairing hypotheses are not combined into a single completion.

## A. Original and mirrored readings of one cell

P↔E, N↔N produces 44 PE pairs and 40 NN pairs on the 84 tetrahedra. It never produces PP. Moreover, the carrier is still tetrahedral: renaming its paired reading cannot turn it into an octahedron. This is diagnostic only, with no geometry preview.

## B. Reflection across an adjacent octahedron centre

Each opposite-orientation tetrahedron has four face-adjacent octahedra. Reflecting through each octahedron centre reaches an actual assigned tetrahedron across its opposite face. Geometry is checked in both directions. There are 140 complete paths (35×4), plus 84 directions whose reflected cell would lie outside the carrier.

Each path reverses P/E and retains N. Results:

- 6 target tetrahedra have four agreeing proposals: **1 P, 4 N, 1 E**.
- 29 targets have conflicting proposals; no priority resolves them.
- The 140 source/mirror pairs contain 74 PE and 66 NN, with no PP.

The mirror preview shows only the six agreeing targets, including the interior E, as P?/N?/E? wireframes. These are conditional mirror results, not a committed completion.

## C. Independently coloured source neighbours around an octahedron

Each of the 56 octahedra has four assigned same-orientation tetrahedral face neighbours. Their six unordered pairs yield 336 comparisons. These source faces are **not opposite faces**, so this is a distinct interpretation, not a polarity involution.

There are 15 PP rule matches and 55 PE rule matches; 266 comparisons have no supplied rule. These are pair counts, not particle or carrier counts.

| Whole-octahedron assessment | Count | Meaning |
| --- | ---: | --- |
| Covered N | 1 | All six pair results defined and N |
| Partial P | 38 | Known pair results agree on P; some pairs unspecified |
| Partial N | 2 | Known pair results agree on N; some pairs unspecified |
| Conflicting | 7 | Known pair results require both P and N |
| Unspecified | 8 | No pair has a supplied rule |

The octahedral preview shows 41 wireframes: 38 P? and 3 N?. **40 are partial**. The seven conflicting octahedra are listed, not force-coloured. The eight unspecified octahedra are not assigned. These previews are alternatives to the six mirrored-tetrahedron candidates; they are not presented as one consistent global solution.

## Structural result and next question

**PP → N cannot occur under strict P↔E mirroring of one input. It requires two independently coloured inputs.** The neighbor-pair interpretation does produce PP and PE using existing geometric octahedra, but the two rules do not yet determine a whole-cell colouring.

The next structural issue is which pair is actually admitted by the comparison/transport mechanism—or whether several pair readings must coexist on one carrier. Complete rules for unlisted pairs would also be needed if all six comparisons are to constrain one cell colour. No arbitrary choice of pair or colour has been made here.

Implementation: `../realization-tower/polarity-pair-experiment.mjs`.
Verification: `tests/polarity-pair-experiment.test.mjs` and `scripts/test-cell-fibration-process.mjs` (both previews, E retained, counts unchanged, disabling and cut isolation).
Screenshot: `results/cell-fibration-viewer/polarity-pair-trial.png`.
