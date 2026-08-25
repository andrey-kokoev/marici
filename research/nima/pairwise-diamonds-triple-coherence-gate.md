# Pairwise diamonds do not imply triple coherence

## Problem

A constructor compiler may fill every pairwise critical diamond while still
failing on triple overlaps. Pairwise comparison cells are one-dimensional
coherence data. Their compatibility is a separate higher cell.

Let three local presentations live on charts \(p,q,r\). Suppose pairwise
comparison data

\[
H^{pq},\qquad H^{qr},\qquad H^{pr}
\]

exist. On the triple overlap, their Cech defect is

\[
\delta H
=H^{qr}-H^{pr}+H^{pq}
\]

with signs interpreted in the relevant coefficient system.

Pairwise coherence closes only when this defect vanishes or is killed by a
source-authorized triple cell \(K^{pqr}\) through the total differential.

## Smallest finite witness

Over \(\mathbb F_2\), take

\[
H^{pq}=1,\qquad H^{qr}=0,\qquad H^{pr}=0.
\]

Every pairwise cell is present, but

\[
\delta H=1.
\]

Thus all pairwise compiler checks can pass while the triple presentation is
incoherent.

Adding

\[
K^{pqr}=1
\]

with total boundary \(\delta H+K=0\) fills the triple defect. The new cell is
not optional metadata: deleting it changes the total cocycle from closed to
open.

## Benincasa instance

For each ordered second label \(ij\), Benincasa's chartwise products
\(A_{ij}^p\) glue through pairwise cells

\[
H_{ij}^{pq}
=h_i^{pq}D_j^p+D_i^q h_j^{pq}.
\]

Their triple defect is killed canonically by

\[
K_{ij}^{pqr}=h_i^{qr}h_j^{pq}.
\]

Across three charts the verified tower contains eighteen pairwise \(H\)
cells and six triple \(K\) cells. The second-normal object is therefore a
Cech/de Rham total cocycle, not a flat collection of chartwise products.

Any direct-image reducer must consume the typed triple

\[
(A,H,K).
\]

Feeding only \(A\), or \(A,H\) without \(K\), into an ordinary reducer erases
source-support coherence and can manufacture rank or pivot independence.

## Constructor-tree interpretation

Pairwise critical-pair joinability provides comparison cells between two
factorizations. With three or more overlapping factorizations, the
comparison cells themselves form constructor data. A triple cell witnesses
that the two composites of pairwise comparisons agree.

Therefore the compiler hierarchy begins:

\[
\begin{aligned}
\text{nodes}&:\text{constructors},\\
\text{edges}&:\text{rewrites/comparisons},\\
\text{2-cells}&:\text{pairwise diamond fillings},\\
\text{3-cells}&:\text{compatibility of fillings on triple overlaps}.
\end{aligned}
\]

The naming dimension may shift by convention; the invariant content is that
coherence cells themselves require coherence.

## Finite gate

For each triple overlap:

1. enumerate the three pairwise comparison cells;
2. compose them around the boundary;
3. compute the typed defect \(\delta H\);
4. accept only if it vanishes or a named source-authorized \(K\) kills it;
5. accumulate the support and resource contract of \(K\);
6. reject deletion or substitution of \(K\).

The rejection witness is

\[
\texttt{triple\_coherence\_cell\_missing}
\]

with the three charts, boundary cells, and nonzero defect.

## Cross-sector consequences

- **Benincasa.** The direct-image reducer must be source-wall-only and
  total-cocycle aware. Gradient pivots cannot be inserted into the ordinary
  rank-34 reducer as if pairwise gluing were enough.
- **Strominger.** Pairwise constructor diamonds do not establish coherence
  for three compilation trees. The normalizer needs explicit higher-cell
  obligations when comparison cells are operative.
- **Kitaev.** Equality of several schedule orderings needs coherent
  comparison across triples, not only pairwise output equality. Exact
  simultaneous diagonality can supply this law at the ideal algebraic level,
  but physical fault/resource cells remain separate.
- **Arithmetic/RH.** Pairwise agreement among endpoint, gamma, and prime
  presentations does not guarantee a coherent triple coupling. The
  endpoint-gamma-prime balance is inherently a higher overlap condition.

## Durable statement

> Filling every pairwise diamond does not close a constructor descent
> problem. The comparison cells must satisfy their own triple coherence law,
> witnessed by a source-authorized higher cell when the boundary defect is
> nonzero.

