# Regulator naturality square

## Question

Does the relative logarithmic and tame realization commute with geometric-pair morphisms?

## Claim boundary

Yes on the strict transverse subcategory. Require Cartesian regular centers, base change for the associated graded/Rees algebra, reduced labeled wall pullbacks of ramification index one, and an orientation-preserving ordered conormal map.

The Rees condition identifies blowups and incidence strata. Pullback commutes with relative `dlog` and wedge. Index-one divisor pullback commutes with tame symbols, preserving

`(v^-1,u,-v/u,1)`.

Reduced oriented strata preserve `Gamma` and `sigma123` with coefficient one. Therefore `Phi:C_rel -> K_Ger` is natural on this subcategory.

This restriction is necessary. Under `u -> u^e` and `v -> v^f`, the logarithmic coefficient and every outer tame exponent scale by `e f`. For positive ramification indices, the primitive unit survives only at `e=f=1`.

## Disposition

Unqualified transverse naturality is narrowed to strict transverse/Rees-compatible naturality. Ramified maps require weighted horns and do not preserve the primitive constructor. The next leaf classifies that weighted variant.

## Verification

- `research/voevodsky/check_cosmology_regulator_naturality_square.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
