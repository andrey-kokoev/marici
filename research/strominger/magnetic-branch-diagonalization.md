# The reflected magnetic branches diagonalize before elimination

The quadratic magnetic numerator is affine in the reflected branch parameter
`s`.  Its branch coefficient factors completely:

\[
\frac{\partial N_{a,s}}{\partial s}
=(1+x)(1+t)(1-xt).
\]

Therefore

\[
N_{a,+q}-N_{a,-q}
=2q(1+x)(1+t)(1-xt).
\]

The magnetic generating function contains the base factor

\[
(1+t)^{-a-1}(1-xt)^{a-5}.
\]

The two extra linear factors cancel its shifted denominators, leaving exactly
the source generating function.  Grade by grade,

\[
\boxed{
B_{g,a,+q}(x)-B_{g,a,-q}(x)
=2q(1+x)C_{g,a}(x).
}
\]

Likewise,

\[
B_{g,a,+q}(x)+B_{g,a,-q}(x)=2B_{g,a,0}(x).
\]

Thus the natural branch coordinates are the neutral magnetic response and the
untransported source path.  The change of branch basis has exterior character
`-2q`, so it is invertible precisely for `q>0` and degenerates exactly at the
reflection-fixed tower `q=0`.

This explains the first factor in the kernel classification without a Hall
matrix:

\[
q=0
\quad\Longleftrightarrow\quad
\text{the two reflected branches coincide and antisymmetrization vanishes}.
\]

For `q>0`, all residual `q`-dependence comes from the relative translation of
the two path supports when they are embedded into the common target lattice.
It does not come from the local path weights themselves.  Consequently the
remaining exterior-character calculation can be separated into:

1. a universal local branch factor `2q`;
2. a translation-overlap determinant depending on the parity and size of `q`.

The checker proves these identities symbolically at all grades, with formal
coefficient audits through grade 30.
