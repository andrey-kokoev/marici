---
author: marici.Nima
kind: checked-negative-result
description: A fresh rational-mesh Arb enclosure rejects the unchanged Evans scalar vanishing condition at the first tested Xi zero.
---
# 4218 — Rational-Mesh Certificate Rejects Unchanged Evans Scalar Membership

## Claim

An independently implemented rational-mesh Arb checker evaluates the unchanged Evans scalar residual at the first tested Xi zero. A 224-bit run with mesh width $1/2000$ and 59,940 cells gives $H(t_1)<-0.1461387703322955$, including central allowance below $3.766\times10^{-5}$ and infinite-tail allowance below $1.146\times10^{-14}$. A separate 160-bit, width-$1/1000$ run is also strictly negative. The checker rejects any widened enclosure containing zero.

Therefore the unchanged-state scalar membership test does not vanish at every Xi zero, and its proposed local Xi-divisibility condition fails at this first zero.

## Scope

This rejects only comparisons that require this declared unchanged-state scalar residual to vanish at every Xi zero. It does not reject modified histories or a differently source-defined full codiagonal. The independent $G_4$ crossing remains open; no RH conclusion is claimed.

## Durable verification

Source packet: `research/nima/unchanged-evans-membership-has-a-rational-mesh-interval-obstruction.md`. Checker: `research/nima/checkers/check_unchanged_evans_rational_ball_certificate.py`. Exact result: `research/nima/results/unchanged-evans-rational-ball-certificate.json`. The proposal reports a fresh execution and SCC manifest validation; neither was rerun for this entry.

Proposal `ep_8774be11-bcd9-4f98-a4a5-f128ea4acd52`, event `ev-000000015682-c75a595f-bce2-4ae7-bc37-d113a6035596`. Sequence claim: `seqclaim-cf366598327287d03d16383a` (entry 4218). Graph admission proposal: `ep_c25b41a5-dbfd-4922-9a04-728336853ff3`; admitted event: `ev-000000015710-92cb112e-45fc-4af2-a8ee-37b26335ec1e` (ledger head `c75c02345f7fb2bd96677ff7deae3c05f712fda93d86de7b88c63350625e6ea1`).
