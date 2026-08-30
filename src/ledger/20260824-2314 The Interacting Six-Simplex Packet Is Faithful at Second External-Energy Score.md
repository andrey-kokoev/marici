---
authors:
  - marici.Benincasa
date: 2026-08-24
---

# 2314 — The Interacting Six-Simplex Packet Is Faithful at Second External-Energy Score

## Frozen source packet

Use exactly the six simplex terms in arXiv:2408.16386, equation (4.15), in
source order

\[
(G12|g23,G12|g31,G23|g31,G23|g12,G31|g12,G31|g23).
\]

After removing the common denominator

\[
q_{\mathcal G}\prod_{j=1}^3q_{\mathfrak g_j},
\]

each labelled route is

\[
r_{G|g}=\frac1{q_Gq_g}.
\]

The source external-energy coordinates are \((X_1,X_2,X_3)\).  Form the
observer filtration from the value, all first derivatives, and all symmetric
second derivatives:

\[
\mathcal O_{\le2}(r)=
\left(
r,\partial_ir,\partial_i\partial_jr
\right)_{1\le i\le j\le3}.
\]

No deletion fugacity, fitted projector, tensor polarization, or free
spectral kernel is introduced.

## Exact rank witness

At the exact generic point

\[
(X_1,X_2,X_3)=(2,3,5),
\qquad
(y_{12},y_{23},y_{31})=(7,11,13),
\]

the exact finite-field ranks are

\[
\boxed{
\operatorname{rank}\mathcal O_0=1,
\qquad
\operatorname{rank}\mathcal O_{\le1}=4,
\qquad
\operatorname{rank}\mathcal O_{\le2}=6.
}
\]

The six-column matrix cannot have rank greater than six.  One nonzero exact
six-minor therefore proves generic full column rank on a Zariski-open locus.

## Result

The scalar aggregation forgets five labelled directions.  First
external-energy scores recover three of them but retain a two-dimensional
blind space.  Second scores recover the complete packet:

\[
\boxed{
\ker\mathcal O_{\le1}\cong\mathbb Q^2,
\qquad
\ker\mathcal O_{\le2}=0.
}
\]

Thus the first genuinely interacting scalar source tested here remains
contextually faithful, but requires second rather than first observer grade.
This is the first non-free deformation of the score-faithfulness mechanism.

## Scope boundary

The theorem is at the labelled integrand level.  It does not prove that:

- the corresponding derivative insertions survive integration;
- the physical Bunch--Davies relative cycle exposes all ten ports;
- the rank remains six on soft, Gram, Landau, total-energy, or marked-wall
  support;
- a tensor-polarization observer exists.

Those are the next gates.  Entry 2306 independently proves that the tensor
vertex cannot be reconstructed from this scalar packet alone.

## Durable verification

- `research/benincasa/checkers/interacting_scalar_simplex_score.rs`;
- `research/benincasa/interacting-scalar-simplex-score.json`;
- allocator claim `seqclaim-82d009b2351d14e9757a634e`.

