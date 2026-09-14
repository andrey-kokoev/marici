# Mesh-charge positivity is exactly the zero-sum Weil sector

For an equally spaced stationary kernel, let

\[
G_{ij}=K((i-j)h)
\]

and let \(D\) be the adjacent-difference matrix. The discrete-wave mesh-charge matrix is

\[
\boxed{C=DGD^*.}
\]

Its entries are

\[
C_{ij}
=
2K((i-j)h)
-K((i-j+1)h)
-K((i-j-1)h).
\]

This is exactly the Gram matrix of primitive increments.

The image of \(D^*\) is the finite coefficient-zero-sum subspace. Consequently,

\[
C\succeq0
\]

at every rank is equivalent to Weil positivity on every equally spaced composite whose coefficients satisfy

\[
\sum_jc_j=0.
\]

Thus the primitive/primitive-square mesh observer provides a genuine and extensive positive sector: the complete zero-sum sector.

It does not control the total-mass direction. An exact equicorrelation fixture has positive mesh-charge matrix while its all-ones Weil value is negative. Hence

\[
C\succeq0
\not\Longrightarrow
G\succeq0.
\]

This matches the previously identified anchored-lift residual. A packet with nonzero total coefficient requires an endpoint/archimedean balancing channel before it enters the zero-sum order completion.

The revised RH programme is therefore:

1. realize the kinematic mesh charges as the source primitive-increment pairings;
2. prove their positive common-carrier realization on the zero-sum tower;
3. construct the coupled endpoint--gamma balancing packet for the one remaining mass direction;
4. prove the cross-incidence Schwarz square between that mass channel and the zero-sum sector.

The first two steps concern the forward coherence plane. The final mass/zero-sum incidence square is the remaining rung-four RH gate.

## Verification

```text
python research/voevodsky/checkers/check_mesh_charge_zero_sum_scope.py
```

Artifacts:

- `research/voevodsky/checkers/check_mesh_charge_zero_sum_scope.py`
- `research/voevodsky/results/mesh_charge_zero_sum_scope.json`
