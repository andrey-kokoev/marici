# Horn assumption-relaxation census

## Question

Does relaxing any premise of the fixed-horn no-go preserve the original problem or a source-derived readout?

## Claim boundary

None of the four relaxations solves the original horn.

- Changing or subtracting the target removes the required `(Xi_log,-sigma123)` boundary.
- Changing the degree or differential equation retains `{u,v}` as a closed degree-two obstruction but abandons the degree-one horn.
- Dropping chain-map compatibility makes boundary and cohomology transport undefined; representative-level assignments do not replace it.
- Dropping regulator detection permits a quotient to kill `Xi_log`, but then it cannot read the verified primitive class.

Only the second relaxation preserves the sourced invariant. It defines a new, bounded question: treat the K2/triangle class as an obstruction or period candidate rather than a filler. This reformulation must remain explicit and supplies no backward claim that the horn exists.

## Disposition

The original fixed horn has no admissible escape among the four logical premise relaxations. The next leaf computes the canonical torus period of the K2 regulator, its orientation dependence, and the boundary between a mathematical period and any physical readout claim.

## Verification

- `research/voevodsky/check_cosmology_horn_assumption_relaxation_census.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
