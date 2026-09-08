# Seven-point local ideal: bounded fiber test

## Question

Do overlapping local rectangle equations miss triangle toric relations of degree two or three?

## Claim boundary

Use the 42 labelled seven-point triangulations and all facet rectangles, not merely rectangles based at one chosen cell. This test concerns homogeneous polynomial degrees at most three; it does not determine the full ideal or its boundary components.

The checker generates 63 distinct local quadratic moves. In each fixed degree, vertices are all monomials of that degree and edges multiply a local move by a complementary monomial. Triangle-incidence sums define the toric fibers. A binomial belongs to the local ideal exactly when its two monomials are connected by these moves: edge differences span each connected component's zero-sum subspace, over any field. Homogeneity prevents higher-degree multipliers from supplying additional relations in the tested degree.

All 903 quadratic monomials give 840 fibers, each connected. All 13244 cubic monomials give 10801 fibers, each connected. Thus every triangle toric binomial in these two degrees lies in the local ideal. No degree-two or degree-three counterexample survives this exhaustive test.

## Disposition

The proposed low-degree boundary obstruction is not found. Full seven-point ideal equality, primeness, radicality, and saturation remain undecided. A next discriminating test must either establish a generating-degree bound or examine a new degree; the present counts do not supply such a bound. The checker and results preserve the exact ordering for reuse.
