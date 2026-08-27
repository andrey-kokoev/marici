# Protected conditional Gram: WP673

## Independently typed metric

For WP672's source coordinates \((u,v)\), the ideal response Jacobian is

\[
J=\begin{pmatrix}1&1\\ \alpha&-\alpha\end{pmatrix}.
\]

Declare an independently calibrated detector precision

\[
W=\begin{pmatrix}p&r\\r&q\end{pmatrix},
\qquad p>0,
\qquad pq-r^2>0.
\]

No entry of \(W\) is inferred from the desired source separation. The
conditional information Gram is \(G=J^TWJ\), with exact determinant

\[
\det G=4\alpha^2(pq-r^2).
\]

The two-port family is therefore faithful exactly when the analyzer is
nonzero and the independently supplied detector metric is positive definite.

## Stability bound

If calibration establishes

\[
|\alpha_0|>\delta_\alpha,
\qquad
\lambda_{\min}(W)\geq w_{\min}>0,
\]

then

\[
\lambda_{\min}(G)
\geq2w_{\min}\min\left\{1,(|\alpha_0|-\delta_\alpha)^2\right\}.
\]

This is an uncertainty-stable rank certificate, not a fitted covariance.

## Hostile metric

For independent total-rate and chirality precisions \(W=\operatorname{diag}(1,\tau)\),

\[
\det G=4\alpha^2\tau.
\]

At \(\tau=0\), the conditional Gram has rank one even if the formal chirality
coordinate is written down. Algebraic port existence is not detector control.

## Disposition

WP673 completes the conditional information theorem. It does not supply the
metric. Physical authority still requires a named polarimeter and calibration
sample establishing \(\alpha\), \(W\), support, acceptance, backgrounds, and
covariance independently of the target signal.

The operation identifies protected vertex magnitudes conditionally. It
selects neither their values nor a physical16 point.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp673_protected_conditional_gram.py

Generated result: results/wp673_protected_conditional_gram.json.
