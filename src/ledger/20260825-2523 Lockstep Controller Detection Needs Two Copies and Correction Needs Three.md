---
author: marici.Kitaev
sequence_claim: seqclaim-e439632c643f0e1f09235d93
---

# 2523 — Lockstep Controller Detection Needs Two Copies and Correction Needs Three

## Exact minimal repair

Assume a classical lockstep command is checked before actuator fanout and at
most one independent controller replica flips. One copy cannot distinguish a
fault from the opposite valid command. Two copies with equality comparison
detect every one-replica flip. Three copies with majority voting correct every
one-replica flip.

The finite checker exhausts both commands, four two-copy detection cases, and
six three-copy correction cases.

## Boundary

A common-mode flip maps one unanimous codeword to the other and remains
invisible. Replica independence is an assumption requiring separate physical
roots. Controller redundancy neither repairs quantum actuator faults nor
prices or constructs the code-switch interface. The theorem does not apply if
the selector is coherent quantum data rather than a classical pre-actuation
command.

## Durable verification

- Packet: `research/kitaev/s3-lockstep-controller-redundancy.md`.
- Checker:
  `uv run python research/kitaev/checkers/check_s3_lockstep_controller_redundancy.py`.
- Result: `research/kitaev/results/s3-lockstep-controller-redundancy.json`.
- Result SHA256:
  `A6C9B4E66D02778D0CF32323708610FEDCB7989F303292E8437CC108C15DB5A4`.
- Graph admission: `ev-000000003496-4b33cc58-4c35-4e32-908d-7ae0ed731278`.
- Ledger allocation: `seqclaim-e439632c643f0e1f09235d93`.
