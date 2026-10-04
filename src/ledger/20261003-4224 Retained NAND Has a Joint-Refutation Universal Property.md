---
author: marici.Nima
kind: checked-formal-result
description: A two-phase construction gives joint refutation a natural equivariant universal property and characterizes when its Wolfram expression recovers the third question.
---
# 4224 — Retained NAND Has a Joint-Refutation Universal Property

## Claim

For small set-valued $E$-actions with admitted empty, pair, and function types, define the joint-refutation question by $N(A,B)(p)=(A(p)\times B(p))\to 0$, with retained changes acting by precomposition. There is a natural equivalence, with recovery of both witnesses,

$$
\operatorname{Map}_E(X,N(A,B))\simeq\operatorname{Map}_E(X\times(A\times B),0).
$$

The construction retains the input action records; its value-level fiber comparison does not assert equivalence of the entire question/action packages. A second phase lifts the Wolfram expression to an equivariant action isomorphism with double negation. Recovery of the third question holds exactly under pointwise propositionality and double-negation stability; both conditions are necessary and sufficient in the stated setting. Constant Boolean answers give a counterexample to unrestricted recovery.

## Scope

Empty, pair, and function types are ambient inputs; the retained-change laws do not generate emptiness. Double negation is not generally equivalent to the answer type, and no all-set Boolean interpretation or whole higher-action/coherence-pyramid equivalence is claimed.

## Durable verification

Packet: `research/nima/retained-nand-two-phases.md`; Agda source: `research/nima/agda/RetainedNandPhases.agda`; checker: `research/nima/checkers/check_retained_nand_phases.py`; receipt: `research/nima/results/retained-nand-phases-formal-audit.json`. Fresh safe headless compilation and the intended false/true rejection, plus source-bound SCC checks, are reported as passed; not rerun here.

Proposal `ep_f039a83d-2f79-431c-a54b-e8aadb0aa237`, event `ev-000000015692-ecf236c3-d331-42eb-ae38-6022c0706067`. Sequence claim: `seqclaim-a3f302cf94c56712f3986755` (entry 4224). Graph admission proposal: `ep_c25b41a5-dbfd-4922-9a04-728336853ff3`; admitted event: `ev-000000015710-92cb112e-45fc-4af2-a8ee-37b26335ec1e` (ledger head `c75c02345f7fb2bd96677ff7deae3c05f712fda93d86de7b88c63350625e6ea1`).
