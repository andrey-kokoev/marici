# Finite atomic histories — cycle 9

## Increment

`TemporalAuthority.LinearConsumption.runAtomicOrder` extends the two-site
atomic specification to an arbitrary finite labeled operation list. The first
operation succeeds and consumes the cell; every later operation fails.

`FiniteLinearizationWitness` supplies an ordering that is a permutation of the
invoked operations and whose sequential atomic execution equals the observed
event list. Every nonempty witnessed history has success count exactly one.
The explicit two-operation history in which both operations succeed has an
empty witness type.

## Disposition

**Generalized from two attempts to finite labeled histories.** The ordering is
an explicit witness, not an inferred consensus protocol. The formalization
does not yet constrain the order by real-time precedence.

## Missing inputs

1. Invocation and response intervals and the happens-before relation.
2. The linearizability condition that non-overlapping real-time precedence is
   preserved by the witness order.
3. Duplicate operation identifiers, retry identity, and exactly-once request
   semantics.
4. Infinite histories, fairness, crashes, and liveness.
5. A refinement proof from a concrete concurrent implementation.

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
