# Disconnected three-demand signatures occur in independent cuts

## Question

Are active supply signatures connected intervals in the lexicographic demand order?

## Claim boundary

No. After 206 triples in 99 terminal cases, an independent cut contains signature \(101\): one supply neighbors the two outer ordered demands but not the middle.

The obstruction occurs for base \(\{1\}\), \((i,j)=(0,2)\), ordered demands

\[
\{0,2\},\qquad \{0,4\},\qquad \{1,3\},
\]

with supply \(\{1,2\}\) carrying signature \(101\). Active signatures are

\[
001,
\quad100,
\quad101,
\quad110,
\quad111.
\]

The collective slack is strictly smaller than every proper-subset slack. Chain-interval compression is therefore false.

## Disposition

No demand ordering currently compresses signatures source-independently. The surviving exact quotient is the generic neighbor-signature construction: for \(m\) demands, aggregate supplies by their nonempty subset of neighbors, requiring up to \(2^m-1\) classes. Prove and test that quotient and state the exponential residual explicitly. Any smaller all-order representation now requires additional source-derived MTP2 structure, not Hasse incidence alone.
