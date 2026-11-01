# Reflection assembly: exact ports and routed history comparisons

Date: 2026-10-28.

## Result and scope

All 32 endpoint requests from the four-bit history graph have been routed through actual shared edges of the existing variant-A assembly. Each has a unique shortest path in the geometric seam graph. The 22 requests that also have a second simple route produce exactly the same complete affine transport along either route.

This is a new, explicitly selected geometric routing convention. It is not a recovered native Su-32 rule or a derivation of 32 independent physical wires. The previous input supplied a 16-history, 14-cell assembly and seam reflections; it did not supply a port or routing policy. No native repository files or native P/N/E records were used in this audit.

## Inputs retained

The source is `reflection_32_connection_view.html`, including its embedded exact transformations, history labels, and cell incidences. `reflection_experiment_note.md` supplies the two full 4D simplex lifts. The copied `check_reflection_variants.py` supplies the earlier exact affine arithmetic.

The seed projected vertices are O=(0,0), A=(1,0), B=(0,1), in a triangular basis. The maps are

    W(u,v) = (u+v,-v)
    R(u,v) = (-u-v,u)
    E(u,v) = (1-v,1-u).

A history b=(b1,b2,b3,b4) has frame

    T_b = R^b4 E^b3 R^b2 W^b1.

There are 16 history records and 14 different ordered frames. The two duplicated frames have all their original history IDs retained. The geometry is a readout; histories are not identified.

Each frame is extended by the identity on the two hidden coordinates. The full five-vertex simplices are exactly the two prior nonregular realizations, not claimed native Su-32 cells:

    centered:  D=(1/3,1/3,1,0), E=(1/3,1/3,0,1);
    asymmetric: D=(1/4,1/4,1,0), E=(1/2,1/4,0,1).

O,A,B have zero hidden coordinates. The projections of D,E lie strictly inside the seed triangle. Consequently a point of a full simplex that projects onto one of its outer triangle edges has zero D and E coefficients: a positive convex contribution from an interior point cannot lie on that supporting edge. Thus each shared projected edge is the actual shared 4D edge, not an unseen thick overlap. The two full simplices meet exactly along that edge. This argument uses the declared lifts and cannot be transferred to arbitrary projected 4-simplexes.

## 1. Port and continuation definitions

For every cell and each of its three projected OAB edges, create a local port retaining:

    cell ID;
    full inherited endpoint labels of the edge;
    exact four-coordinate edge midpoint;
    adjacent cell ID, or external-boundary status;
    all construction histories recorded over that cell.

Choosing the midpoint is a new symmetric representative-point convention; the geometry fixes the entire seam pointwise, not just this representative.

There are 42 local ports. Twenty-eight are paired over the 14 internal seams. Fourteen remain exposed boundary ports. We do not invent exterior cells or connect ports through vertex-only contacts. These ports belong to the actual OAB seams, not to all tetrahedral facets of a 4-simplex.

Each of the 32 requests retains its original pair of four-bit history labels. The routing convention is: use a path with the fewest seam crossings between their endpoint cells. Exhaustive simple-path enumeration shows that every request has exactly one shortest path in this specific finite graph. This is not a general theorem that shortest routes are unique.

At an intermediate cell the packet retains request ID, full route, current route index, exact ingress and egress ports, and its payload. The next port is the next seam on that route. Reversal reverses the route and uses inverse seam transport. No branch is selected merely from a geometric endpoint or from an erased history.

To realize a route as a continuous curve in the full 4D union, connect each selected seam midpoint to the current simplex's five-vertex barycenter. Every segment lies in the corresponding convex simplex. Paired seam points agree in all four coordinates. The display shows the planar projection of this piecewise-linear curve. Curves may share segments or cross; no independent physical lane capacity is inferred.

## 2. Seam transport is derived, not an added route-dependent map

Let T_i be the ordered source-to-cell frame. Let S_ji be the orthogonal reflection in the actual common seam, extended by the identity on hidden coordinates. For every one of the 14 seams, exact calculation establishes

    S_ji = T_j T_i^(-1).

All five ordered vertices, not just the triangle, match. This is true for both tested lifts. In the inherited label coordinates, the permutation of O,A,B,D,E is the identity. Their physical coordinates generally change.

For an arbitrary route i0,...,im,

    S_(im,im-1) ... S_(i1,i0)
      = T_im T_(im-1)^(-1) ... T_i1 T_i0^(-1)
      = T_im T_i0^(-1).

This is an all-finite-walk proof. The finite checker verifies every simple path for all 32 requests as an independent regression. Detours and repeated central windings change route histories but not the affine frame transport. No claim is made that native proof/history payloads have trivial transport or that route histories are literally equal.

A five-slot opaque payload indexed by inherited vertex labels therefore survives every seam and inverse route without relabelling or numerical mixing. This is a stated payload convention, not a newly inferred physical quantity.

## 3. All 32 requests are realized

| Minimum seam crossings | Number of requests |
|---:|---:|
| 1 | 10 |
| 2 | 12 |
| 3 | 4 |
| 4 | 1 |
| 5 | 2 |
| 6 | 2 |
| 8 | 1 |

The sum is 32. There are 54 simple paths in total over the 32 requests: 10 have one, 22 have two. All 32 shortest paths are unique. The longest selected route is

    history 0110 -> history 0111
    C6 -> C7 -> C4 -> C0 -> C3 -> C2 -> C10 -> C13 -> C12.

A previously point-contact-only comparison, 0000 -> 0001, now follows

    C0 -> C3 -> C2.

Its other simple route is

    C0 -> C1 -> C8 -> C9 -> C2.

Both give exactly the requested endpoint transformation R. No discontinuous jump at the common central vertex is used.

A previously separated-cell comparison, 0010 -> 0011, now follows

    C4 -> C0 -> C3 -> C2 -> C10.

For the simultaneous census of shortest requests there are 80 seam traversals, using 13 of 14 seams. The unused seam is C1--C8. The maximum shared load is 12 requests on C2--C3. These are routing counts, not capacities. Unique request tags allow a formal multiplexed record; they do not prove physical independence of those payloads.

## 4. What fibration is actually constructed

The geometric seam graph B has 14 vertices and 14 edges, is connected, and has one independent graph cycle. It has four vertices of degree 1, six of degree 2, and four of degree 3.

Define a discrete state over each cell by choosing one of the five inherited vertex labels. Seam transport supplies the label permutation. Because every permutation is identity in the global source frames, the derived graph has

    vertices (cell,label),
    edges ((i,label),(j,label)) whenever i,j share a seam.

The projection forgetting the label is locally bijective on incident edges and is a genuine five-sheet covering of B. The checker verifies this at all 70 lifted vertices. The lifted graph has 70 edges and five connected components, each isomorphic to B. Thus this explicitly defined covering is the trivial cover

    B x {O,A,B,D,E} -> B.

This is a bundle of label states, not the actual spatial union of the 4-simplexes. Similarly, retaining the entire barycentric simplex as a state fiber yields a trivial associated bundle after specifying the graph-based construction. Neither is a Hopf bundle or evidence for nontrivial native fiber transport.

The general permutation-labelled graph-cover construction is described in Dalfó et al., “Spectra and eigenspaces of arbitrary lifts of graphs,” Journal of Algebraic Combinatorics, sections 2.1--2.2:
https://link.springer.com/article/10.1007/s10801-021-01049-3
The source gives the general framework; the identity permutations and counts above are computed here.

The 16-history projection is not that covering: two cells have two histories and twelve have one, and a single history-cube link can map to a multi-edge geometric path. The 32 requests are edges of a selected source graph, not a fiber cardinality.

## 5. What is forced and what remains selected

Forced by the tested geometry: exact contacts, seam reflections, complete five-vertex maps, and route-independent geometric transport.

Explicitly selected in this experiment: midpoint port representatives, the five-label payload interface, shortest-seam routing, per-request multiplexing, and the graph-cover interpretation of label states.

At a trivalent cell, geometry admits multiple outgoing seams. It does not select one from the incoming seam alone. The target/request and selected route are real inputs to our continuation rule. A unique geometric transport between cells does not make their route histories unique.

This makes an executable 32-request router, not a derivation of a native 32-independent-wire law. A geometric route cannot be silently promoted to a source-authorized P/N/E operation. No further replication or primitive wiring was introduced to make the number 32 appear.

## Reproduction and verification

    python check_port_routing.py --output results.json
    python build_viewer.py

Exact arithmetic checks: 692 assertions. All 14 seams were checked on both full 4D lifts; all 32 routes and all 54 simple alternatives were checked. Negative controls reject a swapped full label map, a point-only shortcut, and a disjoint-cell shortcut.

Browser checks use Python Playwright with the installed Chromium. Every request was stepped to completion and reversed; available alternatives, both lifts, port display, and seam loads were exercised. Desktop and mobile screenshots are retained; the mobile page has no horizontal overflow. No browser script errors occurred. The script uses `set_content` because this runtime blocks `file://` navigation; the delivered HTML has no external dependency.

No Agda or Lean compilation, native Su-32 execution, or repository write occurred. Source snapshots and SHA-256 manifest are included.
