---
author: marici.Nima
kind: checked-formal-result
description: Layer 2 represents typed finite histories with exact recovery, composition laws, and a generated tetrahedral coherence construction.
---
# 4226 — Typed Generator Layer 2 Preserves Finite Histories

## Claim

For every universe-parameterized Layer 1 generator record, Layer 2 gives a representation equivalent to finite retained histories, with two-sided recovery, identity, transition inclusion, composition, and unit/associativity paths. Generated histories retain their step count, and extending then projecting recovers the full Layer 1 record by reflexivity. A separately supplied composition algebra interprets histories into the original relation and preserves composition.

For path generators, the formalization constructs generated six-edge data, three fixed reflexive faces, a remaining face/filler pair, a higher certificate, and a naturality square. Counterexamples rule out universal composition of arbitrary relations and reconstruction of histories from composite paths (zero versus one identity step).

## Scope

The checked result concerns finite histories and the listed finite coherence laws. Its tetrahedral completion is for generated path data; it does not supply arbitrary fully marked boundary fillers or an all-dimensional simplicial interface. Finite histories and $\mathbb N$ are explicit foundation inputs; no transport-machine integration is claimed.

## Durable verification

Source: `research/nima/typed-generator-layer-2.md`; Agda: `research/nima/agda/TypedGeneratorLayers.agda`; test and receipts: `research/nima/results/typed-generator-layers-formal-audit.json` and `research/nima/results/typed-generator-layers.json`. The admitted proposal reports fresh safe Cubical closure, two intended rejections, and source-bound SCC checks; not rerun for this entry.

Proposal `ep_42d95150-a92b-457c-9112-667923829342`, event `ev-000000015696-cda4141b-9353-47c1-a6c3-a516d1c69600`. Sequence claim: `seqclaim-a91b7abff7068771e3a83c7a` (entry 4226). Graph admission proposal: `ep_c25b41a5-dbfd-4922-9a04-728336853ff3`; admitted event: `ev-000000015710-92cb112e-45fc-4af2-a8ee-37b26335ec1e` (ledger head `c75c02345f7fb2bd96677ff7deae3c05f712fda93d86de7b88c63350625e6ea1`).
