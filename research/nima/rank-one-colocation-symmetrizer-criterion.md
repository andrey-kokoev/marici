# Rank-one colocation symmetrizer criterion

Let `H` be a complex Hilbert space and let nonzero vectors `b,c in H` represent one input column and its desired output covector under Riesz identification. There exists a bounded self-adjoint invertible operator `J` satisfying

$$
Jb=c
$$

if and only if

$$
\langle c,b\rangle\in\mathbb R.
$$

## Necessity

If `J=J*`, then

$$
\langle c,b\rangle
=\langle Jb,b\rangle
\in\mathbb R.
$$

## Sufficiency

Work on the at-most-two-dimensional space `M=span{b,c}`. After normalizing `b`, write

$$
c=\alpha b+d,
\qquad d\perp b.
$$

The hypothesis says `alpha` is real. If `d` is nonzero, choose the Hermitian matrix on `span{b,d}` whose first column is the coordinate vector of `c` and choose its remaining real diagonal entry away from the single value that makes the determinant zero. If `d=0`, use multiplication by the nonzero real scalar `alpha` on `span{b}`. Extend by any nonzero real scalar on `M^perp`. The resulting operator is bounded, self-adjoint, invertible, and maps `b` to `c`.

Thus the six-row Green equation

$$
G_{\rm src}B_G=C_G^*
$$

has no rank-one Hermitian obstruction precisely when

$$
\langle C_G^*,B_G\rangle\in\mathbb R
$$

and the output column is nonzero. This criterion does not impose the source block decomposition or generator equation

$$
A^*G_{\rm src}=G_{\rm src}A.
$$

Those are the substantive remaining constraints.

For a positive symmetrizer, necessity strengthens to

$$
\langle c,b\rangle>0.
$$

Positivity also imposes quantitative bounds relating the component of `c` orthogonal to `b` to the chosen positive extension.

Status: abstract rank-one colocation existence reduced to one scalar reality test; source-block and generator compatibility remain open.
