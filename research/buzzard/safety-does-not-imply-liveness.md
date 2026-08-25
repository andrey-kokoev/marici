# Finite safety does not imply liveness

Owner: `marici.Buzzard`

Strength: execution-trace countermodel for the distributed single-consumption
fixture. This packet does not assume or define a universal scheduler ontology.

## Lean result

`SafetyLiveness.lean` defines Boolean infinite traces where `false` means
waiting and `true` means completed. The transition relation permits waiting to
continue or completion to occur, but forbids returning from completed to
waiting.

Lean proves:

- every valid trace preserves completion once reached;
- the constant waiting trace satisfies the transition relation;
- every finite safety prefix of that trace passes;
- nevertheless the trace never reaches completion;
- a separate `CompletionScheduled` premise suffices for eventual completion;
- transition validity does not imply that premise;
- the existing finite coverage and semantic-fidelity proofs coexist with the
  nonterminating trace and therefore do not supply liveness.

The positive fixture `completingTrace` moves to completed at the first step,
remains valid, and has an explicit eventual-completion witness.

## Missing interfaces

A source-level liveness theorem requires a scheduler/environment contract,
the exact enabledness relation, a fairness or bounded-delay premise, failure
and recovery behavior, temporal bounds, and authority for the actor that
promises progress. None follows from finite safety, semantic fidelity, or
transition preservation.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/SafetyLiveness.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

Results on 2026-08-25: targeted exit code `0`; full project build completed
successfully with `8734 jobs`. No site build or Git command was run.

Changed owned files:

- `research/buzzard/marici_formal/MariciFormal/SafetyLiveness.lean`
- `research/buzzard/marici_formal/MariciFormal.lean`
- `research/buzzard/safety-does-not-imply-liveness.md`
