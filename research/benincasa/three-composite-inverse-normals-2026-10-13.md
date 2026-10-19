# All three selected composite inverse normals — iteration 5, 2026-10-13

## Fresh frontier and substantive result

Freshly read the mutable work net. The recommended composite-normalization task requested actual inverse normals for histories 8 and 9, continuing history 5 without weakening its criterion.

Constructed source-constraint rational inverse circuits for both remaining cells, reproduced history 5 with the generalized implementation, and verified all three alpha4=0 normals and oriented local residue squares at both fixed positive external Z fixtures.

No gate verdict is resolved: the normalization/component/global attachment tasks are broader than these selected local tests.

## History 9: seven-label H support

The support is {1,2,3,5,6,7,8}, with zero column 4 and parallel pairs (3,5) and (7,8). Let L be the left inverse of Z supported on the first six active labels, and k the kernel row on all seven active labels. Then

    C=YL+(u,v)^T k, LZ=I, kZ=0, C4=0.

The two parallel minors give an affine two-by-two linear system in u,v, since the shared vector's self-determinant vanishes. Its adjugate inverse is the actual rational source-fiber inverse on the nonzero-determinant open. No history-5 coordinate labels were reused without changing the constraints.

## History 8: full-support A cell

The parallel triples are (3,4,5) and (6,7,8). For each triple T, form M from the five other Z rows. M has rank five and a one-dimensional annihilator h. For normalized target Y, set

    g=(-Y2*h, Y1*h), r=g*Y.

Then r*h=0, so r belongs to the span of the five rows of M. A fixed five-coordinate pivot uniquely lifts r to a source row supported away from T. Stack the two source rows and row combinations into S and G respectively. On det G !=0,

    C=G^{-1}S, CZ=Y.

Each source row vanishes on one triple; the other row supplies that triple's common direction. Thus both parallel-triple constraints hold. This avoids treating the full-support cell as a seven-support H cell or selecting one root of an uncontrolled nonlinear fiber system. The circuit receipt records the hyperplane covectors, lifting pivots, inverse matrices and symbolic row-change determinant. The five-space reconstruction identities are checked symbolically.

## Uniform source-derived normal

Undo the signed rotation to obtain ordered source columns v1,...,vr. Write p=3 for H and p=4 for A, the column with canonical lower entry 1. The same source gauge yields

    b(Y) = det(v1,vp) det(v(r-1),vr)
           / [det(v1,vr) det(v1,v(r-1))].

This is alpha4 of the reconstructed canonical source chart. The canonical gauge and all eight recovered parameters are fixed by the source chart, not by a desired target density. Wrapped columns retain their rank-two minus signs.

The fiber determinant and gauge/source denominators are nonzero at all six boundary samples. On six exact rational source arcs (only alpha4=t varies), every recovered parameter agrees identically, the full canonical A/H matrix is reconstructed, CZ agrees with Y, and b(target_arc)=t.

## Oriented differential square and controls

Exact target-direction specializations compute db; db times the full target differential is the unit alpha4 covector. The full ordinary differential is invertible. For seven independent target tangent coordinates, source deletion has sign -1, and both residue routes give exactly the same seven-form density at all six fixtures under the prior reciprocal-log-Jacobian normalization.

Six orientation reversals have nonzero residuals. Six tangent-only substitutes disagree with the actual normal on the transverse arc. The generalized history-5 densities agree exactly with its predecessor receipt.

These are local differential-form tests. They do not establish the supercomponent/bosonization residue square or weighted cross-history cancellation.

## Scope and next executable test

Established: all three previously missing selected alpha4 target normals and their local oriented residue squares, from actual rational inverse circuits at the two fixed external Z.

Still missing: complete invariant 5/6/5 facet provenance, global positive covering and BCFW orientation anchors, component-boundary extraction, normalized nine-image comparison and paired weighted codimension-two cancellation. The 18 absent historical replay inputs remain absent.

Next: use the common physical Y1234 divisor reached by alpha2=0 in histories 5 and 8. Invert one history's target boundary point into the other chart, test localization and positivity, and compare the two oriented residue densities using identical target tangent coordinates. Retain a nonoverlap disposition or nonzero residual if that is what the actual inverse returns. A shared divisor label is not itself a shared positive branch or a cancellation certificate.

## Reproduction

    python research/benincasa/checkers/check_three_composite_inverse_normals.py

Receipt: `research/benincasa/results/three_composite_inverse_normals.json`.

Seven grouped checks pass, encompassing six exact arc reconstructions, six local residue equalities and both sets of hostile controls. Predecessor source/checker hashes are verified. The fresh generalized checker was run twice, including after finalizing the normal and continuation specification.
