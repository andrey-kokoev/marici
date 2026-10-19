# Both invariant internal gluings cancel with derived orientations

Iteration 18, 2026-10-13. Freshly read the mutable work net's two actual-source-key gluing candidates.

## Exhaustive equal-source-key candidates

Among the 28 primitive source facets of the three matched intrinsic cells, exactly two pairs have equal invariant rank-two source boundary keys:

1. H/history5 merge (3,4) with (5), and A/history8 delete7. Source classes are (1),(2),(3,4,5),(6,8); the internal target bracket is Y1268.
2. A/history8 delete4, and H/history9 merge (6) with (7,8). Source classes are (1),(2),(3,5),(6,7,8); the internal target bracket is Y1235.

Common physical bracket labels with different source keys are not promoted to gluing candidates. The earlier physical-divisor positive nonoverlap dispositions remain intact.

## Actual source transitions and orientations

Using the nonsingular positive cyclic frames in the primitive atlas, reconstruct the receiving seven boundary coordinates from the donor source matrix. Canonical first/last framing columns fix the GL(2) gauge; gaps are differences of adjacent middle slopes, and column scales come from the fixed-gauge entries.

The reconstructed receiving source matrix is symbolically GL-equivalent to the donor, and the inverse coordinate transition recovers all seven donor variables exactly. Both transitions have symbolic logarithmic determinant 1.

Independently derive the original intrinsic eight-dlog transition determinant as a generic rational function in all eight gap/scale variables, then restrict its radial coefficient to the boundary. For the two pairs the source coefficients are respectively (-1,+1) and (+1,-1). These signs are not reused blindly from an unrelated target fixture or fitted after testing a density sum.

Thus both paired source seven-form coefficients cancel symbolically under the actual boundary transitions. Reversing one source orientation gives a nonzero coefficient.

## Same positive source and target points

For each pair, use two named positive donor fixtures and invert them into the receiving boundary chart. Every receiving coordinate is positive, source matrices are GL-equivalent, and normalized target points agree exactly at the two fixed external Z.

The receiving logarithmic tangent differential, transported through the derived coordinate Jacobian, equals the donor differential. Use identical seven target tangent entries and the same actual Y1268 or Y1235 bracket normal for both residue routes.

All eight local source-residue/pushforward versus top-pushforward/common-bracket-residue squares agree. All four paired target seven-form sums vanish; all four one-orientation-reversal residuals are nonzero.

## Previous Y1235 witness preserved

Convert the earlier shared-facet source samples into the new cyclic boundary coordinates. Recompute both history8/history9 densities in the predecessor's original seven target coordinate frame. All four predecessor densities are recovered exactly. This preserves the earlier intrinsic deletion convention, rather than replacing it with the new atlas's signs.

## Scope and next executable action

Constructed: both actual invariant internal source gluings among the three intrinsic cells, generic rational inverse/log transition identities, symbolic unweighted source seven-form cancellation, and local positive target cancellation controls.

Not constructed: historical full-chain attachment/global orientation, weighted sector/component maps, supercomponent boundary extraction or weighted codimension-two coverage. Scientific gate verdicts remain open; historical replay inputs remain absent.

Next: the common corner of these two internal gluings, represented in A/history8 by zero columns4 and7 (alpha1=alpha5=0). Construct its H5/H9 boundary closure charts, fix common target normal order Y1268 then Y1235, and derive iterated deletion/transition signs for all three source histories. Retain the exact three-cell sum whether zero or nonzero. Pairwise gluing naturality must not be conflated with a complete three-cell chain or a weighted cancellation theorem.

## Reproduction

    python research/benincasa/checkers/check_three_composite_internal_gluings.py

Receipt: `research/benincasa/results/three_composite_internal_gluings.json`.

Eight grouped controls pass; predecessor source/checker hashes are verified. Evidence is exact generic source transition and local rational differential-form algebra, not a kernel proof or full weighted descent theorem.
