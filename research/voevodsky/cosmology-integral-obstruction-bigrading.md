# Integral obstruction bigrading

## Question

What group retains the free coefficient and primary tame signs, and which parity constraint is actually valid?

## Claim boundary

The full chain-level boundary group is

`D=Z x (Z/2)^3`.

The free coefficient and three constant-sign bits are independent for general Gersten cycles. The earlier fiber product

`B={(n,s): sum(s)=n mod 2}`

is only the image constraint for monomial Milnor-symbol boundaries. It is not the full boundary group: the closed isolated-line class `(0,(0,0,1))` is a counterexample.

Diagonal Milnor boundaries span the even-parity plane

`E={(0,0,0),(1,0,1),(0,1,1),(1,1,0)}`.

Quotienting sign decorations by this diagonal boundary plane leaves one parity bit as bookkeeping for monomial tame-symbol representatives. This quotient is not a cohomology group combining the free class with `H*(-1)`: those terms occupy different positions in the localization/Gersten total complex. At chain level, exact comparison still requires the full decorated vector.

## Disposition

The fiber-product overreach is repaired. It governs monomial symbol images, while `D` governs arbitrary boundary chains. The parity quotient is only representative bookkeeping. Column tests must use all three sign equations at chain level, or one parity equation only after quotienting by explicitly admitted diagonal boundaries.

## Verification

- `research/voevodsky/check_cosmology_integral_obstruction_bigrading.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
