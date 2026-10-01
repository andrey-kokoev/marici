# Contextual overlaps of the experimental mixed relation

## Status and reproduction

This tests the [Frobenius candidate](trivalent-mixed-frobenius-candidate.md) as
an explicitly experimental extension. No rule is admitted to the base calculus
or to the checked native grammar, and no higher filler is asserted.

```text
python research/nima/checkers/check_trivalent_contextual_overlaps.py
```

Full diagrams, rule placements, forks, joining paths, terminal descendants and
excluded matches are in `results/trivalent-contextual-overlaps.json`.

## Three systems compared

All use the same exhaustive census of **874 ordered-boundary connected DAGs**
with one through three vertices and distinguishable local slots.

1. **Original:** forward merge associativity α and its orientation reversal.
2. **Outward mixed extension:** additionally K→F_L and K→F_R.
3. **Inward mixed extension:** instead add F_L→K and F_R→K.

Here K=split∘merge; F_L and F_R are the two ordered Frobenius slides defined in
the candidate document. These are alternative directions for the same proposed
equations, not different primitive vertices. Undirected adjacency agrees for
the two mixed systems, as checked independently of forward reachability.

## Results

| System | Rule placements | Joinable shared-vertex forks | Unjoined shared-vertex forks | Unjoined same-support forks |
|---|---:|---:|---:|---:|
| Original | 444 | 48 | 0 | 0 |
| Outward mixed | 756 | 96 | 0 | 156 |
| Inward mixed | 756 | 120 | 32 | 0 |

Counts retain ordered-boundary instances and placements; they are not counts
of symmetry-inequivalent critical-pair types. The union of all placements across
systems contains 1,068 entries. No directed cycles occur in any of these finite
systems. Disjoint two-vertex supports cannot occur at this vertex bound.

The 48 original forks are the pure merge/split pentagon forks with ordered
boundaries. Both forward routes rejoin. This verifies path joinability, not
the existence of a specified 3-cell identifying the paths.

### Outward: the immediate fork remains

At K, choosing F_L or F_R yields two different normal forms under the outward
orientation. The 156 unjoined forks are contextual instances of these competing
same-support slides. All 96 shared-vertex forks do join in this bound.

Thus the failure cannot be described as a discovery of an inconsistent algebra:
it already follows from the chosen two outward directions and the absence of
a directed bridge between their targets.

### Inward: the problem moves to genuine overlapping supports

Directing both slides toward K removes that same-support fork, but **32
shared-vertex forks fail to join**. They all involve associativity and a mixed
collapse:

- 14 instances of α versus F_L→K;
- 2 instances of α versus F_R→K;
- 14 reversal instances of the first class;
- 2 reversal instances of the second class.

An explicit witness in the saved canonical census has source ID 162 and
terminal targets 246 and 328. Its source consists of merge vertices M0,M1 and
split vertex S2, with wires

    M0.out0 → M1.in0,
    S2.out0 → M0.in1.

The ordered input boundary is (M0.in0, M1.in1, S2.in0), and the ordered output
boundary is (M1.out0, S2.out1). Associativity acts on {M0,M1}; the left mixed
collapse acts on {M0,S2}. The two targets have different canonical incidence
records and neither has an outgoing inward-system step. Their normal-form
sets are respectively {246} and {328}.

These IDs identify this saved report only; the actual graph records and rule
embeddings are the reproducible evidence. Since all chosen rules preserve
vertex count and boundary, searching more vertices cannot repair this specific
fork without changing the rule set or allowed graph sector.

## An important contextual boundary: convexity

Sixteen apparent inward matches are excluded: their two matched vertices are
connected by a path through the third vertex as well as the matched internal
wire. The support is nonconvex. Collapsing the slide would create a directed
cycle, leaving the declared DAG sector.

The checker verifies that all excluded matches are nonconvex and all retained
matches are convex. Such subgraph matches are not valid ordinary DAG contexts
for this replacement. This is a concrete reason to distinguish unrestricted
port matching from admissible contextual rewriting. Allowing feedback would
require a separate cyclic/wheeled experiment, not silently accepting these
sixteen replacements.

## What was checked

- Every contextual replacement has the declared boundary and valid incidence.
- Replacing back with the opposite syntax pattern restores the original graph.
- Targets remain in the exhaustive census.
- All replacements preserve the exact integer tensor map in the scaled
  copy/merge model, which satisfies the experimental equations.
- Reversal preserves directed adjacency in each system separately.
- Outward and inward systems have identical undirected adjacency.
- Joining paths are explicit lists of placement IDs. For unjoined forks,
  terminal descendant IDs are retained.
- No directed cycles occur in the finite rewrite graphs.

A model validating both branches does not make their syntax equal. The model
can identify distinct diagrams, and no completeness theorem for that model is
being claimed.

## Interpretation and next experiment

Neither of these two natural orientations is a convergent presentation of the
experimental mixed equations, even at three vertices. This does not refute the
Frobenius equations: the strict models already demonstrate consistency in the
tested sense. It identifies concrete choices for completion.

The [derived shortcut experiment](trivalent-derived-completion-results.md)
now tests both slide-to-slide shortcuts with replayable provenance and all
sixteen orientations of the elementary equations. Neither single shortcut
converges: each leaves 16 unjoined forks and creates a four-step loop. The best
acyclic elementary orientations leave four forks, all in the cycle-rank-one
mixed sector. Next, test three-vertex shortcuts derived from those residual
routes before proposing an independent generator. A higher comparison
between routes would still be a separate datum unless a specified completion
construction supplies it.

These results concern local rewriting, not seven grades. They sharpen the
research question from “is seven canonical?” to “what completion, if any,
organizes the explicitly chosen mixed comparisons?”
