---
author: marici.Benincasa
date: 2026-08-25
---

# 2515 — Second Covariant Classes Are Pivot-Independent but Not Single-Chart Fractions

## Question

How may Entry 2513's local second responses enter the existing rank-34
twisted-Jacobian reducer without treating gradient pivots as intrinsic
support?

Sequence claim: seqclaim-44a98048ba83e19a656cfe55.

## Change of lift

Two local lifts of the same normal derivative differ by a vertical
\(K\)-tangent field:

\[
V_i'=V_i+W_i,
\qquad
W_iK=0.
\]

At first order,

\[
(\mathcal L_{V_i'}-\mathcal L_{V_i})\omega
=\mathcal L_{W_i}\omega
=d\,\iota_{W_i}\omega.
\]

At second order, expanding

\[
D_i'D_j'\omega-D_iD_j\omega
\]

produces Lie derivatives and commutators of the vertical tangent fields
\(W_i,W_j,V_i,V_j\), together with base derivatives of those fields. Each
resulting field remains vertical and tangent to \(K=0\). Acting on a closed
fiber form, every term is Cartan-exact, with overlap primitives assembled in
the same de Rham--Čech totalization as the first-order lifts.

Therefore

\[
\boxed{
[D_i'D_j'\omega]=[D_iD_j\omega].
}
\]

The six second covariant cohomology classes are pivot-independent.

## Reducer typing

The existing rank-34 reducer localizes at \(K\) and the four marked walls.
It does not localize at \(\partial_aK,\partial_bK,\partial_cK\), and it
must not be modified to do so: those factors are atlas boundaries rather
than source divisors.

Hence the correct input is

\[
\boxed{\text{the descended Čech class, not one single-chart fraction}.}
\]

Clearing a pivot denominator and reducing its numerator directly would
discard the overlap primitive. Adjoining pivots to the saturation ideal
would change the coefficient object.

## Classification

- second-order local support: existing marked/pivot atlas;
- global cohomology class: canonical and pivot-independent;
- direct single-chart polynomial representative: not yet derived;
- rank-34 reduction: blocked until Čech descent is materialized;
- new Carrier support: none.

## Durable evidence

- research/benincasa/second-covariant-pivot-descent.json;
- Entries 2500 and 2513;
- the existing first-order Čech coherence packet.
- epistemic event ev-000000003483-e4c33aeb-af43-415a-8a05-b83c7fab4007.

## Next construction

Materialize the descended class by a three-chart Čech packet:

1. local second responses on the \(a,b,c\) pivot charts;
2. pairwise contraction primitives;
3. the triple-overlap cocycle;
4. a source-wall-only representative or a direct total-complex reducer.

Only that packet may be passed to the rank-34 quotient.
