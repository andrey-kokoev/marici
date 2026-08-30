# Instanton-seed authority (WP355)

## Candidate threshold

A quantized nonperturbative sector could generate the geometry seed

\[
t_n=\exp\left(-\frac{8\pi^2n}{g^2}\right),
\qquad
n\in\mathbb Z_{>0}.
\]

The integer charge discretizes sectors and the exponential protects smallness.
It does not remove coupling authority:

\[
\frac{\partial\log t_n}{\partial\log g}
=\frac{16\pi^2n}{g^2}.
\]

Successive charge sectors differ by another factor
(\exp(-8\pi^2/g^2)).

## Control-domain test

Using WP353's fitted-scale capability estimate, a unit-charge seed would require
a coupling greater than 1. In the declared weak-coupling domain (g\leq1), the
largest unit-charge seed is (exp(-8\pi^2)), more than twenty orders below the
required scale.

This does not exclude a strong-coupling nonperturbative constructor. It excludes
using the elementary semiclassical formula as a controlled explanation at the
required value.

## Disposition

Instantons can carry and protect smallness, but the coupling, determinant
prefactor, threshold scale, and RG matching must be derived independently.
Choosing (g) from the observed (J) would be continuous source fitting.

Run `uv run --with sympy python
research/flavor/checkers/wp355_instanton_seed_authority.py` to regenerate the
exact authority and control audit.
