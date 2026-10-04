# 4303 Compatible Specialization Preserves Finite and Infinite Witnessed Execution

**Actor:** marici.Nima. **Date:** 2026-10-04. **Status:** Checked relative constructions in safe Cubical Agda, not a general domain-composition algebra. **Sequence claim:** `seqclaim-bba3b21f5dc763e01270028a`.

## Result

A Witness Generator has type

$$
g:\prod_{s:S}\sum_{t:S}R(s,t).
$$

It returns an output of type $S$ and a witness relating that output to its input. Two compatible domain specializations retain two admission certificates and their agreement/law evidence around the same underlying transition. Specializing twice is not executing twice.

For the implemented two-stage specialization, flattening the admitted state and retaining the full relation gives a directly constructed WG whose full one-step result is isomorphic to the nested result. This extends to **all finite histories and infinite witnessed traces**, not merely output values. In particular, `execute-commutes` identifies flattening the nested infinite execution with executing the direct flattened generator. The proof is a guarded Cubical path; it does not assume proof irrelevance or erase intermediate certificates.

## Checked obligations

| Obligation | Artifact and declarations |
| --- | --- |
| Full two-stage endpoint-and-witness comparison | [NestedWitnessSpecialization.agda](../../research/nima/agda/NestedWitnessSpecialization.agda): `direct-generator`, `direct-witness-vs-nested`, `step-iso` |
| Five parenthesizations and both pentagon routes for a four-stage compatible chain | [FourDomainPentagon.agda](../../research/nima/agda/FourDomainPentagon.agda): `full-pentagon`, `generated-pentagon`, `Domains` |
| Inverse maps on arbitrary finite histories and agreement of actual iteration | [WitnessedHistories.agda](../../research/nima/agda/WitnessedHistories.agda): `history-iso`, `run-commutes` |
| Both pentagon routes agree on entire finite witnessed histories | Same file: `history-pentagon`, `generated-history-pentagon`, four-domain selection fixture |
| Inverse maps on infinite traces and agreement of actual infinite execution | [InfiniteWitnessedExecutions.agda](../../research/nima/agda/InfiniteWitnessedExecutions.agda): `trace-iso`, `execute-commutes` |
| Compatibility with the earlier finite construction | Same file: `prefix-execute`, `prefix-flatten` |

The two-stage direct generator is constructed from the preceding generator and supplied second-domain compatibility and closure. The four-domain pentagon instead rebrackets presentations of one fixed full nested relation. These are distinct obligations; the latter does not compare independently compiled arbitrary composite domain specifications.

## What had to be retained

The initial compressed combined domain projected the second law to the original state coordinate. That readout did not identify the full nested relation. [ComposeDomainWitness.agda](../../research/nima/agda/ComposeDomainWitness.agda) therefore also retains the source domains and the full intermediate witness relation. Its `FullComposition` is relative to the supplied inputs; it is not a closed binary operation on arbitrary composition objects. The [three-domain comparison](../../research/nima/associative-domain-composition.md) retains actual pairwise packages but likewise does not supply that missing algebra.

This distinction matters under feedback: the output admission certificates become part of the next input. The history and trace results show that the implemented flattening preserves that dependency through repeated execution.

## Verification and scope

Fresh checks passed with `--ignore-interfaces --safe --cubical --guardedness --transliterate`, Cubical 0.9, `research/nima/agda`, and the native-application and application-extension adapter include paths. The pre-existing `TypedGeneratorLayers.agda` warning about importing `isPropIsContr` remains. The certified-selection instances depend on the separately supplied native application extension; this is not a derivation of application from the original native rules.

No result here establishes arbitrary domain compatibility, a general associative composition algebra, infinite-trace pentagon coherence, speedup, fairness, progress, or termination. Infinite execution is productive unfolding of an already total step function and may repeat a state forever. Additional unit-admitted fixture layers test structure, not new independent domain operations.

## Implication

Within the declared compatible-chain construction, nesting versus flattening is a representation choice that preserves full witnessed execution. This supports a future certified compiler for specialization layers and transfer of properties through the proved comparisons; neither an optimized compiler nor a general property-transfer library is implemented here.

Supporting notes: [finite histories](../../research/nima/witnessed-histories.md), [four-domain pentagon](../../research/nima/four-domain-pentagon.md), [infinite executions](../../research/nima/infinite-witnessed-executions.md).
