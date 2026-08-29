# Ordinary paths are universal Euler boundary operators

Set

\[
H_a(x)=x^{-a-g}C_a^{(g)}(x),\qquad D=x\partial_x,
\qquad Q=q+2.
\]

The two canonical ordinary path columns factor as

\[
L_a=A_-H_a,
\qquad
R_a=-x^Q A_+H_a,
\]

where

\[
A_-=(1+x)(D+1-Q)-gx,
\]

\[
A_+=(1+x)(D+1+Q)-gx.
\]

The cancellation of \(a\) is exact: the Laurent weight contributes
\(D(x^{-a-g}C_a)=x^{-a-g}(D-a-g)C_a\), cancelling the depth appearing in
the original path coefficient.

The current becomes

\[
K_a=2(x^Q-1)(1+x)H_a.
\]

Since

\[
A_+-A_-=2Q(1+x),
\]

we obtain

\[
K_a=\frac{x^Q-1}{Q}(A_+-A_-)H_a.
\]

Thus the ordinary module imposes two universal Euler boundary observations,
while the current measures their finite-separation mismatch. All dependence
on pole depth and the source parameter \(\beta\) has moved into the source
orbit \(H_a\).

This separates the pending descent theorem into two independent ingredients:

1. source reflection and unipotent depth transfer for the orbit \(H_a\);
2. a source-independent quotient by \(A_-\) and \(x^Q A_+\).

The finite source window should follow by descending the reflected orbit
through this universal Euler quotient. The two-wedge Fitting factors should
then be properties of how the reflection fundamental interval meets the two
Euler boundary conditions.
## Flat-section factorization

The two Euler operators are rank-one covariant derivatives. Define

\[
u_-(x)=x^{Q-1}(1+x)^g,
\qquad
u_+(x)=x^{-Q-1}(1+x)^g.
\]

Then

\[
A_\pm=(1+x)(D-D\log u_\pm),
\]

so \(A_-u_-=0\) and \(A_+u_+=0\). These are the two tower directions as
flat sections of the boundary operators. Their relative gauge is

\[
\frac{u_-}{u_+}=x^{2Q}.
\]

The current obstruction therefore measures failure to sew two flat
trivializations with relative winding \(2Q\) across the reflected source
packet. Tower zero columns and exceptional current classes are no longer two
unrelated mechanisms: the former are flat sections, while the latter are
boundary obstructions between the two flat connections.
## Constant-mode falsifier

Each conjugated Euler derivative separately has one constant-mode cokernel
coordinate. It is tempting to identify the observed width-two quotient with
those two coordinates. That identification is false without a sewing map.
Exact tests show that ordinary columns from the opposite branch have nonzero
values in both naive constant-mode ports; the ordinary image already fills the
two local chart coordinates.

Thus the flat connections explain the local tower kernels but do not by
themselves construct invariant cokernel observations. A source-dependent
comparison cell must cancel the cross-branch contamination. The correct next
object is a sewn cocircuit annihilating both ordinary branch families, not the
direct sum of their separate integration constants.
