# Gauge-parallelized Yukawa contrast sign theorem: WP733

## Question

Can a shared gauge source fix the sign of WP729's additive portal contrast
while the two scalar flavor groups remain independent, thereby avoiding
WP732's common-frame tensor enlargement?

## Published one-loop nullclines

Use the one-loop gauge–Yukawa form and coefficients in arXiv:2008.08606v1,
equation A.1 and table 7. Set the optional model-A coupling
(alpha_{\kappa'}) to zero. Let

\[
g_1=\alpha_1,
\qquad
g_2=\alpha_2,
\qquad
T=\alpha_t+\alpha_b.
\]

For model A, the nonzero (y_A,kappa_A) nullclines are

\[
8y_A+2\kappa_A=12g_1,
\]

\[
3y_A+9\kappa_A+6T
=\frac{15}{2}g_1+\frac92g_2.
\]

For model B they are

\[
12y_B+\frac12\kappa_B=12g_1+24g_2,
\]

\[
3y_B+\frac{23}{4}\kappa_B+6T
=\frac{15}{2}g_1+\frac{33}{2}g_2.
\]

Here all symbols denote the paper's rescaled nonnegative squared couplings.

## Exact solutions

Solving gives

\[
\begin{aligned}
\kappa_A&=\frac{-8T+4g_1+6g_2}{11},
&y_A&=\frac{4T+31g_1-3g_2}{22},\\
\kappa_B&=\frac{-16T+12g_1+28g_2}{15},
&y_B&=\frac{4T+87g_1+173g_2}{90}.
\end{aligned}
\]

Thus

\[
q_A=\frac{(-4T+2g_1+3g_2)(4T+31g_1-3g_2)}{121},
\]

\[
q_B=\frac{2(-4T+3g_1+7g_2)(4T+87g_1+173g_2)}{675}.
\]

## Sign theorem on the positive nullcline domain

Set

\[
r=\frac{g_2}{g_1},
\qquad
t=\frac{T}{g_1}.
\]

Positivity of (kappa_A) requires

\[
0\le t<\frac{2+3r}{4}.
\]

This also implies positivity of (kappa_B) for (r\ge0). The WP729 additive
contrast is

\[
-4q_A+3q_B
=\frac{2g_1^2}{27225}P(r,t),
\]

where

\[
P(r,t)=150581r^2-91144rt+97338r
+5264t^2+11544t+3681.
\]

This polynomial is strictly positive throughout the positive nullcline
domain. The exact proof divides the domain according to the location of its
convex (t)-minimum:

1. for (r\le1443/11393), the minimum is at (t=0), where every coefficient
   is positive;
2. for (1443/11393<r<191/946), the interior minimum equals
   (-108900(737r^2-596r+8)/329), which is positive because the quadratic is
   negative across that interval;
3. for (r\ge191/946), the minimum is at the positive-Yukawa boundary, where
   (P=121(4r+1)(176r+89)>0).

Therefore the cancellation condition (q_B/q_A=4/3) is absent from the
positive separate-nullcline domain. Gauge parallelization fixes the sign of
the additive portal contrast without identifying the scalar flavor frames.

## Simultaneous-theory boundary

This is not yet the beta system of the combined A+B theory. Both mixed Yukawas
couple to the same Standard Model lepton and Higgs fields. Their shared
wavefunction anomalous dimensions generate cross terms in the simultaneous
(eta_{\kappa A}) and (eta_{\kappa B}) equations that are absent from the
two separately published models. The combined matter content also changes the
gauge beta coefficients.

WP733 proves that the gauge-parallelization route can remove the cancellation
fiber in the separately sourced one-loop system. Selector authority requires
deriving the cross anomalous-dimension coefficients and showing that the sign
theorem survives their inclusion at a common interacting gauge fixed point.

Reproduce with: `uv run --with sympy python research/flavor/checkers/wp733_gauge_parallelized_yukawa_contrast_sign.py`

Generated result:
`results/wp733_gauge_parallelized_yukawa_contrast_sign.json`.

Primary source: Hiller, Hormigos-Feliu, Litim, and Steudtner, arXiv:2008.08606v1,
equations A.1, A.5–A.7 and table 7.
