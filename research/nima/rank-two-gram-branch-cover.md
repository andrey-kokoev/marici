# The Rank-Two Gram Locus Carries a Conditional Two-Sheeted Branch Cover

Gram degeneracy alone does not produce fourfold Kummer branching. On the
generic rank-two stratum there is a separate affine-consistency equation.

Choose coordinates in which

\[
a=(1,0,0),\qquad b=(0,1,0),\qquad c=(x,y,0).
\]

The first two bisector equations fix the planar part of the loop point to

\[
h=(1/2,1/2,0).
\]

The third equation is consistent precisely when

\[
\boxed{x^2+y^2-x-y=0.}
\]

This is the cocircularity condition for the four planar external points
\(0,a,b,c\). Thus the rank-two fourfold-support locus is not the whole Gram
divisor; it is the cocircular sublocus inside it.

Once this condition holds, the affine circumcenter locus is

\[
\ell=(1/2,1/2,z),
\]

and the remaining null equation is

\[
z^2+1/2=0.
\]

It therefore defines a generic two-sheeted complex cover of the consistent
rank-two locus. This is a different realization mechanism from the unique
zero-radius center on \(\det G\ne0\).

For a transverse fifth point \(p=(r,t,s)\), \(s\ne0\), its bisector equation
fixes

\[
z=\frac{r^2+t^2+s^2-r-t}{2s}.
\]

Substitution into the null equation gives the additional external support

\[
\boxed{
(r^2+t^2+s^2-r-t)^2+2s^2=0.
}
\]

Consequently the rank-two lane has the typed sequence

\[
\text{Gram degeneracy}
\to
\text{cocircular consistency}
\to
\text{two-sheeted fourfold cover}
\to
\text{fifth-point selection}.
\]

At meta level, the formal deck degree does not name a single geometric
stratum. The same degree-four symbol can be realized either by a unique-center
discriminant on the nondegenerate chart or by a two-sheeted affine-center
cover on the rank-two chart. Support geometry, not the Boolean label alone,
determines which coefficient object is present.

Artifacts:

- `research/nima/check_rank_two_gram_branch_cover.py`
- `research/nima/results/rank-two-gram-branch-cover.json`
