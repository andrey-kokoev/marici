# Nondecoupling D-term threshold fiber: WP747

## Question

If the conditional WP746 moment map is realized through a heavy broken gauge
sector, does its asymmetric portal survive threshold matching with a fixed
magnitude?

## Exact elimination map

Let (J) denote one component of the light moment-map current and let
(sigma) be its heavy gauge-breaking scalar partner. The minimal quadratic
threshold model is

\[
V(J,\sigma)
=\frac{g^2}{2}(J+M\sigma)^2
+\frac{m_{\mathrm{soft}}^2}{2}\sigma^2.
\]

The heavy equation of motion gives

\[
\sigma_*
=-\frac{g^2M}{g^2M^2+m_{\mathrm{soft}}^2}J.
\]

Substitution yields

\[
V_{\mathrm{eff}}(J)
=\frac{g^2}{2}\epsilon J^2,
\qquad
\epsilon
=\frac{m_{\mathrm{soft}}^2}
{g^2M^2+m_{\mathrm{soft}}^2}.
\]

This is the nondecoupling (D)-term factor. Primary constructions likewise
require an extended gauge sector near the breaking scale for the additional
(D)-term to survive. See
[Maloney, Pierce, and Wacker](https://arxiv.org/abs/hep-ph/0409127).

## What survives

Applying the common factor to WP746 gives

\[
g_n=\epsilon\frac{g^2}{3},
\qquad
g_m=-\epsilon\frac{g^2}{6},
\qquad
g_n-g_m=\epsilon\frac{g^2}{2}.
\]

Thus the relative sign and ratio survive every finite positive threshold
factor:

\[
\frac{g_n}{g_m}=-2.
\]

The strict radial margin also survives conditionally:

\[
4\lambda_n\lambda_m-\lambda_x^2
=\epsilon^2\frac{g^4}{12}>0.
\]

The threshold is therefore a sign/ratio rigidifier.

## Exact survival obstruction

In the supersymmetric limit,

\[
m_{\mathrm{soft}}^2\longrightarrow0
\quad\Longrightarrow\quad
\epsilon\longrightarrow0.
\]

The additional portal decouples completely. In the opposite limit,
(epsilon\to1). Every intermediate value is realized by

\[
m_{\mathrm{soft}}^2
=\frac{\epsilon}{1-\epsilon}g^2M^2.
\]

Hence threshold survival is a continuous source fiber. For example,
(m_{\mathrm{soft}}^2=g^2M^2) gives contrast (g^2/4), whereas
(m_{\mathrm{soft}}^2=3g^2M^2) gives (3g^2/8). Both preserve the same weight
geometry and sign ratio; their exact contrast residual is (g^2/8).

## Disposition

Nondecoupling matching preserves the representation-fixed sign and ratio but
does not select survival or magnitude. It replaces the single gauge-scale
fiber by the pair consisting of the gauge magnitude and a soft-to-vector mass
ratio. The supersymmetric endpoint erases the portal.

A complete source principle must derive the supersymmetry-breaking ratio,
gauge magnitude, and RG clock together. The full labelled heavy spectrum,
finite widths, loop matching, and calibrated physical16 response remain
required. Algebraic nondecoupling is not yet an instrument.

Reproduce with
`uv run --with sympy python research/flavor/checkers/wp747_nondecoupling_dterm_threshold_fiber.py`.

Generated result:
`results/wp747_nondecoupling_dterm_threshold_fiber.json`.
