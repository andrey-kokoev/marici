# Rank-two sector-slope compensation

## Question

What exact quantity allows the coupled gamma--prime determinant to be positive when both sector determinants are negative?

## Claim boundary

An exact normalized decomposition identifies the compensation resource. No arithmetic interval bound is supplied.

## Polarization

Write the two sector moment triples as

\[
a=(a_0,a_1,a_2),
\qquad
b=(b_0,b_1,b_2),
\]

and define

\[
D(x)=x_0x_2-x_1^2.
\]

Then

\[
D(a+b)
=
D(a)+D(b)
+a_0b_2+a_2b_0-2a_1b_1.
\]

The final three terms are the gamma--prime cross contribution observed numerically.

## Normalized slopes and curvature

Assume \(a_0,b_0>0\). Define

\[
\mu_a=\frac{a_1}{a_0},
\qquad
\mu_b=\frac{b_1}{b_0},
\]

and normalized sector curvatures

\[
\delta_a=\frac{D(a)}{a_0^2},
\qquad
\delta_b=\frac{D(b)}{b_0^2}.
\]

Exact algebra gives

\[
D(a+b)
=
(a_0+b_0)
(a_0\delta_a+b_0\delta_b)
+a_0b_0(\mu_a-\mu_b)^2.
\]

The first term is the weighted sector-curvature contribution. The second is always nonnegative and measures separation between the sector first-step ratios.

## Exact compensation criterion

When the weighted curvature is negative, coupled positivity is equivalent to

\[
(\mu_a-\mu_b)^2
\geq
-\frac{a_0+b_0}{a_0b_0}
(a_0\delta_a+b_0\delta_b).
\]

Thus the positive cross term is not an unexplained cancellation. It is the between-sector slope variance.

If

\[
\mu_a=\mu_b,
\]

mixing supplies no positive resource. Two negative sector curvatures then remain negative after coupling.

## Mixture interpretation

Normalize the total mass and put

\[
\theta=\frac{a_0}{a_0+b_0}.
\]

Then

\[
\frac{D(a+b)}{(a_0+b_0)^2}
=
\theta\delta_a
+(1-\theta)\delta_b
+	heta(1-\theta)(\mu_a-\mu_b)^2.
\]

This is the variance decomposition into within-sector curvature and between-sector slope separation. The sectors may each have negative pseudo-variance while their mixture has nonnegative total variance.

## Arithmetic target

A certified rank-two proof can now avoid enclosing three nearly cancelling determinants independently. It should instead enclose:

1. \(a_0>0\) and \(b_0>0\);
2. the slope gap \(|\mu_a-\mu_b|\) from below;
3. the weighted curvature deficit from above.

The decisive inequality is the displayed compensation criterion. This coordinate system may reduce interval overestimation because the positive mechanism is isolated before subtraction.

The source sectors must remain gamma and prime components of the same normalized remainder sequence. Arbitrarily repartitioning terms to enlarge the slope gap would not be source-derived.

## Exact fixtures

The checker verifies:

- the polarization identity;
- the normalized slope-curvature identity;
- a case where both sector determinants are negative but their sum is positive;
- a hostile equal-slope case where coupling cannot repair negativity.

## Disposition

Rank-two positivity is a quantitative separation theorem between gamma and prime decay ratios. The next certified calculation should target the slope-gap inequality directly, with explicit tail bounds, rather than reproduce cancellation-prone determinant arithmetic.

## Verification

- `research/voevodsky/rank-two-sector-slope-compensation-v1.json`
- `research/voevodsky/checkers/check_rank_two_sector_slope_compensation.py`
- `research/voevodsky/results/rank_two_sector_slope_compensation.json`
