# Stability-authorized contrast floor: WP700

## The source supplies the asymmetry support

Define the dimensionless coupling ratio

\[
\alpha=\frac{\lambda}{p}.
\]

For the finite-asymmetry mass-basis coordinate of WP698,

\[
\frac{R}{p}=\frac12\left(t+\frac1t\right).
\]

Strict light-mode stability \(R<\lambda\) therefore gives

\[
\alpha-\sqrt{\alpha^2-1}
<t<
\alpha+\sqrt{\alpha^2-1}.
\]

This is a source-derived reciprocal support window. It is not fitted from the
desired detector answer.

## Uniform contrast

Evaluating the WP699 contrast at the support endpoints gives

\[
C_{\min}=\frac{2}{\alpha+1}.
\]

On the WP696 coupling corridor

\[
1<\alpha<\frac53,
\]

one obtains the universal strict bound

\[
C>\frac34.
\]

The on-shell decay condition is automatic there: \(R\geq p>3\lambda/5\).
Thus stability itself repairs the missing compact-support premise in WP699.

## Authority boundary

WP700 establishes a source-stability-derived uniform identifier margin on a
declared coupling corridor. It does not derive or select that corridor from
the complete flavor source, and it is not a detector calibration. If
\(\alpha\) is allowed to grow without bound, the contrast floor tends to zero.

The remaining gate is an independent full-source derivation or measurement of
the coupling corridor, followed by calibrated propagation of the ideal
greater-than-three-quarters contrast through widths, loops, efficiencies,
backgrounds, and uncertainty.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp700_stability_authorized_contrast_floor.py

Generated result: results/wp700_stability_authorized_contrast_floor.json.
