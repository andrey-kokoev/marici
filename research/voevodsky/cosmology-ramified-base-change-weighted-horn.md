# Ramified base-change weighted horn

## Question

Can a ramified pullback be normalized integrally back to the primitive horn?

## Claim boundary

For a monomial normal-torus map

`u -> x^a y^b`, `v -> x^c y^d`,

let `M` be its character-lattice matrix. Pullback multiplies the logarithmic orientation, Milnor top symbol, and oriented relative horn class by `det(M)`.

The pullback remains primitive exactly when `det(M)=1`; determinant `-1` is primitive with reversed orientation. For diagonal ramification indices `e,f`, the multiplier is `e f`. When `e f>1`, no integral linear operation recovers the primitive generator from the weighted class alone. Transfer does not help because transfer after pullback multiplies by the finite degree.

The reduced pulled-back divisors can define a new intrinsic primitive star upstairs. That is a saturated geometric reconstruction from new divisor data, not division of or equality with the pulled-back horn. Their comparison is

`weighted pullback = det(M) times saturated primitive horn`,

up to orientation.

## Disposition

Ramified maps produce valid weighted `HomotopyLift` classes, not the primitive constructor. Primitive recovery requires a separate saturated geometric witness or rational coefficients. The next leaf classifies the maximal primitive naturality category, including fan compatibility.

## Verification

- `research/voevodsky/check_cosmology_ramified_base_change_weighted_horn.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
