# Visible cubic branch separator: WP695

## A source-derived repair of the WP694 kernel

Use the symmetric radial source slice

\[
\lambda_h=\lambda_x=\frac32,
\qquad H^2=X^2=1,
\qquad \lambda_p=\pm1.
\]

Retune the quadratic masses by the WP694 stationarity rule. Both branches are
stable and have the identical mass-squared spectrum

\[
\{m_L^2,m_H^2\}=\{1,5\}.
\]

Both eigenstates have visible Higgs-overlap squared equal to one half. Thus
their visible production strengths and pole locations remain identical at the
two-point level.

## Cubic separator

Contract the source-derived cubic tensor with one heavy and two light
mass-eigenstate vectors. The two branches give

\[
g_{HLL}^{(+)}=\frac{7\sqrt2}{2},
\qquad
g_{HLL}^{(-)}=0.
\]

Moreover,

\[
\sqrt5>2,
\]

so the heavy-to-two-light channel is open on shell. Since both light states
retain a nonzero Higgs overlap, their subsequent visible decays provide a
detector-facing topology without adding an exit reference port.

## Classification

This is a source-derived branch separator and candidate physical-instrument
topology. It repairs the specific WP694 source-identification kernel. It is not
a selector: the source grammar still permits both branches and does not say
which one nature must realize.

The exact tree-level falsifier is the absence of the heavy-to-two-light decay
on the negative-portal branch despite identical two-point pole and overlap
data. The remaining gate is completion: embed the witness in the full flavor
tensor source, include widths and loop corrections, and calibrate efficiencies
and backgrounds for the visible final states.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp695_visible_cubic_branch_separator.py

Generated result: results/wp695_visible_cubic_branch_separator.json.
