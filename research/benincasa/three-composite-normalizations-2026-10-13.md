# Three composite roots: intrinsic normalization extended — 2026-10-13

## Iteration 1: fresh frontier and execution

Freshly read the weighted-A3 contract and first-composite checker. The recommended node was `composite-normalization-definition`, with next action to extend the history-5 conventions to histories 8 and 9 without fitted scales.

A successor checker now applies the same rule to all three uncorrected composites. The original history-5 note, checker and receipt were not changed. Its source/checker pins are verified and its component values and local target Jacobians are reproduced exactly.

## Matches and normalization

| Root | History | Source seed | Support | Rotation |
|---|---:|---|---|---:|
| [1,2] | 5 | H | 1,2,3,4,5,6,8 | 2 |
| [1,3] | 8 | A | 1,2,3,4,5,6,7,8 | 2 |
| [2,3] | 9 | H | 1,2,3,5,6,7,8 | 2 |

Three exact supertwistor fixtures per history give nine full unit-normalization matches. For each match, all 70 one-SU(4) quotient numerator coefficients are checked alongside bosonic denominators. All three histories have no endpoint update, so K=K0 here.

No independent per-root scale or target residue coefficient is fitted. The scalar rule remains the eta2/eta3 wedge-to-fourth-power selector with outer/inner prefactors divided by <23>^4.

## Local differential pushforward

The source rule is the matched A/H positive chart, twisted cyclic embedding in rank two, and ordered eight-dlog orientation. Wrapped columns are multiplied by -1; the untwisted embedding is retained as a negative-minor hostile whenever there are wrapped columns.

For each history, two exact positive source points and two positive six-dimensional moment-curve external Z samples give six nonzero eight-dimensional target log Jacobians in total. Normalize target columns 1,2 to identity and use free entries in row-major order. The intrinsic regular-branch density is the reciprocal log Jacobian.

For all six tests, an independently differentiated target transition to pivot columns 1,3 carries the Jacobian/density correctly. Every ordered six-by-six external Z minor is positive at the chosen fixtures. Source ordered Plucker minors are nonnegative.

These are local regularity and normalization controls. They do not prove global degree or matching of intrinsic chart orientations to the completed BCFW chain's global anchors.

## What remains open

The top-level intrinsic convention has now been extended to all three roots, but the composite node is not promoted to a normalized physical-residue theorem. Missing witnesses remain:

- global source-chain orientation/target degree;
- the commuting square between four-dimensional supertwistor component extraction and six-dimensional bosonized target forms;
- target boundary generators/normals and the residue pushforward comparison;
- complete 5/6/5 physical facet provenance.

In particular, no regenerated full atlas or oriented eighty-facet bundle is claimed. Existing missing historical inputs remain operationally missing.

## Next nonredundant test

Construct one actual composite source-boundary-to-target differential map from these now explicit charts. Verify its rank and target normal before taking a target residue. Distinguish divisorial, contracted and potentially nonphysical images rather than assigning a physical channel from the A3 root label.

A successful local boundary calculation will be precursor evidence for the missing square, not automatic admission of the complete normalized nine-to-twenty map. The simple-root canonical admission and difference-form gates remain unchanged.

## Reproduction

    python research/benincasa/checkers/check_three_composite_normalizations.py

Result: `research/benincasa/results/three_composite_normalizations.json`.

Eight grouped checks pass. Evidence level: fresh exact finite superfunction matching, source positivity controls and local differential algebra. No owner producer, full source atlas or kernel proof was executed. A passing checker certifies this scoped calculation, not weighted descent.
