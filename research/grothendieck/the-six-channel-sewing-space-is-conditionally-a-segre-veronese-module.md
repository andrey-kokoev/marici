# The Six-Channel Sewing Space Is Conditionally a Segre--Veronese Module

## Proposed identification

Let `S` be the two-dimensional sector space and let `T` be the two-dimensional
control spinor. Strominger's endpoint theorem identifies the three-dimensional
Cartan generator space as

\[
H_1\cong\operatorname{Sym}^2T.
\]

The three paired channels proposed for completed sewing therefore have a
natural conditional factorization

\[
V\cong S\otimes H_1
\cong S\otimes\operatorname{Sym}^2T,
\qquad \dim V=2\cdot3=6.
\]

Projectively, decomposable source states form the Segre--Veronese surface

\[
\mathbb P(S)\times\nu_2(\mathbb P(T))\subset\mathbb P(V).
\]

This gives a precise meaning to the suggestion that the three pairs become a
six-channel object managed by the even Veronese algebra.

## Authorized linear maps

In a basis adapted to `S tensor H_1`, a linear sewing map that preserves both
factors has the form

\[
M=A\otimes B,
\]

where `A` acts on the sector pair and `B` acts on the three Cartan generators.
The Cartan quadric is

\[
q=x^2+y^2+z^2.
\]

For `B` to descend to an automorphism of the even Veronese algebra, it must
preserve the unique relation line:

\[
B^TB=\lambda I_3,
\qquad \lambda\ne0.
\]

Equivalently, `B` lies in the complex conformal orthogonal group. Its
projective action is the symmetric-square action of the control spinor group.

Thus a generic `6x6` matrix is not Veronese-managed. The authorized locus has
dimension seven before any additional metric or reality conditions: four
parameters for `A`, four for conformal-orthogonal `B`, minus one redundant
overall tensor scaling. This is far smaller than the 36-dimensional ambient
matrix space.

## Exact finite gate

Partition a candidate `6x6` matrix into four `3x3` blocks. It factors as
`A tensor B` exactly when all nonzero blocks span one line in the
nine-dimensional block space. After recovering `B`, compute `B^T B`.

The two acceptance gates are therefore:

1. block reshuffling has rank one;
2. `B^T B` is a nonzero scalar matrix.

The first tests the three-pair factorization. The second tests preservation of
Strominger's sole quadratic relation. If both pass, higher symmetric
compositions are governed by the even Veronese algebra and introduce no new
primitive syzygy generator.

## Relation to Aspect's completed sewing map

Aspect's requested six source basis functions and complex `6x6` forward and
reverse matrices now have a non-numerological candidate typing. The six basis
functions should be arranged as a sector pair over three Cartan directions,
not merely numbered from one to six.

The test must use the source Gram metric. In a nonorthonormal source basis,
ordinary transpose is replaced by the metric adjoint, and the quadric matrix
must be transported with the basis. A convenient Euclidean `6x6` Fourier
matrix does not acquire authority by passing the untyped version of this gate.

The forward and reverse maps should each pass the factor and relation tests.
Their two directional composites should then be checked in the same typed
module, followed by cutoff compatibility. This realizes the proposed
`3(2+1)+2+1` architecture without an unbounded coherence tower.

## Scope

This is a conditional structure theorem and preregistered test. We have not
proved that Aspect's unavailable source-derived finite matrices factor this
way, nor that the theta completed readout preserves the same module. The
coincidence of dimension six is evidence only after the source basis supplies
the tensor factorization and Cartan relation.

## Falsifiers

The proposal fails if any source-derived finite sewing matrix:

- has block-reshuffling rank greater than one;
- factors but its three-dimensional component does not preserve the quadric
  relation line;
- passes only after an unsourced change of basis;
- loses the factorization or relation under forward/reverse composition;
- or fails cutoff-compatible completion.
