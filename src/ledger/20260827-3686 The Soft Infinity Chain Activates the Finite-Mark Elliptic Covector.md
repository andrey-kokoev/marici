---
author: marici.Benincasa
date: 2026-08-27
---

# 3686 — The Soft Infinity Chain Activates the Finite-Mark Elliptic Covector

## Frozen gate

Entry 3678 derives the first (P_3)-normal Abel–Jacobi covector of the odd
mark over (t=-1). Its image is the diagonal line dual to

\[
\omega_0+\omega_2
=\frac{(1+t^2)dt}{W}.
\]

The remaining question is whether the source infinity chain has a supported
specialization that pairs nontrivially with this line.

## Soft real-locus factorization

At (z=P_3=0),

\[
W^2=F_0(t)
=(t^2-1)(x^2t^2-y^2).
\]

Choose the generic chamber (x>y>0). The positive branch points on the
source projective ray are

\[
t=\frac yx,
\qquad
t=1.
\]

The real Cayley–Menger boundary has two components,

\[
\left[0,\frac yx\right]
\quad\text{and}\quad
[1,\infty],
\]

while (F_0<0) on the intervening interval. The source boundary-value
prescription therefore supplies the deck-odd loop around the cut

\[
\left(\frac yx,1\right).
\]

This is the supported specialization of the sign-weighted infinity chain.

## Pairing

Up to the source-fixed orientation sign, its pairing with the diagonal form
is

\[
2i\int_{y/x}^{1}
\frac{(1+t^2)dt}{\sqrt{-F_0(t)}}.
\]

The integrand has constant phase and strictly positive magnitude in the open
interval. Both endpoints are simple branch points, so the inverse-square-root
singularities are integrable. The pairing is therefore finite and nonzero.

An exact hostile point is

\[
(x,y)=(2,1),
\]

where

\[
F_0(t)=(t-1)(t+1)(2t-1)(2t+1)
\]

and the supported cut is ((1/2,1)).

## Classification

The finite-mark coefficient direction is physically activated, but only as a
supported class at the existing soft–signed boundary:

- direct incidence on the generic nonsoft infinity ray remains empty;
- first soft-normal transport maps the marked difference into the diagonal
  elliptic covector;
- the source boundary-value chain supplies a nonzero deck-odd pairing;
- no new carrier divisor or incidence stratum is required.

Thus the full marked-relative object contributes physical information through
supported transport rather than through generic pointwise incidence.

## Next falsifier

Transport this local pairing through the three cyclic occurrence charts.
Verify residue orientation, deck character, and whether cyclic summation
preserves the class or cancels it. The local nonzero period does not determine
the global occurrence descent.

## Evidence

- `research/benincasa/checkers/check_infinity_soft_supported_cycle_pairing.py`;
- `research/benincasa/results/infinity-soft-supported-cycle-pairing.json`;
- Entries 796, 3674, and 3678.

The exact checker passes seven of seven gates.

Epistemic graph event:
`ev-000000007913-6e3bb741-a37b-42f8-8d23-0929047e9d8a`.

Allocator claim: `seqclaim-5f30c01787cff47e5b699e3f`.
