# Unshifted Weibull Jacobi coefficients have an n-four diagnostic scale

## Question

What coefficient scale is suggested by the exactly solvable unshifted continuous comparator at \(a=1\), \(\beta=1/4\)?

For

\[
d\nu(x)=e^{-2x^{1/4}}dx,
\]

the moments are exact rationals:

\[
\mu_r=4\frac{(4r+3)!}{2^{4r+4}}.
\]

Exact rational Gram--Schmidt therefore constructs finite Jacobi coefficients without quadrature or floating input.

Through degree six, the normalized values satisfy

\[
\frac{a_n}{n^4}=152.42,180.14,185.12,186.85,187.65,188.09,
\]

while \(b_n/n^4\) decreases from \(2179.19\) to \(524.69\). The stabilization of the first sequence and the moment saddle both identify \(n^{1/\beta}=n^4\) as the candidate scale.

## Disposition

Promote \(n^4\) only as a finite diagnostic and asymptotic conjecture. The computation does not prove two-sided coefficient bounds, does not determine limiting constants, and does not transfer automatically to the shifted measure beginning at \(X=\log q\).

The next leaf is `shifted-unshifted-recurrence-comparison`: determine whether deleting the initial interval \([0,X]\) changes the large-degree Jacobi asymptotics by a controlled relative error.

## Claim boundary

Exact arithmetic certifies the displayed finite coefficients. It does not turn numerical stabilization into an asymptotic theorem or a cocycle summability result.
