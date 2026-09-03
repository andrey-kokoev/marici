# Zero-side Hardy form is bounded but not positive

## Question

Does a stronger analytic polynomial topology make the unconditional complex-zero form closable even though the leading-measure GNS topology may not?

## Claim boundary

For every fixed positive \(t,h\), the paired complex-zero form is bounded on Hardy space \(H^2(\mathbb D)\). This gives an unconditional closed analytic realization. It does not make the form positive and does not construct a continuous comparison from the leading archimedean GNS space.

## Interior sampled zeros

For every nontrivial zero, define

\[
\lambda_\rho
=-\left(\rho-\frac12\right)^2
\]

and

\[
y_\rho=e^{-h\lambda_\rho}.
\]

The verified low-zero exclusion and critical strip give

\[
\operatorname{Re}\lambda_\rho>0.
\]

Therefore

\[
|y_\rho|<1.
\]

All sampled zero evaluations lie strictly inside the unit disk, even without RH.

## Hardy evaluation bound

For \(p\in H^2(\mathbb D)\), point evaluation obeys

\[
|p(y)|^2
\leq
\frac{
\lVert p\rVert_{H^2}^2
}{1-|y|^2}.
\]

This follows from the reproducing kernel

\[
K_y(z)=\frac1{1-\bar yz}
\]

with

\[
\lVert K_y\rVert_{H^2}^2
=
\frac1{1-|y|^2}.
\]

## Zero-side summability

The paired zero coefficient at fixed \(t,h\) has modulus bounded by a constant multiple of

\[
m_\rho e^{-t\operatorname{Re}\lambda_\rho}
\left(1+e^{-h\operatorname{Re}\lambda_\rho}ight).
\]

Since \(\operatorname{Re}\lambda_\rho\geq\delta>0\), the evaluation denominator satisfies

\[
1-|y_\rho|^2
\geq
1-e^{-2h\delta}>0.
\]

At large ordinate, the zero-count bound reduces the remaining sum to a Gaussian shell majorant of the form

\[
\sum_{k
\geq1}
k2^k e^{-ct4^k},
\]

which converges.

Thus the complex-zero quadratic form extends boundedly from polynomials to \(H^2(\mathbb D)\).

## Why this does not prove positivity

Off the critical line, sampled points occur at nonreal conjugate locations. The paired quadratic form is real on the appropriate real subspace but is not a sum of absolute squares. Boundedness and closability do not constrain its lower spectral edge to be nonnegative.

The Hardy realization proves that the zero-side form itself has no intrinsic closability defect at fixed \(t,h\). The issue is compatibility with the positive reference topology.

## Missing comparison map

Let \(\mathcal H_0\) be the leading archimedean GNS space. To transport Hardy closability back to the positivity problem, one needs a continuous map

\[
J:\mathcal H_0
\longrightarrow
H^2(\mathbb D)
\]

extending the identity on polynomials, or a closed graph relation with an explicitly controlled domain.

Such a map would require

\[
\lVert p\rVert_{H^2}
\leq
C_{t,h}
\lVert p\rVert_0.
\]

No such inequality is established. For moment measures supported on an interval, coefficient or Hardy norms are generally stronger than the corresponding \(L^2\) moment norm; endpoint-concentrating polynomials are hostile tests.

## Categorical interpretation

There are now two valid higher observers:

1. the leading-measure GNS observer, adapted to positivity;
2. the Hardy observer, adapted to complex interior evaluations and closability.

The missing object is a comparison morphism between them. Existence of each observer separately does not supply that arrow. Its failure would not refute RH, but it would block this route for transferring closedness into the positive reference geometry.

## Disposition

Unconditional zero-side closability can be obtained in a stronger analytic topology. The remaining question is no longer whether some closed realization exists, but whether the source-coupled form is semibounded in the leading positive topology or admits a controlled comparison from that topology to the Hardy realization.

## Verification

- `research/voevodsky/checkers/check_zero_side_hardy_form.py`
- `research/voevodsky/results/zero_side_hardy_form.json`
