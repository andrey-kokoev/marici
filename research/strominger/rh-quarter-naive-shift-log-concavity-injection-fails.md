# Quarter naive shift-log-concavity injection fails

## Question

Can shift log-concavity be proved by matching each pair of local edge states at shifts \(a,a+2\) to the same states in two copies at shift \(a+1\)?

## Claim boundary

The test rejects only the state-preserving local injection. It does not refute a global path-switching proof that changes mixed states.

## Disposition

For one linear layer with level-edge weight \(u\), the outer pair state `RL` has weight \(u+2\), while the same middle pair has weight \(u+1\). The residual is exactly \(-1\) in all 64 tested `RL` cases. `LL` improves by one and `RR` preserves weight, but pointwise domination fails. The first missing object is a global path switch that compensates mixed states while preserving endpoints and injectivity. This branch is deferred at that blocker. Work reallocates to `quarter-cross-ratio-complete-monotonicity`, an independent executable test of higher degree differences that could expose a moment or barrier structure.
