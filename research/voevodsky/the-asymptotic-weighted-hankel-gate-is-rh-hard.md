# The asymptotic weighted-Hankel gate is RH-hard

This note records the logical status of Step 6; it is not an estimate for the
prime discrepancy.

Let `A` denote the conjunction of the already established analytic statements:

1. logarithmic IMS localization;
2. reduction of every threshold form to the universal edge form plus bulk;
3. range-compatible edge--bulk Schur absorption;
4. the normalized complement gap after finite co-defect extraction; and
5. the fixed-support form-core passage.

Let `C(N0)` say that every threshold below `N0` has a directed positive
certificate.  Let `D(N0)` say that the signed weighted Hankel discrepancy
satisfies, uniformly on all continuation slabs above `N0`, the strict bound
required in the conditional asymptotic-threshold theorem:

\[
 \|K_{N,\delta}\|+{b(\delta)^2\over\alpha}<a(\delta)
 \qquad(N\ge N_0).                                      \tag{1}
\]

## Proposition

Assuming the audited identification of the present quadratic form with the
classical Weil form, one has

\[
 A\land C(N_0)\land D(N_0)\quad\Longrightarrow\quad RH. \tag{2}
\]

### Proof

`D(N0)`, Schur absorption, and the complement gap prove positivity at every
threshold above `N0`.  `C(N0)` supplies all lower thresholds.  Threshold-free
continuation then gives positivity for every finite support.  The form-core
result gives positivity of the global Weil form without taking a limit of its
signed prime sum.  The Weil positivity criterion is equivalent to RH.  This
proves (2).  \(\square\)

Consequently an unconditional proof of (1), when combined with the finite
certification program, cannot be treated as a routine consequence of the
prime number theorem: it completes an RH proof.  In particular, replacing
(1) by a classical zero-free-region remainder does not merely lose numerical
sharpness.  After the `n^{-1/2}` weight that remainder has scale

\[
 \sqrt N\exp(-c\sqrt{\log N}),
\]

which is not absorbable by the available logarithmic edge coercivity.

## Allowed conclusions

The current work establishes a **conditional asymptotic threshold theorem**:
for any explicit directed `Phi` satisfying

\[
 \|K_{N,\delta}\|\le\Phi(N,\delta),\qquad
 \Phi(N,\delta)+b(\delta)^2/\alpha<a(\delta),
\]
all thresholds above the associated `N0` are positive.  It does not establish
an unconditional finite `N0`.

Thus Step 6 is the central theorem still missing.  Numerical continuation,
stronger quadrature, or further finite-rank regularization cannot close this
arithmetic implication.  A claimed completion must either prove a genuinely
new signed weighted-Hankel discrepancy theorem, assume an RH-strength input,
or explicitly remain conditional.
