# Subdivision invariance of the derived pair

## Question

Do toroidal subdivisions preserve the sourced relative horn and regulator?

## Claim boundary

Yes for witnessed regular stellar subdivisions. The sum of oriented refined top cells cancels every internal face and retains the original outer boundary. Hence subdivision gives a quasi-isomorphism of derived pairs and preserves the primitive relative fundamental class.

The toroidal modification leaves the function field and `{u,v}` unchanged. A new divisor with primitive valuation ray `(a,b)` must carry tame unit

`(-1)^(a b) u^b/v^a`.

Including every new exceptional component gives the complete Gersten boundary of the same symbol, so codimension-two residuals still vanish. Omitting those terms would not be a regulator comparison.

Thus the coarse and refined models represent the same relative class through subdivision/common refinement. This preserves a previously sourced horn; it cannot manufacture one from the absorbed rank-26 presentation.

## Disposition

The geometric-pair category may be localized at witnessed toroidal subdivisions. The next leaf formalizes the distinction between preservation and construction so birational replacement cannot launder an unsourced cone.

## Verification

- `research/voevodsky/check_cosmology_subdivision_invariance_of_derived_pair.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
