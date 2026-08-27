# Exit-portal threshold matching: WP687

## Declared matching slice

Use one Dirac exit-messenger block, constant real Higgs and exit-flavon radial
backgrounds, and one-loop modified-minimal-subtraction matching. Write
(H=h^2), (X=x^2), (A=y_q^2), and (C=y_X^2). The heavy squared-mass
eigenvalue has mixed curvature

\[
\frac{\partial^2\lambda_+}{\partial H\partial X}
=\frac{AC}{M_B^2}.
\]

For the fermion Coleman-Weinberg function,

\[
\frac{\partial^2}{\partial H\partial X}
\left[\lambda_+^2
\left(\log\frac{\lambda_+}{\mu^2}-\frac32\right)\right]
=2AC\left(\log\frac{M_B^2}{\mu^2}-1\right).
\]

## Finite threshold

With (N_c) colors and the convention
(V\supset\lambda_ph^2x^2/2), the heavy threshold is

\[
\delta\lambda_p
=-\frac{N_cy_q^2y_X^2}{4\pi^2}
\left(\log\frac{M_B^2}{\mu^2}-1\right).
\]

At the natural matching scale (mu=M_B),

\[
\delta\lambda_p
=\frac{N_cy_q^2y_X^2}{4\pi^2}>0.
\]

This is a source-derived finite contribution with fixed sign in the declared
scheme and slice.

## Authority limit

The threshold is not the total renormalized portal. An independent UV boundary
coupling can add to or cancel it. Other messenger generations,
orientation-dependent invariants, running below the threshold, and the
experimental interference scale remain absent. WP687 therefore upgrades
radiative support to a finite matching contribution, not to a numerical
selector.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp687_exit_portal_threshold_matching.py

Generated result: results/wp687_exit_portal_threshold_matching.json.
