# Sparse object-changing lax existence

## Question

Can projected compositor labels appear compatible while no lax or oplax comparison component exists between staged and direct attachment objects?

## Claim boundary

This packet isolates component existence in a finite thin attachment category. Since the category is thin, it does not test equality of distinct parallel comparisons.

## Sparse attachment category

Let the attachment category be the diamond poset with objects

\[
\bot < p < \top,
\qquad
\bot < q < \top,
\]

where \(p\) and \(q\) are incomparable. Every existing hom-set is a singleton, so forgetting endpoints leaves only one projected morphism label.

Let the map-label monoid contain an identity and an idempotent element \(a\). Assign to \(a\) the monotone functor \(S\) that swaps \(p\) and \(q\) while fixing \(\bot\) and \(\top\). Then \(S^2=\operatorname{Id}\), whereas the idempotent label requires comparison with \(S\).

A lax compositor would require

\[
S^2(x)=x\longrightarrow S(x).
\]

At \(p\) this asks for \(p\to q\), and at \(q\) for \(q\to p\); neither exists. An oplax compositor reverses these arrows and fails at the opposite middle object for the same reason. Thus neither orientation exists globally, although every projected label is the same singleton.

For contrast, the monotone saturation functor \(T\) sends both middle objects to \(\top\) and fixes the endpoints. It is strictly idempotent, so \(T^2=T\) and all comparison components exist as identities.

## DPC cycle

### Governing conjecture

Existence of every typed comparison component is prior to naturality and coherence, and cannot be inferred from projected labels. The mechanism is hard to vary because a natural transformation requires an actual morphism in each hom-set between the staged and direct object images.

### Rivals

1. Compatible projected labels suffice to construct a comparison cell.
2. If the lax direction fails, the oplax direction must exist.
3. Pentagon or naturality checks can detect coherence without a separate component-existence gate.

### Risky consequences

The swap fixture must pass monotonicity and projected-label checks while failing both orientations at explicit objects. A strict idempotent saturation on the same category must pass the component-existence, naturality, and associativity gates.

### Falsification attempt

The checker enumerates every order pair, verifies both functors are monotone, computes staged and direct images for every label pair and object, and tests hom-set existence in each orientation. The swap lacks two lax and two oplax components. The saturation functor admits every component and all thin-category diagrams.

### Residual

The fixture is thin and uses a singleton label projection. Nonthin sparse categories additionally require naturality and equality of parallel paths after existence is established.

### Disposition

All three rivals are rejected. Typed pointwise component existence is retained as the first gate, before naturality or associativity.

## Disposition

Sparse attachment categories can reject both lax and oplax reductions of a staged construction. In that case transport must remain correspondence-valued or partial rather than receiving a fabricated comparison cell.
