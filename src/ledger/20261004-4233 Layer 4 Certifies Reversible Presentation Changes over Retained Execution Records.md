---
author: marici.Nima
kind: checked-formal-result
description: Layer 4 packages supplied dependent decompositions as reversible reductions over fixed Layer 3 records, with recovery, observation preservation, composition, and a canonical history-retaining instance.
---
# 4233 — Layer 4 Certifies Reversible Presentation Changes over Retained Execution Records

## Claim

For a source type $A$ and retained boundary $B$, a Layer 4 reduction supplies a dependent remainder $H$ over $B$, an equivalence presenting $A$ as $\Sigma_{b:B}H(b)$, and a contractibility certificate for each remainder. Compaction exposes the boundary; recovery reconstructs the source using the supplied centers and inverse presentation. The two round trips are paths, so compaction is an equivalence and supplied observations are preserved. The complete recovery package—including the source record and its path to the boundary—and comparisons between such packages are contractible.

The interface checks identity reductions, composition of specified reductions, direct-versus-successive compaction and recovery, associativity, and agreement of the rebracketed complete recovery packages. A canonical Layer 3 instance retains history and initial payload while omitting the output/agreement package, which recovery recomputes. A two-stage circle-machine example retains its two-turn history. Equal scores do not identify histories or license a reversible score-based reduction.

## Scope

Reduction presentations and contractibility certificates are inputs; the interface does not discover certificates, choose rewrite strategies, prove confluence, or give cost bounds. Recovery is up to paths, not identical serialized syntax. It does not contract arbitrary fixed-endpoint comparison types or allow arbitrary components to be erased. The canonical instance starts from Layer 3's retained execution record, not an inverse of the earlier syntax compiler.

## Durable verification

Packet: `research/nima/typed-generator-layer-4.md`; Agda: `research/nima/agda/TypedGeneratorPresentation.agda`; formal receipt: `research/nima/results/typed-generator-presentation-formal-audit.json`; source-bound audit: `research/nima/results/typed-generator-presentation.json`; checker: `research/nima/checkers/check_typed_generator_presentation.py`; SCC model: `research/nima/scc-models/typed-generator-presentation.json`. The admitted proposal reports fresh safe Cubical closure, two intended negative rejections, and a passing source-bound audit; checks were not rerun for this entry.

Proposal `ep_5c044729-0163-4ed2-bb6b-34e50b23fa9e`, event `ev-000000015701-10873321-57ee-4241-9fb5-1bc6d6efd7d1`. Sequence claim: `seqclaim-3d5acab86b7002d569d5de98` (entry 4233). Graph admission proposal: `ep_52b12525-141d-46f3-9aa7-0f65b390aa84`; admitted event: `ev-000000015712-2528f7dd-8081-4b06-8b3e-7b2fed2f7958` (ledger head `70f5af783b4f2f31e7056456e0bb59c358953f8a1ed4cb9ea7946b15cbd3e1c5`).
