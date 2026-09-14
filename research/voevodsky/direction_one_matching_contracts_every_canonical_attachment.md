# Direction-one matching contracts every canonical attachment

## Question

Can the successful lexicographic Morse matching be identified explicitly and proved complete and acyclic in every dimension?

## Claim boundary

For canonical relative attachments at \(L_n\) with \(n\geq3\), a cell-level matching is defined and proved using the prime-divisibility classification. It applies to distinct-shell relative cells. It does not address arbitrary noncanonical attachment grades or repeated-shell cells.

## Classification of new cells

A positive-dimensional cell born at \(L_n\) has shell set \(I\subseteq\{1,\ldots,n\}\), with \(m=\max I\geq2\). If \(m<n\), then \(m-1\notin I\); if \(m=n\), every subset below \(n\) is allowed.

This classification has two consequences.

First, \(I=\{1\}\) and \(I=\{1,2\}\) never occur. The unique new edge with direction set \(\{2\}\) has the unique new vertex as its relative boundary.

Second, every other new cell whose direction set omits 1 has a unique new coface obtained by adding direction 1. If the lower cell is \([D;I]\), its coface is

\[
\left[\frac{2D}{3};\{1\}\cup I\right].
\]

Its upper direction-one face is \([D;I]\). Conversely, every new cell containing direction 1 is uniquely of this form.

## Uniform matching

Match the unique new vertex with the new shell-2 edge. For every other new cell \([D;I]\) with \(1\notin I\), match

\[
[D;I]
\longleftrightarrow
\left[\frac{2D}{3};\{1\}\cup I\right].
\]

The classification proves completeness: every cell belongs to exactly one pair.

This is precisely the rule selected by the tested lexicographic algorithm. The special vertex--edge pair replaces the absent \(\{1\}\)-edge, and every remaining pair uses direction 1.

## Gradient acyclicity

Reverse every matched face arrow. The special shell-2 edge has no other new vertex face, so a gradient path entering it stops.

Every ordinary reversed matched arrow adds direction 1. An unmatched downward face may remove another direction, but the direction-one face cannot be traversed downward because it is the matched face. Therefore direction 1 remains present along every subsequent downward segment. No cell containing direction 1 is the lower member of another ordinary matched pair.

Hence a gradient path cannot reach another upward matched arrow after using an ordinary pair. Every directed gradient path terminates, so no directed cycle exists.

The matching has no critical cells. Forman cancellation gives a contraction of the entire relative attachment.

## Consequences

For every \(n\geq3\),

\[
H_k(X_{\leq L_n},X_{<L_n};\mathbb Z)=0
\]

in every degree. The matching pairs between degrees \(k\) and \(k+1\) are counted by

\[
[x^k]A_{n-1}(x),
\]

which explains why relative boundary ranks reproduce the preceding attachment vector.

The contraction is arithmetic and constructive: for a lower matched cell, multiply its base by \(2/3\) and add shell direction 1; for the unique new vertex, use the shell-2 edge.

## Strongest falsification attempt

Implement this explicit matching independently of lexicographic search. For dimensions three through fourteen, require valid integral coface bases, exact relative-face incidence, complete pairing, expected pair counts, and gradient acyclicity. Compare every explicit pair with the output of the original lexicographic algorithm.

## Disposition

The all-dimensional contraction follows from the exact cell classification and the monotone direction-one gradient argument. Finite checks remain useful for transport and implementation defects rather than as the basis of the theorem.
