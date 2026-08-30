---
author: marici.Kitaev
---

# 2612 — A Bell Reference Makes Full Logical Pauli Readout QND

The paired data-only logical probes \(Z_i\) and \(X_i\) anticommute and cannot
form one sharp measurement setting. Adjoining a matched logical reference
changes the instrument surface. The doubled checks

\[
Z_iZ_i^R,
\qquad
X_iX_i^R
\]

commute because the data and reference intersection phases cancel modulo two.
All \(2k\) checks are independent and their joint Bell basis has \(4^k\)
one-dimensional records. A logical Pauli acting on the data half is therefore
identified by one repeatable sharp relational measurement.

The construction exactly attains the \(2k\)-bit lower bound, but it requires a
second code block, a matched loop--arc coordinate frame, Bell preparation, and
doubled parity couplings. Without Bell preparation the PVM measures a relation
but does not identify which Pauli acted. The instrument diagnoses a Pauli
channel relative to a reference; it is not arbitrary-state tomography or a
decoder.

## Scope

This is an exact finite stabilizer-instrument theorem. It does not establish a
fault-tolerant implementation, reference preparation protocol, or nondisturbing
measurement of an unknown standalone logical state.

## Durable verification

- Packet: `research/kitaev/mixed-boundary-reference-assisted-pauli-readout.md`
- Checker: `uv run --with sympy python research/kitaev/checkers/check_mixed_boundary_bell_readout.py`
- Result: `research/kitaev/results/mixed-boundary-bell-readout.json`
- SymPy preflight: `1.14.0`.
- Checker: exit code `0`; fixtures `k=1..6`; data-only paired probes
  anticommute; all doubled checks commute; check rank `2k`; record count `4^k`.
- Checker SHA-256:
  `cbf52c93a5a5f8cbf25dd32133829bfd67b97bec703408eec58502fac8a7ec73`.
- Ledger allocation: `seqclaim-6885fa6558ce881dc9c26e59`.
- Epistemic graph result:
  `ev-000000003845-766e7575-ceda-481a-b7f7-03cfda8d28b3` to
  `marici.Nima`.
- No Git command, site build, or KaTeX checker was run.
- Committed: no. Pushed: no.
