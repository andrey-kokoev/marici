# Relative-only sign class and horn impact

## Question

Can the isolated hyperplane-sign class alter the horn differential as a same-degree correction?

## Claim boundary

No. A degree audit exposes a prior conflation. `{u,v}` lies in motivic degree two, while the isolated divisor-sign cycle `H*(-1)` represents a class in

`CH^2(P2,1)=H_M^3(P2,Z(2))`.

The full tame tuple `(v^-1,u,-v/u)` is a Gersten boundary of `{u,v}`. Splitting off the `-1` on `Z` creates the nonzero class `H*(-1)` only because the complementary nonconstant unit tuple carries the opposite Gersten class. Their sum remains exact.

Therefore `H*(-1)` is an obstruction to isolating the sign with no compensating residues. It is not an independent degree-two horn component and cannot be added as a same-degree closed corrector.

## Disposition

The prior `Z plus Z/2` horn group, two-lift claim, and index-two localization interpretation are withdrawn. Their parity formulas remain valid only for chain-level tame-sign bookkeeping. The next leaf places K2, divisor K1 units, point valuations, `Xi_log`, and `sigma123` in one correctly graded total complex.

## Verification

- `research/voevodsky/check_cosmology_relative_only_cokernel_horn_impact.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
