# Universal common-line integral horn

## Question

Does the common-line category carry a universal full integral realization rather than only a top-weight class?

## Claim boundary

Yes. Let a base `C` carry a line bundle `L` and an ordered identification

`N^vee=L plus L plus L`.

Tensoring by `L^-1` does not change projectivization, so `P(N)` is the canonical `P2`-bundle. The homogeneous ratios

`u=x1/x3`, `v=x2/x3`

are global rational functions. Hence `{u,v}` is a global Milnor K2 symbol with tame tuple

`(v^-1,u,-v/u,1)`

on `(D1,D2,D3,E)`. Outer ordered residues are `(-1,+1)`, radial residues vanish, and every Gersten sum is zero.

The universal star `Gamma` satisfies

`d Phi(Gamma)=(Xi_rel,-sigma123)`

with the complete integral decoration. Blowup, projectivization, ratios, symbol, star, and regulator equation all commute with base change of `(C,L)`.

## Disposition

A universal full integral geometric `HomotopyLift` exists in the common-line category. It is not an `ElementLift` in the rank-26 or higher-Chow source. The next leaf states the minimal carrier classifying map needed to pull it back.

## Verification

- `research/voevodsky/check_cosmology_universal_common_line_integral_horn.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
