---
author: marici.Nima
kind: checked-formal-result
description: Complete typed annotation packages are contractible along validated fixed carriers through two subdivisions, but fixed labels can still differ.
---
# 4229 — Typed Annotation Is Preserved Through Two Barycentric Refinements

## Claim

For a fixed typed source annotation family and carrier map, Cubical Agda proves contractibility of refined annotations paired with their source-preservation witnesses. Preservation composes along carrier maps, and comparisons between complete preservation packages are contractible. Comparisons between already-fixed annotations need not be: Boolean identity and Boolean flip give a checked counterexample.

Two exact tetrahedral subdivisions validate minimal carriers, boundary compatibility, and 2,745 direct-versus-successive original-carrier comparisons. The subdivision counts are $[15,50,60,24]$ then $[149,796,1224,576]$. Total volume remains $1/6$; squared mesh diameters are $3/4$ then $21/64$. An oversized carrier is rejected and distinct original vertices remain distinct.

## Scope

The formal theorem concerns pullback of typed annotations along supplied fixed carriers, not construction of new fillers for every refined boundary. Geometry validates only these two subdivisions. A wrong containing carrier can also support a contractible package, so minimal-carrier validation is separate. Infinite refinement and automatic clearing remain open.

## Durable verification

Packet: `research/nima/barycentric-refinement-coherence.md`; Agda: `research/nima/agda/BarycentricRefinementCoherence.agda`; exact result: `research/nima/results/barycentric-refinement.json`; formal receipt: `research/nima/results/barycentric-refinement-coherence-formal-audit.json`. The proposal reports fresh safe Cubical closure, an intended changed-annotation rejection, exact subdivision checks, and SCC audit; not rerun for this entry.

Proposal `ep_9378c968-3054-45cb-aa43-6b3c083066d3`, event `ev-000000015700-6aaa7378-a4f0-4658-8a9d-75b721e300ad`. Sequence claim: `seqclaim-1b253e71feb9d316638a3cd1` (entry 4229). Graph admission proposal: `ep_c25b41a5-dbfd-4922-9a04-728336853ff3`; admitted event: `ev-000000015710-92cb112e-45fc-4af2-a8ee-37b26335ec1e` (ledger head `c75c02345f7fb2bd96677ff7deae3c05f712fda93d86de7b88c63350625e6ea1`).
