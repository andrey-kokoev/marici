---
author: marici.Kitaev
---

# 2249 — Two D(S3) Flux Ports Give Projective but Not Full Block-Unitary Control

**Sector:** Kitaev (dynamical Lie control)

## Claim and correction

Hermitian gauge quadratures together with one transposition- and one
three-cycle-flux projector generate a real Lie algebra of dimension

\[
\boxed{33<36}.
\]

Full associative generation therefore does not imply full blockwise
`U(d_a)` control.  Three independent central phase combinations are absent;
the available trace-signature rank is five rather than eight.

The derived commutator algebra is nevertheless complete projectively:

\[
\dim[\mathfrak g,\mathfrak g]=28=\sum_a(d_a^2-1),
\]

with block ranks `(0,0,3,8,8,3,3,3)`.  Hence every nontrivial block has full
special-unitary control.  This is sufficient for conjugation twirls because
scalar phases cancel, but not for arbitrary coherent relative sector phases.

## Scope

This exact finite Lie theorem does not derive pulse locality, amplitudes,
time-ordering synthesis, leakage suppression, or fault tolerance from the
Hamiltonian.

## Durable verification

- Packet: `research/kitaev/s3-two-flux-projective-lie-controllability.md`
- Checker: `research/kitaev/checkers/check_s3_two_flux_lie_control.py`
- Result: `research/kitaev/results/s3-two-flux-lie-control.json`
- Invocation: `uv run --with sympy --with numpy python -u research/kitaev/checkers/check_s3_two_flux_lie_control.py`
- Exact result: eight gates pass; fresh stdout matches saved JSON.
- Falsifier residual: full block-unitary dimension deficit `36-33=3`.
- Epistemic graph event:
  `ev-000000003116-cb1a348a-018f-447f-8c11-77f945d7608f`
