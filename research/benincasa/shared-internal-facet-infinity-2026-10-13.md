# Shared facet: seven one-parameter infinity germs are contracted

Iteration 11, 2026-10-13. Freshly read the mutable work net. This tests the prescribed alpha_j=1/t limits of the actual shared positive Y1235 source facet, fixing every other surviving parameter at its prior positive value.

## Finite Grassmannian germs

For each of seven surviving coordinates and both external Z fixtures, choose a target pivot whose determinant has maximal pole order at t=0. Rational cancellation gives an analytic normalized target germ with nonzero remaining denominators at the selected point. The source Grassmannian is independently normalized with a maximal-pole source pivot.

All fourteen source limits have rank two and nonnegative ordered minors. Twenty-eight positive-arc controls at t=1 and t=1/2 reproduce the original forward maps exactly. Fourteen alternative finite target pivots satisfy the exact GL(2) transition identity. These are actual rational compactification germs, not a fitted limiting plane.

## Limiting ranks

The limiting target tangent ranks use derivatives in the six remaining source parameters. The full germ rank additionally includes the t derivative.

| Infinite A parameter | H parameter | Target boundary rank | Target full germ rank |
|---|---|---:|---:|
| alpha2 | alpha1 | 4 | 5 |
| alpha3 | alpha3 | 3 | 4 |
| alpha4 | alpha4 | 3 | 4 |
| alpha5 | alpha5 | 3 | 4 |
| alpha6 | alpha6 | 3 | 4 |
| alpha7 | alpha7 | 4 | 5 |
| alpha8 | alpha8 | 4 | 5 |

The ranks agree at the two fixed positive external Z. Source limiting tangent ranks are retained separately in the receipt; target projection can lose further dimensions.

None of these fixed-other-parameters infinity directions supplies a rank-six target boundary image or a regular rank-seven inverse of the source facet germ. They are retained as contractions, with ordinary target six-form densities unavailable—not declared zero by a nonexistent determinant or counted as completed residue squares.

## Orientation and shared source witness

A/H matrices remain identical after the common surviving-parameter relabeling for all t. The change alpha=1/t has dlog(alpha)=-dlog(t). Combined with the prior internal-facet deletion signs +1/-1 and the coordinate's position in the ordered seven-dlog wedge, the source six-form residue signs are opposite. Their symbolic paired source sum vanishes. Reversing one source orientation gives a nonzero coefficient.

This source cancellation does not establish an ordinary target six-form cancellation for the contracted images.

## Scope and next nonredundant test

Established: fourteen finite positive source/target infinity germs, exact finite-pivot transitions, ranks, orientation signs and retained rank-deficient inverse/residue dispositions.

Not established: the full compactified boundary atlas. One parameter at infinity with all others fixed does not cover correlated scalings or exceptional/blowup charts. Weighted component/sector, global covering/orientation and full shared-stratum gates remain open; historical replay inputs remain absent.

Next: the correlated radial chart

    alpha2=1/t, alpha3=u/t, alpha4=v/t,
    alpha5,alpha6,alpha7,alpha8 finite and positive.

Derive the source logarithmic wedge Jacobian before residue comparisons. Row scaling diag(t,1) gives a finite signed source matrix with an additional zero column 3 at t=0, unlike the fixed-other-parameters limits above. Test its target tangent rank and an actual Y1245 or inverse-radial target normal, and compare paired residues only if the branch is admitted. This supplies a concrete correlated-scaling continuation rather than repeating contracted one-parameter limits.

## Reproduction

    python research/benincasa/checkers/check_shared_internal_facet_infinity.py

Receipt: `research/benincasa/results/shared_internal_facet_infinity.json`.

Seven grouped checks pass. Predecessor source/checker hashes are verified. The fresh checker was rerun after finalizing its continuation. Evidence is exact rational germs and local differential algebra, not a kernel proof or complete weighted-descent theorem.
