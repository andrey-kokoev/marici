# Four-vertex overlaps: the first obstruction beyond boundary swaps

## Status and reproduction

Selected overlapping-support test following the
[retained transport loops](trivalent-transport-loop-results.md). The old
three-vertex derived comparisons are available in context, with their primitive
provenance replayed. No new relation or higher filler is admitted.

```text
python research/nima/checkers/check_trivalent_four_vertex_overlaps.py
```

Evidence: `results/trivalent-four-vertex-overlaps.json`, including seed
provenance, saturated diagrams, rule placements, contextual macro expansions,
fork joins, normal routes, boundary transports and structural invariants.
All assertions pass.

## 1. Selected sector

Start with the four earlier residual fork sources. Glue one primitive merge
or split before or after each, using every nonempty injective one-way port
matching. Include every external boundary ordering. This gives **91 distinct
ordered seed diagrams**.

Saturate these seeds under:

- the selected elementary directions α, inverse reversed-α, K→F_L and F_R→K;
- the two old three-vertex residual macro schemas, whose contextual placements
  already include their boundary-swapped opposite directions.

The saturated universe has **414 diagrams**, and is checked closed under the
full external boundary-permutation action as well as these rule placements.
Every graph has four vertices. This is a selected sector, not a complete census
of all four-vertex diagrams.

| Boundary | Underlying cycle rank | Diagrams |
|---|---:|---:|
| (3,1) | 1 | 108 |
| (2,2) | 1 | 188 |
| (1,3) | 1 | 108 |
| (1,1) | 2 | 10 |

All diagrams are directed acyclic. Underlying undirected cycles are allowed.

## 2. Overlap results

There are **556 elementary placements**, **92 old-macro placements**, and
**257 elementary forks**:

| Fork class | Count |
|---|---:|
| Disjoint supports, joined by elementary rules | 57 |
| Shared vertex, joined by elementary rules | 68 |
| Shared vertex, joined after using old macros | 92 |
| Shared vertex, still unjoined | 40 |

The elementary directed graph has no directed cycles in this sector. Macro
assistance is a reachability test, not a termination claim: the old schemas
are symmetric at some placements.

Each of the 92 macro instances is expanded and replayed as its original
three-step primitive comparison path, allowing inverses in the experimental
reversible extension. Merely matching a macro's endpoints is not accepted as
its justification.

## 3. The crucial new feature: a nonconvex union

**All 40 remaining forks have nonconvex combined support.** Each individual
two-vertex rewrite is admissible and convex, but their overlapping three-vertex
union is not a valid convex local context. A path leaves that union through
the fourth vertex and returns to it.

In contrast, all 92 forks resolved by the old macros have convex combined
support. The difference is contextual, not a different primitive merge/split
operation.

The checker excludes 181 nonconvex individual matches of the inverse-right
Frobenius rule. These are not counted as valid steps. A nonconvex *union of two
separately valid matches*, however, can still give a genuine fork—and does.

## 4. Boundary transport repairs 32 cases, but not eight

Of the 40 remaining terminal pairs:

- **32** are related by an external boundary permutation;
- **8** belong to different boundary-permutation orbits.

The eight remain unjoined even after projecting the whole saturated graph to
its boundary quotient and allowing all old macro placements. They all occur at
boundary **(2,2)** with underlying cycle rank one.

Thus the successful three-vertex boundary-modulo normalizer does **not** extend
unchanged to this four-vertex sector. This is a concrete bounded obstruction
to that chosen directed presentation plus its old macros, not a proof that no
completion exists.

### A structural witness, not just different graph IDs

For source ID 166 in the saved report, the two elementary steps have supports
{1,3} and {2,3}. Their union is {1,2,3}. A path through vertex 0 leaves and
re-enters that union. The source has merge vertices M0,M1 and split vertices
S2,S3, with wires:

    M0.out0 → M1.in1,
    S2.out0 → M0.in0,
    S2.out1 → S3.in0,
    S3.out1 → M1.in0.

The two routes end at terminal IDs 410 and 343. In one terminal, **both external
inputs attach to split vertices**. In the other, one input attaches to a merge
and one to a split. External boundary permutations and orientation-preserving
vertex relabellings cannot change that attachment signature.

The other obstructed cases have analogous input- or output-attachment
invariants. The checker records them and verifies their difference for all
eight cases. Hence these are not another disguised swap of the same ordered
terminal graph.

IDs refer only to the hash-bound saved report. The incidence records and
attachment signatures are the mathematical evidence.

## 5. This is not a counterexample to the Frobenius equations

All eight terminal pairs agree, nontrivially, in the 2×2 integer matrix
Frobenius model. Its associativity, coassociativity and slide equations are
checked before testing the terminal maps.

More importantly, each pair already has a reversible comparison path through
its fork source: reverse one route and follow the other. The failure is that
the **chosen forward rules and existing local macros do not rejoin it**.
A new directed shortcut may be derived from that path; it need not be an
independent primitive law.

Equal model readouts do not prove abstract path equality or contractibility,
and graph nonisomorphism does not prove inequivalence under the experimental
comparisons. Keep these separate.

## 6. Meaning and next executable work

The obstruction has progressed in a specific way:

1. Three vertices exposed boundary-swap residual paths.
2. Retained boundary transport handled those without losing ordered data.
3. Disjoint four-vertex rewrites commuted.
4. Overlapping four-vertex rewrites now expose nonconvex unions and terminal
   differences that cannot all be absorbed by boundary symmetry.

Next, extract the eight remaining fork routes, classify their terminal equations
under the declared symmetries, and test **four-vertex derived macros** with
replayable provenance. Re-run both cycle and joinability tests, including the
boundary quotient. Do not assume the next completion is finite, canonical or
terminating, and do not introduce an independent generator merely because the
previous orientation was insufficient.

This experiment still does not establish seven grades, arbitrary-arity
coherence, native Resolve generation, or a source-signature freeze.
