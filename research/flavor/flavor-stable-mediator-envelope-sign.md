# Stable-mediator envelope sign theorem (WP380)

## Bounded question

Can nonlinear self-interactions of a healthy mediator repair WP379's wrong
sign and generate a positive local penalty for the WP378 shell residual
\(F\), without inserting a direct \(F^2\) contact?

## Local envelope theorem

Let \(A\) denote real mediator coordinates near a stationary configuration.
Write the source Hessian in block form

\[
\begin{pmatrix}H&G\\G^T&K\end{pmatrix}.
\]

A healthy mediator vacuum has positive definite \(H\). Stationary elimination
gives the local envelope curvature

\[
K_{\mathrm{eff}}=K-G^TH^{-1}G.
\]

With no direct contact, \(K=0\), this is negative semidefinite and is strictly
negative in every residual direction coupled to the mediator sector.
Nonlinear interactions can change higher orders and vacuum support, but not
this local Hessian identity.

## Nonlinear hostile example

For

\[
V(A,F)=\frac{m^2}{2}A^2+\frac{\lambda}{4}A^4+gAF,
\qquad m^2>0,\quad \lambda>0,
\]

implicit differentiation at the symmetric vacuum yields

\[
\frac{dA_\star}{dF}=-\frac{g}{m^2},
\qquad
\left.\frac{d^2V_{\mathrm{eff}}}{dF^2}\right|_{F=0}=-\frac{g^2}{m^2}.
\]

The quartic coupling drops out. Ordinary nonlinear stabilization does not
reverse the Gaussian sign.

## Exact missing constructor

A direct contact overcomes exchange only when

\[
K>G^TH^{-1}G.
\]

Then \(K\) itself is the selector-bearing source term; mediator elimination
only renormalizes it downward. Its coefficient needs independent source
authority. The theorem is local and does not exclude constrained
non-minimizing auxiliaries, radiative effective actions, or a separately
derived direct contact.

## Disposition

WP380 extends WP379 to every smooth classically minimized healthy mediator
sector at quadratic order. The contextual partition is the kernel of \(G\):
uncoupled directions receive zero curvature and coupled directions receive
negative curvature. The operation is neither a positive selector nor a
presentation rigidifier.

The smallest exact falsifier is the quartic model curvature \(-g^2/m^2\).
The remaining gate is a source-derived positive direct contact above the
Schur threshold, or a typed mechanism outside classical stable minimization
that fixes sign and coefficient before flavor readout.

Run `uv run --with sympy python
research/flavor/checkers/wp380_stable_mediator_envelope_sign.py` to regenerate
the result.
