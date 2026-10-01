# First reversible trivalent census

## Status

Executable finite combinatorial test of the
[proposal](reversible-trivalent-coherence-calculus-proposal.md), not a proof of
its generation conjecture or a new grammar admission.

Reproduce:

```text
python research/nima/checkers/check_reversible_trivalent_census.py --write
```

Full canonical diagrams, automorphism actions, reversal indices, rewrite
adjacencies, configuration and checker hash are in
`results/reversible-trivalent-census.json`. The checker runs its tests on every
invocation. Results below are for one through three vertices.

## Declared experiment conventions

- Connected underlying undirected graph; directed acyclic wiring.
- No self-loops. Parallel wires are allowed. An underlying undirected cycle
  can occur even though a directed cycle cannot.
- Local input/output slots remain distinguishable.
- Graph isomorphism relabels internal vertices while preserving orientations,
  slot numbers and, in the ordered sector, boundary positions.
- Two sectors: ordered external boundaries; quotient by independent external
  input/output permutations. Counts are not combined across sectors.
- Reversal swaps merge/split, reverses wires and exchanges input/output lists,
  preserving slot numbers. This is a chosen extension of primitive reversal.
- Only merge associativity and its reversal generate rewrite adjacency.
  Adjacency is undirected; neither mixed generators nor higher fillers are
  supplied. Permuting the boundary is not an associativity rewrite.
- Zero-vertex identities and directed-cycle sectors are excluded.

## Results

| Quantity | Ordered boundary | Boundary-permutation quotient |
|---|---:|---:|
| All connected diagrams, 1–3 vertices | 874 | 95 |
| Pure three-vertex (4,1) diagrams | 120 | 5 |
| Pure (4,1) rewrite components | 24 pentagons | 1 pentagon |
| Mixed two-vertex (2,2) diagrams | 20 | 5 |
| Mixed two-vertex (1,1) diagrams | 2 | 2 |
| Mixed two-vertex total | 22 | 7 |
| Mixed two-vertex rewrite edges | 0 | 0 |
| Mixed three-vertex (3,2) diagrams | 264 | 22 |
| Mixed (3,2) rewrite components | 96 singletons + 84 pairs | 8 singletons + 7 pairs |

Reversal produces the corresponding (1,4) and (2,3) counts. All mixed
components in this census have cycle rank zero for the simple undirected
associativity/reversal rewrite graph. This does not classify cycles in a
rewrite multigraph or in a higher completion.

### What the seven actually counts

In the boundary-permutation quotient, exactly one merge and one split give:

1. Merge output to split input: one attachment, boundary (2,2).
2. One split output to one merge input: 2×2=4 attachments, boundary (2,2).
3. Both split outputs to both merge inputs: 2!=2 attachments, boundary (1,1).

Thus this precisely specified sector has **1+4+2=7 diagram classes**. Seven
was not an input to enumeration. The third case depends on allowing parallel
wires. Keeping boundary order yields 4+16+2=22 classes. Removing parallel
wires would remove the two double-wire classes, leaving five quotient classes.

This is a candidate explanation of a small seven-count, not the proposed
port-plus-comparison calculation 2(2+1)+1. These seven objects are diagrams
across two boundary types, not seven dimensions or seven essential coherence
cells. None has an associativity/reversal edge at this vertex bound, because
both orientations occur only once. No additional mixed comparison has been
derived. A claim of canonical seven grades still needs a definition of grades
and a principled reason for the quotient and graph conventions.

The seven rewrite edges in the quotient three-vertex (3,2) sector count a
*different* kind of object; they must not be conflated with these seven diagrams.

### What the pentagon establishes

For pure four-input merge trees, the checker finds five shapes and degree-two
adjacency at each shape, forming a pentagon. With ordered boundary labels,
there are 24 components corresponding to leaf orders. This verifies the
expected low-arity combinatorics of the explicitly admitted associativity
move. It does not derive the move from the vertex or fill the pentagon.

## Checks performed

- Every port occurs exactly once as internal or external incidence.
- Connectivity and directed acyclicity of every graph and rewrite result.
- 3V=2E+B, B=V+2−2b₁, and n−m=S−M.
- Reversal involution, closure of the census under reversal, and reversal
  equivariance of rewrite adjacency.
- Relabelling invariance on explicit fixtures; canonicalization by all vertex
  permutations in the finite bound.
- Automorphism identity and composition closure, with boundary actions stored.
- Orbit–stabilizer mass agrees with labelled enumeration in both sectors.
- Pure four-input components have five vertices, cycle rank one and degree two.
- Rejection fixtures for self-loops, directed cycles and disconnected graphs;
  a parallel-wire fixture is accepted.

These are Python exhaustive finite checks, not Agda proofs or an independent
second implementation. The orbit count is a consistency check against the
pre-quotient enumeration, not a separate generation algorithm.

## Follow-up: inspecting the mixed diagrams

[Mixed Frobenius candidate](trivalent-mixed-frobenius-candidate.md) names all
seven diagrams and tests a specific merge/split slide. Exact integer models
show that associativity/coassociativity do not force this candidate, even with
transpose reversal. Other models satisfy it without inverse/projector laws.
The candidate remains additional, unadmitted structure.

## Conclusions and next tests

The pure-tree prediction is supported in the tested bound. The smallest mixed
sector gives a **conditional seven-diagram count**, but no mixed coherence
connections. Free associativity/reversal alone does not connect that sector.
This is not a falsification of a specified mixed semantic comparison: no such
comparison has yet been supplied.

Next executable work:

1. Make parallel-wire/cycle conventions configurable and compare the seven
   count across those sectors, without changing local slot distinctions.
2. Specify one candidate mixed 2-cell with an exact boundary and semantic or
   structural justification; do not infer it from shared boundary alone.
3. Preserve rewrite placements as a multigraph and enumerate contextual
   critical overlaps before proposing higher fillers.
4. Define “essential grade/cell” before testing a seven-grade claim.

No source-signature freeze, global coherence theorem or interpretation of the
conditional DG model follows from this census.
