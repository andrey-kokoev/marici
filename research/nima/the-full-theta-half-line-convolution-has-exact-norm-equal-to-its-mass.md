# The full theta half-line convolution has exact norm equal to its mass

## Operator

Let \(\Phi\in L^1(0,\infty)\) be nonnegative and define on
\(L^2(\mathbb R)\)

\[
(H_\Phi c)(t)
=
\int_0^\infty\Phi(r)c(t+r)\,dr.
\]

Extend \(\Phi\) by zero to the negative half-line, with the reflection
convention needed to write \(H_\Phi\) as ordinary convolution.

## Fourier multiplier

Under the unitary Fourier transform, \(H_\Phi\) is multiplication by

\[
h(\xi)
=
\int_0^\infty
\Phi(r)e^{i\xi r}\,dr
\]

up to the harmless sign change \(\xi\mapsto-\xi\).

Therefore \(H_\Phi\) is normal and

\[
\|H_\Phi\|
=
\operatorname*{ess\,sup}_{\xi\in\mathbb R}|h(\xi)|.
\]

Nonnegativity gives

\[
|h(\xi)|
\le
\int_0^\infty\Phi(r)\,dr
=
M_\Phi.
\]

At zero frequency,

\[
h(0)=M_\Phi.
\]

Since \(h\) is continuous, every neighborhood of zero has positive measure
and contains values arbitrarily close to \(M_\Phi\). Hence

\[
\|H_\Phi\|=M_\Phi.
\]

The earlier expected equality is therefore exact on the completed full-line
translation carrier.

## Shifted histories

For either reciprocal sign,

\[
\|(I\pm iH_\Phi)f\|
\ge
(1-M_\Phi)\|f\|
\]

whenever \(M_\Phi<1\). Consequently,

\[
D_\pm
=
\frac12(I\pm iH_\Phi)^*(I\pm iH_\Phi)
\ge
\frac{(1-M_\Phi)^2}{2}I.
\]

Thus the analytic completion margin is explicit and no pseudospectral
qualification remains: the convolution is normal.

## Exact versus lower-bound information

The norm identity is exact, but the lower bound

\[
1-M_\Phi
\]

need not be the exact smallest singular value of \(I\pm iH_\Phi\).
The exact value is

\[
c_\pm
=
\operatorname*{ess\,inf}_{\xi}
|1\pm ih(\xi)|.
\]

The mass estimate is a robust source-simple bound.

## Approximate extremizers

The norm \(M_\Phi\) is generally not attained by an \(L^2\) constant
function. It is approached by normalized packets whose Fourier support
concentrates near \(\xi=0\), equivalently by long nearly constant packets
in the translation variable.

This proves completion norm equality without claiming a finite-cutoff
eigenvector.

## Finite cutoffs

A finite interval compression \(H_{\Phi,L}\) satisfies

\[
\|H_{\Phi,L}\|
\le M_\Phi.
\]

Equality need not hold at finite \(L\). Nevertheless the same bounded-below
estimate

\[
\|(I\pm iH_{\Phi,L})f\|
\ge
(1-M_\Phi)\|f\|
\]

is uniform in cutoff. Hence finite sections and completion share the same
sufficient margin.

## Prime scaling

For a labelled history

\[
H_{p}=\alpha_pH_\Phi,
\]

one has exactly

\[
\|H_p\|
=
|\alpha_p|M_\Phi
\]

on the full translation carrier. Uniform auxiliary coercivity follows from

\[
\sup_p|\alpha_p|M_\Phi<1.
\]

The worst prime is determined entirely by the source coefficient
\(\alpha_p\).

## Remaining authority gate

This closes the operator-norm part only. The programme must still prove that:

1. the shifted-history square uses this full-line convolution with the stated
   normalization;
2. \(M_\Phi\) equals the source-declared completed theta mass in that
   convention;
3. the identity term belongs to the same authorized wall/history carrier;
4. prime coefficients are placed before history synthesis as assumed.

## Frontier

For the completed theta convolution itself,

\[
\|H_\Phi\|=M_\Phi
\]

is now a theorem, not an expectation. Once the source normalization diagram
is closed, the analytic auxiliary margin follows immediately.
