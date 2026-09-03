# Integral total-complex degree reconciliation

## Question

Where do the symbol, tame units, signs, point valuations, `Xi_log`, and `sigma123` actually live?

## Claim boundary

The weight-two Gersten complex on `P2` is

`K2^M(Q(P2)) -> sum_D k(D)^x -> sum_p Z`.

Its codimension positions correspond to motivic degrees two, three, and four. Thus `{u,v}` is degree two; its full tame tuple `(v^-1,u,-v/u)` is a degree-three cochain; isolated sign cycles such as `H*(-1)` live in degree-three cohomology. Point valuations occupy the next position.

The logarithmic regulator sends `{u,v}` to `Xi_log` and the tame tuple to logarithmic residue data. `sigma123` is an oriented cycle in the uncontracted flag or dual-complex resolution representing the top-weight part of the same de Rham degree-two class. It is not the isolated degree-three sign class.

The notation `(Xi_log,-sigma123)` does not itself define a total complex. A valid exactness test must specify the flag complex, logarithmic complex, shifts, comparison map, and whether the equation is `d h=Xi_log-f(sigma123)` or a shifted-cone equivalent.

## Disposition

Pair exactness is reopened. Nonvanishing of `Xi_log` alone does not exclude a comparison homotopy. The next leaf defines the comparison cone and separates abstract acyclicity from source-natural horn provenance.

## Verification

- `research/voevodsky/check_cosmology_integral_total_complex_degree_reconciliation.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
