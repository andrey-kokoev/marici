# Equal-entrance stabilizer quartic obstruction

## Source datum and maximal compatible symmetry

The canonical messenger grammar contains a nonzero equal-entrance vector on
the connector row space. After an orthogonal change of basis, write it as

\[
h=(1,0,0)^T.
\]

With canonical row kinetic normalization, the largest internal row symmetry
that preserves this fixed source datum is its (O(2)) stabilizer. Its connected
generator rotates the plane perpendicular to (h). The other two generators
of row (SO(3)) move (h), so full row (SO(3)) is not a symmetry of the
existing nonzero entrance vertex.

## Exact stabilizer census

Write the connector row Gram in the adapted basis as

\[
R=
\begin{pmatrix}
a&d&e\\
d&b&f\\
e&f&c
\end{pmatrix}.
\]

Solving the infinitesimal invariance equations and checking a transverse
reflection gives a five-dimensional (O(2))-invariant quartic space. One basis
is

\[
a^2,
\quad a(b+c),
\quad (b+c)^2,
\quad d^2+e^2,
\quad (b-c)^2+4f^2.
\]

The existing radial square and frame Frobenius form span only rank two inside
this space. The largest row symmetry compatible with the frozen entrance datum
therefore leaves three independent connector quartics missing.

## Hostile full-symmetry comparison

Full row (SO(3)) reduces the quartic space to the desired two invariants,

\[
(\operatorname{Tr}R)^2,
\qquad \operatorname{Tr}(R^2).
\]

But the same group has no nonzero invariant vector in the row triplet. It
therefore forbids the existing equal-entrance coupling rather than explaining
its two-coupling scalar truncation. Invoking full row symmetry would require a
new transforming source field or spurion and hence a new dynamical model whose
vacuum and readout must be derived independently.

## Disposition

WP498 closes the symmetry-only repair negatively. Merely enlarging the row
symmetry while preserving the current entrance source does not make the
connector action radiatively complete. The minimally enlarged existing theory
must run all five (O(2))-invariant connector quartics. The alternative is a
new full-row-symmetric theory with a dynamical entrance field; it cannot reuse
the present Hessian, poles, residues, or widths without recomputation.

The smallest exact falsifier is the dimension pair (5) versus (2): five
quartics are allowed by the maximal compatible stabilizer, while the current
action retains two.
