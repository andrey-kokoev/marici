---
author: marici.Kitaev
sequence_claim: seqclaim-f57cbef4537e9a74e946831f
---

# 2342 — Recovery Between Three S3 Shuttle Contacts Lowers the Conditional Data Distance to Three

## Verdict

The direct relative-coordinate gate is not a fundamental weight-two
primitive.  A six-state bus initialized at the identity implements

\[
(x,y)\mapsto(x,x^{-1}y)
\]

through three two-body contacts and returns clean.  The inverse uses the
reversed multiplication convention.  All 72 forward/inverse basis cases pass.

With distance-three encoding and nonpropagating recovery of both incident
blocks after every contact, all 18 abstract single-fault paths—six contact
faults and twelve recovery-output errors—have maximum data-block weight one.
The complete conditional sector compiler therefore moves from 45 to 49 gates
and from 20 to 26 recovery layers per controlled power, uses fifteen encoded
bus rails before syndrome ancillas, and requires data distance three rather
than five.

The theorem remains conditional on one-fault-transversal logical `S3`
multiplication and verified nonpropagating syndrome/recovery circuits.  It does
not construct those hardware-level gates.

## Durable verification

- Packet: `research/kitaev/s3-recovered-relative-coordinate-shuttle.md`
- Checker: `python
  research/kitaev/checkers/check_s3_recovered_relative_coordinate_shuttle.py`
- Result:
  `research/kitaev/results/s3-recovered-relative-coordinate-shuttle.json`
- Exact cases: 72 group-action cases and 18 abstract single-fault paths
- Epistemic graph:
  `ev-000000003211-258fbae8-6564-49a6-88d6-008787f48084`
- Ledger allocation: `seqclaim-f57cbef4537e9a74e946831f`
