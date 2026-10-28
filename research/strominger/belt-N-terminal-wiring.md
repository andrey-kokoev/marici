# Same-sign N terminal wiring

The operator-selected boundary is now explicit:

- original (+P) parent → its +N vertex;
- clone (−P) parent → its −N vertex.

Each selected vertex has one terminal bundle. The bundle retains all 175 occurrence records of its parent, with native owner IDs, geometry, labels and incidence intact. This is a lossless grouping of the current parent records over one marked base point, not a claim that a native full-field fibration map has been derived. The field-fibration and direction-conversion fields remain null.

## Directional tubes

Each terminal now groups its 16 links into four tubes. At +N these are E1, E2, E3 (outgoing) and P (return); at −N they are P1, P2, P3 and E. Each outgoing tube collects the same satellite arm from all four stars; the return tube collects their four centres. Each lane retains its link ID, star, arm, endpoints and normalized flux. Tube rates are 4, 4, 4 and 12, not equal capacities.

L1 and L1′ now use tube-first geometry: three compact majority-direction four-lane ports surround one minority-direction return port. Each port retains one lane from each original star. The three majority ports and their lane patterns are related by 120-degree rotations; the opposite outer layer is rotated 180 degrees. Original star/arm and grid addresses remain provenance for the unchanged logical wiring. L2/L2′ and L3/L3′ geometry is unchanged. The ports now occupy the four triangular faces of each planar attachment patch; all lane origins lie within their assigned triangle.

The viewer draws one shared trunk and four branches per tube. These are presentation paths, not new graph junctions or field conversion rules. Logical wiring remains 106 directed links. Triangular face bindings are now explicit declared geometric roles on the octahedral surface. Native field maps remain null; no full44 transport is asserted. Parent occurrence fibers remain intact, rather than being reduced to four tube scalars.

## Connections

At +N:

- twelve outgoing E connections supply L1's majority satellites at one normalized flux unit each;
- four incoming P connections receive the minority centres at three units each.

At −N the roles reverse: twelve outgoing P connections supply L1′, and four incoming E connections receive its centres. Each star exchanges three units each way; each terminal exchanges twelve each way.

There are 32 new terminal links, in addition to the unchanged 74 internal links. The displayed graph has 64 arrows plus two neutral terminal markers. Both directions share a terminal bundle identity but retain separate heading labels; no P/E conversion law is inferred from graph adjacency.

Terminals are anchored at the existing displayed N vertices. The six-layer belt is now centred at their midpoint, with its axis directed from clone −N to original +N; layer planes and arrow headings follow that axis. Each parent is now rigidly rotated about its fixed selected N terminal so its outward vertex normal (centroid to N) points toward the other terminal along the belt axis. The original +N normal points toward −N; the clone −N normal points toward +N. Terminal positions, the belt frame, layer spacing, star shapes and all wiring are unchanged. The octahedral body is now extracted from the native ESD7 tetrahedral–octahedral cellulation at its unchanged unit size. The earlier stretched surface has been replaced. Internal geometric balance results do not automatically extend to these newly drawn parent connections.

The renderer draws terminal links in the corresponding arrow colour in both solid and graph views. Terminals/links follow parent-copy, belt and outer-layer visibility. Terminal records have no particle role, and parent particle accounting is unchanged.

## Octahedral surface

`research/realization-tower/belt-octahedral-surface.mjs` selects complete existing cells from `buildFoldedFibration().geometry` in the integer barycentric box `abs(q_i - c_i) <= 1`, with `c = [1,0,0,0]`. No synthetic tetrahedra, octahedral diagonals or fitted surface mesh are introduced. The selected complex has 8 tetrahedra and 6 whole octahedra, 19 vertices, 60 edges, 56 triangular faces (24 internal), and ball Euler characteristic one. Its boundary is the frequency-two octahedral incidence `{3,4+}_{2,0}`: 18 vertices, 48 edges and 32 triangular faces. Six boundary vertices have valence four; twelve have valence six.

Only a rigid transform places this native subcomplex on the belt axis. Every edge has exactly the same length as the displayed parent cell edges (6/7 world units); all pairwise native distances are preserved. Layer spacing and port pitch now derive from the native body's dimensions, rather than stretching its cells to the schematic. Opposite planar four-triangle patches at L1/L1′ carry three majority tubes and one central return tube. Their centroids still match the port centres. The parent shapes and N terminals remain fixed, so terminal trunks span the remaining gap. A common global lattice registration and actual face gluing to the separately posed parents have NOT been established (`parentLatticeAttachment: null`).

Removing the eight patch faces leaves a 24-triangle annulus with two six-edge boundary loops (subdivided triangular boundaries), not the four-edge loops from removing vertex stars. In global Geometry mode the viewer shows the actual cell complex, including its 24 internal faces and 60 unique edges. Global Wiring mode instead shows the graph; these are mutually exclusive. It follows whole-belt visibility; individual layer controls continue to govern arrows rather than cutting the surface.

## Verification

- `tests/belt-native-cellulation.test.mjs`: exact source-cell and face recovery, whole octahedra, connected incidence, common parent unit edge and rigid distance preservation.
- `tests/belt-octahedral-surface.test.mjs`: boundary incidence, orientation, valence, planar patches, tube-centre correspondence, lane containment and whole-cell renderer counts.

- `tests/belt-terminal-wiring.test.mjs`: exact parent-record recovery, chosen N anchors, direction/rate/branch coverage, rendering and omitted endpoints.
- `tests/complex-visibility.test.mjs`: terminal visibility and no dangling displayed links.
- `tests/central-belt-layout.test.mjs`: 106 total links, two terminals, unchanged internal arrangement.
- `scripts/test-neutron-belt.mjs`: browser coverage in graph and solid views, counts, persistence and axial rotation.

The fibration debugger now extracts all 66 actual nodes and 106 edges. It distinguishes the completed terminal graph attachment from the two missing native terminal-field fibrations; the abandoned 49-face assignment is no longer its attachment model.
