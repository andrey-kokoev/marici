# FCC-first sector transport, then esd7 presentation

## Constructed adapter

Read the actual esd7 census and retain its barycentric sites x=(a,b,c,d), a+b+c+d=7. Use the exact FCC chart

    (a,b,c,d) -> (a+b,a+c,b+c).

The image is the integer even-coordinate-sum FCC lattice restricted to the tetrahedral envelope. The inverse is

    a=(y1+y2-y3)/2,
    b=(y1+y3-y2)/2,
    c=(y2+y3-y1)/2,
    d=7-(y1+y2+y3)/2.

This chart preserves the barycentric displacement metric. No length fit or new vertex is introduced.

For each ordered pair i!=j, define the labelled elementary move

    T_ij(x)=x-e_i+e_j.

The twelve sector labels now have twelve explicit geometric move types. On the finite envelope a move is available when x_i>0; on the ambient affine A3 lattice it is a translation. All1008 directed admitted moves are stored, with their source/target vertex IDs and sector labels.

## The hidden presentation choice was recovered

The original343 tetrahedra coarsen exactly to the natural FCC cell complex:

| Item | Count |
|---|---:|
| Sites |120|
| FCC nearest-neighbour edges |504|
| Triangular cell faces |560|
| Unsplit tetrahedra |119|
| Unsplit octahedra |56|
| Total coarse bodies |175|

Each octahedron was split into four tetrahedra along one selected diagonal:

    119 + 4*56 = 343.

Thus all56 longer edges are presentation diagonals, not additional elementary FCC transports. Every fine tetrahedron belongs to exactly one coarse cell. Oriented refinement preserves each coarse boundary: internal diagonal faces cancel, leaving exactly the real tetrahedral/octahedral faces.

## Full S4 transport is recovered

Every permutation p of the four barycentric labels preserves the FCC sites and all175 coarse cells, and

    p T_ij = T_(p(i),p(j)) p.

All24 frame actions and their576 compositions are checked. The explicit affine3D matrices are retained in the receipt. Twelve are proper and twelve improper isometries; S4 covariance does not mean all its elements are proper spatial rotations.

The chosen esd7 split is invariant under only8 of these24 actions. Its S4 orbit consists of **three transported triangulations**. This is not a classification of every possible independently chosen octahedral splitting. To preserve covariance, transport the subdivision with the frame instead of requiring every action to preserve one fixed split.

## Actual route comparisons, not chosen shortcuts

Each selected octahedral diagonal has four shortest two-root paths, through the four remaining octahedron vertices. The output retains all four ordered sector words separately. Each path is linked to its actual comparison triangle in the original census: **224 source face IDs** across the56 octahedra.

This gives the interface back to the existing coherence layout: interpret a presentation diagonal through the retained root paths and its registered comparison faces, not as an invented elementary operation. Equal spatial endpoints do not identify field histories or prove equality of analytical maps.

The existing signed analytical face/filler records must still be bound to these geometric words. The current test checks endpoint squares and incidence, not the C3 coefficient action or a physical P/N/E readout.

## Hostile controls

- A valid ambient S4 action can fail to preserve the fixed triangulation. The transported presentation repairs this without forbidding the ambient action.
- None of the56 diagonals is an elementary root move.
- Selecting the lexicographically first shortest route fails S4 covariance. Retain the alternatives and compare them instead of silently choosing by address order.

## What this changes for the seven-stage construction

The next block should be specified as labelled FCC transport with retained route witnesses. Only then choose the esd7 presentation and carry it with the chart. The [central flag extraction](esd7-seven-stage-handoff-v1.md) and its face IDs remain available as a realization target.

No global next-move selector is inferred from covariance: all admissible move types are present, but neither a particular seven-stage word nor the28-stage P/E exchange is selected. This adapter removes the subdivision bias before that selection problem is attacked. It does not change the existing native particle constructors or reinterpret the175 coarse bodies as particle counts.

## Follow-up binding

The [route-face and central-flag audit](fcc-face-flag-binding-v1.md) now binds all224 comparison faces to signed normalized-chain fillings. It checks ascending inclusions and descending dual restrictions for all24 central bridges, while rejecting naive descending chain projection. The remaining central interface is a graded chain/dual realization, for which the existing Fourier machinery is the next candidate.

## Reproduction and reusable data

```sh
python research/strominger/checkers/check_fcc_first_transport.py
```

**19 exact checks passed:**120 sites,1008 directed moves,8064 admitted geometric two-move squares, all24 frames and576 frame compositions, three transported subdivision variants, complete coarse-to-fine partition and signed boundary cancellation.

[Receipt and reusable adapter data](results/fcc-first-transport.json) include all sites, directed moves,175 coarse cells,560 coarse faces, original refinement IDs,224 diagonal-route comparison faces, affine frame actions and source hashes. The prior census is read-only.

Sources: [coherence-layout recovery](esd7-coherence-layout-recovery.md), [esd7 census builder](../voevodsky/checkers/check_esd7_explicit_analytical_census.py), and [tower research index](../realization-tower/README.md).
