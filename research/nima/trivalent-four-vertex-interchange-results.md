# Four-vertex interchange with two nontrivial operands

## Status and reproduction

A selected-sector follow-up to the
[retained gluing test](trivalent-retained-gluing-results.md). This moves beyond
three total vertices so that **both** operands can have primitive steps in
their saved normalization paths.

```text
python research/nima/checkers/check_trivalent_four_vertex_interchange.py
```

Evidence: `results/trivalent-four-vertex-interchange.json`. It records operand
traces, ordered port matchings, transported indices, labelled composite graphs,
all elementary grid witnesses, semantic counterexamples and source hashes.
All assertions pass.

## 1. Scope

Select the **20 two-vertex ordered operands** whose saved boundary-modulo
normalizations contain at least one primitive rewrite. For every ordered pair
of those operands, enumerate all nonempty injective matchings from left outputs
to right inputs. One, two or three joining wires are possible.

All composites have four vertices. Each factor occupies a fixed block of
vertex labels: left vertices 0,1 and right vertices 2,3. The experiment checks
interchange before quotienting these composite vertex labels.

This is not an exhaustive census of all four-vertex diagrams. It tests no
feedback, self-gluing or replacement on overlapping supports. It also does
not compute a normal form for the whole four-vertex composite.

## 2. Results

| Quantity | Count |
|---|---:|
| Nontrivially normalized two-vertex operands | 20 |
| Gluings with one joining wire | 1,600 |
| Gluings with two joining wires | 1,352 |
| Gluings with three joining wires | 216 |
| **Gluing cases** | **3,168** |
| Elementary interchange squares | 4,320 |
| Exact route-and-inverse round trips | 6,336 |

Each operand path is expressed with its original external order restored.
For path positions i,j, construct the composite obtained after i left steps
and j right steps. This produces a rectangular grid of labelled port graphs.

For every elementary square, the checker finds an actual contextual primitive
placement and a block-local internal renaming for each side. It then reuses
**exactly the same witnesses** in both orders:

    left step; right step
    right step; left step.

The outputs agree as full labelled graph records, including external boundary
order, not merely as graph-isomorphism classes or quotient normal forms.
The two supports are disjoint even when joining wires connect them.

The complete left-then-right and right-then-left routes reach the same graph.
Replaying each route backward recovers the exact starting labelled composite.
The 6,336 count is two such round trips per gluing case, not a count of
independent higher coherence generators.

## 3. Transport and semantics remain necessary

The checker also glues the raw quotient representatives directly, translating
the chosen ports through the retained boundary tags and restoring the remaining
external order. This agrees up to internal vertex relabelling with the grid's
terminal graph.

A deliberately naive control uses old numeric port indices on those quotient
representatives and discards the transport. In **2,496 of 3,168 cases**, that
changes the represented map in the rank-two noncommutative left-zero semigroup
algebra with transpose split. As in the previous test, all four experimental
associativity/Frobenius equations are verified in that model before use.

These failures are witnesses in a specific model, not a model-independent
failure rate. The model is not claimed faithful. The graph-level interchange
checks do not rely on interpreting graph equality through this model.

## 4. Interpretation

The result supports the proposal's expectation that distant placements
interchange structurally. In this selected sector, we needed no new primitive
relation to calculate the commuting squares: port substitution on disjoint
supports, together with explicit boundary transport, gives matching endpoints.

But matching endpoints are not automatically a chosen higher cell between
rewrite paths. If the calculus retains 2-cell paths rather than quotienting
them, it must still specify its interchange/coherence treatment. These finite
checks do not decide that higher presentation.

In particular, this result does not erase the earlier 20 discrepancies between
ordered terminal representatives under direct versus staged normalization.
Those concern boundary transport along different normalization routes. The
present test concerns **disjoint operand-step order**, and establishes neither
overlapping-support confluence nor path-independent normalization globally.

## 5. Checks retained in the report

- Freshness of the existing normalization/report dependency chain.
- Valid DAG incidence for every grid graph.
- Convexity of each operand support and actual primitive replacement matching.
- Block-local renaming only; the other operand's labels stay fixed.
- Exact inverse substitution recovery for every lifted step.
- Reuse of the same step witnesses on both sides of every elementary square.
- Exact full-route recovery in both orders.
- Ordered port transport through the raw quotient representatives.
- Exact integer semantic agreement and explicit naive-control failures.

## 6. Next executable work

Two distinct questions remain:

1. The [transport-loop analysis](trivalent-transport-loop-results.md) now
   classifies those 20 discrepancies into the two earlier three-step path
   families. Pair composition cancels the boundary swap, but does not contract
   the path. Disjoint interchange does not establish that stronger claim.
2. The [overlapping-support test](trivalent-four-vertex-overlap-results.md)
   now finds eight forks still unjoined after boundary quotienting and old
   macros in a 414-diagram selected sector. Their nonconvex support unions and
   distinct terminal attachment signatures explain why disjoint interchange
   and boundary swaps do not settle them.

Neither this experiment nor its counts establish seven grades, arbitrary-arity
completion, a native Resolve interpretation, or a source-signature freeze.
