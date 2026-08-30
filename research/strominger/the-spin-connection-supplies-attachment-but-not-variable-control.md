# The Spin Connection Supplies Attachment but Not Variable Control

## Question

If the spin connection is not an actuator, what legitimate role does it play
in the degree-four selector geometry?

## Fixed reference connection

Let \(\omega_{LC}\) be the oriented Levi-Civita connection on the celestial
tangent-frame bundle. The spin-two polarization bundle inherits

\[
A_0=2\omega_{LC}.
\]

Under a frame rotation by \(\phi\), the polarization angle changes by
\(\alpha=2\phi\), and

\[
A_0\mapsto A_0-d\alpha.
\]

This is a genuine connection on the nontrivial polarization bundle. Its
curvature satisfies

\[
\int_{S^2}F_{A_0}=8\pi,
\]

corresponding to degree four. Thus the spin connection supplies the global
chart attachment and topological curvature that the composite phase
connection lacks.

## Fixed attachment versus variable control

Every other connection on the same polarization bundle has the form

\[
A=A_0+b,

\]

where \(b\) is a globally defined one-form. Relative to the composite phase
connection,

\[
A-A_C=(A_0-A_C)+b.
\]

The first term is a fixed, gauge-invariant attachment field. It carries the
forced compensation at polarization zeros. The second term is the only
variable control degree.

Because \(S^2\) is closed,

\[
\int_{S^2}d b=0.
\]

Variable control can redistribute curvature but cannot change the degree-four
topological charge.

## Reconciliation

The spin connection has two legitimate roles:

1. presentation covariance;
2. fixed bundle attachment and curvature.

It still has no role as an independently selectable actuator. Setting \(b=0\)
leaves only the fixed geometric reference. Active local control requires a
source-authorized nonzero \(b\).

This also sharpens Aspect's overdrive transfer. Passive completion may provide
the fixed reference and its ancillary ports, but it cannot change the forced
generator-state balance. That change belongs to the variable relative field.

## Disposition

The topological attachment is not missing: the weight-two Levi-Civita
connection supplies it. The sole missing physical constructor is now the
global relative one-form \(b\), together with a law connecting it to
gravitational source or control data.

## Verification

```powershell
uv run --with sympy python research/strominger/checkers/reference_connection_relative_control_checks.py
```
