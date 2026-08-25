# Real-time linearizability — cycle 10

## Increment

`OperationInterval` records invocation and response times with a proof of
well-formedness. One operation precedes another when it responds no later than
the other is invoked.

`RealTimeLinearizationWitness` extends the existing two-site atomic witness and
requires its sequential order to preserve both possible real-time precedence
relations. Every such history has exactly one success by the atomic theorem.

An overlapping history with A as winner has an executable witness because
neither operation precedes the other. The hostile fixture has B complete before
A is invoked while its outcome says A won; its real-time witness type is proved
empty.

## Disposition

**Generalized the two-site safety theorem to real-time linearizability.** This
is still a history specification. It does not construct a concurrent algorithm
or prove that a concrete compare-and-set implementation refines it.

## Missing inputs

1. General finite-history happens-before preservation rather than the two-site
   specialization.
2. A clock model if timestamps come from different physical loci.
3. Call identity, retries, crashes, and incomplete/pending operations.
4. A concrete implementation refinement proof.
5. Liveness and fairness; the result is safety-only.

## Verification

From `research/buzzard/marici_formal`:

```text
lake env lean MariciFormal/TemporalAuthority.lean
lake build
```

Results:

- targeted file: passed with no diagnostics;
- project: `Build completed successfully (8716 jobs).`

Lean/mathlib version: `v4.33.1`. The Marici site build was not run.
