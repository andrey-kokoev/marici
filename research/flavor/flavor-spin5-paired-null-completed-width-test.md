# Spin(5) paired null-completed width test (WP902)

## Question

Can common-random-number coupling reduce WP901's zero-drift event budget while
retaining selection-efficiency changes and non-Gaussian detector tails?

## Source-derived paired trial

At each pole, preregister a coupling of the zero-width and maximal-width
generators by sharing the latent phase-space uniforms, shower seed, pile-up
draw, and detector random seed. Only the declared source width differs. The
coupling must be fixed before output inspection and replay-identical from its
seed record; it may not be optimized to minimize observed disagreement.

Each completed trial emits one of seven symbols:

\[
\{\varnothing,B_1,B_2,B_3,B_4,B_5,B_6\},
\]

where \(\varnothing\) means that WP251 selection failed. Retaining this null
symbol is essential: otherwise width-dependent efficiency changes disappear
when the selected sample is normalized.

Let \(D=1\) when the paired outputs disagree. For any coupling,

\[
d_{\rm TV}(P_0,P_1)\leq p_D=\Pr(D=1).
\]

If zero discordances occur in \(n\) independent pairs, the exact one-sided
binomial upper bound with per-pole failure probability \(\alpha/2\) is

\[
p_D\leq1-(\alpha/2)^{1/n}.
\]

For a separately certified selection floor \(a_{\min}\), conditioning on the
six selected bins gives the conservative bound

\[
d_{\rm TV}(P_0(\cdot\mid S),P_1(\cdot\mid S))
\leq\frac{2p_D}{a_{\min}}.
\]

## Zero-discordance design

Using \(a_{\min}=389/14688\) only as a pilot design value,
\(\alpha=0.05\), and selected-shape tolerance \(\varepsilon=0.01\), require

\[
p_D\leq\frac{a_{\min}\varepsilon}{2}
=\frac{389}{2937600}.
\]

The exact minimum is 27856 generated event pairs per pole, 55712 pairs total.
At that count the conditional upper bound is 0.00999977002; one fewer pair
fails. This is much smaller than WP901 because pairing observes eventwise
agreement rather than estimating two six-bin distributions independently.

## Boundary

WP902 is valid only if the common-random-number coupling is executable and
source-authorized, all null trials are retained, pair independence is tested,
and the acceptance floor is calibrated at both poles under nuisance
completion. If any condition fails, WP901's independent-sample certificate is
the fallback.

Zero discordance would certify response stability, not identify the mixing
values, establish collision-data power, or select a flavor point. No paired
CMS samples have yet been executed.

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp902_spin5_paired_null_completed_width_test.py
~~~
