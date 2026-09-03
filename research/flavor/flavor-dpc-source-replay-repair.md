# DPC source-replay repair: WP1177--WP1206

## Defect repaired

The WP1177--WP1206 gate turns previously consumed cited result JSON without
freshly replaying the cited source checkers, and the interaction-net nodes did
not carry the source provenance needed for audit. The formal DPC audit could
therefore pass while the named risky evidence was stale.

## Repair

- Added `checkers/flavor_dpc_source_replay.py`.
- Patched every WP1177--WP1206 checker to replay its cited source checkers
  before reading their result JSON.
- Added per-node `evidence_sources` records to
  `contracts/flavor-interaction-net-state.v1.json`.
- Extended `checkers/flavor_dpc_conformance_audit.py` to require source replay
  hooks, verify provenance records, and run all thirty gates in one
  digest-bounded replay session.
- Replayed the thirty direct source checkers successfully. Historical
  sympy-backed checkers use the repository-local ephemeral dependency target
  `.ai/tmp/flavor-dpc-python-deps`; that target is not repository evidence.

## Verification

`python research/flavor/checkers/flavor_dpc_conformance_audit.py`

Result:

```text
DPC CONFORMANCE PASS: 30 work packages, 170 nodes, 168 fixtures
```

All thirty repaired checkers also compile under `py_compile`.
