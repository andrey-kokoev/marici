# DPC: all higher raw jets through degree six

## Problem

Does any raw `(x,y,z)` derivative of orders three through six survive the unchanged relation quotient?

## Bold conjecture

At least one higher symmetric derivative has a nonzero quotient class and remains a candidate for a higher connecting mechanism.

## Named rivals

Every higher derivative may remain exact; orders above six may vanish by the interpolation bound; or raw derivatives may lack any sourced higher-jet extension.

## Risky consequences and strongest falsification

Directional bases spanning the symmetric powers of dimensions 10, 15, 21, and 28 were constructed for orders three through six. Their 74 components were tested on all 1,224 seed targets: 90,576 reductions against the rank-8,793 source image over `F_32003`. Every residual is zero.

Orders three and four have 3,244 nonzero raw rows in every tested basis direction. Orders five and six range from zero to 2,880 nonzero raw rows. Orders above six vanish by the verified interpolation degree bound.

## Disposition

No higher-jet modular survivor exists in the unchanged quotient. The bold conjecture is rejected at this field, but one-prime vanishing does not prove rational exactness. No higher connecting extension or admissibility rule is defined.

The next bounded gate tests exact rational membership for the 90,576 seed-component targets as one family, not recursively by derivative order.

## Verification

- `research/voevodsky/check_cosmology_higher_jet_degree_six_audit.py` — exit 0
- `research/voevodsky/results/cosmology_higher_jet_degree_six_audit.json`
