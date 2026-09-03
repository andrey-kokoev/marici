# Obstruction universality and minimal extension

## Question

What is the universal minimal relative extension killing the `Xi` obstruction?

## Claim boundary

Starting from `B_R -> G_R`, define

`B_plus=B_R direct_sum Z z`,

`G_plus=G_R direct_sum D(z)`,

where `D(z)` has `Gamma` in degree one, `z` in degree two, and `d Gamma=z`. Send `z` to the complete boundary vector `(Xi_rel,-sigma123,0 residuals)`.

Although `D(z)` is absolutely acyclic, the relative cofiber is

`G_plus/B_plus=(G_R/B_R) direct_sum Z Gamma`.

Thus `omega(Gamma)=1`. In the category of relative extensions under `R` with a chosen element having the exact boundary vector, this construction is initial: the unique map sends `Gamma` to that element and fixes `R`.

One relative generator is necessary and sufficient. Any smaller extension leaves `im(omega)=0`.

This is algebraic initiality, not uniqueness of geometry. Admission still requires a geometric witness. The local ambient star supplies one; no global carrier witness is materialized. Distinct geometric witnesses may realize the same algebraic pair without being equivalent.

## Disposition

The obstruction is killed by a minimal rank-one relative attachment, not by an absolute acyclic enlargement. The next leaf classifies geometric nonuniqueness and the equivalence relation on witnesses.

## Verification

- `research/voevodsky/check_cosmology_obstruction_universality_and_minimal_extension.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
