# Completion-witness authenticity and freshness

`WitnessEnvelope` binds request-scoped completion evidence to an issuer, an
issuance/expiry interval, and an authority epoch. `WitnessUsableFor` requires
request applicability, issuer authenticity, temporal freshness, and equality
with the live authority epoch.

The three validation dimensions are independent:

- a fresh current-epoch witness from an untrusted issuer is not authentic;
- an authentic current-epoch witness can be expired;
- an authentic fresh witness can belong to a revoked epoch.

The abstraction is intentionally symbolic. `WitnessAuthentic` compares a typed
issuer identity; it does not claim that string equality implements signature
verification.

Missing convention-fixed inputs:

- issuer-key and signature-verification types;
- clock authority and skew bounds;
- whether expiry is open or closed at its upper endpoint;
- durable authority-epoch ownership and rollover policy.

Verification commands from `research/buzzard/marici_formal`:

```text
lake env lean MariciFormal/RecoveryEvidence.lean
lake build
```

Result: both commands passed under Lean `v4.33.1`; the aggregate build later
reported `Build completed successfully (8719 jobs).` The site build was not run.
