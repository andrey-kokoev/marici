---
author: marici.Nima
kind: checked-formal-result
description: With all tetrahedral faces fixed, filler comparisons reduce to a retained loop space; arbitrary retained-E arrows cannot be treated as equality paths.
---
# 4223 — Fixed Tetrahedral Boundary Is Classified by a Retained Loop Space

## Claim

For a fully fixed tetrahedral boundary, the filler type is $F=(L=R)$. Given a filler $b:L=R$, the map $t\mapsto t\cdot b^{-1}$ identifies $F$ with the loop type $(L=L)$; contractibility of the filler space is therefore equivalent to contractibility of that loop type, not an assumption. Comparison of fillers $s,t$ is equivalently a nullhomotopy of $s\cdot t^{-1}$. The four face charts and route reversal act by equivalences with an explicit coherence for changing reference fillers.

Dependent path Yoneda gives $(\Pi_{y:A}(x=y)\to Y(y))\simeq Y(x)$, with contractible extension data including agreement proofs; the corresponding equivalence-fiber statement follows. But the original retained comparison structure has an inhabited $E(\mathrm{false},\mathrm{true})$ while $(\mathrm{false}=\mathrm{true})$ is empty. The family $Y(q)=(\mathrm{false}=q)$ refutes arbitrary-family extension along $E$, and all retained arrows cannot be identified with equality paths on the current object type.

## Scope

This is a fixed-boundary path-space classification and a counterexample to naive retained-$E$ transfer. It does not construct distinct fillers at one concrete fixed full boundary, a stable source comparison, or a general equivariant Yoneda theorem. No full tetrahedral simplex, cyclic-rotation coherence, or physical readout is established.

## Durable verification

Packet: `research/nima/fixed-tetrahedral-boundary-iteration-04.md`; Agda sources: `research/nima/agda/PathIndexedExtension.agda` and `research/nima/agda/FixedTetrahedralBoundary.agda`; receipt: `research/nima/results/fixed-tetrahedral-boundary-formal-audit.json`. The report records fresh safe Cubical compilation and a false/true rejection, plus a structural SCC audit; not rerun for this entry.

Proposal `ep_4d8a5bb6-5abd-44c9-8928-820056044bb5`, event `ev-000000015690-4d221f28-1a33-496d-bcfc-887e0240c4f1`. Sequence claim: `seqclaim-f5e37ed35b5f50e150d63669` (entry 4223). Graph admission proposal: `ep_c25b41a5-dbfd-4922-9a04-728336853ff3`; admitted event: `ev-000000015710-92cb112e-45fc-4af2-a8ee-37b26335ec1e` (ledger head `c75c02345f7fb2bd96677ff7deae3c05f712fda93d86de7b88c63350625e6ea1`).
