# Higgs retained-reference response-rank gate (WP414)

## Question

WP412 supplies two readouts under the same quadratic Higgs deformation $c$:

$$
\frac{\partial(H_{\rm rel},J_{\rm rel})}{\partial c}
=
\begin{pmatrix}1\\v_0\end{pmatrix}.
$$

Does observing both components meet the rank-two detector condition needed to
identify two independent source-error directions?

## Exact obstruction

No. The response has one source column and rank one. For any independently
calibrated positive diagonal detector metric
$W=\operatorname{diag}(w_H,w_J)$, its one-parameter information is positive,

$$
J_c^T WJ_c=w_H+v_0^2w_J>0,
$$

but this establishes sensitivity to one parameter only. Naming two source
errors without deriving a second operation merely duplicates the causal column:

$$
J_{\rm det}=
\begin{pmatrix}
1&1\\
v_0&v_0
\end{pmatrix},
\qquad
\det(J_{\rm det}^TWJ_{\rm det})=0.
$$

The exact ambiguity is the difference direction $(-1,1)$. Thus curvature and
relative-tadpole measurements are complementary readouts of one knob, not two
independent source probes. Algebraic duplication cannot supply executable
control.

## Consequence

Even granting the missing WP413 laboratory control, the Higgs quadratic knob
would calibrate a one-dimensional intervention family. It could test the
WP412 common-shift law but could not kill Nima's two-dimensional source-story
ambiguity. Rank-two authority requires an independently derived second source
column not proportional to $(1,v_0)^T$, with its own physical implementation
and common-frame calibration.

Run `uv run --with sympy python
research/flavor/checkers/wp414_higgs_response_rank_gate.py` to regenerate the
JSON result.
