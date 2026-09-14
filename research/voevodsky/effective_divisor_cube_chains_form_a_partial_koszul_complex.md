# Effective-divisor cube chains form a partial Koszul complex

## Question

Can the exterior and Clifford degrees of prime-index directions be mapped to matching cubical-chain degrees in the effective-divisor geometry?

## Claim boundary

Admissible cubes of distinct adjacent-prime moves carry the standard cubical boundary, expressible as a Koszul differential for commuting partial translations. Disjoint-direction cell products satisfy the graded Leibniz rule. Repeated moves in the same shell require a divided-power or labelled-chip extension and are outside the exterior model established here.

## Cubical generators

Let \(D\) be an effective prime-index divisor and let

\[
I=\{i_1<\cdots<i_k\}
\]

be distinct shell directions. Write \([D;I]\) for the oriented cube whose subset vertices are

\[
D_S=D+
\sum_{i\in S}\alpha_i,
\qquad S\subseteq I,
\]

provided every \(D_S\) is effective. Its direction orientation is

\[
e_I=e_{i_1}\wedge\cdots\wedge e_{i_k}.
\]

Thus cubical degree and exterior degree agree by construction.

## Boundary as a Koszul differential

Let \(\tau_iD=D+\alpha_i\) on its effective domain. The oriented boundary is

\[
\partial[D;I]
=
\sum_{r=1}^{k}(-1)^{r-1}
\left(
[D+\alpha_{i_r};I\setminus\{i_r\}]
-
[D;I\setminus\{i_r\}]
\right).
\]

Symbolically this is

\[
\partial
=
\sum_i(\tau_i-1)\iota_i,
\]

where \(\iota_i\) contracts the exterior direction label. The translations commute wherever the containing cube is admissible, while contractions anticommute. Therefore

\[
\partial^2=0.
\]

This is the Koszul complex of the commuting difference operators \(\tau_i-1\), restricted to their common effective domains.

## Cell products

For cells \([D;I]\) and \([E;J]\) with \(I\cap J=\varnothing\), define

\[
[D;I]\cdot[E;J]
=
(-1)^{\operatorname{inv}(I,J)}
[D+E;I\cup J],
\]

where \(\operatorname{inv}(I,J)\) is the number of pairs \((i,j)\in I\times J\) with \(i>j\). This is the shuffle sign needed to reorder \(e_I\wedge e_J\) increasingly.

The boundary obeys

\[
\partial(xy)
=(\partial x)y+(-1)^{\deg x}x(\partial y).
\]

On degree-zero cells, divisor addition is multiplication of natural numbers. On positive degrees, the product superposes disjoint families of shell moves and raises cubical degree.

## Clifford interpretation

Exterior creation \(\varepsilon_i\) adds a cubical direction, while contraction \(\iota_i\) selects its signed pair of faces. The probe-induced Clifford operator

\[
c_i=\varepsilon_i+
\sum_jQ_{ij}\iota_j
\]

therefore combines direction creation with metric-weighted face extraction. A radical Clifford product such as \(a\wedge b\) belongs naturally to cubical degree two. It is realized by a weighted combination of square cells, not by forcing it back into the edge space.

## Typing consequence

The current route checker retains only

\[
C_1\xrightarrow{\partial}C_0.
\]

Its square and cube boundaries are shadows of higher cells in the full Koszul complex. Promoting the checker to

\[
\cdots\longrightarrow C_3
\longrightarrow C_2
\longrightarrow C_1
\longrightarrow C_0
\]

would distinguish a genuine filler from its boundary and would give Clifford exterior products their correct target degree.

## Strongest falsification attempt

Enumerate admissible divisor cubes through degree six. Compute every oriented boundary twice and require exact cancellation. For disjoint cell pairs, compare direct product boundaries with the graded Leibniz expression. Verify every face against the corresponding arithmetic subset vertices. Include overlapping-direction pairs as a deliberate boundary of scope: the exterior product is zero while two labelled chips may still admit repeated physical shell moves.

## Disposition

The exterior-to-cubical degree map is now explicit, and the effective-divisor cube chains carry a source-derived partial Koszul differential. The unresolved extension is the treatment of repeated same-shell moves, which requires more than an exterior algebra on unlabelled shell directions.
