# Scale-normalized Newman discriminant is a shape-entropy Lyapunov function

## Deterministic bulk expansion

For `N` real simple zeros under backward heat, put

`A_i=sum_(j!=i)1/(r_i-r_j)`

and `r_i'=2A_i`. Let

`R^2=sum_i r_i^2`.

Pairwise cancellation gives

`sum_i r_i A_i=N(N-1)/2`,

so

`dR^2/dlambda=2N(N-1)`.

The quadratic size of every finite configuration therefore grows at a fixed
rate independent of its detailed spacing.

## Normalized discriminant theorem

The discriminant scales as length to the power `N(N-1)`. Define

`Delta_hat=Delta/(R^2)^(N(N-1)/2)`.

Then

`d/dlambda log Delta_hat`

` =4 sum_i A_i^2-N^2(N-1)^2/R^2`

` =4 sum_i [A_i-N(N-1)r_i/(2R^2)]^2 >=0`.

The second equality uses `sum_i r_iA_i=N(N-1)/2`. It is equivalently the
Cauchy--Schwarz deficit between the repulsion vector and the radial vector.

## Equality shape

Equality holds exactly when

`A_i=c r_i`

for the common coefficient `c=N(N-1)/(2R^2)`. After scaling, these are the
electrostatic equilibrium equations for Hermite zeros. Thus backward heat
monotonically increases scale-free logarithmic separation toward the Hermite
shape.

## Why this improves the infinite-rank target

The raw discriminant contains an enormous trivial divergence from spectral
scale and zero density. `Delta_hat` removes the finite-rank dilation mode
canonically before any further Weyl subtraction. Its dissipation is already
a centered square, not the difference of two divergent positive quantities.

For completed Xi, the remaining program is:

1. choose symmetric finite windows or polynomial approximants;
2. normalize translation and second moment mechanically;
3. subtract only the residual Riemann--von Mangoldt/Hermite reference energy;
4. prove convergence of the relative shape entropy;
5. pass the centered-square dissipation to the limit;
6. show collision drives the renormalized entropy to negative infinity at
   the Newman threshold.

## Static/dynamic bridge

Static Toeplitz positivity integrates squared Vandermonde evaluation over a
positive measure. Dynamic Newman evolution increases a scale-normalized
Vandermonde of the moving zeros. Both are governed by alternation after null
translation and dilation modes are removed.

## Limitations

This theorem is finite-rank and assumes real simple roots. It does not
construct an infinite Xi discriminant, justify a window limit, or determine
the Newman constant. It provides a substantially better renormalization
candidate than the raw discriminant.
