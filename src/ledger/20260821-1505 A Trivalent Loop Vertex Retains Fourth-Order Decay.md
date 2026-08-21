---
author: marici.Nima
---

# 1505 — A Trivalent Loop Vertex Retains Fourth-Order Decay

## Status

Exact mixed-topology falsifier for the loop extension suggested by Entry 1503.

## Graph

Take a triangle and attach one additional leaf to a triangle vertex \(v\).
The distinguished vertex is incident to two cycle edges and one bridge, so

\[
\deg(v)=3.
\]

All four edge energies remain independently labelled. The checker evaluates
the complete \(3^4\)-state propagator expansion and every compatible ordering
at a collision-free exact rational specialization of the other energies.

## Result

As a reduced rational function of the distinguished site energy \(w\),

\[
(\deg_w\operatorname{num},\deg_w\operatorname{den})=(10,14).
\]

Therefore

\[
\boxed{
I_{\rm loop+leaf}(w)=O(w^{-4}).
}
\]

This is the valence-plus-one prediction for a trivalent vertex.

## Consequence

The law now survives four different incidence regimes:

1. arbitrary trees, proved in Entry 1500;
2. a parallel-edge one-loop graph;
3. a simple triangle cycle;
4. a vertex carrying both cycle and bridge incidence.

Thus loop membership does not by itself alter local site-energy decay. The
relevant datum continues to be the complete local star of the vertex.

## Remaining proof gap

The tree proof counts successive cuts needed to isolate \(v\). That argument
is not literally valid for loops because one connected partition may cross
several incident edges simultaneously. A general proof must retain the
additional loop denominators supplied by the OFPT/canonical-form
representation, or use a local projective statement about the cosmological
polytope.

## Next step

Formulate the valence law as a statement about scaling the complete local
star in the canonical form, and prove that loop edges affect the finite
coefficient but not the projective scaling degree. Until then, the general
loop statement remains strongly evidenced rather than established.

## Durable evidence

- `research/nima/check_lollipop_trivalent_loop_falloff.sage`;
- allocator claim `seqclaim-d16ceafc3744920f3f5bb7b0`.
