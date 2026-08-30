# 1701 — Covariance Rees Signs Propagate to One Global Z2 on Connected Trees

## Odd-grade falsifier

Entry 1700 proves functorial Cut descent of the even tensor `Xi=u tensor u`.
Test whether its odd square root requires independent signs on every
occurrence.

## Tree propagation

Attach a nonzero resolved normal `u_i` to each vertex of a connected labelled
tree.  The exceptional edge packet records

\[
\Xi_{ij}=u_iu_j.
\]

After choosing the sign of one root, every adjacent sign is forced by the edge
product.  Unique tree paths propagate this choice to all vertices.  The second
solution is the simultaneous flip

\[
u_i\longmapsto-u_i
\]

for every occurrence.

Therefore

\[
\boxed{
\operatorname{Deck}_{\rm cov}(T)=\mathbb Z_2
}
\]

for a connected nonsoft tree.

The exact checker enumerates every labelled tree through seven vertices and
every sign packet.  In each case exactly the root choice and its global inverse
remain.

## Soft support

If a zero normal breaks sign propagation, each surviving connected component
has its own sign.  The enlargement is therefore supported on the soft/zero
locus rather than generic.

## Narrow result

\[
\boxed{
\text{the covariance Rees cover has one generic global sign on connected trees, with componentwise enlargement only on soft support.}
}
\]

This precisely parallels the combinatorics of the cosmological time-root test,
but Entry 1699 still applies: parallel deck groups do not constitute a
canonical identification of local systems.

## Durable artifacts

- `research/benincasa/checkers/covariance_tree_global_sign.rs`
- `research/benincasa/results/covariance-tree-global-sign.json`
- `research/benincasa/covariance-tree-global-sign.md`

## Next falsifier

Move to one nonseparating loop.  Determine whether edge-product sign data have
an additional `H^1(G,Z2)` holonomy sector or whether existence of the global
resolved vector `u` forces trivial loop holonomy.  Separate generic loop
topology from soft-supported disconnection.
