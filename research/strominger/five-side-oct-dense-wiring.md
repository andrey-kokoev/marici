# 5-side oct: explicit filler-port routing

> **Downgraded: unvalidated candidate, not completed coherent wiring.** The
> [rule-and-obligation specification](five-side-oct-routing-obligations-v1.md)
> supersedes any admission implied below. The 62 groups, 19 nearest-slot
> admissions and 119 seams are construction choices, not established results.
> The historical implementation description below is retained for comparison.

The former edge-coverage embedding is removed from the active Wiring view. Covering 660 edges did not construct internal coherence. This view now renders the cell-port graph that is actually validated.

## Retained fibration

`octahedral-full-fibration.mjs` retains 80 P source fibres and 80 E target fibres, each with four coordinate-axis slots: 320 distinct slot-wire records. Exact native P-to-E axis correspondences take precedence; unmatched boundary lifts use the existing Sulfur period class and stable cell order. No geometric source/target cells are identified by their period class.

## Internal routing

`octahedral-coherent-routing.mjs` constructs every charged-cell face port and both opposite face ports of every N-cell coordinate slot. It first binds actual shared-face incidences, then follows each retained source/target correspondence through its required N occurrences.

- 85 whole N fillers, each with four explicitly wired opposite-face channels: **340 internal channels**.
- All **560 native shared-face interfaces** are retained, with exact common face IDs.
- All **760 native triangular faces** have port records.
- Each of the **320 slot wires** passes through at least one real N channel.
- Each N-port incidence conserves its incoming and outgoing ID sets; incoming bundles divide into disjoint outgoing bundles. No broadcast, loss or hidden perimeter filler is admitted.

The 19 larger-carrier records whose P and E ports both lie on the boundary previously had no internal N route. They now enter a retained N slot of the same Sulfur channel phase. Selection among those lifts uses distance to the source cell, then a stable ID tie-break. These records join and later leave an existing slot bundle without copying payloads. This **is a declared boundary-lift convention**, not a proof of a unique native boundary realization.

## Coherence groups

N occurrences joined by the same retained wire form connected groups; a whole N cell retains its four slot memberships. For the selected larger-carrier lift matching this produces **62 groups**: one six-cell group, eighteen pairs and forty-three singletons. These are derived port-connectivity groups, not a count inferred from edge coverage or a proof of a higher physical coherence law.

The edge-three regression checks more than counts: every P/axis/E correspondence, every N-group member set, and each wire's N-group assignment agree with `buildSulfur32Wiring()`. It recovers all sixteen Sulfur groups.

## What is native, and what is still a seam

Solid paths are charged-cell port legs and actual opposite-face connections inside N fillers. Their interior control points lie inside their owning cells. Shared native face ports coincide exactly and need no drawn connector.

The remaining **119 boundary-lift connections** are explicit graph seams. They are rendered dashed gold, not passed off as native adjacency or a proven local geometric wire route. A full native physical realization of those seams is still a separate obligation. The graph neither adds 119 new independent wires nor transforms any payload.

The endpoint fibres are distributed over the actual P and E cells. The unsupported single-tip fan-in/fan-out display and unused-edge blue overlay are no longer drawn.

## Inspection and tests

Wiring offers a **Coherence group** selector and **Reveal internal routing**, which sets face opacity to 12%. Selecting a group isolates its channels, retained wires, P/E endpoints and seams. Group selection is a transient inspection filter; it does not mutate the fibration.

`tests/five-side-oct-wiring.test.mjs` verifies the Sulfur correspondence and group regression, full fibre/slot inventories, every N channel's opposite faces and interior points, actual shared interfaces, conservative port flow, nonempty filler passage for every wire, group membership, and rendered channel incidence. Negative tests reject omitted filler slots, copied records, severed routes and missing group wiring.

`scripts/test-ruthenium-98.mjs` verifies the rebuilt viewer, channel audit, group isolation and unchanged Geometry/Lattice modes. The packed renderer caches CPU mesh data and uses five material batches, including the distinct dashed-seam batch.
