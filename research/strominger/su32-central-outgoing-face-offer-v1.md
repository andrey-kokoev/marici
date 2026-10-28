# Root-independence conjecture: conditional theorem and outgoing-face gate

## Outcome

The information-level part can be made precise as a conditional tree theorem. The stronger native claim remains unverified.

A complete central packet can be offered losslessly at any one of its four actual outgoing faces, **if that face is supplied as a control parameter**. This requires no additional independent P/E record and preserves both derivations and the entire reference-selection history. But it is a product-like data envelope, not a proved encoding into native face states or an executed continuation.

The existing constraints admit four distinct offers for exactly the same complete packet. They do not select one. All four outgoing receiver sites lie outside the existing layer-4 comparison grammar; sourced later comparison boundaries still have null maps and filling witnesses.

## 1. Precise relative tree statement

Let each local operation be a deterministic partial constructor

```
F : D ⊆ X × Y → Z
```

whose full result retains the exact ordered input pair, so a left inverse on its image recovers `(x,y)` from `F(x,y)`. Use the single relation

```
R = {(x,y,F(x,y)) : (x,y) ∈ D}.
```

Fix a finite tree of these relations. Each port has a fixed type; internal edges identify complete typed values, with no port reuse or omitted provenance. Boundary ports are leaves. Fix all boundary values except one, and assume a compatible complete assignment exists.

**Claim.** The missing boundary value and every internal edge value are uniquely determined. Recovery is independent of the order of valid tree contractions.

**Argument.** Any two specified ports of a local relation determine at most one value of the third: the forward case uses determinism; either reverse case extracts the retained input from the specified full output and checks the other input. Orient the whole tree toward the missing boundary. Starting at its other boundary leaves, propagate this unique local completion toward the root. Induction on distance through the finite tree proves that every message equals the corresponding value of any compatible global assignment. The assumed assignment guarantees existence at every step. Thus all internal values and the final missing boundary are unique. Contracting connected subtrees merely performs portions of this same elimination; relational gluing is existential matching of the same internal variables, so changing contraction order cannot change the result.

`compareAt` and `reconcileAt` satisfy the local hypotheses on their admitted ordered profiles: both are deterministic on validated inputs, and both store exact `children` in the output. The theorem therefore applies to any finite tree that actually satisfies these typing and compatibility hypotheses.

This is a mathematical induction argument, not a proof-assistant result or an assertion that arbitrary geometrical trees admit these operation profiles. It supplies neither universal existence for arbitrary boundary data nor native permission to query reversed ports. It also does not identify differently ordered constructor histories. Cyclic networks are outside the tree hypothesis.

## 2. The outgoing-face experiment

The carrier is fixed first: the original 51-cell incidence domain for `reading:0:-1`. The four arrows leaving central N are matched to their exact native shared-face occurrences before any packet is offered.

An offer has the form

```
L_f(s) = (actual attachment f, complete retained packet s,
          externally supplied face-choice authority, nativeExecution = null).
```

For each permitted face `f`, recovering the packet gives `recover(L_f(s)) = s`. The packet's central occurrence is not rewritten to the receiver cell. No new record is padded into its core, and neither reconciliation derivation is discarded.

An offer is intentionally named an **offer**, not transport: no native carrier capacity, face encoding, receiving operation or execution has been established. Its injectivity follows from retaining the input, not from a newly discovered physical law.

## 3. Tested cases and refusal witnesses

Across four sign bindings and 17 complete record registries (16 Boolean assignments and one structured/provenance-bearing assignment), test the initial central packet, a changed-reference packet, and a round-trip packet:

- **68 complete preparations**;
- **816 exact face-offer recoveries**;
- **816 data-level squares** comparing reference selection before versus after offering at a fixed supplied face;
- **272 history distinctions** preserved between initial and round-trip packets having equal cores;
- **10 negative controls**.

The negative controls reject an omitted face choice, nonexistent or incoming face, incorrect receiver/face occurrence, overwritten packet origin, missing independent record, replaced derivation, and claims of derived selection or native execution.

The receipt exhibits four offers of the **same full packet** with distinct physical destinations. This proves underdetermination by the checked constraints, not impossibility of a separately specified deterministic selector. A face label is additional routing control, not an independent fifth P/E record. In particular, no arbitrary choice of a lexicographically first face is presented as a sourced law.

All four outgoing destinations reject invocation through the current `compareAt` grammar with `Not a layer-4 comparison`. This is a scoped type refusal, not proof that no other continuation grammar could exist.

The source incidence domain also contains four two-step continuation comparison boundaries beginning at central N. Every one is explicitly `potential-comparison; authorization-unbound`, with `comparisonMap` and `fillingWitness` null. Their full alternatives are retained in the receipt.

## 4. Status of the stronger conjecture

The test separates three obligations:

1. **Preserve complete information at a supplied face:** a candidate envelope exists.
2. **Determine or authorize the outgoing face:** not supplied by the current constraints; may instead be an external control.
3. **Realize the offered packet as an admitted native face state and execute the receiving operation:** still unbound.

The stronger native conjecture is neither verified nor universally falsified. Lossless copying into an envelope cannot discharge the third obligation. The next substantive evidence would be a source-bound face-state encoding and receiver command, not another metadata wrapper or more copies of this enumeration.

No extra independent record was required by the candidate offer. No conclusion is drawn about information requirements of a future native implementation.

## Artifacts and verification

- Adapter: `su32-central-outgoing-face-offer.mjs`.
- Checker: `checkers/check_su32_central_outgoing_face_offer.mjs`.
- Receipt: `results/su32-central-outgoing-face-offer-v1/verification.json`.

```sh
node research/strominger/checkers/check_su32_central_outgoing_face_offer.mjs
```

Fresh headless execution passed the stated assertions. Central-reference completion and undirected-attachment regressions also passed. Existing source comparison and geometry implementations were unchanged. No native inverse, outgoing execution, cyclic action or higher filler was installed.
