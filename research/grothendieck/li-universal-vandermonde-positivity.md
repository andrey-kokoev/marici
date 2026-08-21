# Universal coupled positivity: Toeplitz determinants are Vandermonde energies

## Theorem

Let `mu` be a finite positive measure on the unit circle and let

`hat_mu(k)=integral z^(-k) dmu(z)`.

For `N>=1`, form the Toeplitz moment matrix

`T_N=(hat_mu(i-j))_(0<=i,j<N)`.

Then

`det(T_N) = 1/N! integral_(T^N) product_(i<j)|z_i-z_j|^2
            product_i dmu(z_i)`.

In particular `T_N` is positive semidefinite. Its determinant is strictly
positive exactly when the support of `mu` contains at least `N` distinct
points.

## Proof

The matrix is the Gram matrix of `1,z,...,z^(N-1)` in `L^2(mu)`. Applying
the Gram--Andreief identity expresses its determinant as `1/N!` times the
integral of the squared determinant of the evaluation matrix
`(z_i^(j-1))`. That determinant is the Vandermonde product
`product_(i<j)(z_j-z_i)`. This proves the formula and positivity. Linear
independence of the first `N` monomials in `L^2(mu)` is equivalent to the
support having at least `N` points, proving the strictness statement.

## Li specialization

For the conditional Li increment measure, the Fourier moments are the second
differences `c_k`. Consequently every finite coupled Li determinant is a
Vandermonde repulsion energy of the inverse-square-weighted phases
`u_rho=1-1/rho`.

The degree-two variance theorem is the first nontrivial instance: the
three-by-three determinant measures dispersion among triples of phase
support, while its reflection channels resolve lower-order sine and cosine
spread.

## Explanatory gain

This is the first universal coupled positivity theorem for the proposed Li
moment system. It explains every rank with one invariant mechanism rather
than a separate Cholesky factorization:

> positivity is squared alternation of evaluation, and strict positivity is
> spectral diversity.

It also explains why determinants become small: the inverse-square weighting
concentrates mass at phases approaching `1`, making Vandermonde separations
small.

## Noncircularity boundary

The theorem begins with a positive measure. Applying it to the zero-phase
measure is conditional on RH and does not prove RH. The remaining arithmetic
problem is to construct a positive moment functional with the Li increment
moments directly from the explicit formula. Once that is done, the theorem
supplies every finite determinant and the GNS cocycle automatically.

## Falsifiers for a source construction

- A negative source evaluation on `|p|^2`.
- Failure of the source moments to be Toeplitz-consistent across ranks.
- A null determinant despite a claimed source measure with at least `N`
  support points.
- A rank-dependent measure or completion rule.
- Positivity that appears only after replacing source data by zero phases.
