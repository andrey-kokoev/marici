# Degree-one torsion corrector

## Question

Does `CH^2(U,1)` contain a torus-dependent order-two class capable of correcting the horn signs?

## Claim boundary

No. For `U=(G_m)^2`, the split-motive decomposition gives

`H_M^3(U,Z(2)) = H_M^3(Q,Z(2))`

plus two copies of `H_M^2(Q,Z(1))` and one copy of `H_M^1(Q,Z(0))`. The latter groups vanish: `H_M^2(Q,Z(1))=Pic(Q)=0` and `H_M^1(Q,Z(0))=0`.

Thus only base-field classes can survive in degree one. This conclusion does not require computing their torsion. Their pullbacks are unramified along `X,Y,Z` and have zero coordinate-divisor tame boundary, so they cannot alter the residual sign coordinates.

The classes `{u,u}` and `{v,v}` are torus-dependent but lie in motivic degree two, not degree one. Regrading them is inadmissible.

## Disposition

The absolute higher-Chow degree-one group contains no torus-dependent torsion corrector. Any remaining possibility must be genuinely relative and boundary-supported. The next leaf computes those localization terms and tests their additional residuals.

## Verification

- `research/voevodsky/check_cosmology_degree_one_torsion_corrector.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
