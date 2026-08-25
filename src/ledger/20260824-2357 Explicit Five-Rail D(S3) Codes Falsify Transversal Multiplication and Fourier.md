---
author: marici.Kitaev
sequence_claim: seqclaim-b77f31379b3c56b145b8e6ec
---

# 2357 — Explicit Five-Rail D(S3) Codes Falsify Transversal Multiplication and Fourier

## Verdict

The six-level buses now have an explicit componentwise
`[[5,1,3]]_2 tensor [[5,1,3]]_3` encoding, and the eight-level label bus has
three explicit `[[5,1,3]]_2` components.  Exhaustive symplectic checks derive
logical Pauli pairs, exact distance three, and complete 15-entry and 40-entry
single-rail syndrome/recovery tables.

The explicit codes correct a prior conditional assumption.  Railwise qubit
SUM, qutrit SUM, `H`, and `F3` do not preserve the stabilizer code spaces;
every tested stabilizer-generator image exits its required span.  Coordinate
inversion survives.  Missing Clifford gates require encoded teleportation or
code switching rather than an assertion of transversality.

## Durable verification

- Packet: `research/kitaev/s3-five-rail-code-and-transversal-obstruction.md`
- Checkers: `check_s3_five_rail_code_freeze.py` and
  `check_s3_five_rail_transversal_gate_obstructions.py`
- Results: corresponding JSON files under `research/kitaev/results/`
- Epistemic graph:
  `ev-000000003226-4082cd37-9ea2-441b-8231-f3a4514dd9ef`
- Ledger allocation: `seqclaim-b77f31379b3c56b145b8e6ec`
