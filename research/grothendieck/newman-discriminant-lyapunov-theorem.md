# A universal Newman Lyapunov theorem: the zero discriminant increases

## Polynomial theorem

Let `H_lambda(z)` be a polynomial solution of

`partial_lambda H_lambda=-partial_z^2 H_lambda`

whose zeros `r_1,...,r_N` are real and simple on an interval of `lambda`.
Then

`r_i'=H''(r_i)/H'(r_i)`

`    =2 sum_(j!=i) 1/(r_i-r_j)`.

Define the squared Vandermonde discriminant

`Delta(lambda)=product_(i<j)(r_i-r_j)^2`.

Then

`d/dlambda log Delta`

` =4 sum_i [sum_(j!=i)1/(r_i-r_j)]^2 >=0`.

## Proof

For a simple-root factorization, logarithmic differentiation gives

`H''(r_i)/H'(r_i)=2 sum_(j!=i)(r_i-r_j)^(-1)`.

Also

`partial_(r_i) log Delta=2 sum_(j!=i)(r_i-r_j)^(-1)`.

Pairing the gradient with the velocity field yields the displayed sum of
squares. This is an exact identity at every finite rank.

## Interpretation

Backward heat drives a repulsive gradient flow of the logarithmic
discriminant. Individual roots can move in either direction, and raw spectral
heat need not be monotone, but total logarithmic separation is monotone.

The collision locus is `Delta=0`. As a collision is approached, the
repulsion and logarithmic derivative diverge. This makes the discriminant a
natural Lyapunov detector for the boundary of the real-rooted regime.

## Relation to the earlier Vandermonde theorem

The Li Toeplitz determinants were positive Vandermonde energies of a spectral
measure. The Newman flow now has a Vandermonde Lyapunov function on the moving
zero configuration. This is a genuine structural bridge: alternation and
pairwise separation govern both static positivity and dynamic preservation
of real roots.

## Infinite-divisor target

For completed Xi, the raw infinite discriminant diverges. The next theorem
must construct a renormalized discriminant or relative Vandermonde energy
compatible with:

1. the Riemann--von Mangoldt density;
2. the complete-Bernstein determinant normalization;
3. the Newman backward-heat flow;
4. a nonnegative dissipation limit of the finite sum of squares;
5. collision detection at the Newman threshold.

A viable route is to prove the identity first for real-rooted polynomial
approximants, subtract the universal Weyl divergence, and pass to a controlled
limit. The subtraction must be source-canonical and independent of the
approximation rank.

## Limitations

The finite theorem assumes real simple roots. It does not prove that the Xi
zeros are real at `lambda=0`, determine the Newman constant, or justify an
infinite-rank limit. It does falsify naïve monotonicity targets and replaces
them with an exact coupled Lyapunov law.
