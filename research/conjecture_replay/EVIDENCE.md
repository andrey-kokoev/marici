# Conjecture replay evidence policy

`passed: true` means only that a program executed and its checks passed. It is
not a mathematical proof status.

New result artifacts must contain:

- `claim_status`: `proved`, `supported`, `falsified`, `open`, or `conditional`;
- a nonempty `evidence` array;
- an evidence class for every independently asserted claim.

Evidence classes, strongest interpretation first:

- `FORMAL`: accepted by a named proof-assistant kernel;
- `SYMBOLIC`: exact executable algebra or finite logic;
- `INTERVAL_CERTIFIED`: numerical claim with rigorous enclosures;
- `NUMERICAL`: floating-point or sampled evidence only;
- `SOURCE_DERIVED`: derivation supplied by a cited mathematical source file;
- `DECLARED`: contract or authority declaration, not proof of realization;
- `SPECULATIVE`: design, interpretation, or unproved hypothesis.

Use `evidence_policy.write_result` for new artifacts. It rejects missing or
incompatible evidence metadata. Run:

```sh
python research/conjecture_replay/audit_evidence_hardening.py
```

to inventory legacy untyped artifacts. Legacy files are not silently promoted;
they remain explicitly noncompliant until migrated.

## Incremental enforcement

`legacy_evidence_baseline.json` records SHA-256 digests of existing untyped
results. Run:

```sh
python research/conjecture_replay/check_evidence_gate.py
```

The gate permits an untyped legacy result only while it is byte-for-byte
unchanged. It fails for every new untyped result and every modified untyped
legacy result. Deleting or migrating a baseline entry is allowed; stale
baseline entries are reported for cleanup.
