---
author: marici.Kitaev
sequence_claim: seqclaim-a0461aabb4b145121e20cbb0
---

# 2335 — Centralizer Fourier Gates Replace the Five-Body D(S3) Sector Pulse

## Verdict

The eight sectors are derived from centralizer charge labels for
`S3`, `Z2`, and `Z3` before target residues are assigned.  A six-state
holonomy bus and eight-state label bus compile each controlled power in 45
one-/two-body gates, with four-edge support and exact cleanup.  The three
powers cost 135 gates total and do not assume a sector oracle.

An unverified shared-bus fault can still reach data weight four, so arbitrary
recovery needs distance nine.  A verified cat only improves the control
component.  Five-rail distance-three encoding of each bus plus twenty
interleaved correction cycles conditionally lowers bus spread to one, but the
relative-coordinate primitive leaves total weight two and distance five.
Fault-transversal logical bus gates and syndrome circuits remain uncompiled.

## Durable verification

- Final packet: `research/kitaev/s3-lower-arity-sector-bus-verdict.md`
- Checker: `python
  research/kitaev/checkers/check_s3_lower_arity_sector_bus_audit.py`
- Result: `research/kitaev/results/s3-lower-arity-sector-bus-audit.json`
- Composition: six digest-bound packets and 40 component gates
- Epistemic graph: `ev-000000003197-ac45e52e-dd41-4ad5-b488-b9eac34c48e8`
- Ledger allocation: `seqclaim-a0461aabb4b145121e20cbb0`
