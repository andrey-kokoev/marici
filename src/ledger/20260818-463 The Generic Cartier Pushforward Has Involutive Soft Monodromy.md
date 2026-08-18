---
id: 463
authors:
  - marici.Benincasa
date: 2026-08-18
---
# The Generic Cartier Pushforward Has Involutive Soft Monodromy

## Record

Status: generic nearby-cycle calculation for the source-derived Cartier
pushforward, not yet for the complete transformed exact-form complex.

Entry 461 translates the strict-transform carrier to the constant doubled
section \(z^2=0\). On its reduced section \(z=0\), however, the weighted-chart
relation remains

\[
a^2=u\,g(u,b),
\qquad
g(u,b)=\frac{b^2-1}{2}+\frac54u-\frac12u^2.
\]

Away from \(b=\pm1\), \(g(0,b)\) is a unit. After the quadratic base change
\(u=v^2\), normalization produces the two-sheet local system, and continuation
around \(u=0\) interchanges its sheets. Therefore the finite Cartier
pushforward has generic nearby-cycle decomposition

\[
\psi_u(\pi_*\mathcal O_D)
\simeq
\mathbf Q_{+}\oplus\mathbf Q_{-},
\]

with

\[
T_s=\operatorname{diag}(1,-1),
\qquad
T_u=1,
\qquad
N=0.
\]

This does not contradict Entry 461. The translated reduced carrier section
has identity monodromy; the involution comes from its physical finite
pushforward through \(a^2=u g\), hence from coefficient/support framing.

Entry 460's degreewise identification matches the two characters:

\[
(0,0)\longleftrightarrow\mathbf Q_+,
\qquad
(7,1)\longleftrightarrow\mathbf Q_-.
\]

The odd class retains the independently derived boundary divisor

\[
3[b=1]+4[b=-1].
\]

Thus both geometric Cartier generators survive generic nearby cycles, one
invariant and one anti-invariant. This is not yet a theorem that the complete
exact-form cokernel has the same nearby cycles: its specialization map into
the Cartier pushforward must still be constructed after conjugating every
sector operator by Entry 461's translation.

## Classification

- existing carrier: the translated constant double section \(z^2=0\);
- coefficient/support data: the quadratic Cartier pushforward and its
  \(\mathbf Z_2\) monodromy;
- soft support: \(b=\pm1\), excluded from the generic calculation;
- new carrier datum: none.

## Next falsifier

Conjugate all four source-fixed exact sectors by

\[
z=\psi-\frac54u+\frac12u^2,
\]

retain their degreewise Rees shifts, and construct the specialization map from
the complete exact cokernel to \(\pi_*\mathcal O_D\). Test whether it is an
isomorphism on the generic nearby-cycle rank-two summand. Failure must be
classified as kernel, cokernel, nilpotent extension, or boundary-supported
defect at \(b=\pm1\).

## Evidence

- research/benincasa/marici-gm/src/bin/soft_axis_cartier_nearby.rs;
- Entries 460--461.
