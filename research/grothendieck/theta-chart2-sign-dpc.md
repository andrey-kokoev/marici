# Chart-2 dominant sign DPC

## Problem

On `q in [7/16,1/2]` and `z=q*y in [q/1000,1/64]`, certify the two required
coordinate expressions `q*D_z<0` and `D_q|z+(z/q)*D_z>0` by exact outward
enclosures.

## Bold conjecture

The cancellation-free variables `m(q,z)` and `eta=m(q,4z)-4m(q,z)` retain
enough correlation in the independent `(q,z)` chart to certify both signs
with a shallow disjoint cover.

## Named rivals

1. One natural interval box over a rectangular superset of Chart 2.
2. A disjoint `(q,z)` subdivision respecting the slanted lower boundary.
3. Centered or affine transport if natural local boxes remain dependent.

## Risky consequences

Every accepted cell must enclose only the Chart-2 domain or an explicit
superset, must certify both strict signs, and must retain exact cover geometry.
Finite point tests or a cover of only the rectangular interior are insufficient.

## Strongest falsification attempt and residual

`research/grothendieck/checkers/theta_dominant_chart2_signs.py` evaluates one
exact rectangular superset box in independent `(q,z)` coordinates. It avoids
the false dependency `q*(z/q)` by constructing `m` directly from `z`. The box
fails both signs: `q*D_z` encloses approximately
`[-1.5769e8,5.1611e10]`, and the second expression encloses approximately
`[-3.6993e9,3.6994e9]`. Durable output is
`research/grothendieck/results/theta-dominant-chart2-signs.json`.

An `8x8` exact boundary-aware pilot persists all 64 rectangular-superset
cells but accepts none. Exact algebra gives `D=q^2 R/z^2`, so the signs reduce
without quotient differentiation to `H=z R_z-2R<0` and
`J=q R_q+z R_z>0`. Re-evaluating the same cover with these factors still
accepts none: the best `H` upper bound is about `0.10594` and the best `J`
lower bound about `-0.06715`. In contrast, a separate `3x3` exact point scan
has no failure, with maximum `H` upper bound `-2.586e-7` and minimum `J` lower
bound `7.403e-6`. This point scan is diagnostic only. The scale gap indicates
small-`z` cancellation inside `H` and `J`, not a sampled sign reversal.
An exact rational endpoint series through degree 13 confirms the structure:
`R` starts at `z^2`, `H` starts at `z^3`, and `J` starts at `z^2` in all four
rational `(2*pi,q)` endpoint cases. After scaling, both series have mixed
signs (predominantly alternating), so coefficientwise positivity/negativity is
not available. This is endpoint structural evidence, not a uniform enclosure;
durable output is `results/theta-chart2-scaled-series.json`. A first exact
full-`q` coefficient enclosure of the degree-13 scaled polynomials fails:
`H/z^3` encloses roughly `[-6467,2291]` and `J/z^2` encloses
`[-1624,1658]`. Endpoint polynomial values are instead robust (`H/z^3`
between about `-3088` and `-1734`, and `J/z^2` between `29.27` and `44.48`
at tested boundary cases), so this falsifies only the single full-parameter
coefficient enclosure. Local exact coefficients close the finite-polynomial
gate: a disjoint 64-cell `q` cover certifies all degree-13 scaled polynomials,
with largest `H/z^3` upper bound approximately `-1645.38` and smallest
`J/z^2` lower bound approximately `5.32537`. Exact cell geometry and margins
are persisted in `results/theta-chart2-scaled-taylor-q-cover.json`.

The exact Cauchy checker on complex `|z|<=1/4` bounds the omitted scaled tails
by `1.60415` for `H/z^3` and `0.091284` for `J/z^2`. These are strictly below
the certified finite-polynomial margins `1645.37` and `5.32537`.

## Disposition

Certified. Combining the 64-cell exact finite-polynomial cover with the
uniform exact Cauchy tails proves `H<0` and `J>0`, hence both required Chart-2
strict derivative signs. The scoped theorem and evidence map are recorded in
`theta-chart2-sign-certificate.md`.
