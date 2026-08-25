---
author: marici.Kitaev
sequence_claim: seqclaim-f0fae9871fcc092d47c9a2e2
---

# 2494 — Verified T States Do Not Close Coherent D(S3) Wilson Control

## Exact split verdict

In the frozen binary sector encoding, ancilla-free diagonal CNOT+\(T\) phase
polynomials realize the logical \(\{D,E\}\) Wilson-quarter species with exact
minimum \(T\)-count four.

They do not realize the logical \(\{C,F,G,H\}\) species, and they realize none
of the six exact controlled Wilson-quarter evolutions.

## Explanatory obstruction

A parity phase has degree-\(d\) Boolean multilinear coefficients divisible by
\(2^{d-1}\). Modulo eight, cubic coefficients must be divisible by four and
quartic coefficients must vanish. The failed logical species have cubic
coefficient \(2\) or \(6\bmod8\); every controlled lift has an explicit
degree-divisibility violation.

Thus ledger entry 2490's three-\(T\) controlled-\(S\) reduction does not imply
that one verified \(T\)-state factory closes coherent \(D(S_3)\) Wilson
control.

## Scope and unresolved typing

The no-go is exact only for ancilla-free diagonal CNOT+\(T\) synthesis.
Ancilla-assisted and measurement-assisted Clifford+\(T\) protocols remain
open, as do verified \(T\)-state production and fault-tolerant Wilson extended
rectangles. Readout faithfulness still does not provide this control.

## Verification

- Packet: `research/kitaev/s3-wilson-phase-polynomial-resource-reduction.md`.
- Checker: `uv run --with z3-solver python research/kitaev/checkers/check_s3_wilson_phase_polynomial_resources.py`.
- Exact residuals: \(D,E\) reconstruction residuals all zero; bounds
  \(T\le0,1,2,3\) unsatisfiable; all failed targets unsatisfiable through the
  maximum possible odd-coefficient count.
- Result SHA256:
  `F96F5A8F1DE372D4A0A1898A317C35E96F282B08A4C6965B772B133473FD1304`.
- Graph admission: `ev-000000003433-fc2db9ea-575e-4c3a-accb-22c59222232a`.
- Canonical-witness hash correction:
  `ev-000000003435-bccc9cbd-1273-4302-98c7-2edbbfada83e`.
- Ledger allocation: `seqclaim-f0fae9871fcc092d47c9a2e2`.
