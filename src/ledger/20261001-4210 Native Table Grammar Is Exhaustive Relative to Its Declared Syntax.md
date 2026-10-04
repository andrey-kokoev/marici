---
author: marici.Nima
kind: checked-formal-result
description: The native indexed-table grammar is structurally exhaustive relative to its Agda declarations, without establishing repository-wide coverage.
---
# 4210 — Native Table Grammar Is Exhaustive Relative to Its Declared Syntax

## Claim

The source-defined indexed native table syntax has eight header forms, one typed table-node constructor, twelve rule schemas, and two retained-derivation constructors (`seed` and `apply`). The existing `NativeTableResolution` equivalence covers every legacy constructor, rule, and retained derivation for arbitrary original admission policies. This establishes exhaustion relative to the named native declarations, not merely a representative example list.

The source report records fresh safe/cubical `NativeTableRegression` compilation, six intended compiler rejections, finite audit controls, and the `nima-native-table-equivalence` SCC check. The registry transcription is subordinate to the Agda datatype and rule definitions; metadata validation alone is not the formal result.

## Scope

No repository-wide Marici operation-coverage theorem, structured-S4 source signature, or S4 derivation is established. Potentially infinite premise domains remain possible despite the finite number of schemas. The nine-row policy/native bridge and operational `Resolve` interpretation for retained-path operations remain open; no physical dynamics are claimed.

## Durable verification

Governing sources: `research/nima/agda/IndexedConstructorTables.agda`, `research/nima/agda/NativeTableRules.agda`, `research/nima/agda/IndexedResolutionTransport.agda`, and `research/nima/agda/NativeTableResolution.agda`. Registry: `research/nima/generating-grammar/native-core.json`; verification record: `research/nima/generating-grammar/native-core-verification.json`; checker: `research/nima/checkers/check_generating_grammar.py`; SCC model: `research/nima/scc-models/native-table-equivalence.json`. Results are those reported in the admitted communication and were not rerun for this entry.

Proposal `ep_1a376ecb-db9f-4c7a-b645-037c7c821897`, admitted event `ev-000000015670-9c8263d3-9313-485f-85e1-25e1060f78f3`. Sequence claim: `seqclaim-2ea9b535d2a8072c12bf1257` (entry 4210). Graph admission proposal: `ep_f4a7a6f6-25a7-4ca7-a666-77f7a30716db`; admitted event: `ev-000000015708-8bc0dfb9-c6ee-4261-8940-c837f7ea61e9` (ledger head `3e464f8e211d769b5ec2f1bcbce6eb5451c8db1494c4f9308df2bba1d4c2bcca`).
