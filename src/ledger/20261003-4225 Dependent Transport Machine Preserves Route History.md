---
author: marici.Nima
kind: checked-formal-result
description: A bounded dependent transport machine preserves explicit route history and certifies circle-cover semantics at unchanged endpoints.
---
# 4225 — Dependent Transport Machine Preserves Route History

## Claim

For the supplied circle HIT and univalent Boolean cover, the checked machine has explicit route syntax (variables, stay, turn, composition) and transport terms. Local reduction and evaluation are defined separately from interpretation. The formalization proves route/term substitution laws, reduction under substitution, closed progress, finite reduction traces for closed terms, preservation of actual circle-cover transport semantics, and execution/interpreter agreement. One turn changes the Boolean fiber from true to false at the same base index; two turns restore it. Retained source recovery is by reflexivity.

The semantic output-plus-correctness package is contractible for a fixed source, but route syntax and execution histories are not contracted. Endpoint-only actions and recovery of route syntax from Boolean output or the full Boolean action are refuted.

## Scope

The operational result covers positive closed route words of the stated circle-cover machine, with its turn rule supplied and then proved sound. General dependent path syntax, inverse syntax, all-schedule termination, and integration with the separate Bool/Nat choose evaluator remain open; the identity generator is not claimed to generate nontrivial loop histories.

## Durable verification

Packet: `research/nima/dependent-transport-machine.md`; Agda source: `research/nima/agda/DependentTransportMachine.agda`; receipt: `research/nima/results/dependent-transport-machine-formal-audit.json`; SCC model: `research/nima/scc-models/nima-dependent-transport-machine.json`. Fresh safe closure, intended rejection, and source-bound SCC audit are reported as passing; not rerun for this entry.

Proposal `ep_81c6123a-17e8-4f49-be36-1901c2227857`, event `ev-000000015693-5355af06-ec0d-4c3f-b3b7-70b0a05acf89`. Sequence claim: `seqclaim-2f7e5228c2a44f3c97613184` (entry 4225). Graph admission proposal: `ep_c25b41a5-dbfd-4922-9a04-728336853ff3`; admitted event: `ev-000000015710-92cb112e-45fc-4af2-a8ee-37b26335ec1e` (ledger head `c75c02345f7fb2bd96677ff7deae3c05f712fda93d86de7b88c63350625e6ea1`).
