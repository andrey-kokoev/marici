# No constant reciprocal form on the endpoint packet confines zeros

## Reciprocal endpoint representation

At a zero of the centered completed transform, the phase-space endpoint packet
has the form

\[
p(z)=
\begin{pmatrix}
F'(z)\\
-f(0)
\end{pmatrix}.
\]

Reciprocal symmetry makes \(F\) even and \(F'\) odd. Therefore

\[
p(-z)=Sp(z),
\qquad
S=
\begin{pmatrix}
-1&0\\
0&1
\end{pmatrix}.
\]

This is the exact two-dimensional reciprocal representation carried by the
local zero packet.

## Invariant forms

Let \(B\) be a constant bilinear form. Reciprocal invariance requires

\[
S^TBS=B.
\]

Writing \(B=(b_{ij})\), this condition forces

\[
b_{12}=b_{21}=0.
\]

Thus every invariant constant form is diagonal. Its value on the endpoint
packet depends only on quadratic combinations of \(F'(z)\) and \(f(0)\). The
same statement holds for constant Hermitian forms, with transpose replaced by
adjoint.

Every positive reciprocal-invariant form therefore erases the side
orientation. It can establish observability, but not distinguish the two open
half-planes.

## Anti-invariant forms

Reciprocal anti-invariance requires

\[
S^TBS=-B.
\]

This forces the diagonal entries to vanish. The remaining forms are
off-diagonal. Their nontrivial scalar evaluation is proportional to

\[
f(0)F'(z).
\]

For the canonical symplectic matrix

\[
J=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix},
\]

the reciprocal cross-pairing is

\[
p(z)^TJS,p(z)=-2f(0)F'(z),
\]

up to the chosen ordering convention. It measures the conormal/transversality
channel. It contains no factor depending on the horizontal displacement of
\(z\) from the critical seam.

## No-go theorem

No constant bilinear, Hermitian, symplectic, or Clifford-grade pairing on the
local endpoint packet can produce zero confinement from reciprocal symmetry
alone.

- invariant forms are orientation-blind;
- anti-invariant forms measure transversality but not location;
- every even hostile entire transform with off-seam zeros carries the same
  local representation and form classification.

The coefficient \(2\operatorname{Re}z\) required by a Sommerfeld identity
cannot come from endpoint geometry. It must arise from the spectral parameter
inside the dynamic generator and its Green current.

## Consequence

The local packet has now done all it can do. It faithfully lifts scalar
cancellation and records the first surviving normal jet. The RH-bearing
object must be a dynamic reciprocal conservation law on the full tail and
boundary-current fields. Replacing that law by a constant form on endpoint
coordinates is impossible.

## Falsifier

Any claimed endpoint-form proof must state its matrix \(B\) before using zero
locations. Apply the equations \(S^TBS=\pm B\). If the form is invariant, it
cannot retain side orientation. If it is anti-invariant, verify whether its
value contains anything beyond \(f(0)F'(z)\). A horizontal-displacement factor
inserted afterward is not source-derived.
