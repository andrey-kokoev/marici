# The conductor parity defect factors into two site-exchanged relative-type steps

## Question

Can the conductor's two independent index-two defects be separated into elementary factors of the same arithmetic type as the mined relative intersection matrix?

## Claim boundary

This is an exact factorization in integral linear algebra. “Relative-type” means equality of Smith invariants after stabilization, not a source-derived identification of complexes or pairings.

## Elementary factors

The conductor intertwiner is

\[
J=
\begin{pmatrix}
2&0&1\\
0&2&1\\
0&0&1
\end{pmatrix}.
\]

Define

\[
J_1=
\begin{pmatrix}
2&0&1\\
0&1&0\\
0&0&1
\end{pmatrix},
\qquad
J_2=
\begin{pmatrix}
1&0&0\\
0&2&1\\
0&0&1
\end{pmatrix}.
\]

Then

\[
J=J_1J_2=J_2J_1.
\]

Each factor has determinant two and Smith invariants

\[
(1,1,2).
\]

Its cokernel is one copy of \(\mathbb Z/2\). Their commuting product has Smith invariants \((1,2,2)\) and cokernel \((\mathbb Z/2)^2\).

## Site exchange

Let

\[
S=
\begin{pmatrix}
0&1&0\\
1&0&0\\
0&0&1
\end{pmatrix}
\]

exchange the two conductor wall coordinates. Then

\[
SJ_1S=J_2,
\qquad
SJ_2S=J_1,
\qquad
SJS=J.
\]

Thus the two elementary parity defects are exchanged by site symmetry, while their product is invariant.

## Comparison with the mined relative matrix

The source relative intersection matrix \(C\) has Smith invariants

\[
(1,1,1,2).
\]

After adjoining one identity direction, each \(J_i\) has the same invariants:

\[
\operatorname{Smith}(J_i\oplus[1])=(1,1,1,2).
\]

Consequently each conductor step is integrally equivalent, as an unlabelled lattice map, to the arithmetic defect of the displayed relative intersection matrix. Two commuting, site-exchanged copies reproduce the full conductor defect.

## What this does not construct

Smith equivalence forgets basis labels, differential-form degrees, support, residues, connection, and orientation. It supplies no canonical unimodular matrices identifying \(C\) with either stabilized \(J_i\), and no source says that two copies of the relative example occur in the conductor geometry.

## Bold conjecture

The conductor comparison may factor geometrically through two normalized relative-boundary pairings, one for each wall, exchanged by site symmetry. Each pairing contributes one half-integral normalization, and their commuting composition gives \(J\).

A valid realization must construct two labelled relative complexes, integral intersection lattices, comparison maps equal to \(J_1,J_2\) up to source-authorized bases, compatible Gauss–Manin connections, and the site-exchange isomorphism between them.

## Disposition

The arithmetic two-copy mechanism is exact and site-symmetric. Its geometric and physical realization remains absent.
