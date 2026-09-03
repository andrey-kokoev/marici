# Milnor sign 2-torsion

## Question

Do the diagonal Milnor corrections vanish in `Q(u,v)`, and can localization detect them?

## Claim boundary

They are nonzero of exact order two. The identities

`{u,u}=-{u,-1}` and `{v,v}=-{v,-1}`

show that twice each class vanishes. Their primary tame signs on the three projective boundary lines are

- `{u,u}`: `X -> -1`, `Y -> 1`, `Z -> -1`;
- `{v,v}`: `X -> 1`, `Y -> -1`, `Z -> -1`.

Since `-1` is nontrivial in the characteristic-zero divisor function fields, the classes are nonzero. The product of each sign vector is one, as required by reciprocity.

All secondary valuations of these constant units vanish. Hence the free Parshin triangle vector and `Xi_log` are unchanged. A map from this 2-torsion subgroup to the free Tate lattice is zero, so the signs cannot fill the primitive horn. They remain additional integral K1 boundary components.

## Disposition

The diagonal correction is a genuine regulator-invisible sign layer. Rational comparisons may forget it, but complete integral boundary claims must retain it. The next leaf augments the triangle data by this sign layer and tests full coordinate covariance.

## Verification

- `research/voevodsky/check_cosmology_Milnor_sign_2_torsion.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
