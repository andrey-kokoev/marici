# Adjacent direction merger (2,3,5): positive rank-six shear boundary

Iteration 14, 2026-10-13. Freshly read the mutable work net's balanced-shear continuation.

## Source operation and wedge sign

On the actual shared Y1235 facet use alpha4=1/t, alpha8=t*q and alpha3=u, keeping alpha2,alpha5,alpha6,alpha7 positive and finite. Apply the source shear

    [[1,-1/t],[0,1]].

Its determinant is 1. The resulting shared A/H source matrix is polynomial in t, even though the original chart and shear separately diverge. The ordered new coordinates are (t,alpha2,u,alpha5,alpha6,alpha7,q). Their logarithmic wedge Jacobian from the original seven source parameters has determinant -1. This is derived before residue comparisons; the shear's determinant is not substituted for the form Jacobian.

## Actual positive source boundary

At t=0 the only zero column remains column4. Columns2,3,5 become parallel; columns6,7,8 remain parallel. The resulting active support is {1,2,3,5,6,7,8}, with parallel triples (2,3,5) and (6,7,8).

All ordered source minors are nonnegative. At both external fixtures, the target boundary tangent rank is six and the full facet shear-germ rank is seven. The positive anchor t=1/(prior alpha4) and a second positive point reconstruct the original source chart's target exactly.

The source-authorized A fiber inverse reconstructs the entire boundary matrix symbolically. A nonsingular gauge based on column3 and negative column1 recovers all six boundary parameters symbolically and at both normalized target points. The original column2 canonical gauge is not assumed regular after its direction merges with column3.

## Genuine target normals

The physical bracket Y1678 has a symbolic source pullback divisible by t with nonzero transverse unit at both samples. Independently, the pinned A fiber inverse supplies

    b(Y)=Delta23(C_recovered)*Delta13(C_recovered)
         / [Delta36(C_recovered)*Delta12(C_recovered)].

This is reciprocal alpha4 from the original canonical chart, continued as a regular rational target function in the shear compactification. Its denominator is nonzero at the boundary. Exact rational source arcs satisfy b(target_shear_arc(t))=t, and its target gradient pulls back to the unit t covector.

No tangent plane replaces either defining normal, and no density-dependent source scale is selected.

## Local oriented paired cancellation

The prior internal-facet signs +1/-1 become boundary signs -1/+1 after the derived log-wedge determinant. Using identical six target tangent entries, source residue then pushforward, facet pushforward then Y1678 residue, and facet pushforward then actual reciprocal-alpha4 residue agree for both charts at both external Z.

All four three-route comparisons pass; both paired six-form density sums vanish. One orientation reversal or omission of the log-wedge sign in one route yields a nonzero residual.

## Scope and continuation

Constructed: the omitted adjacent (2,3,5) merger as a positive rank-six compactification boundary, actual source/target inverses and unweighted local paired cancellation. This does not prove complete invariant atlas coverage, weighted component/sector comparison, BCFW-global chain orientation or the full weighted descent theorem. Scientific gate verdicts remain open; historical replay inputs remain missing.

Next: test the remaining adjacent merger of (3,5) with (6,7,8). Set alpha4=t*v, alpha7=r/t and alpha8=1/t, keep alpha3=u and alpha2,alpha5,alpha6 finite, and normalize source rows by diag(1,t). Derive the log wedge and classify source rank-six boundary versus target contraction before asserting any ordinary six-form normal/residue square. Then assemble the rank-two primitive boundary census with contracted cases explicitly retained.

## Reproduction

    python research/benincasa/checkers/check_shared_facet_direction_merger.py

Receipt: `research/benincasa/results/shared_facet_direction_merger.json`.

Eight grouped controls pass. Predecessor source/checker hashes are verified. Evidence is exact symbolic source/fiber and local rational differential-form algebra, not a kernel proof or a complete weighted theorem.
