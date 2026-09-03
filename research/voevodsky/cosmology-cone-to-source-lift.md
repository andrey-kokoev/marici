# Cone-to-source lift

## Question

Does any materialized source contain a degree-one element mapping to the formal comparison cell `tau`?

## Claim boundary

No.

- The complete rank-26 p-normal source has zero image and cannot supply the unit `Xi_log` component.
- A higher-Chow precycle bounding the nonzero symbol would make `{u,v}` motivically exact; `CH^2(U,1)` supplies no torus-dependent alternative.
- The ordinary blowup dual complex is a circle with no geometric face over its primitive cycle.
- `log(u)dlog(v)` is local, and its Cech jumps reconstruct rather than remove the comparison class.

The formal cell `tau` is nevertheless valid inside the comparison cone. A source-natural chain homotopy between regulator realizations would be an operator or natural transformation, not automatically an element of the source complex with the requested differential.

## Disposition

No materialized degree-one source lift exists. The remaining type question is whether the admissible scientific constructor may be a source-natural regulator homotopy rather than a source-chain element. The next leaf states and tests that distinction.

## Verification

- `research/voevodsky/check_cosmology_cone_to_source_lift.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
