# Noncommuting polarities obstruct positive Witt reduction of the absolute fold

## Proposed reduction

A proposed interpretation treated balanced excess in an absolute fold as a common positive diagonal face. Removing the maximal such face was expected to leave the Jordan legs of the signed difference.

This is valid for commuting positive Grams. It is false in general.

## Necessary common remainder

Let \(P,Q\succeq0\) be the two residual Grams and put

\[
D=P-Q.
\]

If one common positive form \(K\) could be removed so that the residuals became the Jordan legs, then necessarily

\[
P=D_++K,
\]

\[
Q=D_-+K.
\]

The common remainder is uniquely forced:

\[
K=P-D_+=Q-D_-.
\]

Equivalently,

\[
K=\frac{P+Q-|P-Q|}{2}.
\]

Thus positive diagonal reduction exists exactly when

\[
|P-Q|\preceq P+Q.
\]

This order inequality is not automatic for noncommuting positive operators.

## Two-dimensional hostile

Take

\[
P=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}.
\]

Let

\[
v=
\begin{pmatrix}
1/2\\
\sqrt3/2
\end{pmatrix},
\qquad
Q=vv^*.
\]

Then \(P\) and \(Q\) are rank-one projections and do not commute. The eigenvalues of

\[
D=P-Q
\]

are

\[
-\sqrt3/2,
\qquad
\sqrt3/2.
\]

Hence

\[
|D|=(\sqrt3/2)I.
\]

The forced common remainder is

\[
K=\frac{P+Q-(\sqrt3/2)I}{2}.
\]

Its eigenvalues are approximately

\[
-0.1830127,
\qquad
0.3169873.
\]

Therefore \(K\) is indefinite.

No common positive diagonal feature can be removed from this fold to produce the Jordan legs.

## Meaning for Witt reduction

The diagonal target subspace

\[
\{(z,z):z\in H\}
\]

is neutral for the Krein form. But quotienting a neutral target direction is not automatically induced by subtraction of a positive source Gram.

For a positive cell reduction, the neutral direction must be reached by the same source-labelled feature in both polarities. Noncommuting source Grams can prevent such a common positive factor from existing.

Thus abstract Krein-space Witt reduction and positive common-face removal are different operations.

## Consequence for the 210-cell lattice

Strict incidence coherence identifies face maps that are already present in two cells. It cannot manufacture a positive common face when the required source Gram is indefinite.

The full lattice can solve the minimalization problem only if its additional face equations imply the order condition

\[
|P_\alpha-Q_\alpha|
\preceq
P_\alpha+Q_\alpha
\]

for the physical residual pair at every coordinate, or an asymptotic version in the phase-energy topology.

Combinatorial commutativity alone does not imply this metric inequality.

## Correct finite gate

For each absolute fold, define

\[
K_\alpha
=
\frac{
R_\alpha^T+R_\alpha^0-
|R_\alpha^T-R_\alpha^0|
}{2}
\]

at Gram level.

The finite positive minimalization gate is

\[
K_\alpha\succeq0.
\]

If exact positivity fails, the asymptotic gate is control of the negative part:

\[
\|(K_\alpha)_-\|_{graph}\longrightarrow0
\]

in the topology used for completion.

Only after that estimate can the absolute fold be reduced to a positive approximation of the Jordan boundary.

## Verification

The executable hostile is

`research/voevodsky/checkers/check_noncommuting_absolute_fold_witt_obstruction.py`.

Its materialized output is

`research/voevodsky/results/noncommuting-absolute-fold-witt-obstruction-v1.json`.

The forced common remainder has one negative eigenvalue, so the checker rejects positive diagonal reduction.

## Disposition

Balanced excess is a hyperbolic diagonal face only when the corresponding source Gram is positive. Noncommuting polarized residuals can violate that condition.

The 210 analytic tetrahedra provide incidence coherence, but a separate metric theorem is required to prove positive Witt reduction or asymptotic disappearance of its negative obstruction.
