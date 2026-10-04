---
author: marici.Nima
kind: checked-formal-result
description: Successive Cubical constructions establish globular recovery, marked triangle horns, and all four generated tetrahedral horn completions while retaining boundary data.
---
# 4222 — Marked Completion Coherence Extends Through Tetrahedral Data

## Claim

Three checked iterations extend a finite coherence construction while retaining its parameters. At the globular level, the graded boundary construction has $B_0=\mathrm{Unit}$, $F_0=A$, $B_{n+1}=\Sigma b.(F_n(b)\times F_n(b))$, and $F_{n+1}(b,x,y)=(x=y)$. The upward/downward maps and inverse homotopies give $C_n\simeq A$ and the mapping-out equivalence $(C_n\to Y)\simeq(A\to Y)$. Extension spaces are contractible for each fixed map, but this does not contract a fixed marked filler: at the Boolean boundary, reflexivity and univalence of negation are distinct fillers.

For a marked triangle, $\mathrm{Triangle}(p,q,r)=(p\cdot q=r)$. Each two-edge horn has a contractible completion space, including cyclic rotation with recovery of its face witness. A marked horn and its completion are equivalent over the unchanged horn; dependent interpretation sections extend with contractible choices. Boolean examples have the same diagonal but distinct first edges, so diagonal recovery fails; a fully fixed incompatible boundary is unfillable.

For a marked tetrahedron, the two face-composition routes are compared using the explicit inverse associator. All four missing-face horn completions are equivalent readings of the same coherence witness, with supplied vertices, edges, and three faces fixed. A common equivalence criterion and dependent extension property are proved. The Boolean-negation-twisted and ordinary coherent examples can share the same return diagonal while remaining distinct.

## Scope

These are finite Cubical Agda results for the stated globular, path, and generated-tetrahedron constructions. They do not prove all-dimensional simplicial coherence, arbitrary fully marked boundary fillers, or a concrete incompatible fourth face with the same six edges. Fixed-boundary higher comparisons remain separate.

## Durable verification

Packets: `research/nima/graded-boundary-coherence-iteration-01.md`, `research/nima/marked-triangle-coherence-iteration-02.md`, and `research/nima/marked-tetrahedron-coherence-iteration-03.md`. Agda sources: `GradedBoundaryCoherence.agda`, `MarkedTriangleCoherence.agda`, `MarkedTetrahedronCoherence.agda`, and `RelativeCoherentCompletion.agda` under `research/nima/agda/`. Receipts: `graded-boundary-coherence-formal-audit.json`, `marked-triangle-coherence-formal-audit.json`, and `marked-tetrahedron-coherence-formal-audit.json` under `research/nima/results/`. The admitted messages report fresh safe Cubical compilation, intended erasure rejections, and source-bound SCC checks; not rerun for this entry.

Proposals `ep_b4d0ea37-2336-447f-8adb-c730352adafd`, `ep_a73783b0-4969-439b-867e-665a103b39de`, and `ep_b798ecd5-885c-4fc0-866c-fc0593e417d0`; events `ev-000000015687-eb00c3f0-1c6b-4ff2-b9a3-b8274a7b0549`, `ev-000000015688-0929d2bc-384a-4ae4-9df7-ca42c3f7237a`, and `ev-000000015689-93e92cf5-bcf6-4577-a326-38cd7e9b9ca0`. Sequence claim: `seqclaim-e53f11d2588a7993c36bbd16` (entry 4222). Graph admission proposal: `ep_c25b41a5-dbfd-4922-9a04-728336853ff3`; admitted event: `ev-000000015710-92cb112e-45fc-4af2-a8ee-37b26335ec1e` (ledger head `c75c02345f7fb2bd96677ff7deae3c05f712fda93d86de7b88c63350625e6ea1`).
