# The minimal conductor cospan cannot carry the two-bit cusp extension

## Question

Can the paired cusp thimbles map geometrically to the existing two-edge conductor cospan and thereby induce the missing cusp-to-conductor comparison?

## Conductor boundary complex

The normalized conductor cospan has two oriented edges and four labelled wall occurrences, with boundary matrix

\[
B=
\begin{pmatrix}
-1&0\\
0&1\\
1&0\\
0&-1
\end{pmatrix}.
\]

Its Smith invariants are \((1,1)\). Hence

\[
\operatorname{coker}B\cong\mathbb Z^2
\]

is torsion-free. The combinatorial boundary complex itself contains no two-torsion.

By contrast, the primitive conductor intertwiner is

\[
J=
\begin{pmatrix}
2&0&1\\
0&2&1\\
0&0&1
\end{pmatrix},
\]

with Smith invariants \((1,2,2)\), so

\[
\operatorname{coker}J\cong(\mathbb Z/2)^2.
\]

Therefore the conductor syndrome is created by the primitive half-sum extension encoded by \(J\), not by the incidence matrix \(B\).

## Equivariant edge matching

The cusp has two nodes exchanged by \(t\mapsto-t\). The conductor cospan has two edges exchanged by site exchange. There are exactly two equivariant bijections between these two-element sets: identity and swap. The cospan geometry does not select one.

More importantly, the local paired-node coinvariant provides only one nonzero mod-two direction. No homomorphism

\[
\mathbb Z/2\longrightarrow(\mathbb Z/2)^2
\]

is surjective. Thus even a chosen node-to-edge bijection cannot produce both conductor syndrome bits from the local thimble data.

## Missing geometric square

A valid comparison requires more than the endpoint incidence diagram. It needs a global relative group \(G\) and maps forming a commuting square

\[
G\longrightarrow\operatorname{coker}J
\]

whose restriction to the local cusp boundary recovers the known width-two class and whose second independent direction comes from a globally marked ambient cycle.

The source cospan packet independently records the missing coordinate map from its endpoint coordinate \(\xi\) to the exceptional coordinate \(r\), matching all four wall labels. The weighted-pairing packet also records that no common relative pair identifies the contour current with the logarithmic coefficient system.

## Disposition

The minimal conductor cospan cannot itself define the cusp-to-conductor map. Its boundary homology is torsion-free, its edge matching is ambiguous up to swap, and the local cusp contributes at most one of the two required mod-two directions. The first viable constructor is a global relative cycle carrying the second direction together with the primitive half-sum extension and the missing \(\xi\)-to-\(r\) wall map.
