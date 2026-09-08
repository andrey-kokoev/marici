# Six-point zero-support audit

## Question

Does admitting zero weights separate locally factorizing supports from triangle-monomial supports?

## Claim boundary

This is an exhaustive six-point Boolean census over a field. It concerns support, not arbitrary values on that support or a theorem for every polygon size. Triangulation indices use results/local_global_torus_lattice.json.

For a proposed support S, collect every factor appearing in a positive monomial. These factors must all be nonzero. Every monomial using only these forced factors must then be positive. This closure condition is necessary and sufficient for Boolean monomial realization: set the forced factors to one and all others to zero. It avoids division and avoids enumerating factor assignments redundantly.

The checker tests all 16384 subsets of the fourteen triangulations. Exactly 4000 satisfy the three local facet cross-products, and exactly the same 4000 are triangle-factor supports. Only 151 are channel-factor supports. The channel supports form a subset of the triangle supports; equality of local and triangle supports is verified setwise, not inferred from equal counts.

## Disposition

The minimum-cardinality triangle-versus-channel separator has positive indices 1 and 2. Their channel factors force index 0 positive, contradicting its prescribed zero. It is realized by triangle factors and passes the local minors. The census excludes a support-only local-versus-triangle obstruction at six points. It does not show that arbitrary nonzero weights on each support admit triangle factors; the restricted integer lattices and possible coefficient obstructions remain to be tested.
