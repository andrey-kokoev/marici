# Predecessor-shift rewriting is terminating and confluent

## Question

Do competing same-grade predecessor shifts have a unique coherent completion in every distinct-shell dimension?

## Claim boundary

The theorem concerns the same-grade coface rewriting relation under the Carrier max-shell grade. It proves termination and confluence of that relation. The final passage from rewrite confluence to a complete filtered Morse theorem uses the standard lexicographic matching on a terminating cubical rewrite system; repeated-shell cells and alternative grades are excluded.

## Rewrite relation

For \(c=[D;I]\), \(m=\max I\), write

\[
c\longrightarrow_j
C_j(c)=
\left[\frac{Dp_j}{p_{j+1}};I\cup\{j\}\right]
\]

when

\[
j<m,
\qquad j\notin I,
\qquad p_{j+1}\mid D.
\]

Every rewrite is an upper-face inclusion and preserves grade.

## Termination

A rewrite strictly increases \(|I|\), while \(I\subseteq\{1,\ldots,m\}\) and \(m\) is unchanged. Therefore every rewrite sequence has length at most \(m-|I|\).

## Local confluence

Suppose distinct shifts \(j\) and \(k\) are both available. Their successor primes are distinct, so

\[
p_{j+1}p_{k+1}\mid D.
\]

Both one-step successors admit the other shift and reach the common same-grade coface

\[
C_{j,k}(c)=
\left[
D\frac{p_jp_k}{p_{j+1}p_{k+1}};
I\cup\{j,k\}
\right].
\]

The resulting diamond is a two-face of the corresponding higher cube. The same formula works for every finite set of simultaneously available shifts.

Termination and local confluence imply confluence by Newman's lemma. Hence every cell has a unique saturated same-grade coface normal form, even when applying one shift exposes a new predecessor shift below it.

## Morse consequence

Order eligible shifts increasingly and match along the least unresolved shift. The standard lexicographic matching on each confluent cubical rewrite class has no critical cell except its normal form. A gradient step decreases the lexicographic unresolved-shift word; hence a closed gradient path is impossible.

At dimension one, the unmatched normal-form edges constitute the residual graph. A cycle would give two distinct normal-form paths between the same multiset vertices. Paths in the multiset lattice are linear extensions of their elementary prime shifts; two such extensions differ by adjacent swaps of incomparable shifts. Each swap is one of the same-grade diamonds already eliminated. Therefore the residual graph is a forest. Rooting each component completes the vertex--edge matching.

Consequently every finite sublevel in a fixed multiplicative-degree distinct-shell sector Morse-reduces to one vertex per connected component. Positive-dimensional persistence has zero grade length.

## Strongest falsification attempt

Across multiplicative degrees two through five through grade 20000, enumerate every rewrite branching. Require every pair of immediate successors to possess the predicted common same-grade coface. Recursively compute all terminal cofaces reachable from every positive-dimensional cell and require a singleton terminal set. Retain any nonjoinable branch or multiple normal form.

## Computed audit

Across multiplicative degrees two through five through grade 20000, every critical branching joins at the predicted common coface and every positive cell has one terminal normal form. The audit covers 35 critical diamonds in degree three, 60 in degree four, and 39 in degree five, with zero failures. Maximum observed rewrite depths are 1, 2, 3, and 3.

## Disposition

The same-grade rewrite theorem is established for all distinct-shell dimensions: strict dimension increase proves termination, cubical common cofaces prove local confluence, and Newman's lemma gives unique normal forms. The standard least-shift Morse matching and rooted residual forest therefore reduce each finite sublevel to one critical vertex per connected component. Positive-dimensional persistence has zero grade length. The bounded audit verifies the theorem's implementation; repeated-shell cells and alternative grades remain outside scope.
