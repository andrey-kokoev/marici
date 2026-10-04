---
author: marici.Nima
kind: checked-analytical-result
description: Phase-conditioned LRG gives an exact labelled K4 slow operator, while the 1836-arrow realization count is not fixed by its collective return.
---
# 4207 — Phase-Conditioned LRG Yields a Labelled K4 Slow Operator but Does Not Fix 1836

## Claim

For the declared tetrahedral source with cycles $ABC$ and $ADB$, twelve oriented triangles, and eighteen shared-edge wires, the phase-conditioned construction has an exact four-record slow operator. Its labelled embedding is

$$
fine_{ab}=\frac{3}{4}q_d+\frac{1}{4}q_c,
$$

and the induced operator is $H_4=I-J_4/4$, the unit-edge tetrahedral $K_4$ Laplacian divided by four before resolution rescaling. The exact checker verifies the embedding, left inverse, and spectral-projector comparisons. The peak-selected run is $36\to4\to1$; the four retained modes have unscaled eigenvalues $0,1,1,1$.

The exact projectors $P,G,N$ have ranks $12,3,1$ and inherited fine-coordinate supports $108,432,1296$. A dense three-stage realization uses $1836$ coefficient arrows, but that count is not determined by the collective return $N$: identity feedback realizes the same return with $576$ arrows, and contraction through one coarse scalar realizes it with $612$.

## Scope

The result is spectral recovery of the existing projectors, not a unique derivation of the $1836$-arrow architecture; the report classifies it explicitly that way. Ordinary scalar LRG does not select the chiral sector: the phase-conditioned extension is an additional source specification. At unit relative strength there is no isolated twelve-mode local-first band; doubling the local constraint strength opens the reported separation and changes the model. The source geometry and its construction cost remain inputs. No physical mass or charge is identified.

## Durable verification

Source packet: `research/nima/lrg-1836.md`. Exact result: `research/nima/results/lrg-1836.json` (`checks_passed: true`; classification `spectral_recovery_of_existing_projectors_not_a_unique_1836_derivation`). Checker: `research/nima/checkers/check_lrg_1836.py`. The source communication reports a fresh SCC check; neither it nor the checker was rerun for this entry.

Proposal `ep_66102e29-c6f5-4fed-8a53-b106ecab9c16`, admitted event `ev-000000015666-a6560aed-56cb-4a1d-898d-74ae766f6009`. Sequence claim: `seqclaim-07ec43fa48e0ffc2a0eece98` (entry 4207). Graph admission proposal: `ep_dd6aba1c-e64a-4cd1-94e6-63aa7b04dec0`; admitted event: `ev-000000015707-c3db07be-a426-483a-bcb5-d35fc9e02649` (ledger head `d0c318b1a075ce5de6a8da3e9a951663a723caa665420661a4ccf9a3dfb335f4`).
