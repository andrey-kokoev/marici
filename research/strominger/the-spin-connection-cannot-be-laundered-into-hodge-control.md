# The Spin Connection Cannot Be Laundered into Hodge Control

## Question

Does the ordinary celestial Levi-Civita spin connection already provide the
connection required for a locally varying Hodge angle?

## Coordinate coincidence

For a real symmetric trace-free tensor

\[
C=\begin{pmatrix}a&b\\b&-a\end{pmatrix},
\qquad
J C=\epsilon C,
\]

a passive oriented-frame rotation by \(\phi\) changes its component matrix by

\[
C\mapsto Q(\phi)^T C Q(\phi)
=\cos(2\phi)C-\sin(2\phi)JC.
\]

Thus spin-two frame covariance uses the same matrix generator as a Hodge
rotation, with doubled angle and a convention-dependent sign.

## Authority separation

The coincidence is representational, not operational. Under a passive frame
rotation, the component variation is cancelled by the basis variation. The
geometric tensor is unchanged. Under an active Hodge rotation the frame is
held fixed and the geometric tensor changes generically.

Therefore the Levi-Civita spin connection supplies the compensation required
for changes of presentation. It does not supply an actuator for active local
Hodge rotation. Using it as the \(A\) of Entry 3789 would convert gauge
covariance into physical control authority.

## Falsifier

At

\[
C=\begin{pmatrix}2&3\\3&-2\end{pmatrix},
\]

the active infinitesimal Hodge change is nonzero, while the full passive
component-plus-basis change is zero. Hence the two transformations cannot be
identified as maps of geometric states.

## Disposition

The existing spin connection closes presentation covariance only. Local
physical Hodge selection still requires an independent active duality
connection or a source theorem identifying one. The similarity of their
component formulas is precisely the laundering hazard.

## Verification

```powershell
uv run --with sympy python research/strominger/checkers/spin_connection_hodge_control_no_laundering_checks.py
```
