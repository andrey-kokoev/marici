---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 791 — Boundary-Minor Regularity Makes the Exceptional Betti Monodromies Trivial

## Frozen Betti object

The source contour is not defined by the top Cayley--Menger determinant
alone. Equations (3.9) and (A.11) of Benincasa--Vazão,
arXiv:2402.06558v3, require

\[
(-1)^{k+1}CM(I_k,J_k)\geq0
\]

for every labelled row/column deletion pair. For the three-site matrix
(A.10), this is the complete set of

\[
100\text{ minors of size }3,
\qquad
25\text{ minors of size }4,
\qquad
1\text{ determinant of size }5.
\]

The source-oriented chamber fundamental relative-cycle class is denoted

\[
\gamma_{CM}.
\]

This class and its measure branch are retained before the \(\mu_2\)-trace.

## Complete weighted-minor audit

Use the frozen physical chart

\[
P_1=1,
\qquad
P_2=u^2t,
\qquad
P_3=u-1-u^2t,
\]

and the collision resolution

\[
A-B=u\xi.
\]

For each of the 126 labelled minors, the exact Rust/Symbolica checker:

1. computes the determinant as a polynomial in \(u\) and \(t\);
2. extracts its first nonzero \(u\)-coefficient;
3. evaluates that initial form independently at \(t=1\) and \(t=-1\).

The census is

\[
\boxed{
\begin{aligned}
N_{\rm audited}&=126,\\
N_{\rm identically\ zero}&=0,\\
N_{t=1\rm\ degenerate}&=0,\\
N_{t=-1\rm\ degenerate}&=0.
\end{aligned}
}
\]

Thus neither coefficient puncture is a discriminant point of the complete
labelled Cayley--Menger relative pair. Entry 788 also shows that the resolved
measure current is regular there through first normal correction.

## Local relative-cycle monodromy

Around each point choose a sufficiently small disk avoiding the existing
\(t\)-independent exceptional discriminant and soft support. The complete
labelled relative pair and the frozen measure branch extend over the disk,
not merely its punctured complement. Therefore the source chamber class has
trivial local continuation.

In the source-normalized basis \((\gamma_{CM})\),

\[
\boxed{
M^{\rm cycle}_{+}=(1),
\qquad
M^{\rm cycle}_{-}=(1).
}
\]

The Poincaré orientation is unchanged and both local \(t\)-loops carry deck
character \(+1\). No symmetry inference is used: the two evaluations are
performed separately.

## Consequence for the descent test

The combined invariance conditions reduce to

\[
\left\langle M^{\rm coeff}_{\pm}v,\gamma_{CM}\right\rangle
=
\left\langle v,\gamma_{CM}\right\rangle.
\]

Hence all nontrivial local obstruction at \(t=\pm1\) must lie on the
coefficient/comparison side. Trivial Betti monodromy does not itself prove
that the pairing descends: the exceptional coefficient line must be fixed by
both coefficient monodromies with a compatible source normalization.

## Verification

- exact checker:
  `research/benincasa/marici-gm/src/bin/cayley_menger_boundary_minor_monodromy.rs`;
- machine-readable convention and result packet:
  `research/benincasa/cayley-menger-boundary-minor-monodromy.json`;
- allocator claim `seqclaim-84116c30f02e61d40ed1c7fd`.

## Narrow status

The Betti half of the two-puncture descent test is closed generically:

\[
\boxed{M^{\rm cycle}_{+}=M^{\rm cycle}_{-}=1.}
\]

The remaining finite falsifier is Nima's independently computed coefficient
monodromy on

\[
\ell_{\rm exc}=\mathbf Q(0,1,0,-3)
\]

and the resulting pairing/intertwining test before the \(\mu_2\)-trace.
