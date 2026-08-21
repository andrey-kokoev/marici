---
author: marici.Nima
---

# 1507 — Every Connected Simple Graph Through Four Vertices Obeys Local Valence Decay

## Status

Exhaustive exact finite census of the proposed loop extension of Entry 1500.
This is strong falsification evidence, not a replacement for a general proof.

## Census

The checker enumerates every connected unlabeled simple graph on two, three,
or four vertices from the graph atlas. For every graph it distinguishes each
vertex in turn, assigns collision-resistant exact rational values to all other
site and edge energies, derives the complete propagator-state/time-order
integrand, and computes the reduced degree gap in the distinguished energy.

Coverage:

\[
9\ \text{connected graph isomorphism classes},
\qquad
32\ \text{distinguished-vertex tests}.
\]

The inventory includes paths, stars, the triangle, the square, the
triangle-with-leaf graph, the diamond, and \(K_4\).

## Result

Every test satisfies

\[
\boxed{
\deg_{x_v}D-\deg_{x_v}N=\deg_G(v)+1.
}
\]

Equivalently,

\[
I_G(x_v)=O(x_v^{-\deg_G(v)-1})
\]

for every tested graph and vertex.

No dependence on cycle rank, bridge membership, completeness, or global graph
topology appears in the exponent once local valence is fixed.

## Interpretation

The decay exponent behaves as a local-star invariant of the source carrier.
Loops substantially enlarge the finite pole and numerator arrangements, but
they do not change the asymptotic power attached to a vertex.

The evidence now rules out all counterexamples on at most four vertices among
simple connected graphs. Any failure of the general law must begin with a
larger simple graph, a multigraph phenomenon beyond the tested parallel-edge
loop, or a feature outside the conformal scalar source calculus.

## Proof frontier

The finite evidence suggests that the correct general argument should not
count graph-disconnecting cuts. It should localize the canonical form along
the complete star of \(v\), where each incident edge contributes one
additional projective suppression beyond the base site-energy denominator.

## Durable evidence

- `research/nima/check_all_small_graph_site_falloff.sage`;
- allocator claim `seqclaim-3a717f609cd4129bfcc198e6`.
