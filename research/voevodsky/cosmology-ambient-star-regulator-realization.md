# Ambient-star regulator realization

## Question

Does the ambient cone chain map to the formal comparison cell with unit logarithmic normalization?

## Claim boundary

Yes at top weight. Let `l1=U`, `l2=V`, and `l3=U+V+P`. On the exceptional complement set `u=l1/l3` and `v=l2/l3`. The logarithmic Thom class of the oriented ambient star is

`dlog(u) wedge dlog(v)=Xi_log`.

The star chain

`Gamma=[E,X,Y]+[E,Y,Z]+[E,Z,X]`

has boundary `sigma123=(1,1,1)`. The coefficient determinant and every ordered double residue are `+1`. Therefore, with the comparison-cone sign convention,

`d Phi(Gamma)=(Xi_log,-sigma123)`.

Thus `Phi(Gamma)=tau` is independently sourced by the ambient semistable blowup rather than by freely adjoining a cone cell.

This is a geometric top-weight `HomotopyLift`, not a degree-one element of the rank-26 or motivic source. The full integral Gersten decoration, especially the exact tame unit `-v/u`, is not yet attached.

## Disposition

The top-weight geometric realization passes. The next leaf decorates `Gamma` with the full tame units and checks all divisor and point residuals.

## Verification

- `research/voevodsky/check_cosmology_ambient_star_regulator_realization.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
