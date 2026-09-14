# Positive additive mesh charge constructs the common primitive/prime carrier

The discrete-wave source has more structure than an arbitrary entrywise-positive matrix. It is a positive additive charge on causal mesh cells.

Let the elementary cells be \(\alpha\), with

\[
c_\alpha>0.
\]

Construct

\[
H_C=\ell^2(\{\alpha\},c)
\]

and assign to every causal region \(D\) the incidence vector

\[
\Phi(D)_\alpha
=
\sqrt{c_\alpha}\,\mathbf1_{\alpha\in D}.
\]

Then

\[
\boxed{
\langle\Phi(D),\Phi(E)\rangle
=
\sum_{\alpha\in D\cap E}c_\alpha
=C(D\cap E).
}
\]

In particular,

\[
\|\Phi(D)\|^2=C(D)\geq0.
\]

Thus positive additive mesh charge canonically supplies:

- a primitive region observer \(D\mapsto\Phi(D)\);
- a primitive-square observer \(C(D)\);
- a primitive-prime or region-pair observer \(C(D\cap E)\);
- positive rung-four Schwarz squares for every pair of regions.

Indeed,

\[
C(D\cap E)^2
\leq
C(D)C(E)
\]

by Cauchy--Schwarz in \(H_C\).

This is likely the common-carrier theorem underlying the positive mesh construction. It uses additivity and positivity of elementary source charge, not merely positivity of a list of \(C_{ij}\).

## RH comparison boundary

The construction proves the intended implication inside kinematic positive geometry. It does not yet identify the arithmetic observations with these region charges:

\[
L(p_D^*p_E)
\stackrel{?}{=}
C(D\cap E).
\]

The completed endpoint--gamma--prime source is signed sectorwise, whereas the mesh carrier begins with positive elementary weights. Therefore a source map must explain how the coupled arithmetic formula becomes positive additive mesh charge before this carrier can prove the Weil gate.

The first missing comparison is now concrete:

\[
\boxed{
\mathcal I_{\mathrm{arith}\to\mathrm{mesh}}:
L(p_D^*p_E)
=
\sum_{\alpha\in D\cap E}c_\alpha,
\qquad c_\alpha>0.
}
\]

If this holds on a dense composite-primitive family and survives completion, universal rung-four positivity follows immediately.

## Verification

```text
python research/voevodsky/checkers/check_positive_mesh_charge_common_carrier.py
```

Artifacts:

- `research/voevodsky/checkers/check_positive_mesh_charge_common_carrier.py`
- `research/voevodsky/results/positive_mesh_charge_common_carrier.json`
