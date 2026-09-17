# Oriented shedding realization interface

For a shedding flip pair `T,T'` with common ridge `R`, orient each facet by the canonical channel order. Let

\[
a=[T:R]\in\{\pm1\},\qquad b=[T':R]\in\{\pm1\}
\]

be the simplicial boundary incidences. On the pair module

\[
P_R=\operatorname{span}\{e_T,e_{T'}\}
\]

define the common-ridge realization

\[
p_R:P_R\to \mathbb R e_R,
\qquad p_R(xe_T+ye_{T'})=(ax+by)e_R.
\]

Its kernel is the one-dimensional relative line

\[
D_R=\ker p_R
=\mathbb R\,(b e_T-a e_{T'}).
\]

The orthogonal common line is

\[
C_R=\mathbb R\,(a e_T+b e_{T'}).
\]

Thus each shedding block has the canonical signed Hadamard decomposition

\[
P_R=C_R\oplus D_R,
\]

and the exact sequence

\[
0\longrightarrow D_R
\longrightarrow P_R
\xrightarrow{p_R}
\mathbb R e_R
\longrightarrow0.
\]

This identifies the relative difference intrinsically: it is not merely the formal subtraction of two facets, but the kernel of their common-ridge realization.

The simplicial relation `boundary squared = 0` makes these local sequences compatible on codimension-two faces. Triangles encode the resulting deletion/link cofiber relations. Tetrahedra compare the triangular reductions, and their stable images are the octahedral compatibilities of the eight-lattice model.

`check_oriented_shedding_relative_cycles.py` verifies the oriented cancellation through all maximum-degree shedding recursions at `n<=8`:

- 2,491 recursive states;
- 4,339 paired relative blocks;
- 3,245 blocks represented by an oriented difference in the fixed basis;
- 1,094 represented by an oriented sum because the two fixed facet orientations induce equal rather than opposite ridge signs;
- zero failures of common-ridge cancellation.

The sum/difference distinction is an orientation convention. Intrinsically every block has one common image line and one relative kernel line.

A realization into the Voevodsky common/difference carrier is now specified locally by a commutative square

\[
\begin{array}{ccc}
P_R & \longrightarrow & \operatorname{span}\{F_T,F_0\}\\
\downarrow p_R && \downarrow p_{common}\\
\mathbb R e_R & \longrightarrow & C,
\end{array}
\]

whose kernel map sends `D_R` to the analytical relative row `D`. Extending these local squares over all triangles and tetrahedra is exactly the simplicial realization-functor problem.
