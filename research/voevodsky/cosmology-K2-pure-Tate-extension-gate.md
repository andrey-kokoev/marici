# K2 pure-Tate extension gate

## Question

Does the mixed-Hodge structure of the fixed torus class contain extension data that could mimic a degree-one Bockstein?

## Claim boundary

No. Since `H^1(G_m)=Q(-1)`, Kunneth gives

`H^2((G_m)^2)=Q(-2)`.

It has rank one and pure weight four: `W_3=0`, `W_4=H^2`, and every other weight-graded piece vanishes. The unique weight-four generator is the class identified with `Xi_log` and the primitive first-homology generator of the boundary triangle.

A nontrivial internal weight extension requires at least two nonzero graded pieces. None exists here. The earlier nearby-cycle `t`-Bockstein would require a separate family or lattice torsion class; it is not hidden in the mixed-Hodge filtration of the fixed torus.

## Disposition

The obstruction is a pure Tate class, not unresolved mixed-weight extension data. The next leaf locates `{u,v}` in motivic and Deligne degree and tests whether regulator extension data there is genuinely distinct from the excluded internal weight extension.

## Verification

- `research/voevodsky/check_cosmology_K2_pure_Tate_extension_gate.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
