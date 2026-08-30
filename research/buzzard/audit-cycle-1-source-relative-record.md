# Audit cycle 1 — source-relative records

Status: **generalized narrowly**. The audit-record envelope removes duplicated
bookkeeping in two independently prepared completion contracts while retaining
their distinct source, model, result, claim, evidence, test, and bound fields.
It does not generalize their topology or operators.

## Lean increment

`marici_formal/MariciFormal/AuditRecord.lean` defines:

- `SourceRelativeAuditRecord (S M R C V ε T B Producer Verifier)` for

  \[
  (\mathcal S,\mathcal M,\mathcal R,\mathcal C,\mathcal V;
  \varepsilon,T,B);
  \]
- separate producer and verifier carriers plus exact authority tags;
- `AuditAuthority` and `Authorizes`, with proofs that verification is not
  production and production is not verification;
- `BoundedClaim`, whose certified domain is explicit;
- the hostile `falseOnlyClaim`, certified on `{false}` but not universal.

## Two-sector positive examples

The instances are transcriptions of already established contract-level facts,
not new sector proofs:

1. `magneticCompletionAudit` references
   `research/strominger/contracts/magnetic-generic-completion.v1.json`: weak-star
   Radon completion, canonical continuous distributional extension, and the
   bounded 21-dimensional completion-only ordinary kernel claim.
2. `thetaCompletionAudit` references
   `research/strominger/contracts/grothendieck-theta-completion-test.v1.json`:
   weighted Hilbert completion, canonical Friedrichs extension, and the bounded
   one-dimensional constant ground-kernel claim.

`two_sector_completion_instances` executes the distinct-sector and
producer/verifier checks.

The common record is admitted because both contracts independently contain the
same audit roles. Their completion categories, extension mechanisms, kernel
dimensions, and physical meanings remain separate strings at this layer.

## Hostile disposition

- `verification_is_not_production` blocks authority smearing.
- `bounded_claim_not_universal` blocks promotion from a certified source domain
  to a universal ontology.
- No completion operator, topology, or kernel theorem was added to this shared
  record. Those belong to a later increment only after their exact interfaces
  preserve the magnetic weak-star and theta Friedrichs distinctions.

## Missing convention-fixed inputs

For the next completion-typing increment:

1. a typed category of source/completed spaces broad enough for locally convex
   weak-star completion and Hilbert completion without identifying them;
2. the exact notion of dense embedding appropriate to each category;
3. separate extension mechanisms (continuous extension, graph closure,
   Friedrichs generator) and their uniqueness witnesses;
4. domain typing for unbounded extended operators;
5. a source-to-completed kernel comparison map;
6. a separate type for evidenced derived/Tor obstruction;
7. explicit refusal to identify support objects with operator kernels.

For the planned authority-category increment, variance, evidence-domain, and
coherence-cell conventions are still required from at least two sector
instances before generalization.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

Result on 2026-08-25: `Build completed successfully (8711 jobs)` with no Lean
diagnostics.
