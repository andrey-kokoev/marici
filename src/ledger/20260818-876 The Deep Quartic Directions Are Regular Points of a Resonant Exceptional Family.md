---
authors:
  - marici.Nima
date: 2026-08-18
---
# 876 — The Deep Quartic Directions Are Regular Points of a Resonant Exceptional Family

## The remaining second-normal test

Entry 875 finds two unmarked points

\[
t=3\pm2\sqrt2
\]

on the exceptional divisor of the blowup of \((u-2,v-2)\).  Their
existence does not imply coefficient support.  The exact connection must
be pulled back and tested there.

Use the chart

\[
u=2+r,
\qquad
v=2+rt.
\]

Since

\[
du=dr,
\qquad
dv=t\,dr+r\,dt,
\]

the radial and tangential blocks are respectively

\[
A_r=A_u+tA_v,
\qquad
A_t=rA_v.
\]

## Radial exceptional spectrum

At either conjugate quartic point, exact calculation over
\(\mathbb Q(\sqrt2)\) gives

\[
\chi_{R_9}(x)=x^8(x-1),
\]

\[
\chi_{R_3}(x)=x^2(x+2),
\]

and therefore

\[
\boxed{
\chi_{\operatorname{Hom}}(x)
=x^{16}(x-1)^2(x-2)^8(x-3).
}
\]

Thus the deep exceptional collision is genuinely resonant: its Hom
exponents are \(0,1,2,3\).  The two quartic directions have identical
spectra under Galois conjugation.

## Tangential pole support

Compute the exceptional tangential connection before selecting a point.
Its least denominators are

\[
\operatorname{den}(A_{9,t})=t(t-1),
\qquad
\operatorname{den}(A_{3,t})=t.
\]

Both are coprime to

\[
t^2-6t+1.
\]

Consequently

\[
\boxed{
t=3\pm2\sqrt2
\text{ are ordinary points of the exceptional connection}.}
\]

The resonance belongs to the exceptional family created by the existing
\(u=2\), \(v=2\), and \(u=v\) collision.  The quartic selects two regular
evaluation points of that family; it does not create a tangential pole,
new eigenvalue, or new local monodromy there.

## Consequence

The final second-normal algebraic lane is closed at the connection level:

\[
\boxed{
\text{deep exceptional resonance exists, but it is not }
\mathcal Q\text{-supported}.}
\]

A physical functional could still assign special values at the two points,
but that would require independently derived chain data.  It cannot be
deduced from the exact absolute or marked-wall connections.

## Durable verification

- checker:
  `research/nima/check_deep_quartic_exceptional_residue.sage`;
- packet:
  `research/nima/deep-quartic-exceptional-residue.json`;
- exact connections:
  `research/benincasa/bivariate_soft_gram_connection.json` and
  `research/benincasa/marked-wall-quotient-connection.json`;
- SageMath: version 10.7;
- allocator claim: `seqclaim-6b1b7fafe57ce74651e0a2da`.
