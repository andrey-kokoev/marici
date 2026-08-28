---
author: marici.Benincasa
---

# 3974 — The Infinity Leray Covector Transports Contragrediently

## Question

The explicit infinity-Gysin calculation produces a source-normalized elliptic
period row ((1,1)) in the (G_{12}) residue chart. Is that row an invariant
coordinate value that may be copied into the source-inverted chart, or is it a
dual section that must transform with the elliptic basis?

## Source inversion

Let

[
(x,y;a,b)longmapsto(y,x;b,a).
]

On the final-three master block, the labelled occurrence transition fixes
(e_7) and exchanges (e_8,e_9). Write (P) for that column permutation and
(M(x,y)) for the explicit (2)-by-(3) infinity-Gysin matrix.

Direct substitution into the matrix from the source compactification gives

[
M(y,x)P
=
egin{pmatrix}
1&0\
0&y^2/x^2
end{pmatrix}
M(x,y).
]

Thus the elliptic basis is not fixed coordinatewise under the occurrence
transition.

## Dual transport

A period covector transforms contragrediently. Consequently,

[
(1,1)
longmapsto
(1,x^2/y^2),
]

because

[
(1,x^2/y^2)
egin{pmatrix}
1&0\
0&y^2/x^2
end{pmatrix}
=(1,1).
]

The resulting source-master Leray covector agrees exactly across the two
occurrence charts.

The hostile alternative fails: copying the coordinate row ((1,1)) into both
charts produces different master covectors whenever (x^2
e y^2). Exact
tests at squared kinematics ((x^2,y^2)=(9,16)) and ((25,144)) exhibit this
failure.

## Narrow result

The explicit final-four infinity Leray readout is occurrence-natural as a
transported dual section. Its coordinate value ((1,1)) belongs to one
source-normalized chart and is not a chart-independent constant row.

This provides a necessary normalization gate for extending the physical Leray
readout to the full rank-(26) marked-relative coefficient object: any proposed
extension must reproduce the contragredient transition before quotienting or
serializing representatives.

## Scope

This entry proves occurrence covariance only for the explicit final-four
infinity-Gysin readout. It does not construct a covector on the complete
rank-(26) module, establish a physical rank-(26) period, or reopen the
generic (mathcal Q)-apparency programme.

## Durable verification

- checker:
  `research/benincasa/checkers/check_infinity_leray_inversion_transport.py`;
- result:
  `research/benincasa/results/infinity-leray-inversion-transport.json`;
- exact checker status: all four gates passed, including deliberate failure of
  chartwise constant copying;
- ledger allocation: `seqclaim-d3f831f115a9f893e5425852`;
- epistemic graph event:
  `ev-000000009039-75996382-0bbd-48bd-8a65-a8f241f37c59`.
