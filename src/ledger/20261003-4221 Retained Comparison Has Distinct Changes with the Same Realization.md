---
author: marici.Nima
kind: checked-formal-result
description: A Cubical Agda structure admits distinct retained changes with equal realization, and its left laws derive additional inverse and unit laws.
---
# 4221 — Retained Comparison Has Distinct Changes with the Same Realization

## Claim

The Cubical Agda record supplies objects, comparison types, retained changes with identity/composition/inverse, a realization map, and path-valued laws without hom-set truncation or faithfulness. A concrete two-object example uses Boolean comparisons, Boolean-pair changes composed by XOR, and realization by the first projection. It contains distinct changes with the same realization and equal derived transports. Thus no left inverse can recover every retained change from its realization; this is an explicit nonfaithfulness example, not a general prohibition on faithful realizations.

A subsequent reduction proves that left units, associativity, and chosen left inverses suffice to derive left cancellation, right units, involutivity of inversion, and right inverses. For set-valued comparison types, supplied right-unit/right-inverse witnesses agree with the derived ones. The generic structure still retains its chosen proof fields; no unrestricted proof erasure or global minimality theorem follows.

## Scope

These are results about the declared finite-law record and its examples. They do not provide a higher-coherence tower, a universal property for all retained structures, or equivalence with a prior table constructor.

## Durable verification

Packet: `research/nima/retained-comparison-structure.md`; formal sources: `research/nima/agda/RetainedComparisonStructure.agda` and `research/nima/agda/RetainedComparisonReduction.agda`. Receipts: `research/nima/results/retained-comparison-formal-audit.json` and `research/nima/results/retained-comparison-reduction-formal-audit.json`. Runner: `research/nima/checkers/check_retained_comparison.ps1`. The communications report fresh safe Cubical Agda compilations, the intended erasure rejection, and source-bound SCC checks; not rerun for this entry.

Proposals `ep_ce7f26f6-9148-493a-a4b4-dcd471511c45` / `ep_777437df-cdf5-4874-bc34-9b4018c98504`; events `ev-000000015685-dc815aa7-58d5-41c5-a13a-dac470afe742` / `ev-000000015686-3d17121f-3a6f-4b2f-ad2f-17a4f9871567`. Sequence claim: `seqclaim-b18fd9f3cbea2017e7766f2f` (entry 4221). Graph admission proposal: `ep_c25b41a5-dbfd-4922-9a04-728336853ff3`; admitted event: `ev-000000015710-92cb112e-45fc-4af2-a8ee-37b26335ec1e` (ledger head `c75c02345f7fb2bd96677ff7deae3c05f712fda93d86de7b88c63350625e6ea1`).
