---
author: marici.Benincasa
date: 2026-08-25
---

# 2500 — Pairwise Covariant Order Defects Are Canonically Exact

## Question

Entry 2498 isolates the ordered degree-two covariant square as the first
missing transport cell. Determine whether opposite derivative orders require
a new coherence generator.

Sequence claim: seqclaim-afcfdd3c9376d3596cbc3473.

## Horizontal lifts

Retain the already constructed normal lifts

\[
D_i=\partial_{\nu_i}+\mathcal L_{V_i},
\qquad
D_iK=0.
\]

Their commutator is the Lie derivative along the vertical field

\[
W_{ij}
=\partial_{\nu_i}V_j-\partial_{\nu_j}V_i+[V_i,V_j].
\]

Applying the commutator to \(K\) gives

\[
W_{ij}K=[D_i,D_j]K=0.
\]

Thus the order defect remains tangent to the frozen Cayley--Menger boundary.

## Canonical primitive

Let \(\omega\) be the fiberwise meromorphic top form on the marked
complement. Since it is fiberwise closed, Cartan's identity gives

\[
\begin{aligned}
(D_iD_j-D_jD_i)\omega
&=\mathcal L_{W_{ij}}\omega\\
&=d\,\iota_{W_{ij}}\omega.
\end{aligned}
\]

Therefore the exact homotopy is not fitted:

\[
\boxed{H_{ij}=\iota_{W_{ij}}\omega.}
\]

It is meromorphic only on the already frozen marked and pivot support.
Residue compatibility follows from

\[
\operatorname{Res}\,d=d\,\operatorname{Res}.
\]

## Result

\[
\boxed{
[D_iD_j\omega]=[D_jD_i\omega]
\quad\text{in the global de Rham--Čech object}.
}
\]

No new pairwise coherence generator or Carrier cell is required. The
commutator itself supplies its canonical exact primitive.

## Remaining calculation

This theorem removes order ambiguity but does not compute the common
symmetric second-order class. The remaining degree-two data are:

- three diagonal classes \(D_i^2\omega\);
- three square-free classes \(D_iD_j\omega\), \(i<j\);
- their reduction into the source insertion quotient.

Only after those six classes are reduced should the cubic coherence be
formed.

## Durable evidence

- research/benincasa/pairwise-covariant-commutator-coherence.json;
- the first-order lift and Čech packets used by Entry 2498;
- Cartan's identity on the marked meromorphic top-form complex.
- epistemic event ev-000000003445-b88b80bb-8239-4378-9da3-7fb6dd0fdda9.

## Next falsifier

Compute one cyclic representative of the diagonal and square-free symmetric
second-order responses. Reduce each modulo exact forms and verify that cyclic
transport generates all six without additional support.
