# Source-derived irregular endpoint packet

## Frozen source formulas

Benincasa--Vazão arXiv:2402.06558v3 fixes

\[
\eta\in(-\infty,0),
\qquad
a(\eta)=(-\ell_\gamma/\eta)^\gamma,
\]

and imposes the Bunch--Davies state at \(\eta=-\infty\) using the
energy deformation \(E\mapsto E-i\epsilon\).

For \(\gamma>1\), \(\eta=-\infty\) is an \(a=0\) endpoint at finite
proper-time distance. Put

\[
\rho=(-\eta)^{-1}.
\]

## Local transformed form

A source site factor with Mellin exponent \(\beta\) has local form

\[
(-\eta)^{-\beta}e^{iE\eta}d\eta
=
\rho^{\beta-2}e^{-iE/\rho}d\rho.
\]

Thus the endpoint coefficient is

\[
\mathcal K_{\rho^{\beta-2}}
\otimes
\mathcal E^{-iE/\rho},
\]

a Kummer factor tensored with a rank-one exponential connection of
Poincaré rank one. In the convention where the displayed section is
horizontal,

\[
\nabla
=d-
\left(
\frac{\beta-2}{\rho}
+\frac{iE}{\rho^2}
\right)d\rho.
\]

## Physical sector

The source regulator gives

\[
e^{-i(E-i\epsilon)/\rho}
=e^{-iE/\rho}e^{-\epsilon/\rho}.
\]

On the physical ray \(\rho>0\), this is rapidly decreasing as
\(\rho\to0^+\). The Bunch--Davies prescription therefore selects a canonical
rapid-decay/Stokes sector at the candidate Big-Bang endpoint.

## Consequence

Ordinary logarithmic nearby cycles and finite Rees grades do not by themselves
capture this endpoint. The correctly typed comparison requires irregular
nearby cycles, enhanced/rapid-decay Betti data, or an equivalent Stokes-filtered
Riemann--Hilbert object.

This adds coefficient/comparison machinery, not a new incidence divisor. The
underlying endpoint and physical sector are both source-derived.

## First finite falsifier

For the one-site primitive, construct the rapid-decay homology of
\(\mathcal E^{-iE/\rho}\) on the source ray and its pairing with the de Rham
class above. Then test compatibility with energy occurrence labels and Cut
sewing. Failure of sewing is the first possible carrier-level obstruction;
nontrivial Stokes data alone is coefficient complexity.
