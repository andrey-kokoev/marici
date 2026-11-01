# Be-9: 3D assembly

This view retains one depth-eight simplex, with 81 nodes, 108 unit-length edges
and 256 routes. It is independent of the eight-copy White-rooted hex simplex
view and the octahedral reference trial.

1. Open the white/red and white/blue directional planes to 120°.
2. Fold the lower portion 60° through the red/blue midpoints immediately above
   the fifth white-edge row. Crossed edges acquire a midpoint bend; identities
   and total lengths are retained.
3. Fold both side triangles 60° toward the same side as the upper triangle.

## Deriving the side hinges

Let A and B be the red/white and blue/white cell translations. The eight white
rows have midpoint carrier corners O, O+7A and O+7B. Step 2's hinge joins
O+3.5A to O+3.5B. The remaining two midlines join those endpoints to
O+3.5(A+B). These define upper, central, red-side and blue-side triangles.

Apply Step 2 to the side hinges before rotating the side triangles. Rotation
signs are chosen geometrically: both outer tips move into the half-space of
the central triangle occupied by the upper triangle. The signs are opposite
around the two oriented axes; the magnitudes are both 60°.

The final branching row extends beyond the white-midpoint triangle. Its middle
output remains a single shared node. After the side folds, its two terminal
unit conductors close at their unit-sphere intersection, choosing the point
nearest the average of their separately rotated endpoints. This is an explicit
terminal-junction adjustment, not a duplicate or disconnected endpoint.

The four triangles describe carrier patches; this does not assert that they
form a closed regular tetrahedron. No extra seed copies or strand connections
are introduced.

Checks:

- `node --test tests/beryllium-9-assembly-steps.test.mjs`
- `node scripts/test-beryllium-9-assembly-view.mjs`

Tests verify actual crease placement, angles, common-side orientation, unchanged
routes and IDs, unit conductor lengths, shared endpoints, reversible steps and
persistence.
