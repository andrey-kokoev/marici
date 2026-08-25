# Atomic shared linearization — cycle 8

## Question

Can the shared-linearization repair derive exactly one success from a state
transition and a history witness, rather than stipulating the output pair?

## Lean increment

Inside `TemporalAuthority.LinearConsumption`, `CellState` has two states:
`unused` and `consumed`. The atomic specification step changes `unused` to
`consumed` with success and every later step returns failure. `executeInOrder`
runs two labeled sites in either sequential order and always has exactly one
success.

`LinearizationWitness` requires a concurrent two-site history to equal one of
those legal sequential outcomes. Every witnessed history therefore has exactly
one success. Both possible winners have executable witnesses, while the
duplicated `(true,true)` hostile history has an empty witness type.

`AuthorizedAtomicLinearizer` additionally carries source authority; it yields
an authorized shared-linearization repair.

## Disposition

**Specialized from an outcome fixture to an atomic specification theorem.**
This proves the sequential state-machine specification and the consequence of
a supplied linearizability witness. It does not prove that a concrete register,
network protocol, database transaction, or hardware primitive implements an
atomic step or produces such a witness.

## Missing inputs

1. Invocation and response times plus the real-time precedence condition for
   histories with overlapping and non-overlapping operations.
2. A refinement proof from a concrete concurrent implementation to
   `atomicStep`.
3. Crash, retry, memory-model, and persistence assumptions.
4. Binding between the source-authority grant and the concrete atomic object.
5. More than two attempts and a general permutation/history semantics.

## Verification

Run from `research/buzzard/marici_formal`:

```text
lake env lean MariciFormal/TemporalAuthority.lean
lake build
```

Results:

- targeted file: passed with no diagnostics;
- project: `Build completed successfully (8716 jobs).`

Lean/mathlib version: `v4.33.1`. The Marici site build was not run.
