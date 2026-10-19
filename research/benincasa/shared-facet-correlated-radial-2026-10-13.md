# Correlated infinity supplies a new rank-six positive boundary

Iteration 12, 2026-10-13. Freshly read the mutable work net's correlated-radial continuation. This is a different compactification from the seven contracted fixed-other-parameter infinity limits.

## Source-derived radial chart and orientation

On the actual shared internal Y1235 facet, substitute

    alpha2=1/t, alpha3=u/t, alpha4=v/t,
    alpha5,alpha6,alpha7,alpha8 finite and positive.

The ordered original seven-log coordinates are (alpha2,...,alpha8); the new order is (t,u,v,alpha5,...,alpha8). Their logarithmic wedge Jacobian has determinant -1, checked symbolically before residue comparisons.

Multiply the source rows by diag(t,1), a positive GL(2) gauge for t>0. The resulting common A/H source matrix is polynomial in t and has a finite rank-two positive limit. This row-gauge determinant is not a differential-form scale; the normalization remains the fixed source dlog convention.

The prior internal-facet source signs were +1 for A/history8 and -1 for H/history9. After the derived radial log Jacobian, the t=0 residue signs are -1 and +1. Their six-dlog source residues cancel symbolically.

## New positive boundary image

At t=0, columns 3 and 4 vanish. The six active labels are {1,2,5,6,7,8}, with parallel triple (6,7,8). Unlike a finite coordinate-zero corner, this boundary removes the baseline column 3, which was identically (1,0) in the original finite source gauge.

At both fixed positive external Z, the boundary tangent rank is six and the full facet radial-germ rank is seven. All ordered source minors are nonnegative. Positive radial-arc controls reproduce the original facet charts; the anchor t=1/(prior alpha2) also reproduces the prior finite positive fixture.

The six active external vectors form a basis. Their explicit supported left inverse reconstructs the boundary source fiber from Y. Canonical gauge extraction recovers all six surviving parameters (u,v,alpha5,...,alpha8) symbolically and at the normalized target samples. This is an actual boundary inverse, not a tangent covector or cell-key match.

## Two actual target normals

The physical bracket Y1245 has a symbolic radial source pullback divisible by t with nonzero transverse unit at both samples. It provides a genuine second normal within the internal Y1235 facet.

Independently, the pinned A source-fiber inverse circuit gives

    b(Y)=Delta23(C_recovered)/Delta25(C_recovered).

The denominator is nonzero at the compact boundary even though the original canonical A gauge's baseline column has vanished. Exact rational radial arcs satisfy b(target_arc(t))=t. Its target gradient pulls back to the unit t covector. Thus an actual inverse-radial normal is available, and agrees with the physical-bracket residue convention through the transverse slope.

## Paired residue result

Choose identical six target tangent entries for both source histories. For each chart and fixed Z, three routes agree exactly:

1. Radial source residue then boundary pushforward.
2. Facet pushforward then Y1245 residue.
3. Facet pushforward then actual inverse-radial b residue.

All four three-route comparisons pass. Both paired six-form target density sums are zero. Reversing one orientation, or omitting the derived radial sign in one route, gives a nonzero residual. No independent normalization was fitted.

## Scope and next action

This constructs one new positive correlated-infinity boundary and local unweighted paired cancellation at the two pinned external Z, with symbolic source wedge and boundary inverse identities. It does not complete the compactified atlas, weighted sector/component map, global BCFW source-chain orientation or full shared-stratum coverage. Scientific gate verdicts remain open; historical replay inputs remain missing.

Next: test the omitted baseline-column6 boundary with mixed scaling

    alpha2 finite,
    alpha3=t*u, alpha4=t*v,
    alpha5=w/t, alpha6=1/t, alpha7=r/t, alpha8=q/t.

Normalize source rows by diag(1,t), derive the seven-log wedge Jacobian and test the finite limit with extra zero column 6. Classify its target rank and construct an actual second normal before comparing residues. This scaling changes both vanishing and growing coordinates and is not covered by either the one-parameter infinity screen or the current all-growing triple.

## Reproduction

    python research/benincasa/checkers/check_shared_facet_correlated_radial.py

Receipt: `research/benincasa/results/shared_facet_correlated_radial.json`.

Eight grouped checks pass; predecessor source/checker hashes are verified. Evidence is exact symbolic source and local rational differential-form algebra, not a kernel proof or complete weighted descent theorem.
