# Compare-and-set refinement of fenced execution

`boolToFencedState` maps concrete Boolean memory to the token-4 fenced-effect
state: `false` is unused and `true` records one completed protected effect.

The one-step refinement theorem proves that concrete `compareAndSet` and
`attemptFencedEffect ... 4` return equal abstract states and success bits for
both possible memory states. The two-operation theorem then proves that both CAS
schedules refine the corresponding fenced sequential order and have exactly one
success.

Hostile boundaries:

- the split read/write implementation produces `(true,true)`, which no fenced
  sequential order can explain;
- transition-level CAS refinement does not establish crash-atomic persistence;
- the simulation proof does not supply source authority for installing CAS as a
  shared linearization repair.

Missing convention-fixed inputs:

- the concrete memory model and CAS linearization guarantee;
- durability semantics for the CAS word and protected effect;
- memory ordering across the fence register and external resource;
- installation authority for the concrete shared primitive.

Verification commands from `research/buzzard/marici_formal`:

```text
lake env lean MariciFormal/CASFencingRefinement.lean
lake build
```

Result: both commands passed under Lean `v4.33.1`; the project reported
`Build completed successfully (8728 jobs).` The site build was not run.
