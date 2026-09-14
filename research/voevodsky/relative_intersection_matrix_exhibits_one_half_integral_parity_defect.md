# The relative intersection matrix exhibits one half-integral parity defect

## Question

Does the mined relative-cohomology source contain integral evidence relevant to the remaining two-primary conductor defect?

## Claim boundary

This computes the determinant and Smith form of the displayed intersection matrix in the source's chosen bases. The paper works over twisted cohomology and calls the matrix full rank; it does not assert that these bases define canonical integral lattices. The Smith calculation is therefore an arithmetic observation, not a physical or source-certified torsion class.

## Source matrix

`Cosmology meets cohomology`, equation (3.44), gives the intersection matrix between its dual relative basis and canonical-form basis:

\[
C=
\begin{pmatrix}
0&-1&1&0\\
1&0&0&0\\
1&1&0&1\\
-1&0&1&-1
\end{pmatrix}.
\]

The paper uses its full rank to identify the two cohomology bases over the coefficient field.

## Integral audit

Exact computation gives

\[
\det C=-2
\]

and Smith invariants

\[
(1,1,1,2).
\]

Thus the integer span of the displayed columns has index two in \(\mathbb Z^4\). The inverse is

\[
C^{-1}=
\begin{pmatrix}
0&1&0&0\\
-\tfrac12&0&\tfrac12&\tfrac12\\
\tfrac12&0&\tfrac12&\tfrac12\\
\tfrac12&-1&\tfrac12&-\tfrac12
\end{pmatrix}.
\]

Projection through the intersection pairing therefore introduces halves in three rows for generic integral coordinate vectors.

## Comparison with the completed Aspect target

The conductor comparison \(J\) has Smith invariants

\[
(1,2,2)
\]

and cokernel \((\mathbb Z/2)^2\). The relative worked example contains one index-two defect, whereas the conductor completion contains two independent index-two defects.

A speculative mechanism is that two independent relative boundary comparisons, each with a matrix of the displayed arithmetic type, could account for the two conductor parity directions. This is only a rank-and-prime match. The source provides one matrix in a different arrangement, not two maps into the conductor lattice.

## Strongest falsification attempt

The intersection matrix is an isomorphism over \(\mathbb C\), exactly as the source claims. Its index-two behavior depends on treating the displayed basis coordinates as integral. Twisted differential forms carry normalizations and coefficient parameters, so there is no automatic integral lattice. Rescaling one basis vector by two would change the Smith result while preserving the complex isomorphism.

Therefore the matrix does not verify the conductor torsion. It instead demonstrates concretely why a full-rank complex intersection pairing can conceal a parity normalization problem.

## Disposition

The source supplies a direct arithmetic analogue of one missing parity direction: a full-rank relative intersection matrix with half-integral inverse. Matching the conductor's two directions requires two source-derived integral relative pairings and fixed normalization conventions. Neither is yet constructed.
