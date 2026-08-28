# Fourier graph--anti-graph transversality

## Exact finite splitting

Let `F` be the unitary finite Fourier transform. The reciprocal bulk packet is
the graph

`L = {(x,Fx)}`.

Its metric normal is the anti-graph

`N = {(y,-Fy)}`.

Indeed, unitarity gives

`<(x,Fx),(y,-Fy)> = <x,y>-<Fx,Fy> = 0`.

Thus the required seam transversality is not an additional fitted angle. It is
the opposite sheet orientation already demanded by reciprocal boundary-flux
cancellation.

## Source-derived normal frame

Insert the normalized augmentation comb and control pulse into the anti-graph:

- `(Omega/sqrt(N), -e_0)`;
- `(e_0, -Omega/sqrt(N))`.

Their normal Gram eigenvalues are

`2(1 plus or minus 1/sqrt(N))`.

For every `N>=2`, the uniform smallest eigenvalue is at least

`2-sqrt(2)`.

The pair is orthogonal to every vector in the full `N`-dimensional bulk graph,
not merely linearly independent of two selected bulk probes. Adding it raises
the doubled packet rank from `N` to `N+2`.

## Optical implementation

Prepare the same flat-comb and control-pulse anchors as before, but distribute
each across the reciprocal sheets with a pi phase reversal on the second
sheet. Bulk probes use the Fourier-related same-sign graph embedding. Coherent
cross-Gram tomography must return zero between every bulk probe and both
normal probes.

This supplies three simultaneous tests:

1. Fourier unitarity;
2. graph--anti-graph orthogonality;
3. the source-fixed normal Gram floor `2-sqrt(2)`.

## Remaining frontier

Finite transversality is closed, but the normalized augmentation anchor is
non-Cauchy under cutoff growth and diverges in positive primitive grades.
Thus the anti-graph packet does not extend as a two-state normal bundle. Its
augmentation direction must be retyped in the continuous dual.

The apparatus can test growing cutoffs for drift, but the global theorem must
come from uniform continuity of the source maps, not extrapolation from a
finite run.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_fourier_graph_antigraph_transversality.py
```
