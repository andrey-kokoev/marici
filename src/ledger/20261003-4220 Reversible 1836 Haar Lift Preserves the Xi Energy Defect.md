---
author: marici.Nima
kind: checked-negative-result
description: An exact reversible Haar amplification preserves the original Xi energy defect rather than eliminating it.
---
# 4220 — Reversible 1836 Haar Lift Preserves the Xi Energy Defect

## Claim

Reconstructing the native $1836$-mode projectors gives ranks $(12,3,1)$ and support counts $(108,432,1296)$. With $w=Ne_0$, $\|w\|^2=1/180$, the normalized vector $v=w/\sqrt\nu$ defines $J h=v\otimes h$ and $R=J^*$. The exact identities are $RJ=I$, $JR=N\otimes I$, and energy preservation. Amplifying the source diagonal prime operation by $I\otimes T_p(z)$ preserves intertwining and recovery, but the scalar two-history defect remains exactly $\widehat\delta_p=\delta_p$.

Attempting to unitarize $T_p$ breaks faithful intertwining off the seam. A bounded intertwiner from full Haar translation to a fixed finite-dimensional unitary representation is zero because Haar translation has no $L^2$ eigenvectors. This is a whole-representation obstruction, not a no-go for reduced-fiber energy equality or moving/rigged realizations.

## Scope

The construction is reversible but copies, rather than closes, the energy-defect equation. No off-seam Xi zero, Xi-specific one-step conservation, RH result, or global source realization is established. A finite-period Fourier substitute also loses a concrete norm-two orbit difference.

## Durable verification

Source packet: `research/nima/1836-to-haar-reversible-realization-retains-the-energy-defect.md`. Checker: `research/nima/checkers/check_1836_haar_reversible_amplification.py`. Exact result: `research/nima/results/1836-haar-reversible-amplification.json`. The report records 24 defect tests, 20 gain fixtures, and two off-seam controls; checks were not rerun for this entry.

Proposal `ep_3ff7e1b0-8a70-4223-b7bd-6a81db9119d7`, event `ev-000000015684-bcadcbdf-6e4b-4840-8a6d-16ba6722fcdd`. Sequence claim: `seqclaim-5ae9a4fa2bc695e02489099f` (entry 4220). Graph admission proposal: `ep_c25b41a5-dbfd-4922-9a04-728336853ff3`; admitted event: `ev-000000015710-92cb112e-45fc-4af2-a8ee-37b26335ec1e` (ledger head `c75c02345f7fb2bd96677ff7deae3c05f712fda93d86de7b88c63350625e6ea1`).
