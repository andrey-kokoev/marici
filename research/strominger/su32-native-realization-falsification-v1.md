# Falsification attempt: one native coherent four-record realization

## Conjecture and decision

> The four central comparisons are restrictions of one native four-record realization, with a source-defined coherence witness connecting the two reconciliation routes—not merely compatible descriptions.

**Decision: underdetermined by the audited native specification.** No contradiction among the supplied requirements was found. The existing implementation does not supply the restrictions and higher witness needed to establish the conjecture. Missing maps are not a proof that the proposed realization is impossible.

The result specifically rules out treating our previous data-recovery checks as verification of a native tetrahedral filler.

## Fixed test domain

Use `reading:0:-1`, its incoming N `neutron:0,0,2,1`, central N `neutron:1,1,1,0`, and explicit sign binding `[0,0]`. Independently rebuild the actual obligation sites and the complete comparison domain through four interfaces from the native 51-cell geometry.

No other occurrence charts or middle-routing candidates are used to select orders or fill missing operations. No circular orders or simplex attachments are introduced.

## 1. What the comparisons actually retain

The four central candidate comparison trees have the four three-label supports. Each retains **two** channel operands, not three simplex edges:

| Ternary support | Existing channel operands | Additional pair needed for proposed ordinary triangle |
|---|---|---|
| P+, P-, E+ | P+E+, P-E+ | P+P- at E+ |
| P+, P-, E- | P+E-, P-E- | P+P- at E- |
| P+, E+, E- | P+E+, P+E- | E+E- at P+ |
| P-, E+, E- | P-E+, P-E- | E+E- at P- |

Of the twelve putative triangle-edge restrictions, eight have an existing channel child in the candidate tree. Four would require an additional restriction interpretation.

Importantly, **the same-role comparisons are not absent**: comparing P+ with P- at E+ is exactly one central comparison's purpose. What is absent is a supplied rule making the two differently referenced P/P comparisons restrictions to one common edge object, or identifying their contexts coherently. Likewise for E/E. Absence of a channel with a same-role support does not prove that no contextual pair object could ever serve this purpose.

Thus the native entry diagram provides contextual comparisons/spans. Its three-record support alone does not identify it with an ordinary triangle.

## 2. Data consistency succeeds

All six pairwise intersections of the four ternary record supports agree in record identities, reference-cell identities and payloads. On cross-P/E intersections, the two candidate faces retain exactly the same channel operand tree.

On a same-role intersection, projected record dictionaries agree, but the original comparisons retain different opposite-role references and different comparison locations. Agreement after forgetting that context is not a native context-identification operation.

The checker exercises all sixteen Boolean assignments plus one independently tagged/provenanced registry:

- **17 data cases**;
- **408 commuting restriction checks**;
- both reconciliations recover the same complete registry;
- the four ternary dictionaries are recoverable from either final registry;
- the other canonical reconciliation tree can be reconstructed from the recovered registry.

These projections are explicitly implemented only as ordinary data operations in the audit. They are not registered or described as native restrictions.

A sensitivity control changes the shared record in an otherwise valid operand. The existing comparison rejects it. Thus the checker would detect that kind of actual compatibility contradiction; none occurs in the sourced test case.

## 3. What reconciliation adds—and what it does not

`byE` contains the two E-referenced P comparisons. `byP` contains the two P-referenced E comparisons. Each has two immediate children; together they retain all four comparison trees.

The `agreement` wrapper stores both complete derivations and their equal final record dictionaries. Its explicit field is

```
nativeFiller: null
```

An ordinary container holding both trees is not automatically a 3-simplex with specified face operators. Nor is recomputing the other canonical tree from the registry a source-supplied higher comparison. Such recomputation shows information sufficiency, not an admitted filling law.

The source is explicit even before the higher-filler question:

- all **four required prefix comparison maps** remain unbound;
- their `fillingWitness` fields are null;
- the full entrance-to-center cone contains **16 presentations and 20 context moves**, with **zero supplied move witnesses**;
- its **five graph cycle-basis elements** have no supplied fillers.

These graph cycle counts are diagnostics, not a claim that filling five chosen cycles would constitute a complete higher coherence theory.

## First missing objects

1. Native ternary-to-pair restriction operations, especially a common meaning for the same-role pair across its two opposite-role reference contexts. If these are contextual edge objects rather than bare pairs, specify their types and identification maps.
2. A native higher comparison between the two reconciliation routes, with its actual boundary, preservation requirements and coherence laws.

The source's null map/witness fields and the inspected API establish the absence in this bounded implementation. They do not establish a mathematical impossibility or exclude future operations.

## Consequence for K(Z,2)

The audit does not license choosing either a tetrahedral boundary or a filled tetrahedron as the native simplicial base. It therefore does not proceed to circular-order enumeration or a Chern cocycle.

The useful distinction is now explicit:

- **Record-level joint realization:** supplied by the candidate common registry; restrictions commute as ordinary projections.
- **Native operational joint realization:** not specified by the audited source.

The conjecture remains open at that second level. Continuing by freely adding the missing maps would test a new model, not falsify or verify the present native claim.

## Verification

```sh
node research/strominger/checkers/check_su32_native_realization_falsification.mjs
```

Fresh headless execution passes the audit assertions, not the conjecture. Source hashes are checked before use and retained in the receipt:

`results/su32-native-realization-falsification-v1/verification.json`.

It includes all four ternary restriction tables, their six shared-pair checks, contextual references, both route boundaries, native null-map evidence and the exposed comparison API. No native implementation was changed and no proof assistant was run.
