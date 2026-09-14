# The source e6 node is a component difference in the global pencil

The source node-to-\(e_6\) calculation is centered at

\[
(X_1,X_2,X_3)=(1,0,1),
\qquad
(u,v)=(2,0),
\qquad
(a,b)=(2,1).
\]

In the global Cayley--Menger surface, set

\[
(x,y,z)=(1,0,1),\qquad h=1.
\]

The reflection-adapted pencil coordinate is \(q=b/h\), so the local center lies on \(q=1\). This equals the global critical value

\[
q=y+z=1.
\]

The complete fiber equation specializes exactly to

\[
W^2=(a^2-4)^2.
\]

Hence it splits as

\[
C_+:W=a^2-4,
\qquad
C_-:W=-(a^2-4),
\]

and the components meet at the paired nodes \(a=\pm2\). The chart used by the source calculation is precisely the node at \(a=2,b=1\), not an unrelated local degeneration.

Its anti-invariant sheet generator

\[
\tau=e_+-e_-
\]

is geometrically the oriented component difference \([C_+]-[C_-]\). Under the global reflection \(a\mapsto-a\), each component is preserved while the two nodes \(a=\pm2\) are exchanged. Therefore

\[
r_a(\tau)=\tau.
\]

The existing source-equivariant nonzero Gysin comparison

\[
\tau\longmapsto-\frac12e_6
\]

then places the rational \(e_6\)-line in the reflection-invariant algebraic subspace. The factor \(-1/2\) still does not determine an integral normalization, but the character statement is independent of rescaling:

\[
r_a(e_6)=e_6
\]

on the source rational line.

This supplies the first geometric identification between the source basis and the global Picard geometry. The remaining support direction \(v_{\rm alg}\) must now be expressed using the component differences of the other split fibers.

Certificate:

- `research/voevodsky/checkers/match_soft_node_to_split_fiber.py`;
- `research/voevodsky/results/soft_node_split_fiber_match.json`.
