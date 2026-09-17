# Common-tree complexes as independence complexes of common-interval overlap graphs

## Rooted interval model

Fix a distinguished label `r` and cut both cyclic orders immediately at `r`. For every channel split `S | S^c`, orient it by choosing the side `I` that does not contain `r`.

Then the channel is planar in a cyclic order exactly when `I` is an ordinary contiguous interval in the corresponding cut linear order. Therefore the channels planar in both `alpha` and `beta` are precisely the nontrivial proper **common intervals** of the two resulting permutations, subject to the usual channel size bounds.

## Compatibility becomes non-overlap

For two rooted sides `I,J`, the corresponding splits are incompatible exactly when all four split intersections are nonempty. Since `r` belongs to neither `I` nor `J`, the complement intersection is automatically nonempty. Thus incompatibility is equivalent to

\[
I\cap J\ne\varnothing,\qquad I\setminus J\ne\varnothing,
\qquad J\setminus I\ne\varnothing.
\]

That is precisely interval overlap: `I` and `J` intersect, but neither contains the other.

Let `O(alpha,beta)` be the graph whose vertices are the admissible common intervals and whose edges join overlapping intervals. Then

\[
K(\alpha,\beta)=\operatorname{Ind}(O(\alpha,\beta)),
\]

the independence complex of the common-interval overlap graph.

A forbidden-channel recursive state is simply

\[
\operatorname{Ind}(O[A])
\]

for an induced subgraph on the remaining allowed intervals `A`.

## Translation of the theorem

Purity means that `O[A]` is **well-covered**: all maximal independent sets have the same cardinality.

A channel is a shedding vertex of the simplicial complex exactly when it is a shedding vertex for the independence complex. Equivalently, every maximal independent set containing it can replace it by another allowed interval.

A tempting computational conjecture is that every well-covered induced subgraph of this overlap graph has a vertex-decomposable independence complex. This is false. Exhaustive restriction testing finds:

- at six points, a pure but facet-disconnected restriction consisting of two disjoint edges;
- at seven points, even purity plus facet connectivity is insufficient. Taking the seven short cyclic channels in the full seven-point associahedron gives the independence complex of a 7-cycle. It has seven triangular facets, is pure and facet-connected, but is not vertex-decomposable.

Thus arbitrary forbidden-channel restrictions are too broad. The successful recursion occupies a narrower class of restrictions produced by prior shedding deletions and links.

## Prior-art interface

Common intervals of permutations have an established decomposition theory:

- Uno and Yagiura, *Fast Algorithms to Enumerate All Common Intervals of Two Permutations*, Algorithmica 26 (2000), DOI 10.1007/s004539910014;
- Bergeron et al., *Common Intervals of Permutations* (2004), DOI 10.1007/978-3-0348-7915-6_1;
- Habib et al., work on common intervals and modular decomposition;
- Bui-Xuan, Habib, Limouzy, and de Montgolfier, *Tree-representation of set families and applications to combinatorial decompositions*, European J. Combin. 33 (2012), DOI 10.1016/j.ejc.2011.09.032.

The family of common intervals admits strong-interval/decomposition-tree representations. Overlap components are controlled by prime or linear nodes of that tree. This remains a plausible induction mechanism, but the 7-cycle obstruction shows that well-coveredness and connectivity alone do not suffice; an additional invariant of shedding-generated restrictions is required.

## Next proof task

Characterize the restrictions reachable by successive shedding deletion/link operations. Candidate invariants to distinguish them from the forbidden 7-cycle restriction include:

1. recursive contractibility of deletion branches;
2. exclusion of induced odd-cycle overlap blocks at prime strong-interval nodes;
3. a dismantling order inherited from the original complete common-interval family;
4. closure conditions on allowed intervals stronger than arbitrary vertex subsets.

Only after identifying this invariant should one attempt induction on the strong common-interval tree.
