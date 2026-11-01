# Edge-five local operation transport and the remaining overlap transition

## Construction

The edge-three comparison/reconciliation fragment now transports to **all 44 edge-five comparison cones** in `reading:0:-1`.

`su32-cone-operation-transport.mjs` derives each translation from the source and target incoming N-cell centres. It then requires exact equality of translated native vertex sets, cell roles and kinds, all 14 cells, all internal shared-face incidences, and the entire set of 16 ordered paths. This is not a type assignment based on matching counts.

The target chart is the transported source occurrence chart. The original atlas constructor still rejects an edge-five fixture; its edge-three guard was neither changed nor bypassed by falsifying the fixture's edge size. Target operation evaluation calls the unchanged `channelOperand`, `compareAt` and `reconcileAt` implementations.

Only structural addresses, reference cells and occurrence anchors are transported. Opaque payloads are copied unchanged, including deliberately planted strings and nested fields that look like source-cell addresses.

## Checked local diagrams

For all 44 cones and all four sign bindings:

- native path identification covers 704 path presentations;
- 5,632 constructor-naturality tests compare transporting an edge-three output with computing the corresponding edge-five output;
- 5,632 full-history two-corolla reconstructions pass;
- 1,760 arc-duality checks preserve the typed opposite-incidence pairing;
- 1,584 cyclic-gluing checks pass;
- 704 structured-payload sentinel checks confirm that geometry transport does not rewrite content.

The Boolean enumeration includes both orders of the external comparison's retained children. This preserves distinctions that the previous header-only matching hostile showed cannot be discarded.

These are finite executable checks plus an explicit structural adapter, not a proof-assistant theorem for arbitrary payloads or all trees. The transported operations retain their source status as candidate information operations.

## Reference overlap is not equality of local signs

There are **56 cone pairs with nonempty initial-reference overlap**. Their restricted reference sections agree in all 16 pairs of sign bindings: 896 comparisons.

The comparison is indexed by the actual reference cell, retaining both chart contexts. The receipt exhibits a shared physical reference labelled differently in the two charts; matching the same local sign label instead picks a different payload.

The payload bank used here is an opaque cell-indexed test section. It tests restriction/reindexing, not the derivation of a physical state or a global operational section.

No initial reference occurs in three distinct cones: maximum reference multiplicity is two. Therefore there are **no nonempty triple-reference restrictions** to test. This is not evidence that higher operational coherence is automatic. The initial prototype's expectation of a nonempty triple test was rejected by the actual incidence census.

## The next transition is now localized

The cone audit finds **224 contextual cross-level contacts** at which one actual P/E cell is:

- an upstream comparison output, carrying three referenced records and two retained operand histories; and
- a downstream cone's reference, whose payload slot currently accepts opaque JSON.

Each contact is recorded with the two occurrence charts, actual cell, upstream reference support and children, and downstream reference type. Its `transitionFromExistingFibration` remains null.

Matching the cell alone does not specify the required map between these types. Nor does the fact that a comparison packet can be serialized as JSON establish the intended fibration transition. The next task is to **extract that transition from the existing content-bearing fibration**, preserve its context, and test its composites. This is not a request to invent a new interaction rule.

Thus local operation transport is established by the present checks; full overlap coherence of the operation fibres is not. The 44 cones have not been treated as independent complete copies whose separate success proves a global result.

## Hostiles and reproduction

The checker rejects a reversed path even though its cell inventory is unchanged, rejects a wrong native cell role, preserves the old atlas guard, and refutes raw-sign overlap matching.

```sh
node research/strominger/checkers/check_su32_edge5_operadic_transport.mjs
python research/aspect/scc/scc.py validate research/strominger/scc-models/su32-edge5-operadic-transport-v1.json
python research/aspect/scc/scc.py check strominger-su32-cyclic-port-fragment-v1
python research/aspect/scc/scc.py check strominger-su32-edge5-operadic-transport-v1
```

Both SCC checks pass through fresh-execution Python-to-Node adapters. The initial direct `.mjs` registration failed because SCC invokes Python; the two owner-local manifests now point to the adapters.

Contract: `contracts/su32-edge5-operadic-transport-v1.json`.
Receipt: `results/su32-edge5-operadic-transport-v1/verification.json`.

The receipt pins source hashes and retains all 44 cell maps, the 56 reference overlaps, all 224 typed transition obligations, a full transported operation example and the sign-matching counterexample. No previous operation/geometry module was modified; no proof assistant was run.
