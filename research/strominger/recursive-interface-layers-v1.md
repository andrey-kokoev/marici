# Recursive interface expansion: geometric probe

Operator hypothesis: after the initial central-P / coherence / P,E,N,N-surface construction, each boundary between retained radial layers becomes a new coherence layer.

## Implementation

`checkers/check_recursive_interface_layers.mjs` retains old layer objects and replaces each interface A|B with A|C(A,B)|B. The inserted layer records the old interface identity and endpoints. Every new interface remains available for the next iteration.

Geometry uses concentric tetrahedral surfaces between fixed radii 1 and 2, with the same central tetrahedron and four outer P,E,N,N caps as the previous insertion probe. Each coherence band is triangulated into 12 tetrahedra using consistent vertex order across all six edge seams. On refinement, retained coherence layers keep their identities but are compressed into narrower radial intervals; this is explicitly a change of their metric embedding.

## Fresh results

| Radial layers | Coherence bands | Untyped band tetrahedra | Total tetrahedra |
|---|---|---|---|
| 3 | 1 | 12 | 17 |
| 5 | 3 | 36 | 41 |
| 9 | 7 | 84 | 89 |
| 17 | 15 | 180 | 185 |

Assertions pass for retained identities, expansion provenance, nondegenerate tetrahedra, consistent shared faces, exactly four faces across each consecutive-layer interface, no inter-layer adjacency shortcuts, fixed center and outer caps, constant collar volume, and exactly 12 exposed outer cap faces. Each band triangulates the corresponding convex homothetic tetrahedral frusta with matching lateral triangulations.

The recurrence L'=2L-1 holds after the initial three-layer construction. It does not generate the initial 1-to-3 transition: a single layer has no internal interface to expand. Radial counts are not primitive edge lengths or particle counts.

## Boundaries of this result

This demonstrates a consistent piecewise-linear geometry and retained interface genealogy. It does not supply P/N/E types for inserted tetrahedra or establish native trajectory/coherence witnesses. It uses shrinking rational band widths inside a fixed envelope, not successive unit-length growth on esd7. The earlier caveat also remains: the outer caps were dilated relative to the pre-insertion boundary cells, rather than moved as rigid unit cells.

No production rules or viewer changed. The output is an exploratory combinatorial/geometric result, not a particle realization.

## Reproduce

`node research/strominger/checkers/check_recursive_interface_layers.mjs`

Receipt: `results/recursive-interface-layers-v1.json`.
