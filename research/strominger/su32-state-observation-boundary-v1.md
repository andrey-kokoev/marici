# Which packet distinctions must continuation preserve?

## Result

The source supports an **observation-relative information-state boundary**, not yet a physical state contract.

Two kinds of history must be separated:

- **Reference-selection log (`parent`, `operation`):** unnecessary for predicting the existing full current-state readout after further valid reference selections. It remains necessary for exact packet recovery and audit-history queries.
- **Retained comparison/reconciliation trees (`core.derivations`):** observable in the existing full current-state API, even when records and physical reference attachments agree. They cannot be discarded while claiming to preserve that API exactly.

No audited source-bound native continuation accepts these central packets and demonstrates a physical response to either distinction. Neither physical encoding of all histories nor their physical irrelevance follows.

## The tested observations

We distinguish tasks explicitly rather than calling every returned field physical:

| Task | Required distinctions |
|---|---|
| Exact recovery of the entire packet | All records, attachments, derivation trees and selection log |
| `currentCentralReferenceState` after any sequence of E-reference selections | Complete current core, including both derivations, and active reference; not the prior selection log |
| Explicitly reduced record/reference observation after those selections | Four attached records, occurrence and active reference; neither history class |
| Exact rooted reconstruction or recovery of opaque operands | Retained derivation ordering remains relevant |
| Native physical continuation | Required state distinctions remain unbound |

The reduced observation is a declared projection for this audit, not a newly admitted native API or permission to discard production data.

## 1. Selection logs do not affect the tested current-state task

Compare an initial E+ packet with the packet obtained after E+ → E- → E+. Both are valid; their complete cores, current references and current views agree, while their logs differ.

Applying any common subsequent selection word produces equal `currentCentralReferenceState` results. The implementation gives an all-word argument: selection retains the entire core and computes the new view only from that core and the requested reference. Induction extends the equality beyond the enumerated words.

The agreement is restricted to validated inputs. Invalid log entries are still rejected by admission checks. Thus a predictive quotient must not be confused with deleting required fields from an existing API input.

## 2. Derivation order remains visible in the existing current-state API

Use the original constructors to reverse the two channel children of the E+-referenced comparison, then reconstruct its reconciliation. The resulting central packet is valid and has exactly the same attached four records and active reference as the original.

Nevertheless:

- `view.sourceComparison` differs when that comparison is selected;
- `currentCentralReferenceState` differs before and after any common selection word, because it includes the retained core;
- record readout and central boundary agree;
- the two selection logs agree when the same commands are applied.

This is a real distinction in the candidate information API, but it is a retained syntax distinction—not a demonstrated native detector response. Source comments explicitly classify the comparison/reference operations as candidate information operations.

## 3. The retained derivation freedom is finite at fixed data

For a fixed layout, sign binding and four attached records:

1. Each channel operand is determined.
2. Each of the four comparisons has two admitted orders of its channel children.
3. Each of the two reconciliation routes has two admitted orders of its comparison children.

Consequently, the pair of retained reconciliation trees has exactly

```
2^4 × 2^2 = 64
```

distinct orderings. Two active-reference choices give **128 full current states**. The checker exhausts these cases for one structured record assignment. Equality here is the APIs' structural equality, not object allocation identity or serialized object-key order.

Thus the full current-state task requires, in principle, **six binary derivation choices plus one current-reference choice**, in addition to the complete attached record data and fixed occurrence. These are syntax distinctions, not a derivation of seven physical bits or modes.

The unbounded selection log is separate. Removing it from the prediction task does not require collapsing the 64 possible retained derivations.

## 4. Record and attachment requirements cannot simply be dropped

An E+ view with the same P/P active pair and E+ record can conceal two different E- complement records. The already supplied E- selection exposes that difference. Keeping only the active ternary data is therefore insufficient even for the reduced future-reference task.

Changing reference cells or using another occurrence/sign binding is rejected by current validation. These are typed-interface requirements. A physical gauge equivalence or relabelling law cannot be inferred by forgetting the corresponding fields.

No physical payload alphabet or numerical precision bound is supplied by these operations: payloads remain arbitrary JSON-compatible data. Therefore the earlier finite-numerical-receiver obstruction still applies to universal exact record recovery. Separating audit logs does not remove that independent capacity mismatch.

## Verification and scope of the source audit

Across four bindings and 17 record assignments:

- **68 preparations**;
- **476 equal-current-state checks** for different prior selection logs;
- **476 reduced-data agreements** for different retained derivations;
- **476 full-current-state distinctions** for those same derivations;
- exhaustive **64-core / 128-current-state** fixed-data census;
- four admission controls for missing derivations, an invalid log, wrong reference attachment and a foreign binding.

The command words tested have length at most two; the arbitrary-word statement above is justified by source inspection and induction, not exhaustive testing.

A bounded consumer search found the packet imports in the comparison/reference candidate adapters and their checkers. The existing native-continuation audit was replayed successfully: the wire interface has no bound four-record continuation, and the marked coefficient model remains a different carrier without a supplied packet encoder/attachment. This does not establish that no future native operation could distinguish the histories.

## Contract boundary to retain

For now, maintain separate claims:

- **Audit retention:** keep the complete existing packet unchanged.
- **Current candidate API:** attached records, both retained derivations and active reference determine future current-state observations.
- **Physical receiver state:** unspecified until a source-bound operation fixes its admissible inputs and observable outputs.

No adapter, production state reduction or physical history-erasure law was installed. In particular, an encoding that preserves only the reduced data must not be advertised as exact recovery of the original packet.

## Artifacts

- Checker: `checkers/check_su32_state_observation_boundary.mjs`.
- Receipt: `results/su32-state-observation-boundary-v1/verification.json`.

```sh
node research/strominger/checkers/check_su32_state_observation_boundary.mjs
```

Fresh headless execution, central-reference regression and native-continuation audit all passed their assertions. No proof assistant was run; the physical state contract remains explicitly null.
