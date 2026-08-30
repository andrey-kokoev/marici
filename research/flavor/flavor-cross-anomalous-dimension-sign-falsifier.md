# Cross-anomalous-dimension sign falsifier: WP734

## Question

Does WP733's strictly oriented portal sign survive arbitrary nonnegative cross
anomalous dimensions in the simultaneous A+B Yukawa system?

## Deformed simultaneous nullclines

Retain the exact published coefficients on the simple source slice

\[
g_1=1,
\qquad
g_2=0,
\qquad
\alpha_t+\alpha_b=0.
\]

Let (x\ge0) multiply (kappa_B) in the (kappa_A) nullcline and let
(y\ge0) multiply (kappa_A) in the (kappa_B) nullcline. These terms
represent the most general positive cross wavefunction contributions at this
level:

\[
\begin{aligned}
8y_A+2\kappa_A&=12,\\
3y_A+9\kappa_A+x\kappa_B&=\frac{15}{2},\\
12y_B+\frac12\kappa_B&=12,\\
3y_B+\frac{23}{4}\kappa_B+y\kappa_A&=\frac{15}{2}.
\end{aligned}
\]

The exact solution is

\[
\begin{aligned}
\kappa_A&=\frac{144x-540}{32xy-1485},
&y_A&=\frac{96xy-72x-4185}{64xy-2970},\\
\kappa_B&=\frac{96y-1188}{32xy-1485},
&y_B&=\frac{64xy-8y-2871}{64xy-2970}.
\end{aligned}
\]

## Exact cancellation surface

For (q_A=y_A\kappa_A) and (q_B=y_B\kappa_B), the additive portal contrast
is

\[
-4q_A+3q_B=-\frac{18F(x,y)}{(32xy-1485)^2},
\]

where

\[
\begin{aligned}
F(x,y)={}&1536x^2y-1152x^2-512xy^2+576xy-62640x\\
&+64y^2+22176y-33129.
\end{aligned}
\]

Thus (F(x,y)=0) is the exact cross-anomalous-dimension surface on which the
representation-oriented portal source cancels.

## Positive hostile witness

Choose

\[
x=1,
\qquad
y=\frac{759}{28}-\frac{33}{56}\sqrt{1493}.
\]

Both cross coefficients are strictly positive. The nullcline determinant is
nonzero, all four Yukawa coordinates are strictly positive, and

\[
-4q_A+3q_B=0.
\]

This is an exact falsifier of sign robustness under unspecified positive cross
terms. It does not assert that the actual simultaneous theory takes these
coefficient values.

## Disposition

WP733 remains correct on the separate-nullcline truncation, but its sign
conclusion does not extend to the simultaneous theory from positivity alone.
The first nonfaithful arrow is omission of the shared-field anomalous-dimension
block. Gauge parallelization can still succeed if the calculated point lies a
strict distance from (F=0); that distance, with perturbative uncertainty,
is the required sign margin.

The next calculation must derive (x) and (y) from the common Higgs and
lepton wavefunction graphs, then evaluate (F(x,y)). Fitting them to avoid the
cancellation surface would have no source authority.

Reproduce with: `uv run --with sympy python research/flavor/checkers/wp734_cross_anomalous_dimension_sign_falsifier.py`

Generated result:
`results/wp734_cross_anomalous_dimension_sign_falsifier.json`.
