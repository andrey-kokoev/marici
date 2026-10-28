# Root-independent attachment on the comparison motif

## Result

A single proposed undirected attachment rule supports all four boundary-root choices of the existing two-operation motif. Exact retained records, reference attachments and constructor histories survive, and reconstruction agrees with the existing rooted gluing adapter.

**The absence of reversed arrows from the earlier forward-only reading was not an algebraic attachment obstruction.** Under an explicit bidirectional retained-packet policy, the original shared-face incidence supports the tested queries without conflict.

This is a conditional construction, not evidence that native dynamics already supplies that policy. All 104 supplied interface witnesses remain null; no native reverse operation has been added.

## Carrier and assignment before local evaluation

The construction first records the entire native shared-interface inventory: 104 faces of the 51-cell carrier, their two actual cell-face occurrences, and their original witness fields.

On each interface, orientation reversal swaps its two occurrences and leaves the shared face fixed. This is a fixed-point-free involution on oriented interface occurrences. It does not reverse P/E reference signs, identify different references, or supply a cyclic action on operations.

A complete test motif is then fixed, independently of the root or payloads:

```
a ----\
       C ----\
b ----/       R ---- out
other -------/
```

C is the E+-referenced comparison; R is reconciliation; `other` is the complete E--referenced comparison supplied as an opaque boundary operand. The four physical wires are original shared faces among five cells. The `R--out` link is a **local readout at central N**, not a fifth physical face.

The complete tree is oriented toward the chosen boundary using global distances, before any local reader is evaluated. Local recovery does not grow or choose the wiring. The rest of the 51-cell carrier is retained as incidence data, not assigned a new routing or a complete native dynamics.

## One attachment rule

Every wire has a root-independent packet type:

- node kind and occurrence/sign binding;
- retained construction origin;
- record labels and their exact reference-cell attachments.

The added carriage policy allows the matching complete packet in either direction across its native shared face. A separate envelope identifies the actual sending and receiving face occurrences. The packet's `at` field remains its original constructor location; it is not silently rewritten to the current receiver.

At an operation vertex, any missing port is recovered by satisfying the **same original constructor equation**. A missing forward output is constructed normally. A missing prior operand is extracted from the supplied full retained output, and the original operation is recomputed to check that the other supplied operand agrees. All full packet types are checked on their wires.

Thus the construction separates three items that must not be conflated:

1. Original undirected physical incidence.
2. Proposed bidirectional carriage and relational recovery.
3. Native execution authority, which is still absent.

Original constructor histories remain directed histories. Selecting a different query output does not reverse their causal interpretation.

## Checks

Across four sign bindings, all 16 Boolean four-record registries, one structured/provenance-bearing registry, and both retained child orders of the opaque comparison:

- **136 complete boundary assignments**;
- **544 missing-boundary recoveries**, covering every root;
- **544 agreements with original rooted gluing**;
- **2,176 subsequent root-change checks**;
- **2,176 physical-interface message checks**, including **680 reversed messages**;
- **544 local readout traversals**, separately classified rather than counted as physical interfaces;
- **10 negative controls**.

Every physical message preserves its original face-occurrence identities, packet origin, reference cells, payloads and nested history. Inputs and the prepared problem remain unchanged.

Negative controls reject wrong bindings, nonincident faces, duplicated operation slots, wrong origins, a fabricated physical output face, missing or overprovided boundary data, and removal of required histories. A separately valid opaque comparison with inconsistent shared payloads also fails: native incidence and matching types do not waive the existing record-consistency condition.

The layer-4 comparison and previous rooted-gluing regressions passed fresh headless execution.

## What was assumed, not derived

The positive result requires:

- permission for bidirectional carriage of compatible retained packets;
- a distinction between retained construction origin and current message endpoint;
- permission to query the retained operation relation at a formerly incoming port;
- complete compatible retained states, including provenance where needed.

None is inferred solely from geometric adjacency. No shared-interface native witness, color involution on operation types, unit, higher filler, physical inverse or autonomous root-selection law is installed.

There is also a concrete remaining boundary issue: the original reconciliation output is a **state at central N**, not yet a selected outgoing face with an admitted payload operation. Treating this readout as another physical boundary port would require an additional attachment/continuation map. The checker expressly refuses to invent that face.

The bounded conclusion is therefore:

> Root choice can be a presentation choice for compatible retained-state queries on this motif, with one consistent undirected attachment extension. It is not yet shown to be a presentation choice for native physical execution.

## Artifacts

- Adapter: `su32-undirected-reference-attachment.mjs`.
- Checker: `checkers/check_su32_undirected_reference_attachment.mjs`.
- Receipt: `results/su32-undirected-reference-attachment-v1/verification.json`.

```sh
node research/strominger/checkers/check_su32_undirected_reference_attachment.mjs
```

The receipt includes the fixed carrier/problem, a complete boundary assignment, a reversed recovery certificate, original native witness fields and source hashes. Existing comparison and geometry implementations were not modified.
