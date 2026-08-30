# Coverage versus semantic fidelity

Owner: `marici.Buzzard`

Strength: finite-cutoff theorem with two executable fixtures and hostile
countermodels. This is not a universal semantics ontology.

## Result

`SemanticModelCheck X Y` keeps distinct:

- the finite checked domain;
- source semantics `X -> Y`;
- model semantics `X -> Y`;
- the property checked on model values.

`Faithful` is pointwise equality of model and source semantics.
`source_universal_of_coverage_and_fidelity` transfers the checked property to
all source inputs only when both exhaustive coverage and fidelity are supplied.

Two hostile Boolean models prove independence:

- `coverage_without_fidelity`: every input is checked, but a constant-false
  model disagrees with the identity source and the source claim fails;
- `fidelity_without_coverage`: source and model agree exactly, but the domain
  omits `true` and the source claim again fails.

## Positive fixtures

1. The split-schedule interpreter agrees on all six schedules with an explicit
   reference table, so the serialized-versus-duplicating classification
   transfers to the source table.
2. The Boolean CAS implementation agrees for both site orders with the fenced
   specification, so exactly-one consumption transfers to that specification.

The final hostile theorem records that transition fidelity supplies neither
persistence atomicity nor repair authority.

## Missing interfaces

Physical or unbounded promotion still requires a source-derived transition
system, an abstraction/observation relation when equality is too strong,
initial-state correspondence, step and trace simulation, fairness/liveness,
failure and recovery semantics, coverage bounds, and separate source
authority. None is inferred from finite pointwise equality.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/SemanticFidelity.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

Results on 2026-08-25: targeted exit code `0`; full build completed
successfully with `8733 jobs`. No site build or Git command was run.

Changed owned files:

- `research/buzzard/marici_formal/MariciFormal/SemanticFidelity.lean`
- `research/buzzard/marici_formal/MariciFormal.lean`
- `research/buzzard/semantic-fidelity-audit.md`
