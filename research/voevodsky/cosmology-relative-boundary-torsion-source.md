# Relative boundary torsion source

## Question

Does the boundary-supported relative degree contain a sign corrector with no additional residuals?

## Claim boundary

No. The tuple with constant unit `-1` on `Z` and `1` on every other divisor is a Gersten cycle because all secondary valuations vanish. On `P2`, the projective-bundle formula contains the direct summand

`H CH^1(Q,1)=H Q^x`.

The isolated sign cycle represents `H` times `-1` in this summand. It is nonzero of exact order two.

Consequently, no rational-function K2 element has `-1` on `Z` as its sole divisor residue with every other residue zero. Any symbol producing that sign requires compensating divisor data. The class is closed in `CH^2(P2,1)`; adding it to a degree-one candidate does not change the candidate's differential.

## Disposition

The relative search finds a hyperplane-sign obstruction, not a corrector. The next leaf combines this order-two class with the primitive pure-Tate class into the complete integral obstruction object.

## Verification

- `research/voevodsky/check_cosmology_relative_boundary_torsion_source.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
