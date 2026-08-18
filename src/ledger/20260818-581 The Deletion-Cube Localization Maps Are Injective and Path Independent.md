# 581 — The Deletion-Cube Localization Maps Are Injective and Path Independent

## Hard-to-vary claim

The rank cube of Entry 580 is the objectwise shadow of a functorial deletion diagram: source-divisor localization descends to injective maps on every edge, and every square commutes after exact reduction.

## Canonical map

For masks \(S\subset S\cup\{j\}\), represent a lower-mask class

\[
\frac{P}{K^m\prod_{i\in S}q_i^{n_i}}
\]

in the higher simple-\(q_j\) presentation by

\[
\boxed{
\frac{Pq_j}{K^m q_j\prod_{i\in S}q_i^{n_i}}.
}
\]

This is not a chosen splitting. It is the localization transition already present in the frozen product-pole complex.

Use the fixed descending-column elimination order at

\[
\gamma=5,\qquad
\mathbb F_{32003},\qquad
\text{pole depth }2,\qquad
\text{ambient degree }9.
\]

For each mask, nonpivot monomials in its simple-pole block give a deterministic normal-form basis. These monomial lists are not nested across masks; compatibility must therefore be tested by the induced quotient maps.

## Edge audit

For every edge, the image rank equals the source rank:

\[
\begin{array}{c|c}
\text{edge}&\operatorname{rank}(\mathrm{image})/\operatorname{rank}(\mathrm{source})\\
\hline
000\to001&7/7\\
000\to010&7/7\\
000\to100&7/7\\
001\to011&8/8\\
001\to101&8/8\\
010\to011&8/8\\
010\to110&8/8\\
011\to111&9/9\\
100\to101&16/16\\
100\to110&16/16\\
101\to111&18/18\\
110\to111&18/18
\end{array}
\]

Hence all twelve localization maps are injective in the tested complex.

## Square audit

Transport each source basis vector by both orders of adding the two missing divisors, reducing after each edge. The two normal forms agree exactly on all six squares:

\[
\begin{aligned}
000 &: (0,1),(0,2),(1,2),\\
001 &: (1,2),\\
010 &: (0,2),\\
100 &: (0,1).
\end{aligned}
\]

The entire edge and square audit is reproduced at both generic kinematic points

\[
(2,3,4),\qquad(3,5,6).
\]

## Narrow conclusion

The deletion cube is now more than eight matching dimensions:

\[
\boxed{
S\longmapsto H_S
}
\]

is a covariant localization diagram on the tested generic fibers, with injective edge maps and strict square coherence in canonical quotient normal forms.

This supplies the incidence-compatible coefficient packet needed before Gauss--Manin transport. It does not yet establish that parameter derivatives preserve these subspaces.

No basis fitting or carrier modification was used.

## Next falsifier

Differentiate the frozen product-pole presentation in two independent kinematic directions. Reduce the differentiated basis vectors in the same normal forms and test:

1. preservation of every edge image;
2. naturality of each connection matrix with all twelve localization maps;
3. vanishing curvature modulo exact rows.

Failure of any test is coefficient-extension data unless it forces a new incidence divisor independently.

## Artifacts

- \`research/benincasa/marici-gm/src/bin/generic_q_pole_twisted_derham_rank.rs\`
- \`research/benincasa/deletion-localization-map-audit.json\`
