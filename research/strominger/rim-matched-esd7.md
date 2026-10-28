# One natural rim-matched ESD7 assembly

The operator withdrew the two-belt weaving requirement. The viewer now uses one six-cone annular belt between the two ESD7 halves, via the existing `placeFaceOnRim` construction.

Implementation: `research/realization-tower/rim-matched-esd7.mjs` and `rim-assembly-presentation.mjs`.

- Rigidly move each 175-cell parent to a triangular belt rim, with its apex outward.
- Uniformly scale the reference belt to the parent edge length: here 6/sqrt(3), rather than the old viewer's sqrt(8/3).
- Use the native six cones directly: six belt cells, with no resolution-7 volume refinement.
- Match all 42 parent rim subsegments (21 on each rim) to the six coarse belt rim edges. Gold graph links denote these **subsegment identifications**, not whole-face adjacency. The belt's volume cells are not subdivided.
- Preserve the source exclusion of cap cones. The parent interfaces are rim loops, not inserted filled caps or a nonsingular filled tunnel.
- The parents lie strictly on opposite outer sides of the rim planes; the belt lies between those planes. Vertex matching error is below 1e-12.

The viewer's **Annular belt between the faces** checkbox switches between this placement and the original directly face-glued pair. Graph mode renders all 356 actual cell nodes with native shared-face links, plus explicitly distinguished rim links. Solid mode uses the same cells. Teal/violet encode source panel circulation signs, not P/E particle assignments. A flowing time evolution is not implemented.

Parent colour-rule evaluation still uses the original glued-pair reference. These labels are carried to the rigidly moved parents; a propagation/interaction law through the inserted belt is NOT inferred. Belt cells are untyped and excluded from parent counts. The parent's metric is unchanged; the native belt is uniformly scaled. Its six cone shapes are not congruent to the regular parent cells. The earlier 1050-cell refinement has been removed from the live assembly; its standalone research module does not supply the viewer geometry.

Verification:

```
node --test tests/rim-matched-esd7.test.mjs tests/refined-neutron-belt.test.mjs
node scripts/prepare-normal-ray.mjs
node scripts/test-neutron-belt.mjs
node scripts/test-double-esd7.mjs
```
