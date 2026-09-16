# Correction: the Hardy defect realization is not the elementary conductor tetrahedron

## Audit of the proposed coordinate assignment

For a contraction \(M_\Theta\), define

\[
D_\Theta
=
(I-M_\Theta^*M_\Theta)^{1/2}.
\]

The canonical positive construction is the Stinespring column

\[
V=
\begin{pmatrix}
M_\Theta\\
D_\Theta
\end{pmatrix},
\qquad
V^*V=I.
\]

It gives the diagram

\[
\mathcal H_{\rm in}
\longrightarrow
\mathcal H_{\rm out}
\oplus
\mathcal H_{\rm def}.
\]

This is a span completed by an isometric dilation. It is not automatically a tetrahedron.

## Missing edge

The elementary conductor tetrahedron has an edge

\[
B\to C.
\]

Under the previously proposed interpretation, this would require an operator \(T\) satisfying

\[
T M_\Theta
=
D_\Theta.
\]

Such a factorization exists only if

\[
\ker M_\Theta
\subseteq
\ker D_\Theta
\]

and the induced quotient map is bounded.

Neither condition follows from contractivity. In fact, the scalar contraction

\[
m=0
\]

has defect

\[
d=1.
\]

No scalar \(T\) satisfies

\[
T m=d.
\]

Thus even a perfectly valid contraction need not supply the required tetrahedral edge.

## Exact checker

Checker:

`research/voevodsky/checkers/check_hardy_defect_is_not_a_full_tetrahedron.py`

Result:

`research/voevodsky/results/hardy-defect-not-full-tetrahedron.json`

The obstruction is exact.

## Correct geometry

The Hardy construction naturally forms a defect triangle or Stinespring square:

- incoming space;
- outgoing image under \(M_\Theta\);
- defect image under \(D_\Theta\);
- their orthogonal direct sum.

The conductor tetrahedron contains additional transfer data between the outgoing and defect vertices. That transfer is not supplied by the contraction identity

\[
M_\Theta^*M_\Theta
+
D_\Theta^*D_\Theta
=I.
\]

## Consequence

The lattice coordinates

\[
(6,0,1,0),
(5,0,2,0),
(5,1,1,0),
(5,0,1,1)
\]

cannot yet be assigned canonically to the Hardy incoming, outgoing, defect, and terminal spaces.

Doing so requires an additional bounded factorization or comparison map that realizes the missing \(B\to C\) edge and satisfies all four face equations.

## Disposition

The prior coordinate assignment was only an analogy and is rejected as a proved identification.

The Hardy defect operator remains the correct analytic positivity filler, but its natural incidence shape is not the established elementary conductor tetrahedron. A separate comparison theorem is required before the two geometries can be identified.
