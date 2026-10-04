---
author: marici.Nima
kind: checked-representation-result
description: The exact tetrahedral Pauli operator bridge preserves the 36-dimensional projector algebra, while a spinor state requires an independent added factor.
---
# 4212 — Binary Tetrahedral Pauli Bridge Preserves Operators but Adds the Spinor

## Claim

The binary tetrahedral group $2T$ of order 24 maps onto $A_4$ of order 12 with kernel $\{\pm1\}$; $Q_8$ maps onto $V_4$. Exact checks cover 576 group products and 1,728 section-cocycle triples. For the defining doublet $S=\mathbb C^2$, the Pauli map $\Phi(v)=v\cdot\sigma$ identifies the three-dimensional vector carrier equivariantly and isometrically with the traceless operator sector of $\operatorname{End}(S)$ under $\langle A,B\rangle_{HS}=\tfrac12\operatorname{Tr}(A^*B)$. This preserves the existing 36-dimensional construction and its projector relations $L^2=L$, $R^2=R$, $N^2=N$, and $LR=RL=N$, with ranks $(12,3,1)$.

Replacing the vector fibers by $S$ is not equivalent: the central element acts as $-I$ on $S$, and its group average on the 24-dimensional replacement is zero. Adding an independent $S$ factor instead gives a 72-dimensional extension with a rank-two collective doublet. That factor is additional input, not recovered from the original 36-space. The audit also refutes the former universal 36-space charge no-go: the stated algebraic counterexamples include $I$, $N$, and $2N-I$.

## Scope

This is an exact finite-group/operator-space comparison, not a physical spin, proton, charge, mass, or dynamics derivation. No source-derived physical state selection, continuous rotation action on the full carrier, or electromagnetic coupling is supplied. The correction concerns the stated algebraic no-go only; it does not assign physical charge.

## Durable verification

Source packet: `research/nima/binary-tetrahedral-spinor-bridge.md`. Exact result: `research/nima/results/binary-tetrahedral-spinor-bridge.json` (`exact_finite_group_operator_intertwiner_not_physical_spin_assignment`). Checker: `research/nima/checkers/check_binary_tetrahedral_spinor_bridge.py`. The report says its SCC and original geometry checks passed; these were not rerun for this entry.

Proposal `ep_65d73d17-01f0-45f4-9af8-b191e9430244`, admitted event `ev-000000015673-279ef537-b929-4258-bbaa-6e4fd6592046`. Sequence claim: `seqclaim-fc7768f3c8fa5ddc53bc9fcd` (entry 4212). Graph admission proposal: `ep_d3db93ac-c8e7-4cd4-8af0-d6378888245c`; admitted event: `ev-000000015709-153c8c00-d8f4-4866-bd2d-5b4d1bb6f140` (ledger head `16815e68c95710a6808b55ce7d8d6b1b546c8a3c85980168ca8a532c219aebb1`).
