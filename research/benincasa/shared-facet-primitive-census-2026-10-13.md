# Bounded invariant primitive census of the shared source cell

Iteration 16, 2026-10-13. Freshly read the mutable work net's primitive-census task. This assembles the earlier source-authorized germs without equating a coordinate-zero screen with an invariant boundary atlas.

## Rank-two source coverage argument

The actual shared internal source cell has active support {1,2,3,5,6,7,8} and cyclic projective direction classes

    (1), (2), (3,5), (6,7,8).

A rank-two positive cell has m active column magnitudes and r cyclic RP1 directions modulo the four-dimensional GL(2) action. Its dimension is m+r-4, here 7.

In the rank-two positive closure, active labels can disappear and cyclic consecutive direction classes can coalesce. Original parallel classes cannot split. A primitive codimension-one degeneration loses exactly one dimension:

- delete one member from a nonsingleton class, preserving r;
- merge one adjacent pair of cyclic direction classes, preserving m.

Deleting a singleton loses both m and r, hence two dimensions. Multiple deletions or nonadjacent direction coalescences require at least two losses. Rank-one matrices are not cells of Gr(2,8).

The checker exhaustively enumerates active support subsets and cyclic gap coarsenings. It obtains 481 rank-two closure stratum keys, exactly nine at dimension six. This agrees with the direct five-deletion/four-merger enumeration.

## All nine primitive facets attached to actual germs

| Source operation | Actual second target normal | Target rank |
|---|---|---:|
| Delete 3 | Y1245 | 6 |
| Delete 5 | Y1234 | 6 |
| Delete 6 | Y1278 | 6 |
| Delete 7 | Y1268, nonphysical | 6 |
| Delete 8 | Y1267 | 6 |
| Merge (1),(2) | actual inverse alpha4 | 6 |
| Merge (2),(3,5) | Y1678 | 6 |
| Merge (3,5),(6,7,8) | contracted fixed-line incidence | 5 |
| Merge (6,7,8),(1) across the cyclic cut | Y2345 | 6 |

The checker derives symbolic active support and parallel-minor keys from every pinned source matrix, rather than trusting its chart name. All nine keys match the invariant covers. Fresh source Grassmannian ranks are six for all nine facets at both fixtures. Target ranks are recomputed at all eighteen source/external points.

Eight regular target faces attach sixteen previously verified paired six-form zero sums, with actual normal/residue-route witnesses. Their normals comprise six physical brackets, one nonphysical bracket and one nonlinear inverse normal. The remaining primitive source facet retains its target rank-five contraction, exact positive source fiber and unavailable ordinary six-form density; it is not entered as a false zero.

The finite coordinate alpha7=0 and alpha8=0 screens delete singleton labels1 and2. They are dimension-five source strata, not primitive facets of this source cell. Seven fixed-other-parameter infinity directions also cannot replace the invariant cover enumeration.

## Coverage controls and scope

A scoped validator rejects a missing primitive, duplicate primitive, coordinate-only list, replacement by a lower-dimensional coordinate image, and a fake target zero assigned to the contracted facet. All predecessor receipt/source/checker hashes are verified.

Constructed: the complete primitive rank-two positive-cell stratum census of this one shared internal source cell, matched to actual source germs and local unweighted residue/contraction evidence.

Not constructed: the complete original three-composite 5/6/5 physical facet provenance, global target covering or BCFW orientation anchors, weighted component/sector maps, or full weighted A3 stratum coverage. The 481 source stratum keys are not declared weighted target strata. Scientific gate verdicts remain open; eighteen historical replay inputs remain absent.

## Next executable continuation

Apply the same invariant deletion/adjacent-merger enumeration to the original history5,8,9 top cells. Their source dimension is eight. Use positive cyclic gap-and-column-scale charts to construct primitive germs, choosing anchors that remain nonsingular under each deletion or merger. Derive the logarithmic transition to the frozen intrinsic A/H ordered source forms before interpreting target residues. Then classify target ranks and physical-normal fingerprints, retaining contracted and nonlinear dispositions.

This tackles the missing top-cell primitive provenance rather than promoting this bounded internal-cell atlas to full three-composite completeness. The 5/6/5 numbers concern physical provenance, not the total number of primitive rank-two source facets.

## Reproduction

    python research/benincasa/checkers/check_shared_facet_primitive_census.py

Receipt: `research/benincasa/results/shared_facet_primitive_census.json`.

Eight grouped checks pass, including eighteen fresh rank calculations and five rejected coverage hostiles. Evidence combines the written rank-two closure argument, exhaustive finite combinatorial enumeration, symbolic matroid keys and exact local differential algebra. It is not a kernel proof or complete weighted theorem.
