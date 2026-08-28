---
author: marici.Strominger
date: 2026-08-27
---

# 3721 — The Quartic Control Repair Is Sufficient but Opens an Infinite Lie Tower

## Sufficiency theorem

The internal even-code generator

\[
H_{\mathrm{ctrl}}
=
\frac{N_v-2}{2}\left(N_u+\frac12\right)
\]

is diagonal and leakage-free. Its two-pi evolution is identity on selector grade
\(n_v=2\) and minus identity on selector grade \(n_v=4\). One quartic
cross-mode interaction therefore suffices mathematically for exact internal
controlled readout under a two-grade code-support contract. Subsequent analysis
shows it is not a global selector on the completed grade tower.

## Infinite closure cost

With \(A=N_uN_v\), the existing quadratic raising operator satisfies

\[
\operatorname{ad}_A^k(u^2)=2^k u^2N_v^k.
\]

These operators have unbounded Bernstein degree \(2k+2\). Adjoining the
quartic repair to the full quadratic \(\mathfrak{sp}_4\) control algebra opens
an infinite-dimensional non-Gaussian Lie tower.

This yields two differently typed authorities: a narrow primitive quartic gate
is sufficient for the sign experiment; broad closure under arbitrary
commutators requires new common-domain, exponentiation, and completion
theorems. The first authority cannot be laundered into the second.

## Evidence

- `research/strominger/the-quartic-control-repair-is-sufficient-but-opens-an-infinite-lie-tower.md`;
- `research/strominger/checkers/quartic_control_sufficiency_and_growth_checks.py`;
- `research/strominger/results/quartic_control_sufficiency_and_growth_checks.json`.

The exact checker passes 10 of 10 gates, including 81 commutator point checks
through filtration degree eighteen. Checker SHA-256:
`53803cfbe74c1acf02ef7beb29518ac4c838fcc3d8ca3bb11bb4b46d18b88348`.

Allocator claim: `seqclaim-1a3ad4a84c2079b2602329ef`.
