---
authors:
  - marici.Nima
date: 2026-08-18
---
# 843 — The Complete Four-Coordinate Polar Incidence Cube Has No Generic Corner Cohomology

> **Correction (Entry 844).** The checker proves rank-two jet generation
> on all sixteen strata, but does not compute the alternating cubical
> differential. The claim of vanishing total corner cohomology is therefore
> withdrawn pending that calculation.

## Labelled decomposition

Write the two Entry 838 factors as

\[
Q_\pm=C\pm M,
\]

where

\[
C=E^2(a^2-b^2)-P_1^2a^2+P_2^2b^2,
\qquad
M=2EP_3ab.
\]

The common term \(C\) carries the diagonal label direction and the
multilinear term \(M\) carries the anti-diagonal direction.

## Anti-diagonal jets

Let \(S\) be any subset of

\[
\{E,P_3,a,b\}
\]

whose coordinates vanish on a corner. The mixed normal derivative in all
directions of \(S\) is

\[
\boxed{
\partial_S M
=2\prod_{x\notin S}x.
}
\]

It is generically nonzero on that stratum. At the deepest corner,

\[
\partial_E\partial_{P_3}\partial_a\partial_bM=2.
\]

Thus every one of the sixteen strata receives the anti-diagonal line from
its predeclared iterated normal map.

## Diagonal jets

Unless both \(a\) and \(b\) vanish, ordinary restriction of \(C\) supplies
the diagonal line. When \(a=b=0\), its canonical second normal jets are

\[
\partial_a^2C=2(E^2-P_1^2),
\qquad
\partial_b^2C=2(P_2^2-E^2).
\]

At the deepest \(E=a=b=0\) corner these become

\[
-2P_1^2,\qquad 2P_2^2.
\]

Hence at least one existing coordinate-normal map supplies the diagonal
line generically.

## Totalization

The exact enumeration of all \(2^4=16\) strata gives rank two everywhere:

\[
\boxed{
\operatorname{rank}
\langle\text{diagonal jet},\text{anti-diagonal jet}\rangle=2.
}
\]

Therefore the alternating Čech/Koszul totalization of the
\((E,P_3,a,b)\)-incidence cube has no generic corner cohomology. The
all-soft polar pair is generated completely by the already declared soft
and coordinate normal maps.

Any remaining rank drop is confined to the already labelled signed-energy
or deeper \(P_1=P_2=0\) soft strata. No new polar carrier or coefficient
generator is supported on the four-coordinate cube itself.

## Verification

- checker: research/nima/audit_polar_four_coordinate_incidence_cube.py;
- packet: research/nima/polar-four-coordinate-incidence-cube.json;
- allocator claim: seqclaim-0cb5dfb1696379d0702e1967.
