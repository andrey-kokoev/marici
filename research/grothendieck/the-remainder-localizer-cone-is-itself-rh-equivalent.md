# The remainder localizer cone is itself RH-equivalent

## Question

Did endpoint-atom extraction reduce the problem to a positivity statement weaker than RH, or merely isolate a new exact equivalent?

## General zero-side expansion

For a zero `rho`, set

\[
\lambda_\rho=-(\rho-1/2)^2,
\qquad
y_\rho=e^{-h\lambda_\rho}.
\]

The remainder localizer moments have the formal zero-side expansion

\[
a_n
=c_h(t)y_E^n
+
\sum_\rho
 e^{-t\lambda_\rho}
(1-e^{-h\lambda_\rho})y_\rho^n,
\]

with `y_E=e^(h/4)`. Normal convergence for positive heat scale makes the associated generating function meromorphic in its initial disk, with singularities at reciprocals of the distinct `y_rho` unless exact multiplicity grouping cancels a coefficient.

## RH implies the cone

On RH, every `lambda_rho=gamma^2` is positive real. Hence every `y_rho` lies in `(0,1)`, and

\[
e^{-t\gamma^2}(1-e^{-h\gamma^2})>0.
\]

The displayed sequence is then the moment sequence of a positive atomic measure on `(0,1)` plus the endpoint atom `c_h(t) delta_(y_E)`. Every remainder Hankel matrix is PSD.

## The cone forces real spectral bases

Conversely, suppose the remainder Hankel cone holds at every rank. The endpoint asymptotic gives a unique compact positive representing measure. Its moment generating function is the Stieltjes transform of a measure on the real axis, so its nonremovable poles occur only at real support coordinates.

Comparison with the normally convergent zero-side expansion forces every surviving base `y_rho` to be real. Since

\[
\operatorname{Im}\lambda_\rho
=-2\gamma(\beta-1/2)
\]

and nontrivial zeros have `gamma` nonzero, reality of `y_rho` for all sufficiently small positive rational meshes forces

\[
\beta=1/2.
\]

Using every small rational `h` removes the possible alias `h Im(lambda_rho) in pi Z` that a single mesh could miss.

## Exact status

Subject to the exact general-zero Gaussian expansion, normal convergence, and uniqueness comparison, the family of gamma-plus-prime remainder Hankel cones is equivalent to RH. Endpoint extraction does not weaken the theorem. It removes the polar subtraction from the positivity proof and identifies where the full strength remains.

## Consequence for proof search

A universal source Gram factor for the remainder is already an RH proof. Numerical PSD, generic moment theory, or a formal J-fraction cannot establish it without arithmetic input that excludes complex spectral bases.

The useful search question is therefore narrower: which endpoint--gamma--prime identity forces the remainder Jacobi coefficients or Stieltjes poles to be real and positive? Additional semigroup coherence cannot answer that question.

## Boundary

Pole comparison must account for repeated zeros, quartet grouping, convergence domains, and possible coefficient cancellation. The statement is a theorem schema until those analytic details and the general-zero explicit formula are attached.

## Disposition

Treat remainder positivity as the exact arithmetic gate, not an easier auxiliary lemma. Continue only with source identities capable of controlling the reality of the remainder J-fraction or excluding nonreal `y_rho`.