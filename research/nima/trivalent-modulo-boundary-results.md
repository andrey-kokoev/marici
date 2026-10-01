# Normalization modulo boundary symmetry, with retained recovery

## Status and reproduction

Bounded computational result following the
[residual symmetry obstruction](trivalent-residual-completion-results.md).
The experiment explicitly quotients external input/output permutations, while
retaining local slot distinctions and enough evidence to recover the ordered
representative. It does not identify ordered operations as equal.

```text
python research/nima/checkers/check_trivalent_modulo_boundary.py
```

Evidence: `results/trivalent-modulo-boundary.json`. The checker verifies the
hash-bound chain of prior reports/checkers, and records quotient graphs,
ordered lifts, normalization ledgers, topological order and semantic controls.
All assertions pass.

## 1. The declared quotient and rewrite system

At boundary (m,n), quotient the full external action S_m × S_n. Internal
vertices are still identified only by slot-preserving graph isomorphism; local
merge-input and split-output slots are not independently quotiented.

Use the previously selected elementary directions:

    α forward; reversed α backward; K→F_L; F_R→K.

The system remains the experimental Frobenius extension, not the original
primitive calculus. Derived residual terminal-swap macros are **not** needed
as extra quotient reductions: all their placements lie within boundary orbits.

This tests the same closed DAG census with one through three vertices. It does
not establish that forgetting all boundary order is appropriate for every
application, or that the quotient is compatible with arbitrary ordered gluing.

## 2. Quotient results

| Quantity | Result |
|---|---:|
| Ordered canonical diagrams | 874 |
| Boundary-permutation orbits | 95 |
| Distinct nontrivial directed quotient edges | 72 |
| Terminal quotient normal forms | 33 |
| Maximum length of the chosen normalization strategy | 5 |
| Exact ordered-representative round trips | 874 / 874 |
| Boundary-action invariance checks | 12,442 |

A topological sort covers all 95 quotient nodes: there is no directed cycle.
For each node, the checker computes **all** reachable terminal nodes, not merely
a preferred one. Each set is a singleton. Thus termination and unique normal
forms hold for this finite quotient rewrite graph.

This is not a general-arities convergence theorem. It is also not a seven-grade
result: 33 counts terminal representatives of this particular bounded quotient.

## 3. What the retained record contains

For each ordered canonical input diagram, the chosen finite strategy stores:

1. The boundary permutations and internal vertex renaming that place the
   current representative at an available ordered lift of the next quotient
   edge.
2. The primitive rule placement used there.
3. The internal renaming used to canonicalize its target.
4. A final boundary/vertex transport into the terminal quotient representative.

Recovery starts from that terminal representative. It undoes the final
transport, then reverses the recorded rules and symmetry transports. The
checker reconstructs the exact original ordered canonical graph in all 874
cases; recovery does not consult the source-ID label in the ledger.

Recovery uses invertibility of the experimental comparison cells. It is not a
forward reduction and does not follow from primitive orientation reversal alone.
The ledger retains a path, not a canonical higher proof that every possible
path agrees.

The normal form alone is insufficient: there are terminal ordered diagrams
whose nontrivial boundary permutations are lost if the final witness is erased.
The checker records concrete failure examples. Even with a unique quotient
normal form, ordered data must not be silently discarded.

## 4. Semantic countercontrol: order genuinely matters

To test that boundary quotienting is a representation choice rather than a
universal equality, use the noncommutative algebra of 2×2 integer matrices.
The basis elements are E00,E01,E10,E11, with

    E_ij E_kl = delta(j,k) E_il.

Let split be transpose multiplication in this basis. The checker verifies
associativity, coassociativity and both experimental Frobenius equations as
complete integer matrix identities.

Nevertheless, at the primitive merge:

    E00 * E01 = E01,
    E01 * E00 = 0.

Merge and merge-with-swapped-input-order belong to the same external-boundary
orbit but are **different ordered linear maps**, even in a model satisfying the
experimental laws. Thus a quotient normal form cannot replace an ordered map
without its boundary transport information.

This is stronger than merely observing different graph labels: it witnesses
semantic loss from treating the quotient alone as the operation.

## 5. What has and has not been established

Established in this bounded Python experiment:

- the particular quotient rewrite graph is acyclic and uniquely normalizing;
- the residual terminal-swap macros collapse to symmetry, not additional
  reductions;
- every ordered canonical input has an exact replay/recovery ledger;
- quotient normal forms are invariant under the tested boundary action;
- forgetting the ledger can lose both syntactic ordering and semantic behavior.

Not established:

- a globally convergent presentation at larger vertex counts;
- context-compatible normalization for arbitrary ordered gluing;
- equality or uniqueness of retained comparison paths or higher fillers;
- a source-signature freeze, native Resolve interpretation, or DG interpretation;
- a canonical seven-grade structure.

## 6. Next executable test

Test composition of these retained normalizations: normalize diagrams, glue
specified ordered output/input ports using their stored transports, and compare
with gluing first and normalizing afterward. The glued graph must stay within
the declared DAG/connected sector; unsupported cases must be rejected, not
silently quotiented away.

The [retained-gluing test](trivalent-retained-gluing-results.md) now checks all
1,572 such gluings within three total vertices. Transported composition agrees
in quotient normal form and in a noncommutative Frobenius model, with explicit
contextual paths and exact composite recovery. Naive gluing without transport
changes the map in 1,167 cases. Twenty cases retain different ordered terminal
representatives, so strict path-independent composition is not established.
Next test those comparison loops and two nontrivial operands at four vertices.
