# Three-demand cells exceed the two-demand three-signature quotient immediately

## Question

Does fixed-eight source structure keep independent three-demand cuts within three active supply signatures?

## Claim boundary

No. The second tested negative triple already gives an independent collective cut with four active signatures. For empty base and \((i,j)=(0,3)\), demands \(\{1\},\{3\},\{5\}\) have signatures

\[
001,
\qquad 011,
\qquad 100,
\qquad 110.
\]

Thus the two-demand three-capacity compression does not persist. The collective slack is strictly below all six proper-subset slacks.

The run is a strongest-first falsifier, not a complete three-demand census: it stopped after three terminal cases and two triples when the first above-three-signature independent cell appeared.

## Disposition

The observed signatures form an alternating seven-vertex chain: endpoint singleton classes and adjacent-pair shared classes. The disconnected signature \(101\), middle singleton \(010\), and all-shared \(111\) are absent. Test the sharper surviving conjecture that active signatures in irreducible three-demand cells are connected subsets of an induced demand order; the first disconnected \(101\) signature would refute chain-interval compression.
