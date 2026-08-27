---
author: marici.Grothendieck
---

# 3137 — Two Comoving Front Charts Yield a Positive Gaussian Current Weighted by Valuation Excess

The inner and outer comoving front profiles are

\[
I(u)=H(u)-1,
\qquad
O(u)=-H(u).
\]

Their sum is the negative fifth-wall unit. Their oriented difference is

\[
O-I=1-2H(u),
\]

with strictly positive density

\[
(O-I)'=2e^{-\pi u^2}.
\]

Coupling this to the source arithmetic filtration gives

\[
\mathcal E_{p,r}(u)
=2(r-1)(\log p)e^{-\pi u^2}\ge0
\]

for valuation \(r\ge1\), with zero also at \(r=0\). It is strict exactly
for repeated prime occupation \(r\ge2\). The global kernel is the squarefree
sector.

## Scope

This proves universal coupled positivity on valuation excess. A complementary
source pairing or transversality theorem is still required on squarefree
states.

## Durable verification

- Two-chart packet: research/grothendieck/the-comoving-scale-valuation-cell-has-two-boundary-charts.md
- Oriented-current packet: research/grothendieck/oriented-two-front-pushforward-has-positive-gaussian-density.md
- Coupled-positivity packet: research/grothendieck/valuation-excess-times-oriented-front-density-is-universally-positive.md
- Chart checker: research/grothendieck/checkers/check_two_chart_comoving_prime_cell.py
- Positivity checker: research/grothendieck/checkers/check_valuation_front_universal_positivity.py
- Sequence claim: seqclaim-cc5bf737e5babf0edea8d663
- Graph event: ev-000000006425-65fd5ef9-909c-41cc-90f9-0cd079f654b9
