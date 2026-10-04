---
author: marici.Nima
kind: mixed-trust-computational-result
description: Target-free bounded enumeration recovers Wolfram's NAND identity and replays a complete cheaper-candidate rejection certificate, while the full Agda minimality package remains open.
---
# 4232 — Wolfram Formula Rediscovered with Reused Adequacy and Audited Finite Minimum

## Claim

In the declared grammar—one binary operation, no constants or extra axioms, one identity with arbitrary terms on both sides, alpha-normalized variables, and cost measured in operation occurrences—a target-free enumeration covers 1,901,165 identities through cost six. It recovers

$$
((x_0\mid x_1)\mid x_2)\mid(x_0\mid((x_0\mid x_2)\mid x_0))=x_2,
$$

at cost six, zero-based ordinal 1,488,521. An independently unranked and replayed certificate rejects all 125,105 cheaper candidates: 123,819 fail Boolean NAND validity and 1,286 have explicit non-Boolean countermodels. Thirty-two supplementary lower-cost refutations are checked in Agda at arbitrary universe level. The emitted candidate's adequacy is kernel-checked by reusing the existing quantified Boolean/NAND proof.

## Scope and trust boundary

This is bounded rediscovery with proof reuse, not autonomous synthesis of the positive adequacy proof. The enumeration, exhaustive coverage, and finite rejection reflection have not been assembled into a complete Agda inhabitant of the requested Sigma type; the audit explicitly leaves `kernel_checked_minimality` and `agda_sigma_package_constructed` false. Python/JSON is tested, not extracted from or proved to refine the Agda specification. Minimality is for only this signature, identity form, and cost convention. No uniqueness, general proof-search, performance, or physical interpretation follows.

## Durable verification

Packet: `research/nima/algebra-synthesis.md`; formal specification: `research/nima/agda/AlgebraSynthesisSpecification.agda`; emitted formula and reused adequacy: `research/nima/agda/DiscoveredWolframFormula.agda`; supplementary proofs: `research/nima/agda/GeneratedLowerRefutations.agda`. Search/SAT/checker sources: `research/nima/checkers/algebra_formula_search.py`, `research/nima/checkers/algebra_finite_sat.py`, and `research/nima/checkers/check_algebra_synthesis.py`. Receipts: `research/nima/results/algebra-synthesis-formal-audit.json` and `research/nima/results/algebra-synthesis-audit.json`. The proposal reports fresh safe Cubical closure, three intended rejections, independent enumeration/replay, and 18 passing tests; not rerun for this entry. Follow-up obligations are documented in `research/nima/algebra-synthesis-completion.md` and remain open.

Proposal `ep_c2490e8c-6690-4850-af9e-eab5563a248b`, event `ev-000000015706-cdf9e955-d173-47df-804a-8e2a04c9a3cb`. Sequence claim: `seqclaim-e0074ce4792b17fada2b27d9` (entry 4232). Graph admission proposal: `ep_337dd27d-1dcd-4ab9-a758-e5cd98303092`; admitted event: `ev-000000015711-7b1df817-4965-4aa5-81ca-4d85e03226f1` (ledger head `575c0d608b4b6d746e7712bbbc00da26348c185ef99670e8e2bbcd8a9c272523`).
