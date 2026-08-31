# Corner-blowup logarithmic Gysin unit

## Question

Can the oriented blow-up already required by the source boundary-corner germ supply the missing unit `Xi_log` leg, rather than merely the exceptional Cech face?

## Claim boundary

The local source coordinates are `u=q1`, `v=q2`, and `q3=u+v+p`; the three vertices coalesce at the center `(u,v,p)=(0,0,0)`. On the ordinary blow-up, write

`u=rU`, `v=rV`, `p=rP`.

The exceptional valuation of the primitive center coordinate `p` is one. Therefore the logarithmic Gysin residue is

`Res_E(dlog p)=ord_E(p)=1`.

The oriented exceptional simplex already has unit coefficient on `-sigma123`. Coupling these two legs gives the column `(1,1)` in `(Xi_log,-sigma123)`. Its pair-face residue is zero; reversing the orientation gives `(-1,-1)`.

This constructs the previously missing local comparison coefficient provided `Xi_log` is the source-normalized logarithmic divisor class represented by `dlog p`. It does not yet construct the full chain map from the resolved source carrier to the rank-26/relative complex.

## Disposition

The prior statement “the blow-up exceptional simplex only gives `(0,1)`” is refined: the simplex alone does, but the same blow-up geometry has a canonical logarithmic Gysin leg of coefficient one because `p` is a primitive coordinate in the blown-up center. The next leaf is to verify the normalization and chain-map identification `Xi_log = [dlog p]` in the source carrier, then test compatibility with the absorbed rank-26 quotient.

## Verification

- `research/voevodsky/check_cosmology_corner_blowup_log_gysin_unit.py`
- `research/voevodsky/results/cosmology_corner_blowup_log_gysin_unit.json`
