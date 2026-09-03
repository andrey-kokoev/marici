# Regulator homotopy constructor

## Question

Does the full Gersten/log/flag comparison produce a nonzero natural homotopy whose value is the formal cone cell?

## Claim boundary

No. There are three sourced maps:

- `R_log` from the weight-two Gersten complex to logarithmic residue data;
- `R_flag` from tame units to ordered secondary valuations;
- `Res` from logarithmic data to the flag complex.

On `{u,v}`, its tame tuple, all six ordered flags, and the three oriented edges,

`Res R_log = R_flag`

strictly. The flag vector is `(-1,1,-1,1,-1,1)` and the edge vector is `(1,1,1)` on both routes. The constant `-1` in `-v/u` has both `dlog` and secondary valuation zero.

Hence the canonical homotopy between the two maps after placing them in the common flag codomain is `H=0`.

In the signed comparison cone, the same strict equality is encoded by the boundary `(Xi_log,-sigma123)=d tau`; composing the signed graph map with the canonical cone contraction gives a nonzero target nullhomotopy taking `{u,v}` to `tau`. This is a formal HomotopyLift determined by the cone, not an ElementLift in the source.

## Disposition

The common-codomain comparison is strict, while the signed cone packages that equality as a formal path. The next leaf separates this target path from a source-chain horn.

## Verification

- `research/voevodsky/check_cosmology_regulator_homotopy_constructor.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
