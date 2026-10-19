# Mixed radial scaling recovers the baseline-column6 boundary

Iteration 13, 2026-10-13. Freshly read the mutable work net. The task is a mixed vanishing/growing chart of the actual shared positive internal Y1235 facet, not another fixed-other-parameter infinity direction.

## Fixed source operation and orientation

Use

    alpha2 finite,
    alpha3=t*u, alpha4=t*v,
    alpha5=w/t, alpha6=1/t, alpha7=r/t, alpha8=q/t.

The new ordered variables are (t,alpha2,u,v,w,r,q). The original ordered seven-log variables are (alpha2,...,alpha8). Their logarithmic wedge Jacobian has determinant -1, derived symbolically before density tests. Combined with the prior A/H internal-facet signs +1/-1, the boundary source coefficients are -1/+1.

The positive row gauge diag(1,t) produces a finite polynomial source germ shared by both histories. Its determinant is not a differential-form scale. Columns 4 and 6 vanish at t=0; column6 is exactly (t*(u+v),t). The boundary support is {1,2,3,5,7,8}, with parallel pairs (3,5) and (7,8).

An initial assertion compared expanded t*u+t*v with factored t*(u+v) by structural equality and failed. It was replaced by exact rational cancellation. The source chart, normalization and mathematical equality were unchanged; the subsequent fresh run passes.

## Positive regular boundary

All ordered source minors are nonnegative at both boundary fixtures. The boundary target tangent rank is six, while the full seven-variable mixed facet germ has rank seven. The chart anchor t=1/(prior alpha6), with the corresponding positive ratios, reproduces the original finite positive source fixture; a second positive arc point also reconstructs exactly.

The six active external Z rows are a basis. Their supported left inverse reconstructs the boundary source matrix, and the unique canonical gauge recovers all six surviving mixed parameters symbolically and at both normalized target points. This confirms an actual new baseline-column6 boundary, not a label-only comparison or a duplicate finite zero-column7/8 face.

## Actual normals and paired residues

The physical bracket Y1278 has a symbolic source pullback divisible by t with nonzero transverse slope. Independently, the pinned A fiber inverse supplies the regular radial function

    b(Y)=Delta36(C_recovered)/Delta38(C_recovered).

Its denominator is nonzero at the compact boundary. Exact rational source arcs satisfy b(target_mixed_arc(t))=t, and its target gradient pulls back to the unit t covector. Canonical A gauge extraction is not used where its baseline column6 has vanished.

Using the same six target tangent entries, each A/H chart at each external fixture has identical densities through three routes: mixed source residue then pushforward; facet pushforward then Y1278 residue; and facet pushforward then b residue. All four three-route comparisons agree. Both paired target six-form sums are zero. Reversing one orientation or dropping the derived mixed log sign in one route gives a nonzero residual.

## Scope and continuation

Constructed: one positive rank-six mixed compactification boundary, a source-authorized log wedge sign and boundary inverse, two actual normals and local unweighted paired cancellation at the two pinned Z. This is not full compactified atlas completeness, weighted component/sector normalization, global BCFW orientation or full shared-stratum coverage. Scientific verdicts remain open; the missing replay inputs remain absent.

Next: the omitted adjacent direction merger (2,3,5). Set alpha4=1/t and alpha8=t*q, with alpha3=u and alpha2,alpha5,alpha6,alpha7 finite. Apply the determinant-one source shear [[1,-1/t],[0,1]] to obtain a finite source germ. Derive its wedge sign and test positivity, target rank, candidate physical Y1678 and an actual reciprocal-alpha4 inverse normal before residue comparisons. This shear chart merges directions rather than deleting the baseline columns handled so far.

## Reproduction

    python research/benincasa/checkers/check_shared_facet_mixed_radial.py

Receipt: `research/benincasa/results/shared_facet_mixed_radial.json`.

Eight grouped checks pass; predecessor source/checker hashes are verified. Evidence is exact symbolic/rational local differential-form algebra, not a kernel proof or a complete weighted theorem.
