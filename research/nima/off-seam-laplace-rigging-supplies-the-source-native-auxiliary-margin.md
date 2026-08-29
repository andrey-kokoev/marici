# Off-seam Laplace rigging supplies the source-native auxiliary margin

## Laplace-weighted relative energy

The open-sector parameter already supplies a positive displacement \(\sigma>0\). Use the source-native exponential derivative weight

\[
w_\sigma(u)=e^{2\sigma|u|}.
\]

The relative graph energy is

\[
\|f\|_{\sigma}^2
=
\int_{\mathbb R}
e^{2\sigma|u|}
|f'(u)|^2\,du
+
|f(-\infty)|^2
+
|f(+\infty)|^2.
\]

This is the Sobolev history form associated with the same Laplace rigging that makes the primitive channel Hilbert-continuous off the seam.

## Optimal jump cost

The inverse-weight mass is

\[
I_\sigma
=
\int_{\mathbb R}e^{-2\sigma|u|}\,du
=
\frac1\sigma.
\]

For normalized jump coordinate \(b\), the optimal derivative cost is

\[
\frac{2|b|^2}{I_\sigma}
=
2\sigma|b|^2.
\]

Hence the reduced endpoint energy is

\[
E_{\partial,\sigma}(a,b)
=
|a|^2
+
(1+2\sigma)|b|^2.
\]

The boundary Green exchange therefore has normalized norm

\[
\|K_{\partial}(\sigma)\|
=
\frac1{\sqrt{1+2\sigma}}.
\]

The source-native auxiliary margin is

\[
\delta_{\mathrm{aux}}(\sigma)
=
1-
\frac1{\sqrt{1+2\sigma}}.
\]

## Correct uniformity region

On every compact off-seam region

\[
\sigma\ge\sigma_0>0,
\]

one has

\[
\delta_{\mathrm{aux}}(\sigma)
\ge
1-
\frac1{\sqrt{1+2\sigma_0}}
>0.
\]

This bound is uniform over primes, grades, cutoffs, and Mellin translations because the exponential weight is transported with the object fiber.

At the seam,

\[
\delta_{\mathrm{aux}}(\sigma)\to0
\qquad
(\sigma\downarrow0).
\]

That collapse is expected and matches the primitive-channel transition from Hilbert continuity to a distributional boundary value.

## Resolution of the weight-authority issue

The earlier polynomial exponent \(\epsilon\) was a convenient topology parameter and could not explain strictness. The Laplace parameter \(\sigma\) is already source data in the open sector. It therefore supplies the derivative weight and the exact contraction margin without introducing an arbitrary supercritical rung.

The projective exponential rigging contains all \(\sigma>0\) fibers. One must not take an infimum over all positive \(\sigma\); uniformity is only claimed on compact subsets of the open sector.

## Constructor consequence

The auxiliary gate now has the correct scope:

\[
\text{off seam: strict boundary contraction},
\]

\[
\text{at seam: distributional degeneration}.
\]

The next task is to insert the exact theta incidence map into this positive auxiliary block and check endpoint loading against the real endpoint energy. This is the second nested local contraction gate.
