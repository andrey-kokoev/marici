# Two reciprocal tetrahedral lattices: P/N assignment prototype

## Question and boundary

Operator proposal: two tetrahedral lattices, vertices of either at barycenters
of tetrahedra on the other; P is a tetrahedron of one, N of the other.

This realizes the literal reciprocal-center rule as a bipartite, four-coordinate
network (a diamond-type coordinate realization). It does NOT silently require
Euclidean space-filling or identify it with the conventional cell-dual of two
face-to-face tetrahedral tilings. The selected same-family tetrahedra meet only
at vertices. Coordinates are one checking/drawing chart for the abstract network.

P has A vertices and a B center; N has B vertices and an A center. Colored dots
are lattice sites, NOT nucleons. P/N names label entire tetrahedra and are the
operator's proposed assignment, not derived charge or native particle identity.

## Exact source construction

Use primitive translations (0,2,2), (2,0,2), (2,2,0). A sites are integer sums
of these. B is A+(1,1,1). Four A-to-B displacements are

    (1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1).

They sum to zero. Reversing all four gives the B-to-A neighbors. Consequently
EVERY A is the exact arithmetic barycenter of a B tetrahedron and EVERY B the
barycenter of an A tetrahedron. All six squared tetrahedron edges are 8, all
center-to-corner squared distances are 3, and the oriented volume determinants
are opposite signs with absolute value 16 (positive volume 8/3 in this chart).
The exact duality is the involution x -> (1,1,1)-x: it exchanges A and B
and maps each whole P tetrahedron to an N tetrahedron. Consequently geometry
alone does not distinguish intrinsic P/N properties such as electric charge.
This local construction extends without an upper size bound.

A periodic 4x4x4 quotient retains 64 sites of each family and 256 center links.
For centroid checks retain unwrapped neighbor indices and deck translations:
averaging wrapped coordinate representatives would be a frame/variance error.
An explicit unwrapped six-link cycle certifies that the first loops are genuine,
not just periodic-boundary artifacts. The network has no three- or four-link
center loops; shortest loops have length six.

## New structural restriction, not a nuclear prediction

If a CLOSED finite occupied region is fully saturated, with every center using
all four reciprocal links and every opposite tetrahedron occupied, double-counting
links gives 4P=E=4N, hence P=N. Lead-208 (82P,126N) therefore cannot be represented
as a closed fully saturated region under that extra occupancy condition.

With boundary or vacancies, missing N-side slots minus missing P-side slots is
4(N-P)=176 for those counts. This is conditional port accounting, not evidence
that 176 physical nuclear bonds are missing. Site occupation, open boundaries,
extra interfaces and fiber constraints have not been selected. Geometry alone
does not decide isotope composition or stability. No comparison/holonomy maps
are invented from the six-link rings.

## DPC and verification

Problem: give the mutual-barycenter proposal a literal construction rather than
an arbitrary drawing. Candidate: the stated two-lattice incidence realizes both
centers and gives fourfold links with six-link first loops. Rivals: one-way
centroid construction; mere geometric proximity; a false conventional cell-dual
claim; wrapped-coordinate averaging; geometry mistaken for nuclear occupation.
Risky tests: exact centroids both ways, reciprocal neighbor membership, all local
tetrahedral metrics/orientations, no same-family face sharing, periodic degrees
and an unwrapped shortest-loop witness. Retain failures of naive wrapping and
closed unequal-count saturation rather than adjusting the geometry to fit Pb208.
Disposition is in `research/strominger/results/dual-tetrahedral-lattices/verification.json`.

    python research/aspect/scc/scc.py check dual-tetrahedral-lattices-v1 --verbose

The owner checker verifies exact integer geometry and graph structure, then real
browser controls and desktop/mobile screenshots. The viewer draws a selected
reciprocal pair and a finite lattice window with full halo corners. No force,
energy, native P/N/E response, stability, physical radius or capacity is derived.
Live loopback URLs are recorded in the generated `server-info.json`; do not
substitute relative file links for an operator-facing browser URL.
