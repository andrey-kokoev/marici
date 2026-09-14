# Prior positive-carrier search reduces the missing mesh weights to complete monotonicity

## Search result

Repository search for source-derived positive circle measures, cycle forms, and prime weights found several positive constructions, but none directly supplies the Gaussian Weil measure:

- the shell response form is positive only after a measurement design and weights are chosen;
- the theta completion differential gives a positive operator and positive Riemann Fourier kernel, but explicitly does not imply real zeros;
- prime heat measures are positive in isolated source sectors, while the complete endpoint--gamma--prime formula remains coupled and signed;
- GNS, Herglotz, and spectral reconstructions begin after positivity and are therefore completion theorems, not RH proofs.

## Exact surviving constructor

`research/grothendieck/complete-monotonicity-is-the-common-positive-constructor.md` gives an exact equivalence under the established entire-even heat conformance identities.

Set

\[
H(t)=\mathcal K(t,0).
\]

If

\[
(-1)^kH^{(k)}(t)\geq0
\qquad(k\geq0,\ t>0),
\]

then Bernstein's theorem constructs a positive measure

\[
H(t)=\int_0^\infty e^{-t\lambda}\,d\nu(\lambda).
\]

Symmetric square-root lift through \(\lambda=u^2\) gives a positive measure \(\mu\) on the spectral line and

\[
\mathcal K(t,z)
=
\int_{\mathbb R}e^{-tu^2}e^{izu}\,d\mu(u).
\]

This is precisely the translation-coherent oriented mesh factorization sought:

\[
c_\alpha=d\mu(u)>0,
\qquad
s_z(u)=e^{izu}.
\]

## Revised arithmetic gate

The missing positive mesh weights need not be guessed cell by cell. They are forced uniquely by Laplace inversion if the coupled on-axis source is completely monotone.

Thus the noncircular source target is

\[
\boxed{
(-1)^k\frac{d^k}{dt^k}
\left[
H_E(t)+H_\Gamma(t)+H_P(t)
\right]
\geq0
}
\]

for every derivative order and every positive heat width, with all three sectors retained before differentiation and comparison.

Under the conformance theorem, this single scalar hierarchy is equivalent to:

- the positive spectral measure;
- the oriented positive mesh carrier;
- universal rung-four Schwarz positivity;
- all finite Gaussian Gram positivity;
- the Weil/RH gate.

## Status

No prior packet proves these coupled derivative inequalities. This is the remaining arithmetic problem, not a missing abstract carrier construction.
