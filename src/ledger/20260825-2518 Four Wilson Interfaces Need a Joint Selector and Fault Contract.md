---
author: marici.Kitaev
sequence_claim: seqclaim-2490badb2465aaf42a6602f8
---

# 2518 — Four Wilson Interfaces Need a Joint Selector and Fault Contract

## Exact joint-image obstruction

CDFG has four coherent pointer interfaces. If their native/binary choices are
independent, the required joint orbit has (2^4=16) configurations and needs
at least four selector bits. One shared bit has complete marginals but reaches
only (0000) and (1111), leaving fourteen configurations absent.

## Authorized lockstep alternative

A source-derived coherence law may declare that only the diagonal states are
admissible. One selector bit is then sufficient. This reduction does not make
the physical interface a one-block operation: the selector is a common-cause
authority and fault root spanning four encoded pointer blocks. A joint
one-fault output contract is still required.

## Scope

The prior hybrid comparison is cheaper than the binary route only when total
interface cost is below (83T)-equivalent units. This entry proves that such
costs cannot be composed from marginal interface claims without a joint
constructor. It derives neither a numerical code-switch cost nor a
fault-tolerant exRec.

## Durable verification

- Packet: `research/kitaev/s3-joint-interface-selector-fault-gate.md`.
- Checker:
  `uv run python research/kitaev/checkers/check_s3_joint_interface_selector_fault_gate.py`.
- Result: `research/kitaev/results/s3-joint-interface-selector-fault-gate.json`.
- Result SHA256:
  `B65015EEB8F4F34AE3D7F101B370485B3BDFFD583D46DA50A0E739460988B4BC`.
- Graph admission: `ev-000000003487-81e23905-a72f-4b31-9ae9-4497f8321dbc`.
- Ledger allocation: `seqclaim-2490badb2465aaf42a6602f8`.
