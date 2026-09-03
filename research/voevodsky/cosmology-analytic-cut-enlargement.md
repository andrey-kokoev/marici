# Analytic cut enlargement

## Question

Can declaring the logarithmic cut to be a boundary make `Xi_log` exact while preserving comparison to the uncut torus?

## Claim boundary

No. Cutting `T^2` along one generator gives a cylinder. Its absolute second homology is zero, so the logarithmic form becomes exact there. But the cut cylinder has no nonzero second-homology class that can map faithfully to the torus generator.

For the relative pair consisting of the cylinder and its two boundary circles, second homology is again `Z`. Its relative fundamental class maps to the torus fundamental class, but its cut-edge boundary data remain present. Thus the comparison is faithful only when the obstruction is retained.

Cellularly, the cut face has boundary `e_right-e_left`. Dropping this term loses descent. Keeping it yields the unit jump; gluing the edges converts the face into the nonzero torus cycle, not a boundary.

## Disposition

The cut construction has a strict dichotomy: absolute treatment kills faithfulness, while relative treatment preserves both comparison and obstruction. The next leaf tests whether a nontrivial rank-one local system can kill the class and specialize faithfully to the trivial character.

## Verification

- `research/voevodsky/check_cosmology_analytic_cut_enlargement.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
