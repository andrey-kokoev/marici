# Cell-local face realization: three outgoing directions

Retired at operator instruction. Face navigation was an assistant-introduced
interpretation, not the requested realization-axis construction. The active UI
is now specified by `three-realization-axes-v1.md`; the former URL redirects to
it. This packet retains the historical construction and overlap result only.

## Question

Operator accepted trying realization through shared carrier faces instead of a global vertical coordinate. Implement an explorable local complex with one incoming face and three outgoing continuation choices; retain carrier selectors without independently placed geometry.

## Construction and claim boundary

`face-model.mjs` starts with a declared unit regular tetrahedral seed and generic node identities v0..v3, not a particle. Its incoming face is retained context. The other three faces are local exits R1/R2/R3. Crossing reuses all three shared vertex identities and reflects the omitted opposite vertex across that face to generate the next vertex. Cell addresses are words of local exits, not coordinates on a global R axis. Different word orders are retained, not silently commuted or merged.

The three exit displacements are noncoplanar. Reflections are involutions and commute with the tested rigid chart change. One crossing reverses reflection parity; no physical time is assigned. The planar model's 60-degree rotation and automatic C/M swap are NOT imported into this candidate. A source-derived particle/type transition law remains missing.

Carrier selectors label generated cells: P is the anchor cell, N is its R1 neighbor, and E is the R1/R1 neighbor. All carrier vertices reference actual complex node identities. The previous P/N/E face-incidence signatures are preserved as conditional labels, not derived species. Carrier anchors remain fixed while the user explores. Only Place at current cell changes the anchor.

The empty default shows the current cell and three adjacent cells. Faces, scene R labels and sidebar controls cross into a neighbor. Undo restores the previous exact cell. Controls show/hide neighbor context, traversed cells and node labels. Both the original carrier viewer and planar comparison link to this new mode.

## Concrete global-embedding obstruction

The regular reflection complex is not asserted to tile Euclidean space. A separating-axis test reports actual displayed cell-interior overlaps; touching faces/edges are not counted.

The explicit word R1/R3/R3/R3/R3 generates an edge-ring whose terminal cell overlaps the root interior. The initial local star is non-overlapping, but this longer route refutes a globally non-overlapping spatial-tiling interpretation of this unchanged regular-cell candidate. Node/cell identities are retained, not merged or moved to hide the obstruction. The browser displays an embedding-conflict banner. This is a geometric residual, not a checker failure or physical particle falsification.

## Disposition

Implemented at `http://127.0.0.1:8766/experiments/particle-overlap-tetrahedron/face-space.html`. New owned sources: `face-model.mjs`, `face-space.js`, `face-space.html`, `face-space.css`. Both public mirrors regenerated with the existing guarded publisher.

Fresh live execution `structured_command_execution:e_24480_1792174472008376000_29` and SCC closure `structured_command_execution:e_24480_1792174489836766500_30` each pass 33 checks. These include shared-face node identity, reflection reversal, unit cell volumes, noncoplanar directions, chart covariance, noncommuting route retention, actual rendered node coordinates, anchored carrier selectors, face/label navigation, undo, drag rejection, mobile interaction and the explicit longer-route overlap warning. A parse-only preflight caught and repaired one excess parenthesis before browser execution; that was an execution defect, not a scientific residual.

Retained planar-view regression passes all 80 checks in `structured_command_execution:e_24480_1792174495962221200_31`.

Receipt and visually inspected desktop/mobile screenshots: `research/strominger/results/face-space-viewer/`, including empty local star, all carriers and `overlap-edge-ring.png`. Final carrier labels are separated from the exit controls. The local construction is usable; the same regular reflection rule does not provide a global non-overlapping Euclidean space. Particle/type selection remains unresolved.

Changes uncommitted; no deployment performed.
