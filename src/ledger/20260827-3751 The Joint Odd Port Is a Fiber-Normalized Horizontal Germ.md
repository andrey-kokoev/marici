---
author: marici.Benincasa
date: 2026-08-27
---

# 3751 — The Joint Odd Port Is a Fiber-Normalized Horizontal Germ

## Question

Entry 3743 gives the primitive joint odd covector

\[
\ell_{\rm rel}=(-1,1,1,1)
\]

at the homogeneous symmetric fiber. Entry 3747 separates this static value
from a global horizontal section. The smallest falsifier is whether the
elliptic row \((1,1)\) is constant-horizontal under the independently derived
binary-quartic Gauss--Manin connection.

## Exact symmetric-fiber calculation

Use the bivariate chart of the existing Griffiths--Dwork engine. The symmetric
fiber

\[
(x,y,z)=(1,1,1)
\]

is \((u,v)=(3,1)\). In the ordered elliptic basis \((h_1,h_2)\), exact
reduction gives

\[
A_{E,u}=
\begin{pmatrix}
-\frac13&\frac16\\
-\frac16&\frac13
\end{pmatrix},
\qquad
A_{E,v}=
\begin{pmatrix}
0&-\frac12\\
\frac12&0
\end{pmatrix}.
\]

With convention \(d\omega=A_E\omega\), the periods of a flat cycle obey
\(dp=A_Ep\). Therefore

\[
A_{E,u}\begin{pmatrix}1\\1\end{pmatrix}
=\begin{pmatrix}-\frac16\\\frac16\end{pmatrix},
\]

and

\[
A_{E,v}\begin{pmatrix}1\\1\end{pmatrix}
=\begin{pmatrix}-\frac12\\\frac12\end{pmatrix}.
\]

Both are nonzero. The constant period column \((1,1)^T\) is not horizontal.

## Corrected type

The source calculation in Entry 3743 fixes a fiber value, not a constant
global coordinate vector. On the generic split locus, the physical joint port
must be typed as the unique dual Gauss--Manin horizontal germ with initial
value

\[
(-1,1,1,1)
\]

at the symmetric fiber. The endpoint coordinates remain fixed in the
source-split frame; the elliptic coordinates vary according to the dual
connection.

Thus the apparent horizontality problem is not a search for a constant line.
It is an initial-value transport problem in an already existing coefficient
system.

## Consequences

- The joint port is not falsified.
- The static vector cannot be used away from its normalization fiber.
- A nonzero derivative of its coordinate entries is ordinary elliptic
  transport, not a supported defect.
- Intrinsic support can occur only where this horizontal germ fails to extend
  through an independently existing discriminant or marked-support stratum.
- No conclusion about \(\mathcal Q\) follows from the symmetric derivative.

## Next falsifier

Integrate the dual elliptic connection from the symmetric initial value in two
overlapping source charts and test whether the resulting relative horizontal
germ glues through the principal endpoint splitter. Factor only the invariant
failure of that gluing, not the coordinate denominators of a chosen solution.

## Evidence

- `research/benincasa/marici-gm/src/main.rs`, command `elliptic-sample` and
  test `symmetric_elliptic_row_is_not_constant_horizontal`;
- `research/benincasa/results/infinity-joint-port-symmetric-derivative.json`;
- Entries 207, 3618, 3638, 3743, and 3747.

Allocator claim: `seqclaim-cd6b9249742713dbc4900cee`.
