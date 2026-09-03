# Integral decoration of the ambient cone

## Question

Can the ambient cone be decorated with the full tame units while canceling every radial and codimension-two residual?

## Claim boundary

Yes. On the blowup, `u=l1/l3` and `v=l2/l3` have divisors `D1-D3` and `D2-D3`; both have exceptional valuation zero. The tame symbols are

- `D1`: `v^-1`;
- `D2`: `u`;
- `D3`: `-v/u`;
- `E`: `1`.

At each outer pair, the two ordered valuations are `(-1,+1)`. They cancel in the Gersten differential and induce the oriented edge coefficient `+1`. At every radial pair `Di intersect E`, both valuations are zero. There are no additional divisor components.

The constant `-1` on `D3` has zero valuation. It is not isolated: the complete tuple is the exact tame boundary of `{u,v}`.

Thus the ambient star has logarithmic component `Xi_log`, incidence boundary `sigma123`, exact integral tame decoration, zero radial residuals, and zero codimension-two sums.

## Disposition

The ambient semistable star supplies a complete integral geometric `HomotopyLift` realizing `tau`. It remains distinct from a rank-26 or higher-Chow `ElementLift`. The next leaf tests whether this local normal-slice realization extends functorially to the full characteristic-zero carrier.

## Verification

- `research/voevodsky/check_cosmology_integral_decoration_of_ambient_cone.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
