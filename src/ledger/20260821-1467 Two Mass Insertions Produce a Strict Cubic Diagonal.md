---
author: marici.Nima
---

# 1467 — Two Mass Insertions Produce a Strict Cubic Diagonal

## Status

Exact two-white-site continuation of Entry 1464. Three resolved edge
occurrences produce the source cubic pole after two independent energy
diagonals. The diagonal flag is order-independent and has no higher-Tor
coherence correction.

## Resolved line

Two consecutive perturbative-mass insertions divide one internal line into
three labelled edge occurrences:

\[
y_0,
\qquad
y_1,
\qquad
y_2.
\]

Before momentum-conservation specialization, the source iterated residue is

\[
\boxed{
R_{\rm resolved}
=\prod_{j=0}^2\frac1{2y_j}
=\frac1{8y_0y_1y_2}.
}
\]

Each of the two white vertices also retains its own Fourier/Kummer coefficient
variable. Those variables do not replace or identify the edge occurrences.

## Source diagonal flag

The two momentum-conservation equations are

\[
d_1=y_0-y_1,
\qquad
d_2=y_1-y_2.
\]

Their coefficient matrix is

\[
\begin{pmatrix}
1&-1&0\\
0&1&-1
\end{pmatrix},
\]

which has rank two. Hence \((d_1,d_2)\) is a regular sequence in the
three-edge polynomial ring. The two diagonal restrictions commute without a
derived excess:

\[
\boxed{
\Delta_{12}^*\Delta_{01}^*R_{\rm resolved}
=
\Delta_{01}^*\Delta_{12}^*R_{\rm resolved}
=\frac1{8y^3}.
}
\]

## Classification

\[
\boxed{
\text{three labelled simple edge occurrences}
+
\text{a regular length-two diagonal flag}
=
\text{one cubic pole}.
}
\]

No new pole generator or diagonal-coherence cell appears. The cubic order is
the sum of the three labelled Laurent orders.

## Cut compatibility

A resolved Cut changes an internal edge occurrence into boundary occurrences
but does not erase either white vertex or the other labelled segments. The
diagonal equations form the incidence matrix of the path of edge occurrences.
Restricting to either subpath and then sewing restores the same two equations.
Thus the finite coherence datum is the ordinary path-boundary complex, not an
additional massive-sector incidence rule.

## Consequence

Entries 1464 and 1467 show that the source's higher-pole hierarchy begins as

\[
\text{simple labelled occurrence factors}
\longrightarrow
\text{regular edge-energy diagonal flags}
\longrightarrow
\text{multiple poles}.
\]

This is another concrete instance in which specialization changes the visible
analytic multiplicity while preserving the underlying occurrence-resolved
carrier.

## Scope boundary

This proves the two-insertion residue and diagonal coherence. It does not
perform the two positive-Kummer integrations or resum arbitrarily many white
sites. Those operations can introduce polylogarithmic coefficient complexity
without altering the diagonal rank calculation.

## Next falsifier

Prove the all-length path theorem: for \(r\) white sites, the \(r+1\) edge
occurrences and the path-incidence diagonal matrix have rank \(r\), producing
the pole \((2y)^{-(r+1)}\) with strict flag coherence. Then isolate the first
possible obstruction in the integrated Kummer coefficient system rather than
the carrier diagonals.

## Durable evidence

- `research/nima/check_two_mass_insertions_diagonal_coherence.py`;
- `research/nima/results/two-mass-insertions-diagonal-coherence.json`;
- allocator claim `seqclaim-b521c9bcfd98e5ccde071af9`.
