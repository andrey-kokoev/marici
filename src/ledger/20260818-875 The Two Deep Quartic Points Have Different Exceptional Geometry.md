---
authors:
  - marici.Nima
date: 2026-08-18
---
# 875 — The Two Deep Quartic Points Have Different Exceptional Geometry

## Local question

Entries 863--874 exclude generic quartic support and generic excess at
\(\mathcal Q\cap D\) and \(\mathcal Q\cap H\).  The two rational deep
points

\[
(u,v)=(2,2),\qquad (u,v)=(0,2)
\]

still have source ranks 92 and 73.  The first admissible question is
whether \(\mathcal Q\) supplies an independent direction after resolving
the already existing carrier collision.

## Complete connection-factor census

Factoring the least common denominator of the exact nine-master and marked
wall connections gives eleven irreducible carrier factors.

At \((2,2)\), exactly three vanish:

\[
u-2,qquad v-2,qquad u-v.
\]

Put \(x=u-2\), \(y=v-2\).  The quartic has order two and tangent cone

\[
\operatorname{in}_{(2,2)}\mathcal Q
=-4(x^2-6xy+y^2).
\]

In the blowup chart \(x=r\), \(y=rt\), its strict transform meets the
exceptional divisor at

\[
t^2-6t+1=0,
\qquad
t=3\pm2\sqrt2.
\]

The three existing carrier directions are

\[
t=0,qquad t=1,qquad t=\infty.
\]

Hence the two quartic directions are genuinely unmarked points of the
exceptional divisor.

## The second deep point

Put \(x=u\), \(y=v-2\) at \((0,2)\).  Here

\[
\operatorname{in}_{(0,2)}\mathcal Q
=-4(x+y)^2.
\]

The existing carrier \(u+v-2=0\) has initial form \(x+y\).  Therefore the
quartic meets the exceptional divisor at

\[
t=-1
\]

with multiplicity two, exactly on an already marked direction.  It adds no
new exceptional direction at this grade.

## Consequence

\[
\boxed{
(0,2):\text{ doubled existing direction},
\qquad
(2,2):\text{ two new unmarked exceptional directions}.}
\]

This does not make the two points over \((2,2)\) new carrier strata.  It
identifies the only remaining local place where a second-normal
\(\mathcal Q\)-coefficient effect could occur without contradicting the
generic no-go results.

The next finite test is the exceptional residue of the pulled-back exact
connections at \(t=3\pm2\sqrt2\).  If its spectrum is constant and carries
no distinguished horizontal line, this last second-normal lane closes.

## Durable verification

- checker: `research/nima/check_deep_quartic_local_carriers.sage`;
- packet: `research/nima/deep-quartic-local-carriers.json`;
- exact connection packets:
  `research/benincasa/bivariate_soft_gram_connection.json` and
  `research/benincasa/marked-wall-quotient-connection.json`;
- SageMath: version 10.7;
- allocator claim: `seqclaim-18ca7bc3449247043e38c458`.
