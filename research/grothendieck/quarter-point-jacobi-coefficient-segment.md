# A certified finite Jacobi segment from source moments

Let `Delta_n=det(A_(i+j))_(0<=i,j<=n)` and `Delta_(-1)=1`. For a positive
moment functional, the monic Jacobi recurrence has off-diagonal squares

\[
 b_n=\frac{\Delta_n\Delta_{n-2}}{\Delta_{n-1}^2}.
\]

The four certified ordinary corners determine `b_1,...,b_4` without zero
locations. Outward propagation gives strictly positive boxes for all four.
This is the first finite operator segment extracted from the quarter-point
source calculus rather than postulated from a desired spectrum.

Numerically, the certified boxes are centered at

\[
 b_1\approx3.64049861967\,10^{-6},\qquad
 b_2\approx1.31934476230\,10^{-6},\qquad
 b_3\approx4.85841580836\,10^{-7},\qquad
 b_4\approx3.07178707075\,10^{-7}.
\]

Positivity of each `b_n` is exactly the nonbreakdown condition for its Lanczos
step. The rapidly shrinking raw determinants are largely a normalization
effect; these ratios are better-conditioned operator observables.

The finite recurrence segment is unconditional moment algebra. Its meaning as
an initial compression of a self-adjoint Hilbert--Polya operator remains
conditional on positivity and consistency at every order. Scalar moments also
retain the known multiplicity blindness.

## Scope

This does not construct the Jacobi diagonal, an infinite self-adjoint closure,
or an operator proved to have the Riemann-zero spectrum. It does not prove RH.

## Durable verification

- Checker: `checkers/quarter_point_jacobi_coefficients.py`
- Result: `results/quarter-point-jacobi-coefficients.json`
