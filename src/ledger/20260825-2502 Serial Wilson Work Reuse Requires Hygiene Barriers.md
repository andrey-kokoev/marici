---
author: marici.Kitaev
sequence_claim: seqclaim-8708f01a5eff2e6821fb604d
---

# 2502 — Serial Wilson Work Reuse Requires Hygiene Barriers

## Conditional one-fault theorem

Under the frozen support automaton, a persistent rail fault in a reusable work
block adds at most one rail error to every incident encoded data block per
gadget. If the work block is reused by overlapping gadgets without hygiene,
the same data block can receive two or more errors.

Serial reuse therefore requires a recover/verify-or-replace barrier between
every pair of overlapping work-using gadgets. All controlled nonlinear
monomials contain the control block, so a controlled target with \(k\) such
gadgets requires exactly \(k-1\) barriers:

\[
D,E,F:1,\qquad C,G:2,\qquad H:3.
\]

Without barriers, controlled \(H\) can accumulate four propagated rail errors
in its control block. Logical targets need no inter-gadget barrier because
each selected compiler uses at most one work-using gadget.

## Boundary

This is a conditional macro-support theorem. It does not construct the work
recovery, verification or replacement factory, and it does not certify a
microscopic exRec or stochastic threshold. Fresh parallel work blocks remove
reuse propagation but retain their own verification obligation.

## Verification

- Packet: `research/kitaev/s3-wilson-work-ancilla-hygiene-theorem.md`.
- Checker: `python research/kitaev/checkers/check_s3_wilson_work_ancilla_hygiene.py`.
- Result SHA256:
  `6355837C4C8829D8351BD319CC05B808052642F57DD075A3C08C3E12CCD4E63E`.
- Graph admission: `ev-000000003449-da6d8cf4-b035-4f42-98c7-5510079819b0`.
- Ledger allocation: `seqclaim-8708f01a5eff2e6821fb604d`.
