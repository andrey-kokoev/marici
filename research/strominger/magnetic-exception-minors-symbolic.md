# Both magnetic exception templates are grade-two boundary shortenings

The `q=1` exception comes from the reflected `a=0` pair.  On semantic rows
`1,2`, its all-grade block is

\[
\begin{pmatrix}
-g4^{\overline g}&-2\,4^{\overline g}\\
0&(g-2)4^{\overline g}
\end{pmatrix}.
\]

Its determinant is

\[
-g(g-2)(4^{\overline g})^2.
\]

For every `g>=3` this block has rank two.  At `g=2`, the second row vanishes
and the primitive circuit is `(1,-1)`, representing `1-zb^-2` up to orientation.

The second exception belongs to the alignment family

\[
q=g+5
\]

on columns `(a,s)=(0,-q),(4,+q),(6,+q)`.  The fixed rows `0,1,2` give a
three-by-three minor whose determinant simplifies to

\[
-4g(g-2)(g+5)
6^{\overline{g-1}}(4^{\overline g})^2.
\]

Again it is nonzero at every `g>=3`.  At grade two, `q=g+5=7`, the minor loses
one rank and its primitive kernel vector is

\[
(1,-3,2).
\]

The common mechanism is the factor `g-2`.  The `a=4` plus column acquires an
additional endpoint row with coefficient

\[
(g-2)(-1)^g4^{\overline g}.
\]

That row restores independence at every higher grade.  It disappears only at
grade two, allowing the shortened paths to form the exceptional circuits.

This proves that the two known collision geometries cannot continue to higher
grade.  It does not yet prove that no entirely different finite-initialization
geometry exists for unbounded `g,q`; that remaining statement is now purely an
interval-Hall classification of initial support blocks.
