# Source audit: what can 36 = 12+12+12 count?

## Test contract

Keep the native geometry, coordinate lists, metrics and projectors unchanged.
Compare counts of raw scalar field coordinates, support blocks and geometric
edges without identifying their types. Re-run the existing exact baryon tensor
grid reconstruction; inspect the independent electron source rather than
assuming three equal P/N/E sectors. A matching count is not a selected physical
interpretation, a solid construction or a closure witness.

## Result

The best source-supported meaning of36 is a **single baryon field**:

| Native chart | Raw coordinates | Native geometric presentation |
|---|---:|---|
| P |36|12 surface patches times3 components|
| N |36|18 belt patches times2 components|
| E |8|Native electron coordinate list; not a12-coordinate third block|

For both P and N, the actual projector supports derive12 blocks of size3 and
3 blocks of size12. Every fine/coarse pair intersects at exactly one coordinate.
The common rank-one return column supplies an invertible diagonal gauge, and
the induced metric factors exactly into row and column weights. Every operator
coefficient, not just its rank, matches the resulting weighted tensor form:

    V = C^12 tensor C^3
    Fine = I_12 tensor A_3
    Coarse = A_12 tensor I_3
    Return = A_12 tensor A_3

P has Fine=L and Coarse=G; N exchanges those roles. Consequently36 can indeed
be partitioned into three12-coordinate support blocks **inside either baryon
chart**. Those blocks are not P, N and E, nor are they automatically three
independent invariant species sectors: Fine mixes the three columns.

One independent raw field of each species would have direct-sum dimension
36+36+8=80, not36. If P and N are alternative charts related by an explicitly
chosen36-dimensional transport, adding an independent E field gives44 raw
coordinates. Neither accounting choice supplies a self-closing spatial solid.
The existing conditional44-channel N/E exchange has its own preservation
contract; it is not a36-dimensional PNE decomposition.

## Consequence for the shape search

The field interpretation has a genuine source-derived12+12+12 partition;
the truncated octahedron has a different, geometric edge partition. No map
between those partitions has been constructed. The count alone therefore
cannot choose the spatial solid, element, center family or global coverage.

The next missing object remains a source-defined PNE assembly and a map from
its constituent/readout data to the chosen count. A nonconvex candidate is not
excluded by the convex edge obstruction, but it must be specified and tested
rather than selected solely to recover36.

## Verification

    python research/strominger/checkers/check_native_36_count_screen.py

This freshly imports/runs the existing full coefficient-level baryon grid
checker, verifies the referenced source fingerprints, and checks all native
raw dimensions and coordinate partitions. It does not replay all source
geometry or establish field sewing. Receipt:
`results/native-36-count-screen/verification.json`.

Sources: `baryon-tensor-grid-v1.md`,
`tessellated-reader-fields-closeout-v1.md`, and the native protocols named in
the receipt. No production, viewer, native permission or geometry is changed.
