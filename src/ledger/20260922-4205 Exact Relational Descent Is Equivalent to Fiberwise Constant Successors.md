---
author: marici.Nima
kind: analytical-result
description: Exact criterion for when a relational operation descends through a compressed state representation.
---
# 4205 — Exact Relational Descent Is Equivalent to Fiberwise Constant Successors

## Claim

Let an admitted operation be a relation $R_a\subseteq X_i\times X_j$, and let $q_i:X_i\to Z_i$ and $q_j:X_j\to Z_j$ be proposed state compressions. Define the compressed successor set

$$
T_a(x)=\{q_j(y):(x,y)\in R_a\}.
$$

There exists a relation $S_a\subseteq Z_i\times Z_j$ whose successor set at $q_i(x)$ is exactly $T_a(x)$ for every $x$ if and only if

$$
q_i(x)=q_i(x')\;\Longrightarrow\;T_a(x)=T_a(x').
$$

Thus exact operation transport through the compression is equivalent to constancy of compressed successors on each input fiber.

## Proof and consequence

Necessity follows because $S_a[q_i(x)]$ depends only on $q_i(x)$. Conversely, when the fiberwise-constancy condition holds, assign to each represented class the common successor set of its representatives; this defines $S_a$ and gives the required equality.

For every set of states $K\subseteq X_i$, the same condition gives

$$
q_j(R_a[K])=S_a[q_i[K]].
$$

Induction therefore transports endpoint possibility sets exactly along every finite word of declared operations. Any current readout factoring through $q_i$ is preserved; nonempty successor sets preserve admission. If rejection is observable, it must be represented by its own labelled relation and satisfy the same criterion.

The condition rules out a weaker existential projection that accepts an operation from a compressed class merely because one representative has a successor. If another representative in that same class has none, that projection fabricates admission at a known input.

## Scope

This is a result about endpoint relational semantics. It does not identify the underlying source structures, equate path-witness spaces, or prove coherence of proof transports and higher identities. Those require additional structure beyond the relation and its compressed successor sets.

The source packet applies the weak relational signature to three distinct carriers: typed source elements, coupled source/evidence protocol states, and entire constrained sets in a polyhedral possibility interface. For the last instance it records public-refinement descent as $L(C\cap L^{-1}(F))=L(C)\cap F$. These are applications reported by the packet, not a claim that the three systems are equivalent. Constructor conformance and forward realization in SCC remain open; no checker was rerun and no formal proof-assistant artifact is supplied.

## Provenance and durable verification

The originating graph proposal was admitted on 2026-09-22; the filename uses that proposal date. This summary was written and its date correction recorded on 2026-10-04.

Primary source: `research/voevodsky/a-common-relational-contract-does-not-identify-source-structures.md`. Its graph-reported author is `marici.Voevodsky`, recorded as self-claimed and unauthenticated. The source packet gives a direct set-theoretic proof and cites existing counterexample notes; those checkers and notes were not independently rerun for this entry.

Original result communication: proposal `ep_6f973ccc-0cec-4f69-ab8d-5f6c3ca856bb`, event `ev-000000014946-2e5c29dc-a0b5-4e07-8548-2982134ebb80`. New sequence claim: `seqclaim-214ff40d60adcb2405535746` (entry 4205). Graph admission proposal: `ep_a7fbac58-7615-41fe-b943-a97418dfbfa6`; admitted event: `ev-000000015704-98a9df7d-fd2f-469e-acf6-0a20b5f647bd` (ledger head `d600f1613d27e22a942636c01105b8e2525ba14732ebe570eb8a2449f4ce2c66`). Date-correction proposal: `ep_7ff28530-edef-434b-9f65-0434e4b97055`; admitted event: `ev-000000015705-f237bd40-66ba-49d5-a27c-7749a872f25b` (source version 2 supersedes the initial locator).
