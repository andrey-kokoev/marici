# First non-Gaussian fourth-cumulant covariance residual

For \(H_4=\lambda q^4\), decompose the Weyl-ordered fourth moments into their
Gaussian Wick part and connected cumulants:

\[
\langle q^4\rangle=3V_{qq}^2+\kappa_{qqqq},
\]

\[
\langle\{p,q^3\}\rangle
=6V_{qp}V_{qq}+2\kappa_{pqqq}.
\]

Subtracting Entry 1626's averaged-Hessian Gaussian tangent leaves

\[
(\dot V_{qp})_{\kappa}=-4\lambda\kappa_{qqqq},
\qquad
(\dot V_{pp})_{\kappa}=-8\lambda\kappa_{pqqq}.
\]

Therefore

\[
(\partial_t\det V)_{\kappa}
=8\lambda
\left(
V_{qp}\kappa_{qqqq}-V_{qq}\kappa_{pqqq}
\right).
\]

This is generically nonzero and has no fixed sign.  It is not a Gaussian
Hamiltonian tangent and is not, by itself, a positive Cut norm.

The source formalism permits higher initial interactions in
\(\mathcal S_{\rm int}\), but the frozen primary calculation does not specify a
quartic initial kernel or its positivity constraints.  The residual is
therefore a typed cumulant-coefficient slot whose physical admissible cone is
not yet source-derived.
