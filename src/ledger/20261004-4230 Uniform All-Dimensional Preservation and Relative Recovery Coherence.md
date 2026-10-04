---
author: marici.Nima
kind: checked-formal-result
description: Certified Layer 1–4 compactions preserve every finite-dimensional typed cell, with contractible higher comparisons inside complete recovery fibers.
---
# 4230 — Uniform All-Dimensional Preservation and Relative Recovery Coherence

## Claim

For every admitted Layers 1–4 stack and pair of execution endpoints, each supplied certified compaction induces equivalences on the iterated identity types of its typed globular cells at every finite dimension. The maps are the iterated congruences of the actual compaction function, with inverse maps and source/target recovery paths.

For any fixed compact boundary, Layer 4's complete recovery package (source record together with its path to the compact view) is contractible; by induction, every iterated comparison type over that complete recovery fiber is contractible. The theorem constructs `Coherent4` for every admitted `Stack4` and its endpoint reductions. For a fixed reduction, the complete certificate type is also contractible. Canonical and checked two-stage reductions instantiate the theorem.

## Scope

“All-dimensional” is a structural induction for every natural-number dimension, not finite sampling. Boundaries and reductions must be well-typed and supplied by the admitted interfaces. This preserves retained-record identity and gives relative coherence inside complete recovery fibers; it does not provide arbitrary fillers or relation composition, contract arbitrary source types or fixed-endpoint comparisons, identify different reduction policies, or cover transfinite dimensions or a general infinity-category interface.

## Durable verification

Packet: `research/nima/typed-generator-coherence.md`; Agda: `research/nima/agda/TypedGeneratorCoherence.agda`; formal receipt: `research/nima/results/typed-generator-coherence-formal-audit.json`; source-bound audit: `research/nima/results/typed-generator-coherence.json`; checker: `research/nima/checkers/check_typed_generator_coherence.py`; SCC model: `research/nima/scc-models/typed-generator-coherence.json`. The admitted proposal reports fresh safe Cubical compilation, two intended negative rejections, and a passing structural/source-bound audit; checks were not rerun for this entry.

Proposal `ep_00b3f8b2-d101-4440-ab00-1254539a5b32`, event `ev-000000015702-18c1605a-bdeb-40e5-a3bd-0e1207817cec`. Sequence claim: `seqclaim-d700b996ffd54579a2b3a8d2` (entry 4230). Graph admission proposal: `ep_337dd27d-1dcd-4ab9-a758-e5cd98303092`; admitted event: `ev-000000015711-7b1df817-4965-4aa5-81ca-4d85e03226f1` (ledger head `575c0d608b4b6d746e7712bbbc00da26348c185ef99670e8e2bbcd8a9c272523`).
