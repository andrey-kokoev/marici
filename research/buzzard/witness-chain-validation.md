# Completion-witness delegation chains

`ChainGrant` carries issuer, subject, request scope, authority kind, epoch, and
validity interval. `LinkLocallyValid` requires symbolic signature validity,
endpoint typing, request and kind preservation, nondecreasing epoch, and a
pairwise live overlap.

End-to-end validity adds two independent interfaces:

- the trusted root charter must authorize the request;
- all grants in the chain must share one common live time.

Finite hostile chains prove that:

- two locally valid links do not imply root charter scope;
- pairwise interval overlap does not imply a common three-link live time;
- even with a trusted in-scope root, local validity does not imply end-to-end
  temporal coherence;
- transporting the same links does not repair the missing global condition.

The `signatureValid` field is symbolic evidence. No cryptographic signature
scheme, adversary model, or verification theorem is assumed.

Missing convention-fixed inputs:

- concrete issuer keys and signature verification;
- charter versioning and revocation;
- whether epoch order is global, per issuer, or per request;
- clock authority for comparing validity intervals across issuers.

Verification commands from `research/buzzard/marici_formal`:

```text
lake env lean MariciFormal/WitnessChain.lean
lake build
```

Result: both commands passed under Lean `v4.33.1`; the project reported
`Build completed successfully (8726 jobs).` The site build was not run.
