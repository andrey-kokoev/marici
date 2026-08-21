# The first source-derived Jacobi compression

Interval Lanczos applied to the certified moments gives diagonal coefficients

\[
\begin{aligned}
a_0&\approx0.00160638655829,\\
a_1&\approx0.00349620928615,\\
a_2&\approx0.00179746610029,\\
a_3&\approx0.00121668000346.
\end{aligned}
\]

Together with the previously certified positive `b_1,b_2,b_3`, these define
the first `4x4` symmetric tridiagonal Jacobi compression, with off-diagonal
entries `sqrt(b_n)`. Each `a_n` interval lies strictly inside `[0,4]`, and the
norm-ratio identities `b_n=||p_n||^2/||p_(n-1)||^2` overlap the independent
Hankel-determinant boxes.

This makes the finite Hilbert--Polya analogy concrete: arithmetic source jets
produce a positive Lanczos chain and a symmetric finite operator without
inserting zero ordinates. The lower and upper localizer certificates say more
than coefficient positivity: they are the compressed quadratic-form bounds
`0<=J<=4` on polynomial degrees supported by the available moments.

The coefficients are naturally small because the compact spectral coordinate
is `u=1/(1/4+lambda)`, whose Riemann-zero values cluster near zero. That
interpretation is conditional; the finite source construction itself is not.

## Scope

This is a finite compression. It neither establishes convergence to an
infinite self-adjoint operator nor identifies its spectrum with all Riemann
zeros. It does not resolve multiplicities or prove RH.

## Durable verification

- Checker: `checkers/quarter_point_jacobi_diagonal.py`
- Result: `results/quarter-point-jacobi-diagonal.json`
- Off-diagonal input: `results/quarter-point-jacobi-coefficients.json`
