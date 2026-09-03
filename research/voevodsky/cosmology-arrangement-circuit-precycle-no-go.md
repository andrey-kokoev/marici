# Arrangement-circuit precycle no-go

## Question

Can the first-order arrangement circuit lift to a regular total degree-one precycle `h` satisfying

`d(h)=t (Xi_log,-sigma123)`

with no residual components?

## Claim boundary

No, provided the family comparison preserves the already verified generic regulator class. Restricting such an identity to `Q[t,t^-1]` makes `t` invertible and gives

`(Xi_log,-sigma123)=d(t^-1 h)`.

This contradicts the established nonexactness of the generic class, which generates the constant rank-one second cohomology on every nonzero fiber.

A `t`-Bockstein identity can represent only a cohomology class killed after inverting `t`. Here `Xi_log` survives after inversion and is lost only upon specialization to the concurrent fiber. The circuit residual `tZ` is therefore a dependence determinant, not a total differential identity compatible with the regulator comparison.

## Disposition

The regular arrangement-circuit branch is falsified. A subsequent route must change the generic comparison, introduce a new source complex, or target a different torsion class. The highest-value remaining test is whether higher-dimensional geometry can add a face while retaining a faithful pullback to the nonzero generic class.

## Verification

- `research/voevodsky/check_cosmology_arrangement_circuit_precycle_no_go.py`
- Execution pending: structured-command MCP was unavailable in this turn, so no results JSON is claimed.
