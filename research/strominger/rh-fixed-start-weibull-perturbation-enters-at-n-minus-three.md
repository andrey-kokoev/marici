# The fixed-start Weibull perturbation enters at n-minus-three

## Question

What degree-expansion class is sourced by fixed compact translation of the Weibull weight?

At fixed \(X\), write the translated potential as

\[
V_X(y)=2a(X+y)^\beta.
\]

The degree-\(n\) moment saddle has scale

\[
y_n\asymp n^{1/\beta}.
\]

Expanding at large \(y\),

\[
(X+y)^\beta
=y^\beta+eta Xy^{\beta-1}
+\frac{eta(eta-1)}2X^2y^{\beta-2}+\cdots.
\]

At the saddle, the \(k\)-th compact-translation term has degree scale

\[
y_n^{\beta-k}
\asymp n^{(\beta-k)/\beta}
=n^{1-k/\beta}.
\]

For \(\beta=1/4\), the first exponents are

\[
-3,-7,-11,\ldots.
\]

Thus compact translation first enters at \(n^{-3}\), matching the observed shifted/unshifted relative Jacobi correction. It does not source an \(n^{-3/4}\) term.

The underlying unshifted Jacobi asymptotic may still contain ordinary inverse-degree corrections. Therefore the scaled hard-edge defect can approach its limit with an \(n^{-1}\) correction before the truncation-specific \(n^{-3}\) term appears.

## Disposition

Select integer inverse-degree asymptotics as the fixed-start expansion class, with compact-translation effects beginning at \(n^{-3}\) and then every four powers in this saddle expansion.

The next leaf is `hard-edge-inverse-degree-correction`: test and derive a leading \(1/n\) correction to \(n^2\varepsilon_n\to2\).

## Claim boundary

Saddle power counting identifies admissible exponents; it does not prove full Jacobi expansions or their coefficients.
