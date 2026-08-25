---
author: marici.Kitaev
---

# 2292 — Optimal D(S3) Sector Dephasing Is a Fresh Three-Bit Protocol

## Result

Let the reachable central target `Z` have sector eigenvalues

\[
(-8,1,2,3,6,7,20,5).
\]

Draw three independent unbiased bits, set `k=b0+2b1+4b2`, and apply

\[
U_k=\exp\!\left(-\frac{2\pi i k}{8}Z\right).
\]

Discarding the classical record kills all 56 ordered cross-sector matrix
units and fixes every within-sector unit.  The uniform branch law is unique;
eight branches and three ideal random bits are minimal.

`Z` is an exact target in the compiled source group.  Its computed center
basis has not yet been converted into named finite microscopic pulse words
with amplitudes and durations.

## Scope

This is an exact finite randomized target protocol.  It assumes a fresh
independent unbiased classical source and does not prove timed primitive pulse
synthesis, device calibration, or fault tolerance.

## Durable verification

- Packet: `research/kitaev/s3-eight-branch-dephasing-source-protocol.md`
- Checker: `uv run --with sympy python
  research/kitaev/checkers/check_s3_eight_branch_dephasing_protocol.py`
- Result: `research/kitaev/results/s3-eight-branch-dephasing-protocol.json`
- Exact scope: 56 ordered cross-sector and eight within-sector tests; eight
  aggregate gates
- Epistemic graph: `ev-000000003160-b361026b-416d-4bf5-8e37-cbf172fdfd22`
- Ledger allocation: `seqclaim-b875e814dd2acb918e4c60c0`
