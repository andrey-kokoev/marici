# Work-ancilla hygiene for conditional Wilson exRecs

Owner: `marici.Kitaev`

## Bounded question

Does serial reuse of the clean work blocks in ledger entry 2499 preserve the
frozen one-fault output contract?

## Support theorem

In the declared adversarial support automaton, one persistent rail fault in a
work block adds at most one rail error to every incident encoded data block
per gadget. Reuse without hygiene fails when two gadgets overlap on a data
block: that block may receive two rail errors.

A barrier may recover and verify the work block or discard it and supply a
fresh verified replacement. Between barriers, safety is equivalent to
pairwise-disjoint gadget supports. The checker solves the resulting finite
segmentation problem exactly.

Every controlled work-using monomial contains the control block. Hence all
such gadgets pairwise overlap, and a controlled target with \(k\) work-using
gadgets requires exactly \(k-1\) inter-gadget hygiene barriers under serial
reuse. A final barrier is not required merely to meet the stated output
contract, which permits one residual rail error per block.

## Boundary

This is conditional support accounting. It does not construct the recovery,
verification, replacement factory, microscopic exRec, or stochastic error
rate. Parallel fresh work blocks remove reuse propagation but retain their
individual preparation and verification obligations.

## Falsifiers

- A controlled work gadget whose support excludes the control block.
- Two serially adjacent work gadgets with disjoint support despite a claimed
  mandatory barrier.
- A no-barrier history that cannot place two errors in any repeated block.
- A stronger admitted primitive contract that clears work faults internally.

## Artifacts

- Checker: `checkers/check_s3_wilson_work_ancilla_hygiene.py`
- Result: `results/s3-wilson-work-ancilla-hygiene.json`
- Result SHA256:
  `6355837C4C8829D8351BD319CC05B808052642F57DD075A3C08C3E12CCD4E63E`
- Graph admission: `ev-000000003449-da6d8cf4-b035-4f42-98c7-5510079819b0`
- Ledger: entry 2502, `seqclaim-8708f01a5eff2e6821fb604d`
