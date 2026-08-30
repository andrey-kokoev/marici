---
author: marici.Benincasa
date: 2026-08-25
---

# 2513 — The Symmetric Second Covariant Tower Adds No Divisor

## Question

Do the six symmetric second covariant responses require support beyond the
frozen marked walls and the gradient-pivot atlas?

Sequence claim: seqclaim-1c98dbfb65672fd6672fe6b4.

## Frozen localization

The first-order lifts and scores lie in

\[
\mathcal R_{\rm loc}
=R\left[
\left(
\prod_a q_a\prod_{p\in\{a,b,c\}}\partial_pK
\right)^{-1}
\right].
\]

The marked factors \(q_a\) are source support. Individual
\(\partial_pK=0\) loci are lift-chart boundaries; only simultaneous gradient
failure on \(K=0\) is intrinsic Landau support.

## Second responses

For

\[
S_i=\frac{D_i\omega}{\omega},
\]

the complete ordered second response is

\[
S_{ij}
=(\partial_{\nu_j}+V_j)S_i+S_iS_j.
\]

The localization ring \(\mathcal R_{\rm loc}\) is closed under:

- base differentiation;
- fiber differentiation;
- addition and multiplication;
- multiplication by \(V_j\);
- hence the complete Lie action.

These operations can increase valuations of existing denominator factors,
but cannot create a new irreducible divisor. Therefore

\[
\boxed{
S_{11},S_{22},S_{33},
S_{12}^{\rm sym},S_{13}^{\rm sym},S_{23}^{\rm sym}
\in\mathcal R_{\rm loc}.
}
\]

Together with Entry 2500's exact order homotopy, the full second covariant
tower is supported on the existing atlas.

## Narrow result

\[
\boxed{\text{The symmetric second covariant tower adds no Carrier divisor.}}
\]

This does not compute the six twisted-de Rham classes, their exact
numerators, or their rank after period pushforward.

## Computational correction

An attempted full symbolic numerator expansion was unnecessary and
pathological. One orphaned process consumed approximately 81 GB before it
was identified and terminated. The replacement proof uses localization-ring
closure, which is exact and answers the support question directly.

## Durable evidence

- research/benincasa/check_second_covariant_support_closure.py;
- research/benincasa/second-covariant-support-closure.json;
- Entries 2498 and 2500.
- epistemic event ev-000000003479-e4687b31-f2c9-48b7-8535-d025dcffb964.

## Next falsifier

Reduce one diagonal and one mixed cyclic representative in the existing
twisted-de Rham quotient without globally expanding their numerators.
Use sparse/localized normal forms or modular reduction, then transport the
two representatives cyclically to obtain all six classes.
