---
title: "The Leading e6 Node Grade Is Exact and the Claimed Comparison Is Retracted"
date: 2026-08-20
entry: 1132
status: correction-established
sector: cosmology
---

# 1132 — The Leading \(e_6\) Node Grade Is Exact and the Claimed Comparison Is Retracted

Sequence claim: `seqclaim-ca4f48d5a69cfbb3f5b0d103`.

## Defect

Entry 1127 inferred a node-to-\(e_6\) map from two maps with common source
\(g_{111}^{\rm top}\). That is not functorially valid without the very
specialization/bridge square under investigation. Entries 1128 and 1129
then inherited this untyped arrow. Those claims are retracted.

## Exact associated-grade test

The source double-pole master is

\[
e_6=-\frac{K_1}{2}\frac{da\wedge db}{K^{3/2}}.
\]

At the second center, in the \(p\)-chart,

\[
K=4p^2T^2+O(p^3),\qquad K_1=-16pT+O(p^2),
\qquad da\wedge db=p^2dA\wedge dB,
\]

with \(dA=-dT/2\) and \(W^2=4T^2\). Therefore

\[
\operatorname{gr}_0(e_6)
=\frac{8T\,dA\wedge dB}{W^3}
=-\frac{4T\,dT\wedge dB}{W^3}
=d_T\!\left(\frac1W\right)\wedge dB.
\]

Thus the leading ordinary nodal grade of \(e_6\) is exact.

## Surviving evidence

- Entry 1124's physical activation of the nodal Tate line remains valid.
- Entry 1125's regular cyclic occurrence module remains valid.
- Entry 1130's abstract index-two comparison between sheet-difference and
  odd coinvariant lattices remains valid, but it is not tied to \(e_6\).
- Entry 1131's physical boundary \(e_- - e_+\) remains valid.

## Correct frontier

Any node-to-\(e_6\) comparison must live in the first nonzero higher
normal/Rees correction or in a supported relative complex. The next finite
calculation is the \(O(p)\) class of the complete \(e_6\) form modulo exact
forms, together with the moving conductor boundary. No map may be inferred
from the filtered cospan before that class is computed.

Evidence:

- `research/benincasa/checkers/rank12_u2_v0_e6_leading_exactness.py`;
- `research/benincasa/results/rank12-u2-v0-e6-leading-exactness.json`.

