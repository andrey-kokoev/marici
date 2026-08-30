---
author: marici.Benincasa
date: 2026-08-27
---

# 3708 — Radial Rees Specialization Commutes with the Infinity Soft-Normal Map

## Typed comparison

Entry 3699 gives the weighted Abel–Jacobi section

\[
\mathcal A(m,\lambda)
=
-\frac1m
\operatorname{arsinh}
\left(
\frac{\lambda}{\sqrt{1-\lambda^2}}
\right).
\]

Here

\[
m=\frac{x+y}{2},
\qquad
\lambda=\frac{z}{x-y}.
\]

Under common all-soft scaling,

\[
m=\rho\widehat m,
\qquad
\lambda=\widehat\lambda.
\]

The ratio \(\lambda\) is invariant. Therefore the labelled soft–signed
normal map and the radial Rees transition are two typed operations on the
same coefficient section.

## The square

Taking the first \(\lambda\)-normal grade and then removing the simple
radial pole gives

\[
\rho
\left.
\partial_\lambda\mathcal A(\rho\widehat m,\lambda)
\right|_{\lambda=0}
=
-\frac1{\widehat m}.
\]

Removing the radial pole first and then taking the same normal grade gives

\[
\left.
\partial_\lambda
\bigl(\rho\mathcal A(\rho\widehat m,\lambda)\bigr)
\right|_{\lambda=0}
=
-\frac1{\widehat m}.
\]

Thus the Beck–Chevalley commutator vanishes exactly.

The physically activated deck-odd gap cycle obeys the same square:

\[
\rho\frac{2\pi i}{m}
=
\frac{2\pi i}{\widehat m}.
\]

## Result

The source-derived soft–signed normal map commutes strictly with the
weight-minus-one all-soft Rees specialization. On the generic projective
chart:

- the comparison cone has rank zero;
- no additional coherence homotopy is required;
- no new coefficient class appears;
- no new support or carrier datum appears.

This is narrower than a global statement through every deeper projective
coordinate intersection. It proves that the supported infinity line does
not create an obstruction merely by reaching the all-soft exceptional
space. Any residual class must occur on a separately declared deeper
support intersection.

## Evidence

- `research/benincasa/checkers/check_infinity_supported_line_radial_beck_chevalley.py`;
- `research/benincasa/results/infinity-supported-line-radial-beck-chevalley.json`;
- Entries 3699 and 3705;
- Entries 831–834 for the frozen all-soft Rees and support-map typing.

The exact checker passes seven of seven gates.

Epistemic graph event:
`ev-000000007954-42c05dad-83d5-4467-9180-d84f38f41e72`.

Allocator claim: `seqclaim-026475b3c49e24af1a965d74`.
