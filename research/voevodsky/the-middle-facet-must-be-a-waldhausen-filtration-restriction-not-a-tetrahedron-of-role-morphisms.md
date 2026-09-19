# The middle facet must be a Waldhausen filtration restriction, not a tetrahedron of role morphisms

Fresh inspection of the established analytic target changes the typing of the
edge audit.  In `S_4(C_cl)`, the five simplex vertices index stages of a
filtration; an edge is not merely a morphism between two role objects.  It is
an interval cone package

\[
X_{ij},\qquad 0\le i<j\le4,
\]

and every triple carries a cofiber triangle

\[
X_{ij}\longrightarrow X_{ik}\longrightarrow X_{jk}.
\]

For the middle facet `d_2`, whose retained filtration indices are
`0,1,3,4` and whose role mnemonic is `[S,A,C,G]`, the six edge objects are

\[
X_{01}=X_{SA},\quad X_{03}=X_{SC},\quad X_{04}=X_{SG},
\quad X_{13}=X_{AC},\quad X_{14}=X_{AG},\quad X_{34}=X_{CG}.
\]

The facet requires exactly four cofiber triangles:

\[
X_{SA}\to X_{SC}\to X_{AC},
\]

\[
X_{SA}\to X_{SG}\to X_{AG},
\]

\[
X_{SC}\to X_{SG}\to X_{CG},
\]

\[
X_{AC}\to X_{AG}\to X_{CG}.
\]

These are the four faces `SAC`, `SAG`, `SCG`, and `ACG`.  Their compatibility
is the degree-three octahedral condition.

The reciprocal duality acts on intervals by

\[
\mathbb D(X_{ij})=X_{4-j,4-i}^{\vee}.
\]

It therefore pairs

\[
X_{SA}\leftrightarrow X_{CG},\qquad
X_{SC}\leftrightarrow X_{AG},
\]

and fixes

\[
X_{SG},\qquad X_{AC}
\]

up to duality.  This recovers the earlier orbit calculation, now with the
correct Waldhausen meaning.

The prior six-edge audit remains useful as an inventory of candidate analytic
content, but calling those entries six morphisms was too weakly typed.  Each
must be promoted to a closed interval cone package, and the arrows that matter
are the twelve maps occurring in the four cofiber triangles.

This formulation isolates the first construction target: the absent `CG`
package cannot be supplied as a scalar cofactor-to-Green equality.  It must be
the common cofiber of both maps

\[
X_{SC}\to X_{SG}
\quad\text{and}\quad
X_{AC}\to X_{AG},
\]

with a source-derived equivalence between the two cofibers.  That equivalence
is the octahedral form of the missing determinant--Green mate.
