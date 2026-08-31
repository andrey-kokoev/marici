# Exact-degree source inventory for the relative horn

## Result

The horn requires a sourced degree-one cell with differential column `(1,1)` in the degree-two basis `(Xi_log,-sigma123)`. No currently materialized object has that type.

- The ordered exceptional/Cech face `sigma123` is sourced but already lies in degree two; it maps to pair-face edges.
- The exceptional hyperplane Gysin class `H` is source-derived but has no map to `Xi_log` and does not occupy the incoming horn position.
- Abstract `tau_p` has the right degree and column but is not sourced.
- No Cayley-Menger face exists at the marked-wall collision.

## Typing correction

The preceding attachment and Bezout analyses classify faces filling the boundary triangle. That task is already performed at residue level by `sigma123`. Those analyses do not construct the one-degree-lower preimage of the closed pair `Xi_log+minus_sigma123`.

Consequently the actual degree-one source inventory is empty, and there is no sourced attachment-degree ideal to test for the horn.

## Next gate

Seek a degree-one cell from a genuine totalization mechanism: a sourced mapping cone, deformation-to-normal cone, or relative incidence correspondence. Another boundary face cannot solve the degree mismatch.

## Verification

- `research/voevodsky/check_cosmology_relative_horn_source_degree_inventory.py`
- `research/voevodsky/results/cosmology_relative_horn_source_degree_inventory.json`
