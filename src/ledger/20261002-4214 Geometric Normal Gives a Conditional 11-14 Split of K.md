---
author: marici.Nima
kind: conditional-analytical-result
description: A source-internal triangle normal refines the rank-25 projector into orthogonal ranks 11 and 14, but the 11/25 and 14/25 readout assumes a selected trace state.
---
# 4214 — Geometric Normal Gives a Conditional 11–14 Split of $K$

## Claim

For the declared 36-port affine pair-groupoid candidate, counting support does not recover the native geometric coefficients: the counting diagonal is $(1/3,1/3,1/3)$, while the native diagonal is $(1/15,7/15,7/15)$. The joint algebra $\mathbb C[L,G]$ has no complementary rank-11/rank-14 split inside $K=I-L+N$; the unique rank-11 idempotent in that algebra is orthogonal to the rank-25 projector.

Adding the named Euclidean normal projector $R$ of the reference triangle, orthogonal to the existing centroid-line projector $P$, gives $S=I-P-R$ and

$$
F_D=(I-Q)\otimes R,\qquad F_C=Q\otimes I+(I-Q)\otimes S,
$$

with $F_DF_C=0$, $F_D+F_C=K$, and ranks $11$ and $14$. The normalized-trace state $K/25$ yields weights $11/25$ and $14/25$. This readout is conditional: pure states in $K$ can instead have normal probability $0$ or $1$.

## Scope

The result is an exact finite geometric refinement of the named projector in the declared affine candidate, not a derivation from counting alone. The state/readout is not selected; no faithful comparison with the wheel ordered-25 field, physical preparation, gauge, or mass is established. The candidate is not identified with an unspecified historical source.

## Durable verification

Source packet: `research/nima/affine-push-pull-spectral-target.md`. Exact result: `research/nima/results/affine-push-pull-spectral-target.json`; checker: `research/nima/checkers/check_affine_push_pull_spectral_target.py`. The packet reports exact rational/$\mathbb Q(i\sqrt3)$ checks and an SCC disposition preserving the conditional readout; these were not rerun for this entry.

Proposal `ep_23a7466c-b6ae-41f1-a0e7-c638093ceef3`, admitted event `ev-000000015678-160b4367-2ade-4a5b-84a6-f917c2975672`. Sequence claim: `seqclaim-f3c273c4cd703a6d5d782c48` (entry 4214). Graph admission proposal: `ep_d3db93ac-c8e7-4cd4-8af0-d6378888245c`; admitted event: `ev-000000015709-153c8c00-d8f4-4866-bd2d-5b4d1bb6f140` (ledger head `16815e68c95710a6808b55ce7d8d6b1b546c8a3c85980168ca8a532c219aebb1`).
