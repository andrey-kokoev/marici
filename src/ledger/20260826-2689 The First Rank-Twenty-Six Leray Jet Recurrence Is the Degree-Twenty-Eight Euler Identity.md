# 2689 — The First Rank-Twenty-Six Leray Jet Recurrence Is the Degree-Twenty-Eight Euler Identity

## Frozen test

Entry 2683's primitive source-word basis retains the depth-zero roots

\[
S,\qquad D_0,\qquad D_1,
\]

but not the third source derivative \(D_2\). Express \(D_2\) uniquely in the 26-word basis at the reference point and two independent controls, without selecting a reduced representative as a source form.

## Result

At every point, only the first three coefficients are nonzero. They agree exactly with

\[
D_2
=
\frac{28}{P_3^2}S
-
\frac{P_1^2}{P_3^2}D_0
-
\frac{P_2^2}{P_3^2}D_1.
\]

Equivalently,

\[
P_1^2D_0+P_2^2D_1+P_3^2D_2=28S.
\]

The formula was declared after the first coefficient census and then independently rerun against all three rebuilt presentations. It passed exactly.

## Interpretation

The first omitted physical jet is controlled by source homogeneity, not by a long fitted 26-term recurrence. For any dual readout, including the physical Leray covector,

\[
P_1^2\ell(D_0)+P_2^2\ell(D_1)+P_3^2\ell(D_2)=28\ell(S).
\]

This supplies the first exact compatibility equation for characteristic-zero source-period evaluation. It does not compute any period value and does not prove that all higher modular recurrences lift.

## Artifacts

- `research/benincasa/check_rank26_third_source_derivative_recurrence.py`
- `research/benincasa/rank26-third-source-derivative-recurrence.json`
- `research/benincasa/rank26-source-word-basis.json`

## Next falsifier

Derive the degree-twenty-eight homogeneity directly from the unspecialized source integrand, including measure and regulator weights. Then test the first depth-one omitted word against the corresponding differentiated Euler identity. A mismatch would show that the finite-field quotient recurrence does not lift to the physical period system.
