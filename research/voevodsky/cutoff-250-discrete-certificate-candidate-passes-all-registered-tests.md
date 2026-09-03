# The cutoff-250 discrete certificate candidate passes all registered tests

## Question

Does the refined cutoff-\(250\), rank-\(25\) Schur matrix admit a direct factorization above the reserved margin \(0.001\)?

## Claim boundary

Yes at floating precision. Both cutoff-\(250\) resolutions and all three pseudoinverse tolerances admit Cholesky factorizations of \(S-0.001I\). The direct full discretized operator is positive semidefinite to roundoff. This certifies the computed matrices only heuristically; continuum and interval certification remain absent.

## Cholesky test

At refined cutoff \(250\), the least Schur eigenvalues for relative pseudoinverse tolerances \(10^{-8},10^{-10},10^{-12}\) are

\[
0.00898010,
\qquad
0.00657320,
\qquad
0.00446900.
\]

Every matrix admits a Cholesky factorization after subtracting \(0.001I\). The corresponding minimum Cholesky diagonal entries are

\[
0.24084,
\qquad
0.20740,
\qquad
0.18679.
\]

The least-eigenpair residuals are below \(10^{-15}\).

The coarser cutoff-\(250\) discretization gives the same result, including the tight-tolerance least eigenvalue \(0.00446496\) and minimum Cholesky diagonal \(0.18670\).

## Cutoff enlargement

At cutoff \(350\), all tolerance choices also factor above \(0.001\). Their least Schur eigenvalues are

\[
0.01379213,
\qquad
0.00967181,
\qquad
0.00785498,
\]

with minimum Cholesky diagonals at least \(0.26376\).

The direct truncated operator has no eigenvalue below \(-10^{-10}\) at cutoffs \(250\) and \(350\).

## Counterexample retained

At cutoff \(150\), the tightest pseudoinverse tolerance gives

\[
\lambda_{\min}(S_{150})
\approx-0.00140819
\]

and Cholesky fails. This prevents treating low-cutoff agreement as sufficient.

## Residual

The successful Cholesky factorizations are performed on double-precision matrices whose entries come from non-enclosed Gauss--Legendre quadrature and numerically computed concentration eigenvectors. The computation supplies no interval matrix and no analytic remainder estimate. Cholesky success therefore does not promote the continuum form to positive.

## Disposition

Every registered finite-precision falsifier at cutoff \(250\) passes with room above the target \(0.001\). The remaining gate is no longer numerical sign discovery; it is rigorous enclosure of the matrix construction within the previously allocated \(0.003469\) total error budget.
