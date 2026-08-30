# Distributed single-consumption — cycle 7

## Frozen source

Strominger, `authority-grant-composition-interpretation.md`, section
“Distributed-consumption theorem,” and the
`two_site_partitioned_single_use_no_go` admitted/hostile fixtures.

## Lean theorem

`TemporalAuthority.LinearConsumption.DisconnectedViews State` gives two loci
identical local views and the same deterministic Boolean consume/reject rule.
`decisions` is therefore diagonal and `outcomes_are_00_or_11` gives the exact
finite outcome set. Since exactly-one consumption is inequality of the two
decision bits, `no_unique_consumption_without_coordination` proves the no-go.
A delayed-message theorem records that post-commit communication cannot change
the committed pair.

For randomized rules, independent seeds admit every seed pair, including a
diagonal pair, so they cannot guarantee exactly one success. Any correlation
that does guarantee it must exclude every diagonal pair; `SharedCoordination`
records this additional common resource.

## Three typed repairs

1. `sharedLinearization` produces `(true,false)` and preserves single use.
2. `priorPartition` restricts eligibility to one locus before distribution.
3. `boundedMultiplicityTwo` permits `(true,true)` and is proved not to satisfy
   single-use semantics.

The duplicated-nonce fixture executes the hostile `(true,true)` outcome.
Kind-preserving replay cannot turn multiplicity two into single use. Each
repair requires a separate source-authority witness, and the three repair
constructors are pairwise distinct rather than interchangeable.

Four finite countermodels show that omitting any one premise—same capability,
identical state, identical rule, or no pre-execution communication—permits an
exactly-one outcome and leaves the theorem's bounded scope.

## Disposition

**Generalized as a deterministic symmetry no-go with a diagonal-seed randomized
refinement.** It does not claim an asynchronous consensus impossibility theorem
or a classification beyond the source grammar’s three repair types.

## Missing inputs

1. A state-transition semantics connecting the abstract Boolean commit to a
   concrete executable capability.
2. An atomicity model for the shared linearizer.
3. Failure, crash, and message-delivery assumptions for a distributed-systems
   theorem stronger than the disconnected pre-commit case.
4. Source authority for the linearizer or prior partition in any application.
5. Probability measures and weaker almost-sure/high-probability guarantees;
   the present randomized theorem concerns deterministic guarantee over every
   independently allowed seed pair.

## Build

From `research/buzzard/marici_formal`, run `lake build`.

Verification results:

- `lake env lean MariciFormal/TemporalAuthority.lean` — passed with no output;
- `lake build` — `Build completed successfully (8716 jobs).`

Lean/mathlib version: `v4.33.1`. The Marici site build was not run.
