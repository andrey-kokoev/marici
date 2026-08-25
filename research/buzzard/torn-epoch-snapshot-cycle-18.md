# Torn multi-root epoch snapshot — cycle 18

## Increment

The required two-root epoch vector is `(4,9)`. The early live state is `(4,10)`
and the late live state is `(5,9)`. Neither live state matches the lease.

A non-atomic verifier can nevertheless read root 0 from the early state and
root 1 from the late state, assembling the torn vector `(4,9)`. Lean proves
that every sampled coordinate matches while neither actual global state ever
matched all required roots.

## Hostile conclusion

Pointwise equality checks are insufficient unless they are tied to one atomic
snapshot or an equivalent versioned-consistency witness. This is the exact
implementation gap left by the abstract `MultiRootExecutable` conjunction.

## Disposition

**Failed naive pointwise implementation; retained atomic-snapshot requirement.**
No distributed snapshot algorithm is inferred from the countermodel.

## Missing inputs

1. A versioned snapshot, transaction, or seqlock protocol.
2. A refinement proof that returned epoch vectors correspond to one state.
3. Memory ordering and concurrent update semantics.
4. Crash behavior during snapshot acquisition.

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
