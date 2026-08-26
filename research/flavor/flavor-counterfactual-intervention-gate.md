# Counterfactual second-intervention gate (WP415)

## Deutsch-Popperian conjecture

A second flavor source direction is physically meaningful only if the admitted
theory supplies an independently executable intervention whose calibrated
response is not proportional to the first intervention and whose distinguishing
margin survives uncertainty. It must be specified before the withheld flavor
record is opened.

For two source operations and the curvature/displacement readout pair, write

$$
J=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\qquad
W=\operatorname{diag}(w_H,w_J),
$$

with $w_H,w_J>0$ independently calibrated. Exact factorization gives

$$
\det(J^TWJ)=w_Hw_J(ad-bc)^2.
$$

Thus the contextual equivalence classes are singleton source points exactly
when the response wedge $ad-bc$ is nonzero. When it vanishes, source points
differing along $\ker J$ remain contextually equivalent under the complete
declared readout family.

## Attack specialized to WP412

The Higgs quadratic intervention has response $(1,v_0)^T$. Let a proposed
second source operation have calibrated response $(p,q)^T$. Its entire
distinguishing authority is

$$
\Delta=q-v_0p.
$$

The smallest exact falsifier is $\Delta=0$. With a conservative absolute
calibration uncertainty $\sigma_\Delta$, the robust acceptance condition is

$$
|\Delta|-\sigma_\Delta>0.
$$

This determinant is necessary but not sufficient. Authority also requires a
named source term, an executable setting, a common-frame detector instrument,
and a sealed prediction. A formally nonzero column assembled from unrelated
source and detector models is not an intervention.

## Consequence

The successor search is no longer “find another observable.” It is “derive an
operation whose response wedge against the Higgs mass knob is nonzero.” A
candidate failing that test is another presentation of the existing knob. A
candidate passing only algebraically remains unphysical until its setting and
instrument are demonstrated.

Run `uv run --with sympy python
research/flavor/checkers/wp415_counterfactual_intervention_gate.py` to
regenerate the JSON result.
