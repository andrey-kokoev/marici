# Gluing retained normalizations: bounded composition test

## Status and reproduction

Follow-up to [boundary-modulo normalization](trivalent-modulo-boundary-results.md).
This tests actual port transport, contextual primitive paths and composite
readback, not just equality of quotient normal-form IDs.

```text
python research/nima/checkers/check_trivalent_retained_gluing.py
```

Evidence: `results/trivalent-retained-gluing.json`. It records every matching,
transported port index, external-order restoration, contextual primitive path,
normal form, negative controls and terminal discrepancies. The checker verifies
the hash-bound dependency chain before using prior report IDs. All assertions
pass.

## 1. Exact scope

Take ordered connected operands A and B from the existing DAG census, with at
most three vertices **in total**. Enumerate every nonempty injective matching
from selected outputs of A to selected inputs of B. Multiple joining wires
are allowed. All cross-operand wires point from A to B, so feedback is excluded.

The remaining external order is:

- inputs: all A inputs, then unconsumed B inputs;
- outputs: unconsumed A outputs, then all B outputs.

The checker rejects empty matchings, duplicated ports and out-of-range indices.
Zero-vertex identity operands are not included. At this bound, at most one
operand can have two vertices; this is not a test of composing two nontrivial
two-vertex normalization paths.

## 2. What is compared

### Direct route

Glue A and B at the declared ordered ports, then use the saved normalization
of that composite.

### Staged route

Normalize A and B separately while tracking which original boundary port each
current slot carries. Translate each selected joining port through these tags,
glue the normalized operands, and restore the declared remaining external
order. Normalize this transported composite afterward.

For each case, the checker also lifts every primitive operand-normalization
step through the gluing. Each lifted step must be an actual rule placement in
the existing ordered census. This gives an explicit contextual path from the
direct composite to the transported staged composite.

Finally, reverse the staged composite's retained normalization and then the
contextual path. This reconstructs the original direct ordered composite.
As before, inverse comparisons belong to the experimental reversible extension;
primitive orientation reversal alone does not supply them.

## 3. Results

| Total vertices | Joining wires | Cases |
|---|---:|---:|
| 2 | 1 | 36 |
| 2 | 2 | 8 |
| 3 | 1 | 1,080 |
| 3 | 2 | 448 |
| **Total** | | **1,572** |

All 1,572 cases pass:

- valid DAG incidence after both gluings;
- correct transport of joined ports and remaining external order;
- equality of quotient normal forms;
- explicit lifting of operand rewrites to contextual primitive paths;
- exact composite round-trip recovery;
- equality of represented integer linear maps in the declared noncommutative
  Frobenius test model.

## 4. Forgetting transport fails

The negative control glues the normalized operands using the *old numeric
port indices*, without transporting them or restoring external order.

- It differs syntactically from the correctly transported staged composite in
  **1,351** cases.
- It changes the represented map in **1,167** cases in the test model.

These are model- and convention-specific counts, not a universal failure rate.
They demonstrate that the transport ledger is doing real work: matching
quotient classes alone does not determine ordered composition.

The semantic model is the rank-two integer left-zero semigroup algebra:

    e_i * e_j = e_i,
    split(e_i) = e_i ⊗ (e_0 + e_1).

Multiplication is noncommutative and split is its matrix transpose. Before
checking composite maps, the checker verifies associativity, coassociativity
and both experimental Frobenius equalities as complete integer matrices.
No claim of faithfulness of this model is made; distinct diagrams may have
the same represented map.

## 5. A real qualification: transport is not path-independent

There are **20 cases** where direct and staged normalization end at different
ordered terminal representatives, although they share the same quotient normal
form and represented map:

- 8 cases use the saved terminal pair 272/273 at boundary (2,1);
- 12 cases use pair 626/627 at boundary (1,2).

These are precisely the terminal-swap pairs identified in the earlier residual
completion test. For example, saved operand IDs 440 and 0, glued along output/
input pairs (0,0) and (1,1), give direct terminal 272 and staged terminal 273,
both in quotient normal orbit 27.

Thus the staged construction is compatible **with retained comparison and
boundary-transport evidence**, not by strict identity of ordered terminal
representatives. The test does not identify the two paths by a higher cell.
Keeping that distinction avoids turning bounded quotient convergence into an
unsupported strict compositionality claim.

## 6. What this establishes

Within the stated bound, normal-form-plus-retained-transport supports the tested
one-way ordered gluings without losing the original composite. The witness
paths are essential. Normal form alone does not support those gluings reliably.

Not established:

- arbitrary-arity or arbitrary-context compositionality;
- feedback, self-gluing, or disconnected tensor contexts;
- gluing two independently nontrivial two-vertex normalizations;
- equality, uniqueness or higher coherence of the direct and staged paths;
- a native Resolve or DG interpretation, source-signature freeze, or seven-grade
  conclusion.

## 7. Next executable work

The [retained-loop analysis](trivalent-transport-loop-results.md) now replays
all 20 discrepancies. They form two boundary-action/path-inversion orbits,
exactly the earlier residual families, with three primitive steps each. All
208 compatible pair compositions have identity boundary return; no contraction
of the retained paths is inferred. Next test overlapping four-vertex contexts.

The [four-vertex interchange test](trivalent-four-vertex-interchange-results.md)
now checks that selected extension: 20 nontrivial operands, 3,168 gluings and
4,320 elementary disjoint-support squares pass, with exact labelled graph
agreement and two-route recovery. No whole-composite four-vertex normal form
is computed. The 20 terminal-swap discrepancies and overlapping-support
coherence remain separate questions.
