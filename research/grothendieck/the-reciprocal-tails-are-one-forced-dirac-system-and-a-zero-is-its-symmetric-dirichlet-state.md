# The Reciprocal Tails Are One Forced Dirac System and a Zero Is Its Symmetric Dirichlet State

## Parity rotation

For the reciprocal completed tails, define

\[
P=\frac{G_++G_-}{\sqrt2},
\qquad
Q=\frac{G_+-G_-}{\sqrt2}.
\]

The reciprocal tail equations rotate exactly to

\[
P'=-zQ-\sqrt2 f,
\qquad
Q'=-zP.
\]

Equivalently,

\[
\frac{d}{dq}
\begin{pmatrix}P\\Q\end{pmatrix}
=
-z
\begin{pmatrix}0&1\\1&0\end{pmatrix}
\begin{pmatrix}P\\Q\end{pmatrix}
-
\begin{pmatrix}\sqrt2 f\\0\end{pmatrix}.
\]

Thus the two reciprocal half-plane presentations are one forced rank-two
Dirac system. Their distinction is the diagonal basis of the exchange matrix;
the parity basis exposes the relational system itself.

## Zero as a Dirichlet state

The completed scalar readout is

\[
X(z)=G_+(0)+G_-(0)=\sqrt2 P(0).
\]

Therefore

\[
X(z)=0
\quad\Longleftrightarrow\quad
P(0)=0.
\]

Both tails decay at infinity, so `P` also obeys `P(infinity)=0`. Eliminating
`Q` gives the single forced boundary-value problem

\[
\left(-\partial_q^2+z^2\right)P
=
\sqrt2 f',
\qquad
P(0)=P(\infty)=0.
\]

This is a source-derived zero-to-state bridge. The differential system is
defined before the scalar zero; the zero selects its two-endpoint symmetric
domain.

## Geometry of the critical line

The coupling matrix is

\[
-z\sigma_x,
\qquad
\sigma_x=
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

When `Re z=0`, this coupling is skew-Hermitian. A nonzero real part adds a
Hermitian hyperbolic component. Hence the critical line is exactly the locus
where reciprocal exchange is norm-preserving in the native parity frame.

This explains why the line is canonical independently of the zero set. It
does not yet prove that the forced Dirichlet response can vanish only there.

## Location of the remaining current

The reciprocal bulk identity becomes

\[
2\Re(z)\left(\|P\|^2+\|Q\|^2\right)
=
-2\sqrt2\Re\langle f,Q\rangle.
\]

Thus all indefinite information lies in the forcing's coupling to the
antisymmetric channel. The symmetric Dirichlet condition cancels the seam but
does not control this orthogonal quadrature.

The second-order form expresses the same obstruction as the response of
`sqrt(2) f'` under the Dirichlet resolvent of `-partial_q^2+z^2`. This is more
primitive than the earlier cosine-band integral and gives an operator target:

> derive a theta-specific law preventing the Dirichlet response from having
> zero boundary value when the exchange coupling has a Hermitian component.

## Scope boundary

The inhomogeneous Dirichlet problem is solvable for many generic sources and
does not by itself imply zero confinement. Any positivity claim must use a
source law absent from hostile positive forcings. The current candidate is the
labelled dilation/prime-scale structure of `f'`, not self-adjointness of the
Dirichlet Laplacian alone.

## Result

Reciprocal doubling is exactly one forced Dirac system. A Riemann zero is a
two-endpoint Dirichlet state in its symmetric channel, while the unresolved
orientation is the forcing overlap with its antisymmetric channel. The
critical line is the unitary locus of the exchange coupling.

