# Common-perturbation port calibration (WP366)

## Bounded instrument construction

WP365 requires an operational comparison of the flavor port \(x=J^2\) and
source port \(y=Q/M^2\). Admit one controlled source perturbation \(\epsilon\)
with local responses

\[
p=\frac{dx}{d\epsilon},
\qquad
q=\frac{dy}{d\epsilon},
\qquad q\ne0.
\]

Let detector records be \(X=g_xx\) and \(Y=g_yy\), with independently
calibrated positive gains. Their measured slopes are

\[
R_X=g_xp,
\qquad
R_Y=g_yq.
\]

The gain-corrected response ratio

\[
s_{\mathrm{det}}
=\frac{g_y}{g_x}\frac{R_X}{R_Y}
=\frac pq
\]

is invariant under independent changes of detector units. It is an executable
candidate for the relational port scale in WP365.

## Kernel and hostile pair

Without gain calibration, the raw slope ratio sees only

\[
\frac{R_X}{R_Y}=\frac{g_x}{g_y}\frac pq.
\]

The physical response packets

The pairs \((p/q,g_x/g_y)=(1,2)\) and \((2,1)\) produce the same raw
ratio 2.

Independent gain calibration removes this exact ambiguity.

The common perturbation response Jacobian is a two-by-one column and has rank
one whenever either response is nonzero. It measures one relational ratio; it
does not independently excite or identify two source-error directions. The
Ward condition is operationally testable as

\[
\alpha q-p=0.
\]

## Authority boundary

This construction measures \(s=p/q\); it does not select its value. If the
Ward source theory predicts \(\alpha/s=1\), the calibrated experiment can
falsify that relation. It cannot promote the measured \(s\) into a source
prediction.

The instrument is physically typed only if the same admitted perturbation
causally changes both the flavor invariant and the canonical source response,
the gains are calibrated independently of the desired equality, and both
slopes are evaluated in one threshold and renormalization scheme.

The smallest exact falsifier is the uncalibrated hostile pair above. The
remaining flavor gate is a concrete source operation realizing nonzero
\((p,q)\) without fitting its coupling from \(J\), plus uncertainties and
support bounds showing that \(q\) stays resolvably nonzero.

Run `uv run --with sympy python
research/flavor/checkers/wp366_common_perturbation_port_calibration.py` to
regenerate the exact result.
