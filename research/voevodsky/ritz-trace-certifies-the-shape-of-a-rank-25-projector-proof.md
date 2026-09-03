# Ritz trace determines the shape of a rank-25 projector proof

## Question

Can the concentration threshold projection be certified without enclosing the unresolved numerical eigenvalues near zero?

## Claim boundary

Yes in principle. A 25-dimensional Ritz lower bound proves at least 25 eigenvalues above the threshold, while the exact trace minus the captured Ritz trace proves every remaining eigenvalue below it. The numerical margins are large and the subspace residual is eleven orders below the matrix-entry radius. Analytic and interval enclosure remain to be supplied.

## Lower rank bound

The least Ritz value on the approximate 25-dimensional subspace is

\[
0.03156750089337.
\]

Against threshold \(1/130\), the lower-rank margin is

\[
0.02387519320106.
\]

By the min--max principle, a certified positive lower enclosure of this compression would prove that at least 25 concentration eigenvalues exceed \(1/130\).

## Upper rank bound

The exact concentration trace is

\[
\operatorname{Tr}(T)=\frac{70}{\pi}.
\]

The computed 25-mode Ritz trace is

\[
22.27549801983659.
\]

Their difference is

\[
0.006194013028761
<
\frac1{130},
\]

with margin

\[
0.001498294663547.
\]

For a positive trace-class operator, the sum of all eigenvalues outside any 25-dimensional Ritz subspace is bounded by this trace residual. Therefore the 26th eigenvalue is below \(1/130\) once the Ritz trace is enclosed with error below the displayed margin.

## Projector residual

The independent-grid residual has operator norm

\[
4.304\times10^{-13}.
\]

The separation between the Ritz cluster and the trace upper bound on the complement is

\[
0.02537348786461.
\]

Their quotient is

\[
1.697\times10^{-11}.
\]

This is the diagnostic Davis--Kahan projector error and is far below the Arb entry radius \(10^{-5}\).

## Residual

The Gauss rules and floating eigenvectors are not interval-enclosed. The quotient is therefore diagnostic, not a certified subspace angle. A rigorous version must enclose the 25-vector Gram matrix, Ritz matrix, residual operator norm, and captured trace. It need not resolve any eigenvalue after the 25th individually.

## Disposition

The concentration-projector problem has a stable low-dimensional certification route with two scalar margins. Numerical conditioning is not the obstruction. The remaining work is interval residual evaluation and propagation of the resulting projector enclosure into the rank-25 Schur entries.

## Verification

- `research/voevodsky/checkers/scout_concentration_projector_certificate.py`
- `research/voevodsky/results/concentration_projector_certificate_scout.json`
