# Complete stabilizer-compatible connector Hessian

## Renormalizable source coordinates

Retain the canonical equal-entrance vector and therefore its maximal (O(2))
row stabilizer. In the adapted basis of WP498, write

\[
R=SS^T=
\begin{pmatrix}
a&d&e\\
d&b&f\\
e&f&c
\end{pmatrix},
\qquad t=b+c.
\]

The complete renormalizable connector potential built from (R) is

\[
V=u a+v t
+\lambda _1a^2+\lambda _2at+\lambda _3t^2
+\lambda _4(d^2+e^2)
+\lambda _5((b-c)^2+4f^2).
\]

This packet asserts local stability at the stated vacuum. It does not claim
that the displayed inequalities alone guarantee global boundedness on every
positive-semidefinite (R).

## Isotropic stationarity

At (S=sI_3), set (r=s^2>0). Exact stationarity fixes the two quadratic
coefficients as

\[
u=-2r(\lambda _1+\lambda _2),
\qquad
v=-r(\lambda _2+4\lambda _3).
\]

These are vacuum relations, not predictions of the dimensionless quartics.

## Physical connector Hessian

After separating the three antisymmetric right-(SO(3)_P) gauge tangents, the
six symmetric connector modes decompose under the entrance stabilizer into two
singlets, one vector doublet, and one traceless-tensor doublet. The singlet
mass-squared block is

\[
M_0^2=r
\begin{pmatrix}
8\lambda _1&4\sqrt2\lambda _2\\
4\sqrt2\lambda _2&16\lambda _3
\end{pmatrix}.
\]

The remaining masses are (m_V^2=4r\lambda _4), with multiplicity two, and
(m_T^2=16r\lambda _5), also with multiplicity two.

Strict local positivity of the six physical connector modes is equivalent to

\[
\lambda _1>0,
\qquad 4\lambda _1\lambda _3-\lambda _2^2>0,
\qquad \lambda _4>0,
\qquad \lambda _5>0.
\]

The three remaining zero modes are exactly the gauged antisymmetric frame
directions and do not mix with physical modes.

## Old spectrum as a hostile slice

The WP483 frame potential is recovered on the coefficient slice

\[
(\lambda _1,\lambda _2,\lambda _3,\lambda _4,\lambda _5)
=(\lambda,0,\lambda/2,2\lambda,\lambda/2).
\]

Only there do all six physical connector modes have the common value
(8\lambda s^2). WP498 shows that the full row symmetry protecting this slice
is incompatible with the frozen nonzero entrance vertex. The old degeneracy is
therefore not available as a source-authorized width input in the retained
messenger theory.

## Disposition

WP499 supplies the exact conditional connector pole coordinates for the
minimally completed source. It does not select any quartic, furnish a detector
instrument, or freeze widths. The next calculation must derive or independently
freeze the five couplings and their mixed-sector running before diagonalizing
the complete scalar system and recomputing residues and total widths.
