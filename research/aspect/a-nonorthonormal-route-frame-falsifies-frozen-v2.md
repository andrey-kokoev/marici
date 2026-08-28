# A nonorthonormal route frame falsifies frozen v2

## Target

Frozen v2 requires raw dagger unitarity of every matrix route associator and declares gauge covariance only under unitary route-basis changes. Its required associator fields do not include route-space Gram metrics.

This is not invariant under general invertible coordinate changes.

## Hostile packet

Start with the unused Ising local associator in an orthonormal frame:

\[
F_0=\frac1{\sqrt2}
\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad
F_0^*F_0=I.
\]

Change only the domain route coordinates by

\[
S=\begin{pmatrix}2&0\\0&1\end{pmatrix}.
\]

The same abstract cell is represented by

\[
F'=F_0S.
\]

The transported domain metric is

\[
G_L=S^*S=
\begin{pmatrix}4&0\\0&1\end{pmatrix},
\]

while the codomain metric remains \(G_R=I\).

Raw unitarity fails:

\[
F'^*F'\ne I.
\]

But the coordinate-invariant isometry law holds exactly:

\[
F'^*G_RF'=G_L.
\]

Nothing physical changed. Only the route frame ceased to be orthonormal.

## Decision

Frozen v2 rejects the same Ising associator that its local checker accepted. Therefore v2 is falsified.

The failure is not a missing exotic cell. It is a variance defect in the declared associator type: v2 stored a matrix without storing the metrics that define its dagger.

No patch is made to v2. Its immutable disposition is failed.

## Required future repair

A future v3 would need:

1. domain and codomain Gram metrics as required route-space data;
2. metric-relative dagger isometry \(F^*G_RF=G_L\);
3. covariance under general invertible route-frame changes;
4. positive-definiteness or an explicitly typed indefinite signature;
5. metric-compatible pentagon and hexagon comparisons;
6. uncertainty rules for experimentally reconstructed Gramians.

This repair is already motivated independently by theta optics, where the response Gramian—not a privileged orthonormal detector matrix—is invariant.

## Experimental transfer

WP896 exhibits the same law. A calibrated dimuon or tau response matrix cannot be copied to a new source by retaining numerical entries alone. Parent ancestry, parity, normalization, and their induced metric must travel through the adapter. Matrix resemblance without transported typing is not covariance.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_v2_nonorthonormal_route_frame_falsifier.py
```
