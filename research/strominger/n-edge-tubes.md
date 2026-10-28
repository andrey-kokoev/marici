# Trial N fibres through multiply occupied carrier cells

## Explicit routing rule

An N octahedron has twelve edge ports. Pair each edge with its opposite edge, yielding **six independent local through-strands**. If another N octahedron shares the exit edge, continue through its matching port and opposite edge. The centre is not a junction: strands of different directions can cross in one cell without merging.

This rule uses shared edges, not shared faces. It is therefore a **zero-area fibre-port assumption**, not an open-volume passage, neutron dynamics, or a derived consequence of the ±N boundary labels. P/E routing is not defined by this trial.

Trace each strand from a boundary port to its other boundary port. Preserve all local pass IDs, port coordinates and cell provenance; compress an unbranched strand into one effective channel. Count the reversible channel once, not once per direction.

## Edge-7 result

- 231 N carrier cells, each with six local strands.
- **1,386 local passes** joined at **1,092 shared N–N edges**.
- **294 distinct through-channels**, 49 in each of six root-axis families.
- 588 boundary ends; no branching or closed loops under this rule.
- Every local pass is retained exactly once in the compressed paths.

Thus `1386 − 1092 = 294`. This is not a reduction of 231 neutron particles to another particle number: carrier-cell, local-pass and channel counts are different domains. Per direction, 231 local passes reduce to 49 through-channels.

The result also differs from the one edge-touching N closure network and the 85 enclosed open-void regions. A connected contact network does not imply that all fibres mix, and fibre continuity does not create a positive-area passage.

The tested sizes 1, 3, 5 and 7 have respectively 6, 54, 150 and 294 channels. Each root-axis family has n² channels for these tested edge lengths n.

## Viewer

In the single-octahedron process, open **N tube routing trial**. Select one of six directions or all directions. White dashed overlays show the compressed straight paths, including interior paths, in either Geometry or Wiring; overlay is off by default. The six axes are structural-coordinate differences q_i−q_j, not extra particle colours. Cell adjacency, visible native geometry and the cell/void inventory remain unchanged.

The table adds local-pass and through-channel counts under a separate trial-fibre heading. They must not be summed with cell, face or void counts.

## Verification

`tests/n-edge-tubes.test.mjs` checks all tested sizes for opposite-edge pairing, complete pass coverage without merging, straight continuation, unique boundary ends, six distinct strands per carrier, invariance under cell enumeration reversal, and the optional viewer overlay. The browser regression checks the 49-path and 294-path overlays and the separate channel count.

A physical or signed-state derivation of this routing remains open. In particular, replacing edge ports with finite-width passages would change the geometry and needs a separate construction.
