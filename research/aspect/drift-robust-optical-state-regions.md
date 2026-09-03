# Drift-robust optical state regions

## Question

How should bounded, nonaffine efficiency uncertainty be propagated into a certified path–polarization state region, and when can that region still distinguish attachment lifts or certify entanglement?

## Claim boundary

This packet constructs convex feasibility regions from channel-efficiency intervals and gives an exact Bell-diagonal witness. It does not solve the full experimental semidefinite program or infer a unique state under drift.

## Channel probability intervals

For a channel effect \(E_k\), observed unconditional click probability \(c_k\), and efficiency interval

\[
0<\underline\eta_k\le\eta_k\le\overline\eta_k,
\]

the ideal Born probability satisfies

\[
\frac{c_k}{\overline\eta_k}
\le
\operatorname{Tr}(\rho E_k)
\le
\frac{c_k}{\underline\eta_k}.
\]

Intersect these slabs with

\[
\rho\succeq0,
\qquad
\operatorname{Tr}\rho=1,
\]

and with the settingwise probability-normalization equations. The resulting set

\[
\mathcal R(c,[\underline\eta,\overline\eta])
\]

is convex. It contains every state compatible with the records and declared efficiency bounds. If it is empty, the state model, drift bounds, or records are mutually inconsistent.

A zero lower efficiency bound removes the finite upper probability bound for that channel; such a channel cannot support robust reconstruction by itself.

## Lift separation

For two attachment-lift hypotheses with feasible regions \(\mathcal R_1\) and \(\mathcal R_2\), the records robustly distinguish them when the regions are disjoint in the intended quotient. A sufficient coordinate test is a probe \(A\) with disjoint expectation intervals:

\[
\sup_{\rho\in\mathcal R_1}\operatorname{Tr}(\rho A)
<
\inf_{\rho\in\mathcal R_2}\operatorname{Tr}(\rho A),
\]

or the reversed inequality. Overlapping intervals retain unresolved multiplicity; choosing the nearest point would fabricate a lift selection.

## Bell-diagonal exact sector

Consider

\[
\rho(t)=\frac14
\left(I+t_xX\otimes X+t_yY\otimes Y+t_zZ\otimes Z\right).
\]

Positivity is equivalent to nonnegativity of the four Bell weights. Fidelity with \(\lvert\Phi^+\rangle\) is

\[
F_{\Phi^+}=\frac{1+t_x-t_y+t_z}{4}.
\]

Every separable two-qubit state has \(F_{\Phi^+}\le1/2\). Therefore the entire feasible region is certified entangled when

\[
\inf_{\rho\in\mathcal R}F_{\Phi^+}>1/2.
\]

For intervals

\[
t_x,t_z\in[4/5,1],
\qquad
t_y\in[-1,-4/5],
\]

the interval lower bound is

\[
F_{\Phi^+}\ge17/20>1/2.
\]

This certifies entanglement without selecting one state and without an affine drift model.

## Exact diagnostic

An exact rational checker verifies click-to-Born interval inversion, convex closure of interval constraints, the four Bell weights, the fidelity lower bound \(17/20\), positivity and entanglement of every feasible point on a bounded rational grid, and disjoint coordinate intervals for two path-lift hypotheses.

## Disposition

Bounded calibration uncertainty should produce a convex state region rather than a point estimate. Robust claims are universal statements over that region. Disjoint probe intervals separate attachment lifts; a uniformly negative entanglement witness certifies entanglement. The Bell-diagonal fixture demonstrates both without assuming affine drift, but full fifteen-coordinate certification requires a semidefinite enclosure implementation.
