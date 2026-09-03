# Slope compensation applies only before the gamma-localizer sign crossing

## Question

Does the sector-slope identity uniformly explain the positive gamma--prime rank-two determinant?

## Identity

For triples `a,b` with nonzero initial entries, define

\[
\mu_a=a_1/a_0,
\qquad
\delta_a=(a_0a_2-a_1^2)/a_0^2,
\]

and similarly for `b`. Then

\[
D(a+b)
=(a_0+b_0)(a_0\delta_a+b_0\delta_b)
+a_0b_0(\mu_a-\mu_b)^2.
\]

The second term is a positive slope-separation resource only when `a_0b_0>0`.

## Source scan

The updated gamma--prime checker verified the identity to approximately `10^-52` residual and found two distinct regimes.

At `(t,h)=(0.01,0.005)`,

\[
g_0\approx0.09923,
\qquad
p_0\approx0.0003675.
\]

Both are positive. The weighted curvature term is approximately

\[
-8.5566\times10^{-4},
\]

while slope compensation is

\[
+9.9095\times10^{-4},
\]

leaving

\[
D_2\approx1.3530\times10^{-4}.
\]

Here slope separation is the operative repair mechanism.

At `(t,h)=(0.05,0.01)`, however,

\[
g_0\approx-0.02069,
\qquad
p_0\approx0.02326.
\]

The gamma sector already fails the scalar localizer sign. Consequently

\[
g_0p_0(\mu_g-\mu_p)^2<0,
\]

and the slope term is approximately `-6.51e-9`, not a positive resource. The positive determinant instead appears in the signed weighted-curvature term, approximately `8.20e-8`, leaving total `7.55e-8`.

## Consequence

A uniform proof cannot treat gamma and prime localizers as two positive sector measures. That chart ceases to exist after the gamma initial difference crosses zero.

A regime-adapted proof would require:

1. short heat: gamma dominance with exponentially small primes;
2. intermediate heat while `g_0,p_0>0`: slope-gap compensation;
3. larger heat after `g_0<0`: direct coupled control of the total differences, because even rank-one positivity is cross-sector.

The third regime is the severe endpoint--gamma--prime cancellation region already identified in prior heat reconciliation.

## Boundary

All values are uncertified floating observations. The prime cutoff is negligible under the explicit erfc tail bound, but gamma values still need interval enclosure.

## Disposition

Use the slope-gap inequality only on parameter boxes where interval bounds prove `g_0>0` and `p_0>0`. Do not globalize it across the gamma sign crossing. For larger heat, retain the total coupled localizer as the primitive object.