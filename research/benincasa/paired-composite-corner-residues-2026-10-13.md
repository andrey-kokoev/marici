# One actual shared corner: oriented unweighted iterated residues cancel

Iteration 8, 2026-10-13. Freshly read the mutable work net. The requested test is the actual positive corner identified in iteration 7, not a pairing inferred from matching physical divisor labels.

## Common source witness and orientation

History 8's A chart at alpha1=alpha6=0 equals history 9's H chart at alpha2=alpha6=0 as a signed embedded source matrix. The surviving ordered parameters are

    A: (alpha2,alpha3,alpha4,alpha5,alpha7,alpha8),
    H: (alpha1,alpha3,alpha4,alpha5,alpha7,alpha8),

with H alpha1=A alpha2 and all other surviving parameters unchanged. The logarithmic transition determinant is exactly 1.

Take alpha6 residue first in both charts. Its deletion sign is -1. Second deletion is alpha1 (remaining position 0) for A and alpha2 (remaining position 1) for H. Therefore the iterated source signs are -1 and +1. The paired six-dlog source residues cancel symbolically on this actual shared corner.

No independent scale or orientation adjustment was introduced after seeing target densities. Both charts retain the ordered eight-dlog convention frozen in the intrinsic normalization receipts. Its relation to the complete BCFW source chain remains unanchored.

## Two genuine common target normals

Use the normalized target brackets in this order:

    Y1267: physical divisor reached by alpha6=0;
    Y1235: internal/nonphysical divisor reached by A alpha1=0 or H alpha2=0.

The second normal is not a fitted tangent covector. Exact symbolic raw source pullbacks of both brackets factor by the corresponding source parameters. Their normal slopes are nonzero at the corner, and their target gradients are independent. The target pivot and common normal-frame determinants are nonzero.

The corner has a six-dimensional target tangent image at both fixed positive external Z. The source matrices and ordered six-log tangent differentials coincide. Choose the same six ambient target entries for both routes.

## Three residue routes and paired result

For each chart at each fixed Z, compare:

1. Both source residues, then six-dimensional local pushforward.
2. First source residue, seven-dimensional local pushforward, then second common target residue.
3. Top local pushforward, then both common target residues in the declared order.

All four three-route comparisons agree exactly. Their paired six-form density sums are zero at both fixtures. The source transition/deletion-parity cancellation is symbolic, not merely numerical agreement at those fixtures.

Reverse one orientation: the paired residual is nonzero at both fixtures. Reverse the residue order in one route: its sign changes and again gives a nonzero residual. Reversing the order in both routes flips both signs and preserves cancellation.

## Scientific scope

Constructed: one actual shared positive source corner, its unit six-parameter logarithmic transition, genuine common target normals, oriented local iterated residue squares and unweighted paired cancellation.

Not constructed: the weighted nine-form comparison, component/boundary extraction, sector images, complete shared-stratum coverage, or a BCFW-global chain orientation anchor. The unweighted local six-form equality is a precursor to those gates, not their resolution. Missing historical replay inputs remain missing.

## Next executable continuation

The corner lies on a larger actual shared internal facet. Without setting alpha6=0, A history8 alpha1=0 equals H history9 alpha2=0 under H_alpha1=A_alpha2, with all remaining parameters unchanged. Verify its positive rank-seven image, common Y1235 normal and oriented paired seven-form cancellation. Then test the boundary naturality relation to this corner, with explicit residue-order signs. This extends the source witness rather than repeating the corner's tangent audit.

## Reproduction

    python research/benincasa/checkers/check_paired_composite_corner_residues.py

Receipt: `research/benincasa/results/paired_composite_corner_residues.json`.

Six grouped checks pass. The checker verifies predecessor source/checker hashes. Evidence consists of symbolic source identities, exact bracket pullbacks and local rational differential-form algebra; it is not a kernel proof or complete weighted-descent certificate.
