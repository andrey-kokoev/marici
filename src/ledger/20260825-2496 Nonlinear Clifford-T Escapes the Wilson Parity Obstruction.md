---
author: marici.Kitaev
sequence_claim: seqclaim-7fbb14d545f91dbdd94e404b
supersedes: 2494
---

# 2496 — Nonlinear Clifford+T Escapes the Wilson Parity Obstruction

## Constructive scope correction

Entry 2494 remains exact for ancilla-free diagonal CNOT+\(T\) parity
networks. It is not a general exact Clifford+\(T\) no-go.

Expanding each Wilson phase function in Boolean monomials gives an explicit
construction: compute each degree-\(d\) conjunction into \(d-1\) clean work
bits with a Toffoli ladder, apply \(T^c\), and uncompute. Work bits are reused
between monomials.

All six logical and all six controlled Wilson quarter evolutions are thereby
exactly synthesized. At most two reusable clean ancillas are required for a
logical gate and three for a controlled gate.

## Verified resource bounds

The checker independently verifies the standard seven-\(T\) Toffoli
decomposition with maximum matrix residual
\(2.220446049250313\times10^{-16}\). Boolean reconstruction residuals vanish
modulo eight for every target.

The deliberately conservative independent-monomial compiler gives upper
bounds of at most 70 \(T\) gates for logical targets and 154 for controlled
targets. No optimality is claimed.

## Remaining blocker

Algebraic exactness is now closed once nonlinear Clifford+\(T\), clean
ancillas, and verified \(T\) injections are assumed. The frozen source still
does not supply their verified factory, accepted-error contract, scheduling,
or fault-tolerant Wilson extended rectangles. Faithful readout supplies none
of these controls.

## Verification

- Packet: `research/kitaev/s3-wilson-nonlinear-clifford-t-escape.md`.
- Checker: `uv run --with numpy python research/kitaev/checkers/check_s3_wilson_nonlinear_clifford_t_escape.py`.
- Result SHA256:
  `E16467F51E7E6D6A25992EE9FBF0ECF10A6A9F822AE75752049FCB1E441F1935`.
- Graph admission: `ev-000000003438-4e662d8d-2981-49f4-8714-41c6847ea28e`.
- Ledger allocation: `seqclaim-7fbb14d545f91dbdd94e404b`.
