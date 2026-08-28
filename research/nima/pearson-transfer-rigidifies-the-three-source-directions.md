# Pearson transfer rigidifies the three source directions

## Question

The full-dual carrier reduces the untyped six-port ambiguity to a common
permutation of three primal-dual pairs. Does the source itself remove that
residual \(S_3\)?

## Source roles

The finite Pearson carrier has three nonexchangeable coordinates:

1. the current tail value;
2. the delayed tail value;
3. the wall coordinate.

At degree \(j\), its transfer is

\[
M_j=
\begin{pmatrix}
A_j&-B_j&1\\
1&0&0\\
0&0&c
\end{pmatrix},
\qquad
A_j=j+\frac{19}{4},
\qquad
B_j=\frac32\left(j+\frac54\right).
\]

The full dual carries \(M_j\oplus M_j^{-T}\). A relabelling of the three
primal-dual pairs is source-admissible only if its permutation matrix \(P\)
commutes with every \(M_j\). The dual action is then forced.

## Exact finite result

Enumerating the six permutation matrices shows that already two consecutive
degrees have trivial simultaneous permutation centralizer:

\[
PM_0=M_0P,
\qquad
PM_1=M_1P
\quad\Longrightarrow\quad
P=I.
\]

The reason is structural. The wall is the unique coordinate with its own
one-dimensional propagation, the delayed tail is the unique coordinate fed
by the unit shift from the current tail, and the current tail is the unique
coordinate receiving all three incidences. These are source roles, not fitted
names.

## What this resolves

Once the Pearson transfer family is admitted, the ordered basis of \(V\) and
the contragredient basis of \(V^*\) are rigid against coordinate
permutations. Therefore the sixfold ambiguity left by the split evaluation
form is not a genuine gauge of the finite Pearson source.

This is stronger than choosing labels by matrix convenience: the ordering is
recovered as the unique permutation-compatible presentation of two distinct
source transfers.

## What it does not resolve

The result orders the six coordinates inside \(V\oplus V^*\). It does not
identify those coordinates with the separately typed primitive,
prime-square, seam, endpoint, connected-tail, and archimedean currents.

In particular, the six-dimensional Pearson carrier and the finite boundary
packet are not yet one object. The latter uses several inequivalent
topological grades and contains a five-component archimedean cell. A source
functor must still map the ordered Pearson roles into the boundary packet and
intertwine:

- the Pearson degree transfers;
- the contragredient transfers;
- the arithmetic incidence maps;
- reciprocal Fourier sewing;
- cutoff refinement.

Thus the current frontier is no longer basis selection. It is existence of an
intertwining source functor between two already rigidly typed constructions.

## DPC verdict

Resolved: the residual \(S_3\) coordinate ambiguity of the finite full-dual
Pearson carrier.

Unresolved: source incidence from that ordered carrier into the completed
arithmetic boundary packet.

Finite falsifier for any proposed residual coordinate gauge: a nonidentity
permutation fails to commute with \(M_0\), \(M_1\), or both.

## Verification

The checker `check_pearson_source_direction_rigidity.py` performs exact
rational matrix arithmetic and tests all six permutations against two
consecutive source transfers.

