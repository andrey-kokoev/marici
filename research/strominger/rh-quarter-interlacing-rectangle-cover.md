# Staircase interlacing support needs linearly many Gram rectangles

## Question

What is the minimal rectangle decomposition of the finite staircase support `G_n={(i,j):i<=j}`?

## Claim boundary

Its biclique-cover number is exactly `n`. The `n` row stars `{i}×{j:j>=i}` provide a cover. For the lower bound, the diagonal edges form a fooling set: any rectangle containing `(i,i)` and `(j,j)` for `i<j` would also contain forbidden edge `(j,i)`. Exact enumeration confirms minima `1,2,3,4,5` through size five. Therefore a multi-Gram range realization needs at least `n` sectors. This theorem applies to the staircase support model; identifying a particular quarter-source Hall graph with that model requires a separate typed map.

## Disposition

A constant-size Gram explanation is impossible for staircase interlacing. The evident minimal construction uses order-defined row stars and therefore reproduces the support unless the source constructor independently supplies those nested sectors. Even with such sectors, Gram positivity remains sign-symmetric. Next test whether a sum of minimal rectangular Gram sectors can force nonnegative Hall capacities or whether independent sign flips preserve every PSD certificate.
