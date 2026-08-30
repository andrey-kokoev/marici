---
author: marici.Kitaev
---

# 2300 — D(S3) Center Readout Requires Controlled Powers and a Distinct Three-Qubit Record

## Result

Exact `Z8` phase estimation maps the central residues to sector records as

\[
0:A,\ 1:B,\ 2:C,\ 3:D,\ 6:E,\ 7:F,\ 4:G,\ 5:H.
\]

Three qubits are necessary and sufficient for the eight orthogonal records.
Following this measurement by within-block depolarization gives the
record-producing 36-Kraus center instrument

\[
\rho\mapsto\frac{\operatorname{Tr}(P_a\rho)}{d_a}P_a\otimes|a\rangle\langle a|.
\]

Discarding the record recovers the nonselective center expectation.

The six-level holonomy ancilla, private random-control records, and retained
sector record are distinct resources.  Most importantly, uncontrolled
reachability of `U1,U2,U4` does not supply their controlled versions; a
conditional coupling interface remains source-unproved.

## Scope

This is an exact dilation target and resource inventory, not a proof that a
device supplies controlled central powers, measurement, or reset.

## Durable verification

- Packet: `research/kitaev/s3-ancilla-measurement-reset-and-instrument.md`
- Checker: `uv run --with sympy python
  research/kitaev/checkers/check_s3_ancilla_measurement_instrument.py`
- Result: `research/kitaev/results/s3-ancilla-measurement-instrument.json`
- Eight aggregate gates pass
- Epistemic graph: `ev-000000003167-dcebc7dd-c150-4d3d-bda9-cea53a936110`
- Ledger allocation: `seqclaim-23b2b0f2a2fa311ec6374376`
