# Replace detached carriers by exact lattice-node cells

## Question and correction

Operator rejected the centered/scaled carrier overlay: every vertex must lie on an actual lattice node. The v6 similarity embedding was the wrong implementation of that requirement. Its receipt and carrier screenshots are preserved as `verification-overlay-v6.json` and `*-overlay-v6.png` in the viewer results directory.

## Construction and claim boundary

No source tetrahedron coordinates are imported into the new geometry. An elementary triangle with axial addresses (0,0), (1,0), (1,1) on one realization plane and its vertically corresponding triangle on the adjacent plane form a triangular prism. A three-cell pulling triangulation has exactly the existing P/N/E four-vertex incidence chain:

- P: C0/M0/C1/M1;
- N: M0/C1/M1/C2;
- E: M1/C1/C2/M2.

For the default 60-degree step and base R=0:

| Vertex | R | q | r |
|---|---:|---:|---:|
| C0 | 0 | 0 | 0 |
| M0 | 0 | 1 | 0 |
| C1 | 0 | 1 | 1 |
| M1 | 1 | 0 | 0 |
| C2 | 1 | 0 | -1 |
| M2 | 1 | 1 | 0 |

The exact axial lattice automorphism for +60 degrees is (q,r) -> (q-r,q). Its inverse determines the upper triangle's addresses. Each displayed vertex references `space.frames[level].points[siteIndex]` directly; there is no independent translation, scaling, interpolated coordinate or nearest-node snapping. Lone views select cells from the same six bindings as All three.

The cells are non-regular tetrahedra, not isometric images of the discarded source tetrahedra. Each has volume sqrt(3) h / 12, where h is the R spacing; their disjoint interiors partition the elementary prism of volume sqrt(3) h / 4. The old C/M vertex names supply incidence labels only: a source-derived C/M node-role law and particle operator identification are not established by the geometric binding.

Rotations not divisible by 60 degrees are reported as blocked for this prism constructor rather than silently repaired. At the top displayed R boundary the constructor uses the last available adjacent pair and reports the actual realization levels.

The UI exposes all node addresses and offers Focus cells. Focus changes the camera only. The lattice positions remain unchanged.

## Disposition

Implemented in the existing viewer and both owned public mirrors. Fresh live run `structured_command_execution:e_24480_1792173146864668300_23` and fresh SCC closure `structured_command_execution:e_24480_1792173164533459800_24` each pass 80 checks. Checks now require exact lattice-node references in the constructor and matching actual rendered float32 vertex buffers, prism volumes, opposite-side shared-face apices/disjoint interiors, binding through rotation/spacing/R-boundary cases, no-snapping rejection, node-address inspection and camera-only focus. The prior regular-unit-tetrahedron tests were replaced because that source geometry was explicitly discarded, not weakened to certify the old overlay.

Inspected final focused desktop lone-proton and combined screenshots, plus combined mobile screenshot. Receipt/screenshots: `research/strominger/results/vacuum-space-viewer/`. Route remains `/experiments/particle-overlap-tetrahedron/vacuum.html`. All four selection modes, plane label/node toggles, 60-degree steps and M/C alternation remain available.

Changes remain uncommitted; no deployment performed.
