# Four vertices carry two independent structures unless a source bridge identifies them

## Question

Does the four-system Pfaffian automatically represent the tetrahedral coherence or associator of the same four systems?

## Claim boundary

No. The two constructions use the same vertex set but different typed edge data.

The Pfaffian construction starts with skew pairing coefficients

\[
a_{ij}=-a_{ji}
\]

forming a 2-form \(\omega\). Its question is nondegeneracy:

\[
\omega\wedge\omega\ne0.
\]

The tetrahedral construction starts with composable transition maps

\[
g_{ij}:X_i\to X_j.
\]

Its question is descent coherence: do edge transports, face holonomies, and higher fillers compose consistently?

These are not the same variance, codomain, or composition law.

### Independence

A system can have a nondegenerate skew pairing while its transition connection is flat. It can have a degenerate pairing while its transition maps carry nontrivial holonomy. It can also have both defects or neither.

Therefore none of the implications

\[
\operatorname{Pf}(D)\ne0
\Longrightarrow
\text{tetrahedral coherence},
\]

or

\[
\text{flat tetrahedral descent}
\Longrightarrow
\operatorname{Pf}(D)\ne0
\]

is valid without additional structure.

### Required bridge

To relate them, the source theory must provide a natural assignment

\[
\Phi:g_{ij}\longmapsto a_{ij}
\]

or a common parent constructor from which both transition and pairing edges descend.

The bridge must preserve:

- endpoint and source typing;
- reversal or dagger variance;
- local frame transformations;
- cutoff restriction;
- the coefficient lens;
- completion topology.

Only then may a Pfaffian identity be interpreted as a shadow of higher compositional coherence.

### Three possible bridge strengths

1. No bridge: Pfaffian and holonomy are parallel diagnostics on unrelated edge packets.
2. Lax bridge: transition composition controls pairing only up to a residual comparison cell. That residual is new data and must be audited.
3. Strong bridge: both arise functorially from one source connection. Tetrahedral closure may then constrain the Pfaffian line and its transport.

The third case is the structural prize, but it cannot be inferred from sharing four labels.

### Exact hostile models

A flat transition family can be constructed as pure gauge

\[
g_{ij}=h_jh_i^{-1},
\]

so every loop holonomy is trivial, while an independently chosen skew form may have zero or nonzero Pfaffian at will.

Conversely, choose a fixed degenerate rank-two skew form and independently choose transition maps with nontrivial triangle holonomy. Pairing degeneracy then says nothing about descent curvature.

These witnesses prove categorical independence.

### Programme implication

The next source-native four-object model must expose two edge tables:

- the transition table \((g_{ij})\);
- the pairing table \((a_{ij})\).

It must then state whether they share a parent constructor. The finite audit computes separately:

- face and tetrahedral holonomies from \(g_{ij}\);
- Pfaffian and singular values from \(a_{ij}\);
- the naturality residual of \(\Phi\), if supplied.

A scalar formula in which both happen to vanish is not a bridge.

## Disposition

The four-system discovery remains important, but it bifurcates. Pfaffian nondegeneracy measures emergent relational volume. Tetrahedral coherence measures whether comparison laws share a global realization. Their coincidence would be a new source theorem, not a formal consequence.

This correction sharpens the research target: derive the bridge functor, or keep the two four-system structures separate. The first failure among pairing, descent, and bridge naturality will identify which kind of higher coherencer is actually missing.