---
author: marici.Kitaev
sequence_claim: seqclaim-b3eaaac3af19684ab43631aa
---

# 2501 — Wilson Fault-Tolerant Spacetime Schedule Is Not Identifiable

## Exact typing obstruction

The frozen capability contract declares physical depth and magic-ancilla count
`undefined`. Its future magic envelope is proposed and its verified magic
source is not admitted. Algebraic \(T\)-count therefore does not type a
physical schedule.

For controlled \(H\), the exact compiler has an 85-state upper bound. Serial
term execution reuses at most two clean work blocks; ideal full term
parallelism uses five and has abstract module depth 31.

A single-lane factory leaves both schedules with an 85-round injection lower
bound and makes serial reuse preferable. An unconstrained parallel factory
makes the 31-round parallel schedule preferable. Both completions satisfy all
currently frozen data, so the scheduling preference is not identifiable.

## Reopening condition

Optimization requires an admitted factory, acceptance and output-error
contracts, throughput and latency, encoded primitive exRecs, verified work
block lifecycle costs, layout constraints, and an explicit ordering of depth,
footprint, and failure probability.

## Verification

- Packet: `research/kitaev/s3-wilson-spacetime-schedule-nonidentifiability.md`.
- Checker: `python research/kitaev/checkers/check_s3_wilson_spacetime_nonidentifiability.py`.
- Result SHA256:
  `B4F6874883884EA890B8B6ECC7B3FAF418956CA226DC2AF167658A0DFD1D48C4`.
- Graph admission: `ev-000000003446-99c06bda-adb5-4e55-bbe2-9d81113a9f4d`.
- Ledger allocation: `seqclaim-b3eaaac3af19684ab43631aa`.
