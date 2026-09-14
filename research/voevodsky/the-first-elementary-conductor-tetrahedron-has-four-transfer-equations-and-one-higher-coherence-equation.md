# The first elementary conductor tetrahedron has four transfer equations and one higher-coherence equation

## Vertices

Use barycentric tetrahedral coordinates relative to `V_1,V_2,V_3,V_4`. Let

\[
A=(6,0,1,0)=C_{13,1},
\]

\[
B=(5,0,2,0)=C_{13,2},
\]

\[
C=(5,1,1,0)=I_{123;(5,1,1,0)},
\]

\[
D=(5,0,1,1)=I_{134;(5,0,1,1)}.
\]

Every pair differs by one elementary transfer, so these four nodes form an elementary tetrahedron.

## Edge maps

Write

\[
d_{ij}(\alpha):X_\alpha
\longrightarrow
X_{\alpha-e_i+e_j}
\]

for transfer of one unit from coordinate `i` to coordinate `j`.

The six edges are

\[
f_{AB}=d_{13}(A),
\qquad
f_{AC}=d_{12}(A),
\qquad
f_{AD}=d_{14}(A),
\]

\[
f_{BC}=d_{32}(B),
\qquad
f_{BD}=d_{34}(B),
\qquad
f_{CD}=d_{24}(C).
\]

## Four face equations

The face `ABC` compares transfer `1 -> 3 -> 2` with direct transfer `1 -> 2`:

\[
\boxed{
d_{32}(B)d_{13}(A)
=
d_{12}(A).}
\]

The face `ABD` compares `1 -> 3 -> 4` with `1 -> 4`:

\[
\boxed{
d_{34}(B)d_{13}(A)
=
d_{14}(A).}
\]

The face `ACD` compares `1 -> 2 -> 4` with `1 -> 4`:

\[
\boxed{
d_{24}(C)d_{12}(A)
=
d_{14}(A).}
\]

The base face `BCD` compares `3 -> 2 -> 4` with `3 -> 4`:

\[
\boxed{
d_{24}(C)d_{32}(B)
=
d_{34}(B).}
\]

These equations are schematic typed equalities: each occurrence of `d_ij` has the source object shown in parentheses, and its target determines the transported version of the next arrow.

## Weak commutativity

If the faces commute only up to specified homotopy, replace the equalities by two-cells

\[
H_{ABC}:
 d_{32}d_{13}
\Rightarrow d_{12},
\]

\[
H_{ABD}:
 d_{34}d_{13}
\Rightarrow d_{14},
\]

\[
H_{ACD}:
 d_{24}d_{12}
\Rightarrow d_{14},
\]

\[
H_{BCD}:
 d_{24}d_{32}
\Rightarrow d_{34}.
\]

## Tetrahedral coherence

There are two homotopies from the three-step route

\[
d_{24}d_{32}d_{13}
\]

to the direct arrow `d_14`.

The inner tetrahedral filler requires

\[
\boxed{
H_{ACD}
\circ
(d_{24}\ast H_{ABC})
=
H_{ABD}
\circ
(H_{BCD}\ast d_{13}).
}
\]

Here `ast` denotes whiskering of a face homotopy by the indicated edge map.

## Strict redundancy versus weak necessity

If all four face relations are literal equalities, the tetrahedral equation follows automatically from associativity of composition, and one face equation is algebraically redundant given the other three.

If the faces are specified equivalences or homotopies, the tetrahedral equation is additional data: the two proofs of commutativity must themselves agree.

## Polarity

For polarity `epsilon in {plus,minus}`, write

\[
d_{ij}^\epsilon,
\qquad
H_{XYZ}^\epsilon.
\]

The polarity involution must satisfy

\[
(d_{ij}^+)^\dagger
=d_{ji}^-,
\]

with source/target reversal, and carry the positive tetrahedral coherence equation to its negative counterpart.

## Disposition

The first elementary pyramid has exactly

\[
\boxed{
6\text{ edge maps},
\quad
4\text{ face homotopies},
\quad
1\text{ tetrahedral coherence equation}.
}
\]

Its two non-edge base vertices are face-interior nodes, not `C_12,2` and `C_14,2`.
