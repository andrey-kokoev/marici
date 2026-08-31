# Correction: the Evans theta atoms live in logarithmic half-density coordinate, not the additive Gaussian family

## Question

Do the Gaussian-pair erf kernels derived in the preceding candidate-one packets
apply to the completed forcing \(\Phi(q)\) used by the exact Evans lift?

## Claim boundary

No. They use the Gaussian family \(e^{-\pi n^2x^2}\) in the multiplicative
source coordinate as though it were the completed forcing in the additive
logarithmic coordinate. The Evans forcing is obtained only after logarithmic
pullback, half-density weighting, and the completion differential. The erf
kernels and their Gaussian-vacuum Ward recurrence therefore do not establish a
candidate-one response law. The general shell-autocorrelation reduction remains
valid.

## Correct completed forcing

The source precursor is

\[
 h(u)=\frac12 e^{u/2}\vartheta(e^{2u}),
\]

and

\[
 \Phi(u)=\left(\partial_u^2-\frac14\right)h(u).
\]

For one positive theta label, put

\[
 y_n(u)=\pi n^2e^{2u}.
\]

Up to the fixed theta-series multiplicity convention, the labelled completed
atom is

\[
 \Phi_n(u)
 =e^{u/2}
 \left(2y_n(u)^2-3y_n(u)\right)e^{-y_n(u)}.
\]

Equivalently,

\[
 \Phi_n(u)
 =
 \left(
 2\pi^2n^4e^{9u/2}
 -3\pi n^2e^{5u/2}
 \right)e^{-\pi n^2e^{2u}}.
\]

This is not \(e^{-\pi n^2u^2}\).

## Coordinate mismatch

The Gaussian vacuum packet defines

\[
 \phi_n(x)=e^{-\pi n^2x^2}
\]

in a positive multiplicative coordinate \(x\). The Evans shell uses

\[
 u\in\mathbb R,
 \qquad
 x=e^u,
\]

with half-density and completion operators already applied.

Replacing \(x\) by \(u\) before those operations changes the source object and
its differential equation. Equal label symbols do not construct a comparison
map.

## Affected claims

The following recent packets are valid calculations for the auxiliary additive
Gaussian family but not for the completed Evans forcing:

- `the-localized-polarized-gaussian-correlation-synthesis-has-an-exact-erf-kernel.md`;
- `the-gaussian-vacuum-turns-each-shell-autocorrelation-into-an-endpoint-forced-separation-resolvent.md`;
- `laplace-transform-of-the-gaussian-pair-green-identity-gives-an-exact-spectral-jet-recurrence.md`;
- `the-gaussian-pair-endpoint-transform-is-an-explicit-entire-erfc-section.md`;
- the Gaussian-pair prerequisite list in
  `the-scc-prime-shell-cell-has-no-source-formula-for-its-reciprocal-linking-response.md`.

Their formulas must not be used as evidence for candidate one or SCC mutation.

## Surviving candidate-one result

For the actual completed forcing,

\[
 \rho_{a,b}(t)
 =\int_a^b\Phi(u)\Phi(u+t)\,du
\]

and

\[
 I_{a,b}^{(0)}(z)
 =-\int_0^\infty e^{-zt}\rho_{a,b}(t)\,dt
\]

remain exact. Thus the subleading ordinary shell is still a bulk
Autocorrelation transform and still cannot be inferred from finite endpoint
flux alone.

## Correct labelled kernel route

For ordered labels \((n,m)\), set

\[
 Y=e^{2u},
 \qquad
 du=\frac{dY}{2Y}.
\]

Then

\[
 y_n(u)=\pi n^2Y,
 \qquad
 y_m(u+t)=\pi m^2e^{2t}Y.
\]

The product \(\Phi_n(u)\Phi_m(u+t)\,du\) is a finite polynomial in \(Y\)
multiplied by

\[
 \exp\!\left[-\pi\left(n^2+m^2e^{2t}\right)Y\right]dY.
\]

Therefore the correct finite-shell ordered-pair kernel is a finite combination
of incomplete gamma functions with limits

\[
 Y=e^{2a}
 \quad\text{and}\quad
 Y=e^{2b},
\]

not an erf kernel in \(u\).

## Next exact calculation

Expand the degree-four polynomial from
\(\Phi_n(u)\Phi_m(u+t)\), integrate each monomial in \(Y\), and retain the
ordered dependence on \(m^2e^{2t}\). This will produce the correct
source-labelled density for testing reciprocal/linking responses.

## Disposition

The Gaussian-pair candidate-one advance is retracted as a coordinate-typing
error. The universal autocorrelation obstruction survives, and the corrected
labelled route is an explicit incomplete-gamma calculation in the
multiplicative variable. No RH conclusion is authorized.
