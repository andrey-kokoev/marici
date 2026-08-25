# Arbitrary finite concurrent fenced histories

`FiniteConcurrentRefinement` explains a finite concurrent history using:

- a permutation of exactly the invoked timed operations;
- agreement with sequential fenced execution;
- pairwise preservation of completed-before-invoked precedence.

`FaithfulFiniteConcurrentRefinement` additionally requires operation IDs to be
unique. This field is intentionally separate: event identity is not derivable
from sequential outcome agreement.

The positive three-operation history uses tokens `[4,4,5]`, observes outcomes
`[true,false,true]`, respects real time, and produces two protected effects.

Hostile histories establish independent premises:

- the order `[lateLeft,earlyRight]` agrees with sequential outcomes but violates
  real-time precedence because the right operation completed first;
- two operations with the same ID have a sequential explanation, yet no
  identity-faithful refinement.

Missing convention-fixed inputs:

- whether operation IDs are globally or namespace-locally unique;
- how incomplete invocations appear in finite histories;
- equivalence between concurrent executions and their trace projections;
- progress/fairness assumptions, which are deliberately absent from this safety
  refinement.

Verification commands from `research/buzzard/marici_formal`:

```text
lake env lean MariciFormal/FiniteConcurrentHistory.lean
lake build
```

Result: both commands passed under Lean `v4.33.1`; the project reported
`Build completed successfully (8727 jobs).` The site build was not run.
