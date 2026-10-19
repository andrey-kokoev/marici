# Actual shared Y1235 facet and corner boundary naturality

Iteration 9, 2026-10-13. Freshly read the mutable work net's larger-facet continuation from the completed corner test.

## A genuine positive shared facet

Without setting alpha6=0, the signed embedded matrices satisfy the symbolic identity

    A(history8,alpha1=0) = H(history9,alpha2=0,H_alpha1=A_alpha2).

All other surviving parameters are unchanged. This is the same seven-dimensional source cell: zero column 4, parallel pair (3,5) and parallel triple (6,7,8). The ordered seven-parameter logarithmic transition has determinant 1. Positivity is verified through all ordered source minors at both fixtures.

The actual target image has tangent rank seven at both fixed positive external Z. Its common target normal is Y1235, an internal/nonphysical bracket divisor—not one of the physical A3 sector labels. Symbolic source bracket pullbacks vanish by the corresponding deleted alpha parameter, and their nonzero normal slopes are verified. No tangent plane is substituted for the divisor.

## Oriented paired seven-form cancellation

Deletion of A alpha1 has sign +1. Deletion of H alpha2 has sign -1. Under the unit logarithmic transition, their source seven-dlog residues cancel symbolically.

At each fixed Z, select the same seven ambient target tangent entries for both charts. The source tangent differentials agree exactly. All four local source-residue/pushforward versus top-pushforward/Y1235-residue squares agree, and the paired seven-form target density sum is zero at both fixtures. Reversing one orientation gives a nonzero residual.

The orientation is the prior intrinsic ordered-dlog orientation. This does not supply its missing anchor to the complete BCFW chain or a weighted component-map comparison.

## Naturality to the previous shared corner

Take the next boundary at alpha6=0, equivalently physical Y1267 within the shared internal facet. Use the previous corner receipt's same six target coordinates, not the unrelated seven-coordinate frame at the facet sample.

For each chart and fixed Z, three routes agree exactly:

1. Source internal-facet residue, then alpha6 source residue and six-form pushforward.
2. Source internal-facet residue and seven-form pushforward, then physical Y1267 residue.
3. Top pushforward, then Y1235 and Y1267 target residues.

The paired boundary six-form sum is zero. These densities are the negatives of the previous receipt's Y1267-then-Y1235 densities. The checker verifies this residue-order anticommutation against the pinned predecessor, rather than silently replacing its sign convention.

This establishes local boundary naturality of the seven-form cancellation to the already admitted corner.

## Scope and next executable continuation

Established: actual shared positive source facet, unit oriented transition, internal-divisor local residue squares, unweighted paired seven-form cancellation and corner boundary naturality at the two fixed external Z, with symbolic source identities.

Not established: weighted nine-form sector/component maps, complete invariant source-boundary provenance, global covering or BCFW orientation anchors. Scientific gate verdicts remain open, and the 18 historical replay inputs remain missing.

Next: screen the seven coordinate boundaries of this shared facet using its common source transition. Classify six-dimensional target images versus contractions, determine actual second normals and retain undefined inverse/full-rank cases. Expand paired iterated residue coverage only where the local branch conditions are met. The already completed alpha6 corner should serve as a preserved regression, not a new claim.

## Reproduction

    python research/benincasa/checkers/check_shared_internal_composite_facet.py

Receipt: `research/benincasa/results/shared_internal_composite_facet.json`.

Seven grouped controls pass. Predecessor source/checker hashes are verified. Evidence is exact symbolic source and rational local differential-form algebra, not a kernel proof or complete weighted-descent theorem.
