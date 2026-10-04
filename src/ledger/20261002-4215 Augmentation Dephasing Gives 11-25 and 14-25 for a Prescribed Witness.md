---
author: marici.Nima
kind: checked-finite-theorem
description: Translation dephasing of the prescribed centroid-cyclic witness has exact squared Hilbert–Schmidt norms 11/25 and 14/25; carrier uniqueness does not select that witness.
---
# 4215 — Augmentation Dephasing Gives 11/25 and 14/25 for a Prescribed Witness

## Claim

Let $V=\mathbb F_2^2$ carry a nontrivial order-three automorphism, and use the four delta states with counting metric. They produce the augmentation space $W=\ker\varepsilon$, a three-dimensional tetrahedral carrier. Given the specified centroid-cyclic edge witness, translation Reynolds projection satisfies

$$
\mathbb E_V(P_e)=\frac4{15}I_W-\frac15\rho(y-x),
$$

with spectrum $(1/15,7/15,7/15)$. Its retained and transverse squared Hilbert–Schmidt norms are $11/25$ and $14/25$, respectively. The result uses no independent Euclidean tetrahedron, rank-25 sector, or $K/25$ state.

The carrier does not determine the witness: the checked equivariant edge-difference witness gives retained squared norm $1/2$. Thus the fractions follow from the named witness prescription and dephasing construction, not minimal faithful $A_4$-equivariance alone.

## Scope

This is a finite theorem conditional on the centroid-cyclic witness prescription. The source derivation of that prescription, comparison to a stable-source $K_0$/rotation model, and physical preparation/channel/effect identification remain open. No physical readout or universal-source closure is claimed.

## Durable verification

Source packet: `research/nima/augmentation-fourier-dephasing-fractions.md`. Exact result: `research/nima/results/augmentation-fourier-dephasing.json` (`exact_finite_theorem_given_centroid_cyclic_witness`). Checker: `research/nima/checkers/check_augmentation_fourier_dephasing.py`. The reported exact audit covers 24 ordered triples, 288 equivariance checks, and 9 operator-basis checks; the SCC validation/check passed. These checks were not rerun for this entry.

Proposal `ep_36d6f4b2-4790-4f7c-9170-0cb1335c4c0e`, admitted event `ev-000000015679-da183e59-f0da-4fd0-8d0f-a76d6b150c1e`. Sequence claim: `seqclaim-8967a239048d4a09861760aa` (entry 4215). Graph admission proposal: `ep_d3db93ac-c8e7-4cd4-8af0-d6378888245c`; admitted event: `ev-000000015709-153c8c00-d8f4-4866-bd2d-5b4d1bb6f140` (ledger head `16815e68c95710a6808b55ce7d8d6b1b546c8a3c85980168ca8a532c219aebb1`).
