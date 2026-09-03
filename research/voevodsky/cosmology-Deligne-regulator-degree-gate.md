# Deligne regulator degree gate

## Question

Does Deligne regulator extension data turn `{u,v}` into a degree-one filler?

## Claim boundary

No. The symbol lies in motivic cohomology `H_M^2(U,Z(2))` and maps to `H_D^2(U,Z(2))`. Its curvature is `Xi_log`, and its integral projection is the primitive generator of `H^2(U,Z(2))`, pairing to one with the ordered Betti torus.

The degree-two Deligne group projects to integral classes in `F^2 H^2`. Its kernel is an `H^1`-based intermediate quotient that can alter secondary or logarithmic branch data, but cannot cancel the nonzero integral projection. A Deligne coboundary would have zero projection.

Local expressions such as `log(u) dlog(v)` are degree-one representatives only on branch charts. Their overlap jumps complete a global degree-two Cech–Deligne cocycle; they are not a global precycle whose differential is `Xi_log`.

## Disposition

The Deligne regulator retains the degree-two obstruction. The next leaf computes the branch transitions of the local logarithmic primitives and identifies their monodromy as the precise globalization obstruction.

## Verification

- `research/voevodsky/check_cosmology_Deligne_regulator_degree_gate.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
