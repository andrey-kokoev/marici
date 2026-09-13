# The Green-energy lift places a boundary anomaly at the boundary

## Natural state metric

For Green packet coefficients \(u\), the function-space norm is

\[
\|u\|_K^2=u^TKu.
\]

The two terminal observations are the first and last Green Gram rows:

\[
A=
\begin{pmatrix}
K_{n-1,*}\\
K_{0,*}
\end{pmatrix}.
\]

Given boundary anomaly \(d=(d_R,d_L)\), minimize

\[
u^TKu
\]

subject to

\[
Au=d.
\]

## Endpoint-supported solution

Because

\[
K^{-1}A^T
\]

consists of the first and last coordinate vectors, the minimum-energy lift has support only at the two endpoints.

Set

\[
r=\rho^{n-1}.
\]

Then

\[
u_0=
\frac{d_L-rd_R}{1-r^2},
\]

\[
u_{n-1}=
\frac{d_R-rd_L}{1-r^2},
\]

and

\[
u_i=0
\qquad(0<i<n-1).
\]

## Orthogonal splitting

For every boundary-invisible interior packet \(h\in\ker A\),

\[
\langle u_*,h\rangle_K=0.
\]

Therefore

\[
\|u_*+h\|_K^2
=
\|u_*\|_K^2+
\|h\|_K^2.
\]

The Green geometry splits boundary anomaly from interior history exactly.

## Contrast with Euclidean allocation

Minimizing the coefficient norm \(\sum_i u_i^2\) gives the delocalized representer

\[
A^T(AA^T)^{-1}d,
\]

which spreads exponentially through the block.

Minimizing the actual Green function norm gives endpoint sources only. Thus “least-energy history” depends decisively on which carrier metric is treated as physical:

```text
Euclidean coefficient metric:
  distribute anomaly through the interior

Green function metric:
  place anomaly at the boundary
```

## Interpretation

Under the natural Green metric, a prescribed boundary discrepancy is not evidence for a bulk event. The minimal explanation is a boundary source. Bulk frustration appears only if additional constraints forbid endpoint support or impose a different energy geometry.

This is a useful model-selection principle: do not infer interior history from boundary anomaly before specifying the norm used to choose a lift.

## Verification

```text
python research/coherence/check_green_energy_boundary_lift.py
```

The checker verifies exact endpoint reconstruction, Green orthogonality, and Pythagorean minimality in 480 rational cases through seventeen events.

Artifacts:

- `check_green_energy_boundary_lift.py`
- `green-energy-boundary-lift.v1.json`
