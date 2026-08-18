---
id: 542
date: 2026-08-18
title: Even-Arity Framed Cut Descent Follows by Quadrangulation Induction
---

# Even-Arity Framed Cut Descent Follows by Quadrangulation Induction

Entries 537, 540, and 541 establish framed Cut rigidity at arities eight,
ten, and twelve.  Their common mechanism extends to every even arity in the
cellular fs/Kato sector.

## Combinatorial induction

Let (n=2m).  Physical Cuts are the non-boundary diagonals joining opposite
vertex parities.  There are

\[
m(m-2)
\]

such diagonals.  Each one divides the boundary into two paths of odd edge
length, so both resulting polygons have even numbers of vertices.  A
noncrossing family of (r) physical Cuts therefore decomposes the (n)-gon
into (r+1) strictly smaller even polygons.

If one region has more than four vertices, it contains another
opposite-parity diagonal internal to that region.  Hence the Cut family was
not maximal.  Conversely a quadrilateral has no further physical Cut.
Therefore maximal simplices are exactly quadrangulations, have

\[
r=m-2
\]

Cuts, and decompose the polygon into (m-1) four-point factors.

## Framed categorical induction

Assume framed physical lines and their Cut restriction maps are functorial and
rigid at all smaller even arities.  Every simplex of the (n)-point Cut nerve
then carries a product of pointed contractible lower-arity mapping spaces.
Its relative deformation and automorphism space is again contractible.

For (r) compatible restrictions, changing their order by
(sigmain S_r) contributes

\[
\operatorname{sgn}(sigma)
\]

from the Koszul rule.  The (r) native marked-normal Thom lines are odd, so
their determinant contributes the same character.  Thus

\[
\operatorname{sgn}(sigma)_{m Koszul},
\operatorname{sgn}(sigma)_{m Thom}=+1
\]

for every (r).  On a maximal simplex the remaining coefficient is the
product of (m-1) primitive four-point units, hence (+1).  The top physical
obstruction cochain is literally zero, not merely cohomologically trivial.

The unique local framed points therefore form a global coherent section, and
the diagram of relative deformation spaces is terminal.  Induction from the
four-point unit and the established six-point connector gives

\[
\boxed{\text{framed physical Cut descent exists and is rigid at every even
arity in the cellular fs/Kato sector}.}
\]

## Finite audit

The checker exhaustively verifies all strata through (n=14).  Its nerve
censuses are

\[
\begin{array}{c|l}
6&(3)\\
8&(8,12)\\
10&(15,55,55)\\
12&(24,156,364,273)\\
14&(35,350,1400,2380,1428).
\end{array}
\]

At (n=14), all (1428\cdot120=171360) orders of maximal five-Cut
restrictions pass.

The scope is essential.  The theorem uses the functorial external-product and
Cut-restriction structure already established in the cellular fs/Kato model.
It does not construct a raw global scheme-level six-functor correspondence,
identify a numerical amplitude, or prove that forgetting the logarithmic
framing preserves the class.

The remaining foundational frontier is therefore no longer higher-arity
cellular coherence.  It is comparison of this inductive fs/Kato object with a
raw algebraic normalization-sheet/log-DNC six-functor realization.

The executable audit is
`research/voevodsky/check_general_even_cut_induction.py`.
