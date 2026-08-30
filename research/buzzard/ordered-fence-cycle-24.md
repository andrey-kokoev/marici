# Cycle 24 — ordered fencing needs one authoritative register

## Increment

`attemptOrderedFence` atomically accepts a token strictly greater than the
resource's `lastAccepted` value and advances that value to the token. A replay
of the same token against the same register is rejected.

## Positive examples from two sectors

- Temporal authority: strictly newer tokens preserve the no-authority-by-replay
  boundary.
- Distributed execution: a single atomic resource register accepts token `4`
  once and rejects its duplicate.

## Hostile countermodel

`duplicated_local_fence_registers_accept_twice` gives two disconnected resource
replicas identical state `lastAccepted = 3`. Each locally accepts token `4`, so
the global outcome is `(true, true)`. Local fencing therefore does not repair
distributed single consumption unless the compared register itself has shared
linearization or prior resource partitioning.

## Abstraction disposition

Specialized. Ordered fencing refines the target-validation interface but does
not replace the earlier distributed-consumption theorem.

## Missing convention-fixed inputs

- The authority locus owning the resource register.
- Atomic persistence semantics for register advancement plus side effect.
- Token allocation and exhaustion/wraparound policy.
- Whether replicated resources permit bounded multiplicity instead of single
  consumption.

## Verification

Run from `research/buzzard/marici_formal`:

```text
lake env lean MariciFormal/TemporalAuthority.lean
lake build
```

Result: both commands passed under Lean `v4.33.1`; the project reported
`Build completed successfully (8716 jobs).` The Marici site build was not run.
