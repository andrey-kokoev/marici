# The two-prime conjugacy invariant is source-derived from the local Tate shell resolvent

## Local spectral coordinate

The local Tate observer has the exact operator realization

\[
Z_p(f,z)
=E_0(I-q_p(z)B)^{-1}\mathcal R_pf,
\qquad
q_p(z)=p^{-z}.
\]

Thus `q_p(z)` is not a fitted transfer coefficient. It is the Mellin character
multiplying the source-derived valuation-shell shift.

## Reciprocal doubling

The determinant-one reciprocal transport has eigenvalues

\[
q_p(z)^{-1/2},
\qquad
q_p(z)^{1/2}.
\]

Its projective conjugacy invariant can be written without choosing a square
root:

\[
\kappa_p(z)
=\left(q_p^{-1/2}+q_p^{1/2}\right)^2
=q_p+2+q_p^{-1}.
\]

Therefore

\[
\boxed{
\kappa_p(z)=p^{-z}+2+p^z
}
\]

is source-derived from the local shell resolvent together with reciprocal
sheet doubling.

Equivalently, it is the trace-square invariant of the companion transfer
matrix

\[
M_p(z)=
\begin{pmatrix}
q_p^{1/2}+q_p^{-1/2}&-1\\
1&0
\end{pmatrix},
\qquad
\det M_p=1.
\]

Only `kappa_p`, not a square-root branch, is needed.

## Reality test

Writing `z=x+iy`,

\[
\operatorname{Im}\kappa_p(z)
=-2\sinh(x\log p)\sin(y\log p),
\]

with the sign depending only on the `p^z` versus `p^{-z}` orientation. Its
zero set is unchanged. Reality at primes `2` and `3`, together with `y != 0`,
forces `x=0` by multiplicative independence of `2` and `3`.

## Updated comparison gate

The prime side of the proposed invariant comparison is now fully typed:

\[
(B,E_0,\mathcal R_p,q_p)
\longmapsto
\kappa_p=q_p+2+q_p^{-1}.
\]

The unresolved arrow is the already isolated discrete-to-continuous wall
intertwiner:

\[
\text{valuation-shell shift and endpoint}
\longrightarrow
\text{translated theta wall/history correspondence}.
\]

It must carry the reciprocal trace-square invariant to a real projective
canonical-form invariant at `p=2,3`. Scalar equality of one Weyl return is
insufficient; the comparison must preserve the doubled transfer relation or
the four polarized matrix units.

## Disposition

No full matrix identification with the amplituhedron carrier is required. The
minimal source theorem is preservation and reality of `kappa_2` and
`kappa_3` under the discrete-to-continuous quadratic comparison.