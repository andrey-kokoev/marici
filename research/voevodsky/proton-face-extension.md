# From the proton-like barycenter to a new tetrahedron's barycenter

## Declared attachment

This test chooses the shared-face interpretation: attach a single new tetrahedron to the existing boundary triangle (F_ABC,A,B). Its original vertices are A=(1,1,1), B=(1,-1,-1), and F_ABC=(1/3,1/3,-1/3). The source package's center is O=(0,0,0).

Let q be this small triangle's barycenter. Choose O'=(5/4)q as the new tetrahedron's barycenter, extending radially from O through the interior of the chosen face. The factor 5/4 is a declared example, not a derived physical constant.

Exact calculation gives:

```text
q  = (7/9, 1/9, -1/9)
O' = (35/36, 5/36, -5/36)
d  = 4O' - F_ABC - A - B = (14/9, 2/9, -2/9)
```

The oriented new tetrahedron is (d,F_ABC,B,A). Its shared face has the opposite orientation to the original boundary triangle. The segment from O to O' crosses that face at parameter 4/5, with face barycentric coordinates (1/3,1/3,1/3).

## Geometry verified

The original tetrahedral body lies in the inward half-space of the shared supporting plane. The new apex lies strictly outside, so the added tetrahedron meets the original body exactly along the selected triangular face. It is nondegenerate and has positive oriented volume 2/9.

Gluing removes one old boundary triangle and adds three side triangles. The resulting boundary has 9 vertices, 21 edges and 14 triangles, Euler characteristic 2, paired oppositely oriented edges and circular vertex links. Boundary-integral volume equals original volume plus the new cell volume:

```text
8/3 + 2/9 = 26/9.
```

The same radial procedure succeeds separately at all twelve original boundary triangles. These are twelve alternative one-cell attachments, not a claim that all twelve cells can be added simultaneously without overlap.

For the family O'=lambda*q, the reconstructed apex is (4lambda-3)q. The new cell is strictly outward precisely when lambda>1; lambda=1 degenerates into the face, while lambda=3/4 returns the original center as apex and is an inward cone rather than an outward addition. The tested lambda=3/2 gives added volume 4/9. Geometry therefore admits a continuous family; it does not select a discrete particle excitation.

## Merkle interpretation

The extension root binds the unchanged 1836-arrow focus package, selected face, new barycenter, reconstructed apex, oriented cell, new boundary and barycenter-to-barycenter segment. A standalone verifier recomputes these geometric records from the selected source face and specified center.

The 1836-arrow pruning proof remains valid for the retained original subsystem. No new coefficient arrows or interaction operator have been assigned to the added cell or center segment. The new combined body's pruning-minimality is not established, and the new surface triangles are not silently given the original local projectors.

This is geometric growth, unlike the preceding S4 action on an unchanged carrier. It is not yet a neutron, electron, neutrino, charge change or energy transition.

## Verification and artifacts

All 12 tests passed, including degenerate/inward controls, wrong-apex and wrong-starting-center mutations with honest rehashing, and serialization/reverification.

```text
python research/voevodsky/checkers/check_proton_face_extension.py
```

- `research/voevodsky/results/proton_face_extension.json`: exact result and tests.
- `research/voevodsky/results/proton_face_extension_store.json`: retained focus and Merkle attachment.
- `research/voevodsky/results/proton_face_extension.obj`: resulting surface mesh. Decimal coordinates here are for visualization; verification uses rational coordinates in the JSON store.

Next discriminating obligation: specify the new cell's typed state space and a map across the shared-face interface, then test transport/coherence without assuming a physical particle identity from the extra geometry alone.
