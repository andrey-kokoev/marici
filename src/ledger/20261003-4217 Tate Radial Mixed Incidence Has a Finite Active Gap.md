---
author: marici.Nima
kind: checked-finite-operator-result
description: The finite Tate mixed-incidence operator has an exact radial spectrum and a uniform nonzero singular-value gap on active directions.
---
# 4217 — Tate Radial Mixed Incidence Has a Finite Active Gap

## Claim

On the finite packet of functions supported in $p^{-N}\mathbb Z_p$ and invariant under $p^N\mathbb Z_p$, define $C_{p,h}=R_pT_h(I-R_p)$, where $R_p$ is normalized unit averaging and $T_h$ translation. The exact source calculation gives $R_pC=C$, $CR_p=0$, $C^2=0$, and $C^*=(I-R_p)T_{-h}R_p$. Fourier conjugation identifies it with the radial/character mixed operator $R_pM_{\chi_h}(I-R_p)$.

For $m=v_p(h)$ with $-N\le m<N$, the radial compression has spectrum $1^{(N+m+1)},(-1/(p-1))^{(1)},0^{(N-m-1)}$. Consequently the only positive singular values of $C$ are $1$ and, for odd $p$, $\sqrt{1-(p-1)^{-2}}$. The active rank is $N-m-1$ for $p=2$ and $N-m$ for odd $p$. Thus the finite active sector has a prime-uniform lower gap; exact kernels and packet-dependent active ranks remain.

## Scope

This is a finite local Tate operator result, not an identification with an existing arithmetic primitive/square Green packet. No $\log(p)$ normalization, cycle $1/k$ law, global positive Weil realization, or restricted-product completion follows. Arithmetic labels, metric, orientation, and Mellin comparison remain separate gates.

## Durable verification

Source packet: `research/nima/tate-residue-radial-mixed-incidence.md`. Checker: `research/nima/checkers/check_tate_radial_mixed_incidence.py`; exact result: `research/nima/results/tate-radial-mixed-incidence.json`. The report records 48 exact radial cases and an independent four-state fixture; checks were not rerun for this entry.

Proposal `ep_e5dc7225-3a2b-40a2-8686-3492c721a7c5`, event `ev-000000015681-df3b4abf-8bbf-4e76-b22e-8f64bd45c659`. Sequence claim: `seqclaim-e1c012b55add77bf7d61270c` (entry 4217). Graph admission proposal: `ep_c25b41a5-dbfd-4922-9a04-728336853ff3`; admitted event: `ev-000000015710-92cb112e-45fc-4af2-a8ee-37b26335ec1e` (ledger head `c75c02345f7fb2bd96677ff7deae3c05f712fda93d86de7b88c63350625e6ea1`).
