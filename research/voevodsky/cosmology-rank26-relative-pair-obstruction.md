# Rank-26 relative-pair obstruction

## Question

Can the rank-26 no-go be stated invariantly in the witnessed relative-pair category?

## Claim boundary

For a relative class `gamma`, apply the connecting boundary, the regulator comparison, and projection to the `Xi` coefficient. Call the resulting integer `omega(gamma)`.

The full characteristic-zero absorption theorem gives

`im(omega_R)={0}`

for the rank-26 p-normal source. The required horn has `omega(Gamma)=1`. Therefore its obstruction is

`Ob_R=1 in Z/im(omega_R)=Z`,

which is nonzero. Any comparison-respecting relative-pair morphism carrying a rank-26 class to `Gamma` would preserve `omega` and force `0=1`.

This obstruction survives strict ordered base change and witnessed subdivision. Orientation reversal changes its sign but not nonvanishing. Ramified pullback multiplies it by `det(M)` and cannot turn zero into a unit.

`omega` is only a separating functional: vanishing would not by itself solve the complete boundary-vector problem. Nonvanishing already excludes the lift.

## Disposition

The no-go is functorial in the localized witnessed category. The next leaf classifies the universal minimal witnessed extension that kills this obstruction without confusing an absolute acyclic disk with a relative source object.

## Verification

- `research/voevodsky/check_cosmology_rank26_relative_pair_obstruction.py`
- Input evidence: `research/voevodsky/results/cosmology_full_rank26_characteristic_zero_absorption.json`
- New checker execution pending because structured-command MCP is unavailable in this turn.
