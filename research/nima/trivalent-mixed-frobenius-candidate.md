# Inspecting the seven: a mixed Frobenius candidate

## Status

Finite exact model tests of a proposed mixed relation. **The relation is not
admitted to the calculus, derived from its existing rules, or a frozen source
signature.** This continues the [first census](reversible-trivalent-census-results.md).

Reproduce:

```text
python research/nima/checkers/check_trivalent_mixed_candidate.py
```

Evidence: `results/trivalent-mixed-candidate.json`, including the seven graphs,
ordered candidate boundaries, reversal action, integer tensor models, matrices,
counterexamples and checker hashes. All tests passed.

## 1. The seven diagrams, individually

Let M be the merge vertex with input slots 0,1 and output slot 0. Let S be
its split orientation with input slot 0 and output slots 0,1. External boundary
permutations are quotiented for this table; **local slots are not quotiented**.

| Name | Internal attachment | Boundary | Reversal |
|---|---|---|---|
| K | M.out0 → S.in0 | (2,2) | K |
| A00 | S.out0 → M.in0 | (2,2) | A00 |
| A01 | S.out0 → M.in1 | (2,2) | A10 |
| A10 | S.out1 → M.in0 | (2,2) | A01 |
| A11 | S.out1 → M.in1 | (2,2) | A11 |
| L_parallel | S.out0 → M.in0; S.out1 → M.in1 | (1,1) | L_parallel |
| L_crossed | S.out0 → M.in1; S.out1 → M.in0 | (1,1) | L_crossed |

All unused ports are external. Reversal uses the census convention and
relabels internal vertices afterward. The two L diagrams have parallel wires
and underlying cycle rank one, but no directed cycle. They cannot be compared
to K by a boundary-preserving 2-cell: their boundary types differ.

## 2. A structurally motivated, but additional, mixed comparison

A natural candidate is a merge/split slide: preserve the four external legs
while moving the merge past the split. With explicit ordered boundaries:

    K   = split ∘ merge
    F_L = (merge ⊗ id) ∘ (id ⊗ split)
    F_R = (id ⊗ merge) ∘ (split ⊗ id)

The candidate cells are K ⇒ F_L and K ⇒ F_R at boundary (2,2). Their strict
algebraic version is the **Frobenius law**. No units or counits are imposed here.
In the table, F_L is A01 and F_R is A10. Reversal fixes K and exchanges these
two routes, with the ordered boundary conventions checked explicitly.

Thus one candidate cell and reversal could supply this pair, once reversal's
action on cells is declared. Whether the cells are invertible and which higher
relations they satisfy remain further choices. “Slide” is a motivation, not a
derivation from wiring symmetry.

Adding just these elementary adjacencies to the two-vertex quotient gives:

    {A01, K, A10}, {A00}, {A11}, {L_parallel}, {L_crossed}.

This is five components, not a seven-stage chain. Boundary permutations do
not change the slots of an internal attachment. Relating A00 or A11 would
require additional justified structure, such as suitable local symmetry, or
additional cells. No conclusion about arbitrary contextual completion follows
from this elementary two-vertex graph.

## 3. Is this relation forced? An exact countermodel

Use the free rank-two integer module with basis (1, ε), with multiplication
of dual numbers:

    1·1=1,   1·ε=ε·1=ε,   ε·ε=0.

Let split be the matrix transpose of this multiplication in that basis:

    split(1)=1⊗1,
    split(ε)=1⊗ε + ε⊗1.

The checker verifies associativity and coassociativity as complete integer
matrix equalities. Reversal is interpreted by actual matrix transpose, a
stronger property than the proposal requires. Nonetheless:

    K(ε⊗ε)=0,
    F_L(ε⊗ε)=ε⊗ε,
    F_R(ε⊗ε)=ε⊗ε.

Both Frobenius equalities fail. Therefore Frobenius is **not an equational
consequence** of associativity, coassociativity and transpose reversal. The
model does not prohibit adding a higher comparison in a richer target; it
shows that such a comparison is additional structure rather than a forced
strict identity.

## 4. Is the candidate consistent, and does it force inverse laws?

Two more exact models distinguish those questions.

### Copy/merge model

For basis e0,e1, take

    merge(ei⊗ej) = ei if i=j, else 0,
    split(ei) = ei⊗ei.

Both Frobenius equalities hold. Here L_parallel=id and K is the projector
onto the diagonal span. This witnesses that the candidate has a nonzero
strict model; it is not a proof of universal higher coherence.

### Scaled copy/merge model

Scale **both** maps by 2, preserving the transpose relationship. Associativity,
coassociativity and both Frobenius equalities still hold. But now

    L_parallel = 4 id,
    K = 4 P,
    K² = 16 P ≠ K,

where P is the diagonal projector. Consequently Frobenius does **not** force
L=id or K²=K; normalization or a specialness law would be extra structure.
This supports keeping the proposal's original non-assumptions intact.

## 5. Meaning and next decision

The seven-diagram inventory now has a concrete interpretation: one central
merge/split route, four single-wire returns with distinct attachment slots,
and two double-wire returns. A familiar mixed comparison links only three
of them under the present conventions.

The tests support studying a Frobenius-style extension, but do not select it
uniquely. The countermodel is a useful boundary: the original data are
insufficient to derive this candidate law. Calling the seven objects grades
would still require a new definition and additional evidence.

The [contextual overlap experiment](trivalent-contextual-overlap-results.md)
now tests that extension through three vertices. Outward slides have unjoined
same-support forks; inward slides have 32 unjoined shared-vertex forks. Neither
orientation is confluent in the tested DAG sector. Sixteen nonconvex inward
matches are excluded because replacement would create a directed cycle.

Next executable step: test alternative orientations or derived composite
rewrites with explicit provenance, then rerun the overlap census. Compare the original and extended systems; do not retroactively count
candidate cells as consequences of the primitive syntax. Cyclic gluing and
local-slot quotients should remain separate experiments.
