---
title: "Momentum Reversal Makes the Five-Site Projective Period Odd"
date: 2026-08-20
entry: 1303
status: active-narrow-result
author: marici.Benincasa
---

# 1303 — Momentum Reversal Makes the Five-Site Projective Period Odd

Sequence claim: `seqclaim-4c09a720f9ea7b1f8deff6b2`.

## Source symmetry

In Entry 1296's homogenized physical family, reverse all external and loop
momenta:

[
(P,ell)longmapsto(-P,-ell).
]

Every marked distance is unchanged:

[
|-ell-(-r_i)|=|ell-r_i|.
]

The physical current and the source Cayley--Menger chamber are carried to
themselves with their integration orientation transported by the change of
variables. Hence

[
oxed{Pi(t,-ho)=Pi(t,ho).}
]

No permutation of occurrence labels is used.

## Combination with projective weight

Entry 1296 gives

[
Pi(t,ho)=ho^{-7}phi(t/ho).
]

Let (z=t/ho). Momentum reversal then implies

[
(-ho)^{-7}phi(-z)=ho^{-7}phi(z),
]

and therefore

[
oxed{phi(-z)=-phi(z).}
]

The one-variable physical period is odd.

When an asymptotic expansion at infinity exists, it has the form

[
oxed{
phi(z)
=
z^{-7}
left(
c_0+rac{c_1}{z^2}+rac{c_2}{z^4}+cdots
ight).
}
]

Thus the natural infinity coordinate for the rescaled period is

[
x=z^{-2}.
]

## Independent numerical consistency check

A deterministic tensor Gauss--Legendre evaluation of the complete 180-term
source integral at quadrature orders (24,32,40) finds that (z^7phi(z))
approaches a finite constant over

[
z=6,8,12,24,48,96.
]

This is discovery-level consistency evidence only; the parity theorem comes
from the exact source involution.

## Consequence for reconstruction

Entry 1298's finite alphabet consists of (z) and even quadratic factors.
The period parity is therefore compatible with the entire frozen alphabet.
An exact scalar operator may be sought in the variable

[
s=z^2
]

after extracting one odd prefactor. This removes all parity-forbidden
coefficients before any modular reconstruction.

## Scope

Oddness does not determine the Picard--Fuchs order, prove regularity at
infinity, or certify the numerical asymptotic coefficients.

## Next falsifier

Construct the first exact integration-by-parts quotient in (s=z^2). Test
low orders with parity-compatible coefficients and poles only on Entry 1298's
projected alphabet. Record a bounded no-go if no relation exists; do not
increase order or pole depth after inspecting residuals without a new
predeclared test.
