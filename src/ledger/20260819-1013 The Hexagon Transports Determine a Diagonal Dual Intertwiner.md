# 1013 — The Hexagon Transports Determine a Diagonal Dual Intertwiner

## Repair of the comparison equation

Entry 1012 correctly rejected multiplication of edge cochains by independent
dualization units while leaving the vertex frame fixed.  Its proposed final
adjointness formula was, however, dimensionally incorrect.

Let

\[
\delta_u:C^0_u\longrightarrow C^1_u,
\qquad
(\delta_u\lambda)_k=\lambda_{k+1}-u_k\lambda_k,
\]

and let (delta_{u^{-1}}) be the differential for the dual local system.  A
cellular comparison has type

\[
D_0:C^0_u\to C^0_{u^{-1}},
\qquad
D_1:C^1_u\to C^1_{u^{-1}},
\]

and must satisfy

\[
\boxed{D_1\delta_u=\delta_{u^{-1}}D_0.}
\]

## Diagonal solution

Write

\[
D_0=\operatorname{diag}(g_0,\ldots,g_5),
\qquad
D_1=\operatorname{diag}(h_0,\ldots,h_5).
\]

Comparing the two nonzero entries in row (k) gives

\[
g_k=u_k^2h_k,
\qquad
h_k=g_{k+1}.
\]

Hence

\[
\boxed{
g_{k+1}=\frac{g_k}{u_k^2},
\qquad h_k=g_{k+1}.
}
\]

The frozen hexagon transport obeys

\[
\prod_{k=0}^{5}u_k=1,
\]

so the recurrence closes cyclically.  Its diagonal solution space has rank
one: choosing (g_0) determines every other vertex and edge factor.  The exact
checker fixes (g_0=1) and verifies the full matrix identity on all four
signed recombination sheets.

## Application to the minus primitive

For Entry 1002's primitive (lambda) and edge coboundary
(d=delta_u\lambda), the checker verifies

\[
\boxed{
D_1d
=D_1\delta_u\lambda
=\delta_{u^{-1}}D_0\lambda.
}
\]

Thus the cellular exactness survives passage to the dual local system once
vertex and edge frames are transformed coherently.  Entry 1012's obstruction
was precisely the omitted vertex transformation.

## Narrow conclusion

\[
\boxed{
\text{The minus arc is exact in a canonically determined dual cellular
complex, up to one global scalar.}
}
\]

This is stronger than the local-support result of Entry 1010.  It still does
not identify (D_ullet) with the physical twisted period pairing: the
remaining global scalar, integral orientation, and compatibility with the
KLT occurrence bases have not been derived from the source intersection
normalization.

Consequently there is no cellular Betti obstruction, while integral or
source-normalized Betti exactness remains open.

## Next falsifier

Compare the diagonal frames (D_0,D_1) with the source-normalized twisted
intersection matrix used in Entry 908.  The comparison must fix the global
scalar and reproduce the occurrence permutation of Entry 974.  Failure by a
nonunit index would expose an integral Betti-lattice obstruction; agreement
would close the minus-recombination arc completely.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_diagonal_dual_intertwiner.rs`;
- packet:
  `research/benincasa/string-six-point-diagonal-dual-intertwiner.json`;
- allocator claim:
  `seqclaim-6d32312422d65c58c2e43156`.
- epistemic event:
  `ev-000000000632-1052ef6b-79be-4e38-975b-fbc15f943da5`.
