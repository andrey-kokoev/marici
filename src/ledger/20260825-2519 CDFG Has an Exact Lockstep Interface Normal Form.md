---
author: marici.Kitaev
sequence_claim: seqclaim-f8df6cb678a0b7a9ccff44de
---

# 2519 — CDFG Has an Exact Lockstep Interface Normal Form

## Exact reordering theorem

The CDFG interaction layer has 21 Boolean-predicate-controlled (Z_4^c)
terms. All are diagonal in the common three-bit data and four-pointer residue
basis. Exact enumeration of all (2^3 4^4=2048) basis states gives zero phase
residual modulo four between compiler, reverse, predicate-grouped, and
odd/even-grouped orders.

Therefore all CDFG interactions admit one synchronized digit-exposed window.
The ideal circuit algebra itself authorizes the two-state lockstep selector
orbit; mixed native/binary configurations are not required by interaction
ordering.

## Correction and surviving boundary

Ledger 2518's 16-state and four-bit lower bound applies when port switching
must be independent. The exact CDFG layer does not impose that requirement.
What remains unresolved is physical: the synchronized interface is a joint
channel on four encoded pointer blocks, with a common-cause fault root and no
derived cost or exRec. Native (F_4) layers are not commuted through the
interaction window.

## Scope

This is an ideal-unitary scheduling normal form. It neither constructs the
four-block code switch nor makes the conditional (83T)-equivalent interface
allowance executable.

## Durable verification

- Packet: `research/kitaev/s3-lockstep-interface-normal-form.md`.
- Checker:
  `uv run python research/kitaev/checkers/check_s3_lockstep_interface_normal_form.py`.
- Result: `research/kitaev/results/s3-lockstep-interface-normal-form.json`.
- Result SHA256:
  `6822F9D9283E24292E442C8F2836829971EDDAED85A2FFD365C0A368DF19D265`.
- Graph admission: `ev-000000003489-14d9df04-462e-431b-8cd1-65479299c759`.
- Ledger allocation: `seqclaim-f8df6cb678a0b7a9ccff44de`.
