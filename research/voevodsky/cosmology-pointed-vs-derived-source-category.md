# Pointed versus derived source category

## Question

Which localization-invariant category retains the geometric `HomotopyLift`?

## Claim boundary

The absolute complex

`G=[Z Gamma -> Z z]`

is acyclic. It becomes zero under ordinary derived localization. A bare pointing by `Gamma` is also ill-typed as a chain map because `d Gamma=z`.

Let `B=Z z` be the boundary subcomplex and retain the inclusion `B -> G`. The quotient, equivalently the cofiber of this inclusion, has one relative class represented by `Gamma`:

`H1(G/B)=Z`.

Thus the capability survives in the derived category of pairs or arrows. To retain the actual nullhomotopy rather than only its class, use the stable infinity-category of derived arrows together with the map to the comparison pair and its chosen 2-cell. A triangulated homotopy category alone forgets that 2-cell.

This does not authorize an arbitrary algebraic disk. Admissible pairs must lie in the image of a geometric realization functor from ordered blowup-incidence data. The ambient star qualifies locally; a freely adjoined cone does not.

The rank-26 no-go survives: its absorbed image contains no relative pair whose boundary has primitive `Xi` coefficient one.

## Disposition

The minimal durable source is a derived geometric pair, not an absolute or naively pointed complex. The next leaf defines the provenance functor that distinguishes the ambient star from an unsourced cone.

## Verification

- `research/voevodsky/check_cosmology_pointed_vs_derived_source_category.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
