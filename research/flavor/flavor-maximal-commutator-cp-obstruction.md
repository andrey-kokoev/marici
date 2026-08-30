# Maximal-commutator CP obstruction

## Question

WP973 tests the smallest coefficient-free two-object source interaction left by
WP972. Let two Hermitian coefficient fields \(X,Y\) have source-fixed positive
Frobenius radii. Does a negative commutator-square potential select a
CP-capable relative vacuum?

The admitted operation is simultaneous source \(SO(3)\) conjugation. The
faithful readout is the full weak-basis physical16 quotient. No fitted flavor
coordinate enters the source action.

## Exact obstruction

In a basis diagonalizing \(X\),

\[
\lVert[X,Y]\rVert_F^2
=\sum_{i,j}(x_i-x_j)^2|Y_{ij}|^2
\le 2\lVert X\rVert_F^2\lVert Y\rVert_F^2.
\]

Equality requires the support relevant to the commutator to concentrate on one
eigenvalue pair with opposite eigenvalues. The maximizing commutator therefore
acts on an embedded two-dimensional block and has rank at most two. For three
families,

\[
\det[X,Y]=0,\qquad \operatorname{tr}[X,Y]^3=0.
\]

Thus the coefficient-free interaction
\(-q\lVert[X,Y]\rVert_F^2\), completed by positive radial terms, can select a
noncommuting vacuum but cannot select a CP-capable three-family vacuum.

## Exact equality witness

\[
X=\operatorname{diag}(1,-1,0),\qquad
Y=\begin{pmatrix}0&1&0\\1&0&0\\0&0&0\end{pmatrix}.
\]

Both squared norms equal two. The commutator norm squared is eight, saturating
the bound, while its determinant and cubic vanish.

## Classification

The negative commutator square is a noncommutativity selector and a
presentation rigidifier, but not a physical CP selector. This repeats the
embedded-Pauli structure seen at WP438 in the coefficient-field setting.

The smallest reopening is an independently justified invariant that prevents
two-level concentration and makes the commutator full rank. A fitted target
determinant, oriented tensor, or declared relative matrix is not admissible.

## Reproduction

Run:

    python research/flavor/checkers/wp973_maximal_commutator_cp_obstruction.py

The generated result is
research/flavor/results/wp973_maximal_commutator_cp_obstruction.json.
