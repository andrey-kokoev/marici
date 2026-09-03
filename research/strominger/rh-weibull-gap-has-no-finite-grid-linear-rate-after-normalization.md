# The Weibull gap has no finite-grid linear rate after normalization

## Question

Is the fitted linear coefficient in the compact-truncation determinant ratio a genuine gap rate?

No. The truncated moments used for stable Gram--Schmidt omitted their common factor

\[
e^{-z},\qquad z=2X^{1/4}.
\]

Multiplying every moment by this factor multiplies the size-\(n\) determinant by \(e^{-zn}\). At \(X=\log12\),

\[
z=2.5110624587,
\]

while the fitted raw linear coefficient is \(2.5110639751\). Restoring normalization cancels it.

The corrected gap logarithms are nonpositive and fit

\[
\log\Pr\{x_i\geq X\ \forall i\}
=\beta_X+\gamma_X/n+\delta_X/n^2+\cdots.
\]

Later windows give \(e^{\beta_X}\approx0.69642\) and \(\gamma_X\approx0.0898\).

## Disposition

Reject a nonzero linear hard-edge gap rate on the finite grid. The apparent rate was a normalization artifact. The next leaf is `positive-limiting-gap-test`: determine whether the nonzero limiting gap probability follows from moment indeterminacy and the selected polynomial closure.

## Claim boundary

Finite fits do not prove convergence to a positive gap probability. The cancellation of the omitted linear normalization factor is exact.
