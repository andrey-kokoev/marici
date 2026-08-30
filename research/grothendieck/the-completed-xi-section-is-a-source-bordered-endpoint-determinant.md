# The completed xi section is a source-bordered endpoint determinant

Author: `marici.Grothendieck`

## Question

Can the exact two-endpoint dilation complex be coupled to the decaying theta
bulk through source-defined incidence maps so that its determinant is the
completed xi section?

## Source data

Write the completed Mellin transform as

\[
\Lambda(s)=H(s)+B(s),
\]

where

\[
H(s)
=
\frac12\int_1^\infty
(\vartheta(t)-1)
\left(t^{s/2}+t^{(1-s)/2}\right)
\frac{dt}{t}
\]

is entire and reciprocal-symmetric, and

\[
B(s)=-\frac1s+\frac1{s-1}=\frac1{s(s-1)}
\]

is the oriented two-endpoint packet.

On the endpoint basis \((e_0,e_1)=(1,t^{-1/2})\), the dilation operator and
incidence grading are

\[
D_s=
\begin{pmatrix}
s&0\\
0&s-1
\end{pmatrix},
\qquad
J_\partial=
\begin{pmatrix}
-1&0\\
0&1
\end{pmatrix}.
\]

Let

\[
u=
\begin{pmatrix}1\\1\end{pmatrix}.
\]

The bulk sees both endpoint monomials with the same coefficient, while the
return map carries their opposite boundary incidence. This gives the bordered
analytic family

\[
\mathcal M_s
=
\begin{pmatrix}
D_s&u\\
-u^TJ_\partial&H(s)
\end{pmatrix}
=
\begin{pmatrix}
s&0&1\\
0&s-1&1\\
1&-1&H(s)
\end{pmatrix}.
\]

## Exact Schur bridge

Away from the endpoint punctures, the Schur complement of \(D_s\) is

\[
H(s)+u^TJ_\partial D_s^{-1}u
=H(s)-\frac1s+\frac1{s-1}
=\Lambda(s).
\]

Therefore

\[
\det\mathcal M_s
=
\det(D_s)\Lambda(s)
=
s(s-1)\Lambda(s)
=
2\xi(s).
\]

Both sides are entire, so the identity extends across \(s=0,1\).

For a nontrivial zero \(s_0\), the kernel is explicit:

\[
\begin{pmatrix}
-1/s_0\\
-1/(s_0-1)\\
1
\end{pmatrix}
\in\ker\mathcal M_{s_0}.
\]

This is the first forward-derived zero-to-kernel bridge in the programme.

## Why the coupling is rigid

Let the outgoing endpoint vector be \(u_\alpha=\alpha(1,1)^T\) and the
oriented return vector be \(v_\beta=\beta(1,-1)\). Reciprocal reflection
forces the first vector into the symmetric endpoint line and the second into
the antisymmetric endpoint line. The bordered determinant becomes

\[
\det\mathcal M_s(\alpha,\beta)
=s(s-1)H(s)+\alpha\beta.
\]

The coefficient of the boundary packet in the split Mellin integral is one,
so source normalization forces

\[
\alpha\beta=1.
\]

The remaining transformation

\[
(\alpha,\beta)\longmapsto(r\alpha,r^{-1}\beta)
\]

is merely reciprocal rescaling of the two incidence ports. Thus the matrix
family is unique up to this presentation gauge.

## Reciprocal covariance is left-right, not conjugacy

Let \(P\) exchange the two endpoint basis vectors. With

\[
L=
\operatorname{diag}(-P,-1),
\qquad
R=
\operatorname{diag}(P,-1),
\]

one has

\[
\mathcal M_{1-s}=L\mathcal M_sR,
\qquad
\det L=\det R=1.
\]

The incoming and outgoing comparison maps are different. This is a concrete
instance of the multi-tower warning: reciprocal coherence is a two-sided
comparison cell, not necessarily a similarity of one operator.

## Hostile tests

- Replacing the return vector by a symmetric vector destroys the oriented
  endpoint packet.
- Rescaling only one incidence changes the constant term from one to
  \(\alpha\beta\).
- Adding a symmetric divisor-bearing multiplier requires changing the bulk
  entry or enlarging the source module; it is not a gauge transformation of
  this bordered family.
- Determinant agreement alone cannot authorize the coupling. Its symmetric
  and antisymmetric endpoint lines and their normalization must be derived
  from the theta split.

## Claim boundary

This is a canonical finite-dimensional analytic matrix family with

\[
\det\mathcal M_s=2\xi(s).
\]

It supplies an exact zero-to-kernel bridge. It is not a fixed self-adjoint
operator, a linear spectral pencil, a positivity theorem, or a proof that its
kernel can occur only on the critical line. The full RH burden has moved to
explaining why this source-derived non-self-adjoint analytic family is
invertible in both open half-planes.

## Disposition

The determinant bridge exists and is rigid up to reciprocal port gauge. The
next hostile audit is whether any source-derived metric makes
\(\mathcal M_{1/2+it}\) a boundary value of a definite or conservative
two-sided system. Failure would leave the bridge explanatory but without
zero-confinement force.
