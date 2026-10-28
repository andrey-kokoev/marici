# P-first half-step parent trimming: tested negative result

The existing double-ESD7 viewer now has an **Experimental P-first half-step trim** checkbox under the separated belt controls. It defaults off, persists on ordinary reload, and works in both Geometry and Wiring. Turning it off reconstructs the unchanged reference assembly. The separate octahedral-sector dropdown proposal is not implemented by this experiment.

## Exact rule

Work in each parent's original native coordinates, before reflection or display translation. The original tetrahedral sector has bounds `q_i <= 2`. Define cell-centre depth as

`depth = 2 - max_i(mean(cell.vertices)[i])`.

Keep cells with depth greater than 1/2. At depth exactly 1/2, keep N/E and remove P. Remove cells shallower than 1/2. Explicitly exempt the two declared E-tip replacement cells so their belt contacts survive. Use native geometric roles, not growth-rule labels.

This is a **whole-cell centre selection**, not exact clipping to displaced planes. Some retained cells still reach the old boundary. The outer P tetrahedra have depth 1/4; boundary octahedra lie at depth 1/2 and are retained. Thus this instance removes P before N without the P tie-break actually being invoked. It is not established as a half-cycle in duality/field space.

## Result

Per parent:

- Removed: **73 P**, zero N/E.
- Remaining whole cells: **10 P, 56 N, 36 E** (102 total).
- Surface cells: zero P tetrahedra, 52 N octahedra, one protected E-tip tetrahedron.
- Exposed triangles: **183 P-oriented, 87 E-oriented**; previously 109 P and 87 E.

Including the unchanged belt:

- Wiring: **30 P, 126 N, 82 E = 238 nodes**.
- Links: **426 shared-face links + 2 tip-contact links = 428**.
- Geometry readout: **398 P faces, 126 N fillers, 206 E faces**.

The graph remains connected. Both tip contacts survive. Each parent's boundary has 270 triangles and exactly two incident boundary triangles per boundary edge.

## Interpretation

Deleting P tetrahedra exposes additional **P-oriented faces of their neighbouring N octahedra**. The parent surface-face imbalance therefore worsens from **218P/174E to 366P/174E**, despite removal of all surface P tetrahedra except the separately E-assigned tips.

This distinguishes cell-role erosion from changing the lattice termination phase. The experiment is retained for visual inspection, **not promoted as a symmetry-restoring trim or Pb-208 construction**. No follow-up deletion was chosen to force 82 P.

## Verification

- `tests/p-first-parent-trim.test.mjs`: immutable source, unchanged belt, exact removals, E-tip preservation, boundary incidence, connected graph, adverse surface-face result and explicit persisted opt-in.
- `scripts/test-neutron-belt.mjs`: toggle, both readouts, counts, two contacts, reload and exact restoration of the untrimmed viewer.
- Standard native-belt publication/browser checks remain passing.
