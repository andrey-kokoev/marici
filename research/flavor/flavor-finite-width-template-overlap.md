# Finite-width template overlap: WP654

## Exact line-shape response

Take two equal-width normalized Lorentzian templates with half-width
\(\gamma>0\) and mass separation \(\Delta\). Exact residue evaluation gives

\[
\int_{-\infty}^{\infty}L_0(s)L_\Delta(s)\,ds
=\frac{2\gamma}{\pi(\Delta^2+4\gamma^2)}.
\]

After normalization by the self-overlap, their matched-filter overlap is

\[
\rho=\frac{4\gamma^2}{\Delta^2+4\gamma^2}.
\]

The two-template Gram matrix has determinant \(1-\rho^2\) and smallest
eigenvalue

\[
\lambda_{\min}=1-\rho
=\frac{\Delta^2}{\Delta^2+4\gamma^2}.
\]

Finite width preserves rank two for every nonzero mass separation. At exact
degeneracy, the templates coincide and rank collapses to one.

## Conditioning gate

Demanding \(\lambda_{\min}\geq\epsilon\) is equivalent to

\[
\Delta^2\geq\frac{4\epsilon}{1-\epsilon}\gamma^2.
\]

Nonzero algebraic rank is therefore insufficient near degeneracy; an
experiment must certify a resolution-relative separation margin.

## Disposition

This repairs the finite-width part of WP653's detector model under equal-width
Lorentzian assumptions. Detector-resolution convolution, unequal widths,
backgrounds, efficiencies, and calibrated uncertainties remain open. It
improves source identification but does not select coefficient values.

The smallest exact falsifier is \(\Delta=0\).

Reproduce with: uv run --with sympy python research/flavor/checkers/wp654_finite_width_template_overlap.py

Generated result: results/wp654_finite_width_template_overlap.json.
