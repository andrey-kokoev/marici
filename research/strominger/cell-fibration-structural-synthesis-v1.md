# Cell-level fibration: structural consolidation

## Objective and status

Replace a growing list of placement exceptions with a small, inspectable structural grammar. Preserve the current construction as a checked example; do not change colours or geometry merely to reach a particle count.

This consolidation does **not** change the viewer. The independent classifier in `../realization-tower/cell-fibration-structure.mjs` exactly reproduces all 84 assigned cells, their construction stages, and their colours. `tests/cell-fibration-structure.test.mjs` checks this against the procedural implementation, all 24 corner reindexings, and the failure of P/E exchange symmetry.

## 1. Separate carrier, addresses, colour rules, and schedule

The fixed folded k=7 carrier has 175 whole geometric cells:

- 84 tetrahedra in the orientation currently being filled;
- 35 tetrahedra in the opposite orientation;
- 56 octahedra.

In primitive-tetrahedron volume units, 84 + 35 + 4×56 = 343 = 7³. The current process fills the first sector, not all 175 cells.

Every current-orientation tetrahedron has a unique integer address

    w = (w1,w2,w3,w4),  wi ≥ 0,  sum wi = 6.

The number of such addresses is C(9,3) = 84. Corner i has wi=6 and all other coordinates zero. Relative to that corner, geometric depth is **6−wi**. The classifier recovers these addresses from actual cell geometry and verifies complete coverage, not just a matching total.

Zero coordinates identify outer carrier faces. Consequently the sector decomposes into **4 vertex cells + 30 edge cells + 40 face-interior cells + 10 interior cells**. These are geometric strata, not particle species.

## 2. Nine structural types replace the placement history

Sort the address entries only to identify a type; retain their original corner indices when assigning a colour. Corner colours remain V1=N, V2=P, V3=E, V4=N.

| Sorted address | Multiplicity | Stratum | Current stage | Colour rule |
| --- | ---: | --- | ---: | --- |
| (6,0,0,0) | 4 | Vertex | 0 | Vertex with weight 6 |
| (5,1,0,0) | 12 | Edge | 1 | Vertex with weight 1 |
| (4,2,0,0) | 12 | Edge | 2 | Vertex with weight 4 |
| (4,1,1,0) | 12 | Face | 2 | Opposite vertex: weight 0 |
| (3,3,0,0) | 6 | Edge midpoint | 3 | Explicit neighbour-pair table |
| (3,2,1,0) | 24 | Face | 3 | Nearest other vertex: weight 2 |
| (3,1,1,1) | 4 | Interior | 3 | Source vertex: weight 3 |
| (2,2,1,1) | 6 | Shared interior | 4 | Highest-priority colour of the two weight-2 vertices |
| (2,2,2,0) | 4 | Face centre | 5 | Opposite vertex: weight 0 |

These are all partitions of 6 into at most four parts. Their coordinate-permutation orbits exhaust the 84 addresses without overlap. The multiplicities follow from permutations of repeated entries; they are not fitted to final P/N/E counts.

The procedural layer groups are therefore 4, 12, 24, 34, 6, 4 cells. The final assignment can be evaluated directly from address and corner colours without replaying growth. This does **not** imply that arbitrary temporal reorderings satisfy the existing attachment witnesses.

## 3. Five colour operations, with two explicit policy choices

1. **Source inheritance:** (6,0,0,0), (4,2,0,0), (3,1,1,1).
2. **Target / nearest-other inheritance:** (5,1,0,0), (3,2,1,0).
3. **Opposite-face inheritance:** (4,1,1,0), (2,2,2,0).
4. **Midpoint completion:** P–E → N; N–N → E; P–N → E; E–N → P.
5. **Shared-proposal resolution:** P > N > E on (2,2,1,1), retaining both vertex-relative proposals but assigning the geometric cell once.

The first three families select a boundary datum by an address property. The last two are **declared colour policies**. Neither follows merely from tetrahedral incidence, and neither is a contiguous NPNE/NENP substring law.

In particular:

- Geometry determines where a midpoint is, but not why an N–N midpoint must be E.
- Geometry determines that a (2,2,1,1) site has two competing nearest-corner readings, but not the P > N > E ordering.
- Both of these policy choices break P/E exchange symmetry.
- The construction remains covariant under corner reindexing when the corner colours are reindexed with the geometry. Role preference is not a preference for a numbered spatial corner.

The counts **23 P, 40 N, 21 E** are consequences of the present boundary labels and these policies. They are not independently established particle counts.

## 4. Construction steps are not geometric layers

The current stages 4 and 5 both belong to **nearest-corner geometric depth 4**: both (2,2,1,1) and (2,2,2,0) have maximum coordinate 2. Their different step numbers record a chosen construction order: shared interior resolution before face-centre completion.

A clearer conceptual hierarchy is:

- establish boundary vertex data;
- extend edge and face branches;
- close edge midpoints and the first interior sites;
- reconcile shared interior proposals and complete face centres;
- inspect the unfilled complementary sectors.

Keep the existing controls and history for reproducibility, but do not infer geometric separation from stage numbering. A vertex cut is the inequality wi ≥ 6−depth, together with the retained orientation-reference corners and outline; it is not an isolated shell.

## 5. What has and has not been synthesized

Established in this implementation:

- one exhaustive address grammar for the entire 84-cell orientation sector;
- unique geometric placement, no duplicate counting of shared cells;
- retained provenance and explicit conflict resolution;
- a checked correspondence between structural classification and procedural growth;
- cuts that reveal the vertex complex without changing assignments.

Not established:

- a complete face-glued assignment of the remaining 35 opposite tetrahedra and 56 octahedra;
- a single local law deriving all five colour operations;
- a mathematical fibration with specified base, fibres, and transport;
- neutron dynamics, particle occupancy, stability, or a nuclear isotope realization.

The present assigned tetrahedra attach through vertices; their colouring alone does not supply the missing face-mediated structure. Earlier collective and independent-neutral-channel experiments remain separate declared extensions and must not be treated as a proof of this process's missing sectors.

## 6. Next synthesis gate

Before adding another count-driven rule:

1. **Extract interfaces:** for each unfilled octahedron and opposite tetrahedron, record the already assigned neighbouring faces/cells and their colours.
2. **Group by structural type:** compare equivalent neighbourhoods under corner reindexing, retaining boundary colours and orientation.
3. **State a compatibility rule:** decide which local interface data determine a unique filling. Keep zero-solution and multiple-solution cases explicit.
4. **Check consistency and confluence:** a shared cell must not acquire different results from different incident vertex complexes; do not use traversal order to hide conflicts.
5. **Then assign:** extend the current classifier only when the new cases have a rule and witnesses, and test whether any priority assumption is still needed.

The immediate objective is **structural compatibility across the two orientations and the octahedral sector**, not increasing P/N/E totals. If no common rule emerges, retain the current construction as a finite, well-specified coloured example rather than claiming a stronger synthesis.

## Verification

`node --test tests/cell-fibration-structure.test.mjs tests/cell-fibration-process.test.mjs tests/cell-fibration-cut.test.mjs` — 17 tests passed at consolidation.

Operational history and controls: [cell-fibration-v1.md](cell-fibration-v1.md).
