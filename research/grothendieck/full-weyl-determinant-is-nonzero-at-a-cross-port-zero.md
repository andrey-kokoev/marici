# The full Weyl determinant is nonzero at a cross-port zero

Author: marici.Grothendieck

Date: 2026-08-28

## Canonical two-port compression

Let \(A=A^*\), let \(R(z)=(A-z)^{-1}\), and retain the endpoint and source
ports as columns of

\[
B=(u,v),
\qquad u=\delta_0,
\qquad v=f,
\]

in an admissible rigged realization. The canonical matrix Weyl function is

\[
M(z)=B^*R(z)B
=
\begin{pmatrix}
u^*R(z)u&u^*R(z)v\\
v^*R(z)u&v^*R(z)v
\end{pmatrix}.
\]

The physical theta response is the cross entry

\[
X(z)=M_{12}(z)=u^*R(z)v.
\]

## Determinant at a cross zero

If \(X(z_0)=0\), then

\[
\det M(z_0)=M_{11}(z_0)M_{22}(z_0).
\]

For \(\operatorname{Im}z_0>0\) and any nonzero admitted port \(w\),

\[
\operatorname{Im}\langle w,R(z_0)w\rangle
=(\operatorname{Im}z_0)
\|R(z_0)w\|^2>0.
\]

Hence both diagonal entries are nonzero and

\[
\det M(z_0)\ne0.
\]

The same conclusion holds with the opposite sign convention in the lower
half-plane.

## Meaning

Strict Herglotz positivity does make the full Weyl matrix invertible off the
spectral axis. But the canonical full determinant does not inherit the
cross-response divisor. At every off-axis theta cross zero it is necessarily
nonzero.

Thus two attractive claims are mutually incompatible for the canonical
compression:

1. \(X\) is the source--observer cross response;
2. \(X\) is the determinant of the full passive boundary relation.

An additional source relation would have to change the boundary object, not
merely retain more passive ports.

## Remaining possibilities

The divisor bridge can survive only if theta geometry supplies one of:

- a boundary condition whose Evans determinant is \(X\) and whose
  self-adjointness is proved by a nonstandard Green form;
- a constrained Schur complement in which the diagonal responses cancel by
  an independently derived relation;
- a quotient or relative determinant that removes the diagonal same-port
  channels without discarding their boundary currents.

The last option now appears structurally closest to the programme: the
physical divisor is relative between two differently typed ports, while the
ordinary full determinant measures their complete passive Gram geometry.

