# The low-grade initialization wedge has width-three collision cores

Set

\[
d=q-g>0.
\]

The adjacent stratum `d=1` overlaps the nominal odd depth-zero coordinate and
must be treated separately.  Endpoint peeling leaves rows `(1,0)` and columns
`((0,-),(2,+))`, with determinant

\[
\boxed{
-\frac{g(g+3)(2g-1)g!(g+3)!}{3}.
}
\]

It is nonzero for every integer `g>=2`.  All remaining columns peel at their
outer endpoints, so `q=g+1` has no exceptional initialization class.

Bounded Hall charts expose the following local collision coordinates.  They
depend only on the parity of `d`, but they are not, by themselves, a symbolic
reduction of the entire initialization block.

For even `d`, the residual rows and columns are

\[
(1,0),
\qquad
((0,-),(d,+)).
\]

Their determinant is

\[
\boxed{
\det C^{\mathrm{even}}_{g,d}
=(-1)^{g+1}g(d-g-8)
(4^{\overline g})(d^{\overline g}).
}
\]

The only zero is `d=g+8`, equivalently `q=2g+8`.  This is precisely the
preferred-chart divisor already repaired for every even grade by the symbolic
row-`3` transverse theorem.

For odd `d>=3`, the residual rows and columns are

\[
(1,2,0),
\qquad
((0,-),(d-1,+),(d+1,+)).
\]

All factorial prefactors are nonzero.  Rank loss is therefore controlled by
the single polynomial

\[
\begin{aligned}
P(g,d)={}&d^2g^2+d^2g-6d^2-dg^3-12dg^2-5dg+30d\\
&+5g^3+39g^2+12g-40.
\end{aligned}
\]

At grade two,

\[
P(2,d)=-36(d-5),
\]

so its zero is exactly

\[
(g,d)=(2,5),
\qquad
(g,q)=(2,7),
\]

the known primitive circuit `(1,-3,2)`.

The checker verifies the two symbolic determinants against all generated
local cores through grade 30 and excess 31.  An independent exact arithmetic
scan through `g=500`, odd `d=1001`, finds no other zero of `P`.

The local odd-core arithmetic for `d>=3` reduces to the explicit Diophantine lemma

\[
\boxed{
P(g,d)=0,quad g\ge2,quad d\ge3\text{ odd}
\Longrightarrow (g,d)=(2,5).
}
\]

The Diophantine statement is proved in
`magnetic-odd-core-diophantine.md`.  The global reduction is supplied by
`magnetic-plus-chain-triangular.md` and
`magnetic-plus-boundary-compatibility.md`: the growing aligned plus-chain is
triangular in a two-chart atlas, and its reconstruction support is disjoint
from its boundary-visible support.  Hence its Schur correction is identically
zero and the displayed local coordinates are the literal residual blocks.
Raw forced leaf peeling remains false, as recorded in
`magnetic-low-grade-reduction-falsifier.md`; the successful proof is oriented
elimination, not leaf peeling.
