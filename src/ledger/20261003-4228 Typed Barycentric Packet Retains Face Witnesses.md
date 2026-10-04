---
author: marici.Nima
kind: checked-formal-result
description: A single generated tetrahedron admits typed marked-face recovery and an exact barycentric subdivision, while type-only and volume-score readouts lose occurrences.
---
# 4228 — Typed Barycentric Packet Retains Face Witnesses

## Claim

For one occurrence-labelled generated tetrahedron with fixed packet parameters, Cubical Agda attaches an actual Layer 2 witness and type to each of the fifteen nonempty faces and proves recovery of the face mark, type, and term from each constructed vertex. Bare types and even type/term pairs cannot recover all face occurrences.

An exact rational checker builds the barycentric order complex with counts $[15,50,60,24]$ (vertices, edges, triangles, tetrahedra) and boundary counts $[14,36,24]$. The 36 internal triangle pairs cancel, each of the 24 child tetrahedra has volume $1/144$, and the total volume is $1/6$. All 24 maximal flags share one volume score, so score alone also fails to recover the marked occurrence.

## Scope

The formal packet concerns one abstract occurrence-labelled tetrahedron and a chosen standard affine realization. It does not identify arbitrary types with geometry, recover fixed source parameters from a vertex, give an active-view contraction algorithm, or assert a physical realization.

## Durable verification

Packet: `research/nima/barycentric-witness-packet.md`; Agda: `research/nima/agda/BarycentricWitnessPacket.agda`; exact checker: `research/nima/checkers/check_barycentric_witness_packet.py`; result: `research/nima/results/barycentric-witness-packet.json`; formal receipt: `research/nima/results/barycentric-witness-packet-formal-audit.json`. Fresh closure, intended mark-erasure rejection, exact geometry, and SCC audit are reported as passing; not rerun for this entry.

Proposal `ep_d4d439d9-aad9-43fb-b8d8-0a2c3205f128`, event `ev-000000015699-9c80b6bc-0d48-4a82-9425-80d546616e02`. Sequence claim: `seqclaim-6c75e27cfabbf0a34ec478d0` (entry 4228). Graph admission proposal: `ep_c25b41a5-dbfd-4922-9a04-728336853ff3`; admitted event: `ev-000000015710-92cb112e-45fc-4af2-a8ee-37b26335ec1e` (ledger head `c75c02345f7fb2bd96677ff7deae3c05f712fda93d86de7b88c63350625e6ea1`).
