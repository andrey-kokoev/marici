# Ru-98 tubing investigation

Scope: the current sixteen-strand coordinate-transfer candidate, not an intrinsic or unique Ru routing law. Analysis: `../realization-tower/ruthenium-98-tubing.mjs`. Verification: `tests/ruthenium-98-tubing.test.mjs`.

## Continuous bundles

Using the same exact-strand-membership continuation rule as Sulfur:

| Quantity | Result |
|---|---:|
| End-to-end strand identities | 16 |
| Occupied native edges | 78 |
| Maximal continuous tube segments | 22 |
| Five-edge segments | 12 |
| Two-edge segments | 8 |
| One-edge segments | 2 |
| Three-port merge/split junctions | 4 |
| Closed tube loops | 0 |

Twelve wires run the whole five-edge route without a bundle-membership change. The other four form two pairs, each sharing one edge and then separating: two incoming two-edge tails, a shared one-edge section, and two outgoing two-edge tails. Each pair differs only in information-flow polarity `b`; its other three labels agree.

The shared edges are:

- `(-1,1,-1,2) -> (-1,2,-1,1)`: `ru:wire:++-+` and `ru:wire:+--+` (red–white).
- `(1,-1,2,-1) -> (2,-1,1,-1)`: `ru:wire:-++-` and `ru:wire:--+-` (blue–white).

Both lie on outer tetrahedral edges with **no N-cell edge ownership**. Thus all 20 N-incident continuous segments are single-strand segments, while the two shared sections are outside N-edge incidence.

## Native N identification

All 20 geometric N cells are touched, but coverage is not tube identity:

- 20 segments have N incidence; two do not.
- 16 segments touch more than one N cell.
- Occupied-edge incidence inside each of `ru:base:50`, `ru:base:56`, `ru:base:58`, and `ru:base:59` has two disconnected components.
- There are **64** perfect matchings between the 20 N cells and the 20 N-incident segments using incidence alone. Equal counts therefore do not select a unique identification.

### Reversal obstruction

The established symmetry exchanges coordinate pairs `(0,1) <-> (2,3)` and reverses paths, sending strand labels `(a,b,p,e)` to `(a,b,-e,-p)`.

Under that involution:

- None of the 20 native N cells is fixed.
- Four of the 20 N-incident tube segments are fixed.

An equivariant bijection must preserve fixed points. Therefore **none of the 64 incidence matchings can respect this reversal symmetry**. This is a structural obstruction to identifying these *maximal unchanged-bundle segments* one-for-one with native N cells—not a failure of reversible wire identity or of geometric coverage.

## Completeness audit: the visible gaps are real

The full edge-five tetrahedral honeycomb has **56 vertices and 210 native edges**. Its vertices split into 4 corners, 24 edge-interior vertices, 24 face-interior vertices, and 4 interior vertices. Thus 56 is a natural geometric count here, but it is a vertex count, not yet an N-tube identification.

The current candidate visits 52 vertices, omitting the four corners, and uses only 78 edges. It leaves **132 edges unwired**:

- Surface edges: 70 of 150 wired.
- Interior edges: only 8 of 60 wired.
- Each N octahedron has 12 native edges, of which only 3–5 are used.

The previous claim of coverage meant only that each N cell had some incident wire, not that its required connections were completely realized. Likewise, “complete paths” meant endpoint-to-endpoint continuity of the chosen sixteen records, not complete carrier wiring.

If full native-edge coverage is required, the current monotone routing restriction is insufficient. There are 70 same-height edges and 140 descending edges; the five successive layer cuts contain 20, 32, 36, 32, and 20 descending edges. A monotone end-to-end strand crosses each layer cut once, so **at least 36 strand occurrences** would be needed to occupy every edge of the largest cut. Sixteen monotone paths cannot do that. This is conditional on full-edge coverage and monotonicity; it is not a general impossibility result for sixteen retained identities with more general routing.

## Consequence

The current routing is a sparse retained-path candidate, not a complete wiring of the honeycomb, and it does not derive N as a canonical tube identity. Resolving that requires revisiting either the routing or the definition of an N tube (for example, local carrier passages rather than maximal unchanged-bundle runs). The 54 retained N records belong to the separate witness/extension construction and remain unbound to this tubing analysis.
