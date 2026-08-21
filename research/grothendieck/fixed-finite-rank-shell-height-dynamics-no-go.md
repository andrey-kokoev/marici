# No fixed finite shell rank carries the full prime height flow

Let `I=[-1/4,3/4]`, let `V` be a fixed finite-dimensional subspace of
`L2(I)`, and put `e_T(r)=exp(-iTr)`. If `P_V` is orthogonal projection, define
`delta_V(T)=||(1-P_V)e_T||^2`.

The reciprocal-prime mass of logarithmic shell `k` is `1/k+O(k^-2)`. At any
height with `delta_V(T)>0`, the discarded squared norm therefore contains
`delta_V(T) sum_k 1/k` and diverges. Determinant-class comparison at that
height requires `e_T in V`.

## Finite-rank theorem

Distinct exponentials on a nondegenerate interval are linearly independent:
differentiating a relation at an interior point gives a Vandermonde system.
Hence a rank-`m` space contains `e_T` for at most `m` distinct values of `T`.
It cannot contain the height orbit on any interval. No fixed finite shell
rank can therefore carry the exact prime height flow while leaving a
Hilbert--Schmidt discarded sector.

For the natural moment space `V_m=span(1,r,...,r^(m-1))`, the first omitted
Taylor vector is the monic degree-`m` orthogonal polynomial on a unit interval,
whose squared norm is `1/[(2m+1) binom(2m,m)^2]`. Thus

```
delta_m(T)
 = T^(2m) / [(m!)^2 (2m+1) binom(2m,m)^2]
   + O(T^(2m+2)).
```

Extra moments postpone the local error, but every positive residual still
multiplies the harmonic shell mass. Better approximation is not
determinant-class summability.

The correspondence must retain an infinite height-cyclic fiber, naturally
`L2(I)`, or use ranks growing with `k` fast enough that
`sum_k delta_(V_k)(T)/k` converges locally uniformly in `T`, with derivative
bounds for an analytic Fredholm determinant. The quarter-shifted constant
mode remains the covariance/vacuum channel; within-shell height data is
essential.

