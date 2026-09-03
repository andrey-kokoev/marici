# Rees-splitting obstruction

## Question

What exactly obstructs promotion of the special-fiber horn to the total DNC?

## Claim boundary

Let `K_tot` be the witnessed total-DNC comparison object and `K_0` its special-fiber relative pair, with restriction

`rho:K_tot -> K_0`.

The special-fiber class `tau0` lifts only if it lies in the image of `H(rho)`; its first obstruction is its class in the corresponding cokernel. Retaining the chosen nullhomotopy requires the stronger datum of a point in the homotopy fiber of the mapping-space restriction over `tau0`.

A multiplicative splitting of the completed Rees or `I`-adic filtration supplies a section and kills every such obstruction. It is sufficient, not necessary. A nonsplit formal neighborhood may still lift this particular class.

Stagewise splittings of

`0 -> I^(n+1)/I^(n+2) -> I^n/I^(n+2) -> I^n/I^(n+1) -> 0`

are strong input; compatible multiplicative coherence is additional. Their failure alone does not prove that `tau0` fails to lift.

The relative p-normal theorem uses only `tau0` and is unaffected.

## Disposition

The exact gate is restriction/fiber liftability, not full formal linearization. The next leaf computes this obstruction in the local polynomial carrier.

## Verification

- `research/voevodsky/check_cosmology_Rees_splitting_obstruction.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
