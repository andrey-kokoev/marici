# Gaussian portal sign obstruction (WP379)

## Bounded completion class

Let \(F\) be WP378's polynomial flavor-source residual. Test an ordinary real
heavy mediator \(A\) with positive mass curvature and linear coupling:

\[
V(A,F)=\frac{M^2}{2}A^2+gAF,
\qquad M^2>0.
\]

The exact stationary solution is

\[
A_\star=-\frac{g}{M^2}F.
\]

Completing the square gives

\[
V=\frac{M^2}{2}
\left(A+\frac{g}{M^2}F\right)^2
-\frac{g^2}{2M^2}F^2.
\]

Healthy Gaussian exchange therefore generates a negative square. WP378 needs
a positive penalty \(+\lambda F^2\) to select \(F=0\). The simplest ordinary
tree mediator has the wrong sign and makes large residuals energetically
favored unless other source-derived operators dominate.

## Multiple mediators do not repair the sign

For independent healthy mediators \(A_i\) with positive masses and real
couplings,

\[
\Delta V_{\mathrm{eff}}
=-\frac12\sum_i\frac{g_i^2}{M_i^2}F^2.
\]

The coefficients add in the same negative-semidefinite cone. Adding more
Gaussian ports cannot produce the required positive direction.

A negative mediator mass curvature reverses the matched sign, but its
stationary point is a maximum and the mediator potential is unbounded. An
imaginary coupling would abandon a real Hermitian source action. Neither is an
admitted repair.

## Power-counting boundary

The mediator also fails to cure WP378's operator degree. Since \(F\) has
bifundamental field degree 24, the vertex \(AF\) has total field degree 25.
It is not a renormalizable four-dimensional scalar interaction. Gaussian
linearization is an auxiliary EFT rewriting, not a microscopic completion.

## Disposition

WP379 closes the ordinary healthy linear-Gaussian tree branch. It does not
exclude a fundamental positive contact, constrained auxiliary multiplet,
supersymmetric completion, nonlinear mediator sector, or radiative mechanism.
Each such successor must derive the positive sign and coefficient before
flavor readout and recheck stability and degeneracy support.

The smallest exact falsifier is the matched coefficient
\(-g^2/(2M^2)<0\). The remaining constructive gate is a non-Gaussian or
symmetry-protected microscopic source whose legal elimination produces a
positive \(F^2\) penalty without ghosts or fitted coefficients.

Run `uv run --with sympy python
research/flavor/checkers/wp379_gaussian_portal_sign_obstruction.py` to
regenerate the exact result.
