# Universal integral descent cocycle

## Question

Do the local symbols `{u,v}` glue integrally over an arbitrary ordered line decomposition?

## Claim boundary

Not in general. On overlaps write

`u_beta=a u_alpha`, `v_beta=b v_alpha`,

where `a` and `b` are transition units for `L1 L3^-1` and `L2 L3^-1`. Bilinearity gives

`{u_beta,v_beta}-{u_alpha,v_alpha}={a,v_alpha}+{u_alpha,b}+{a,b}`.

Its tame factors on `(D1,D2,D3,E)` are `(b^-1,a,b/a,1)`. They have zero vertical valuations and product one. On triple overlaps these differences telescope, so they form a Cech one-cocycle.

A nonzero cocycle is nevertheless an obstruction to gluing local K2 sections; a K2 element is not a path between K2 elements. If both ratio line bundles are compatibly trivialized, `a=b=1` and the obstruction vanishes.

The relative logarithmic class and vertical tame residues still descend. A derived integral lift without trivial ratios would require explicit K3-level homotopies and coherence, which are not supplied by the ordered splitting.

## Disposition

Universal top-weight descent passes, while global integral Milnor descent requires trivial ratio torsors or higher K-theory data. The next leaf tests the intended carrier for those trivializations.

## Verification

- `research/voevodsky/check_cosmology_universal_integral_descent_cocycle.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
