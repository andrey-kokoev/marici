# Executable stagewise positive-atlas witnesses

## Result of the strengthened rerun

The missing intermediate embeddings are now supplied, not marked positive by a status flag. With the explicit atlas below retained at every stage, the 1836-, 576-, 73- and 72-arrow coefficient networks all preserve a positive spatial realization throughout their transitions.

This is a geometric lift of the existing networks, not a reversal of the earlier failed literal-coordinate test. A projected complex point is interpreted through a declared chart, not incorrectly used directly as a spatial position.

The scope is explicit:

- Geometry inputs are positive homothetic copies of the registered, labelled twelve-triangle tetrahedron.
- Phase inputs are arbitrary vectors in C^36; every network still implements exactly N, not merely its action on the selected line.
- Every intermediate state carries the same immutable twelve-patch atlas and incidence labels. Shared chart storage does not delete the patches.
- Counts are nonzero scalar coefficient transfers. Static atlas descriptions are declared model data; their storage and the implementation cost of evaluating chart embeddings are not counted as interaction arrows. This convention applies equally to all candidates.

Within that class, the positive three-stage construction attains 73 arrows and the positive two-pass construction attains 72. These are not minima over arbitrary geometric formation algorithms.

## An explicit embedding, rather than a hidden original mesh

Write the reference mode on triangle g as

    v_g = r_g + i*sqrt(3)*s_g.

For the registered tetrahedron:

    r_g dot s_g = 0,
    |r_g|² = 2/3,
    |s_g|² = 2,
    n = v_g^dagger v_g = 20/3.

The reference face-centre offset is recoverable from the mode frame:

    f_g = cross(r_g,s_g)/2.

It need not be fetched from a discarded spatial vertex buffer.

The complex chart coordinate of a reference-plane point p is

    alpha = v_g^dagger p/n.

Use oriented real chart coordinates

    t=Re(alpha), w=-Im_sqrt3(alpha).

For geometric scale a>0, the embedding is

    F_g(t,w) = a*f_g + n*(r_g*t/|r_g|² + s_g*w/|s_g|²).

The three chart corners are

    alpha_0=0,
    alpha_1=a*(-1/10 - 3*i*sqrt(3)/10),
    alpha_2=a*(-1/10 + 3*i*sqrt(3)/10).

The scale is part of the current chart data: a=-10*Re(alpha_1). The oriented chart area is 3*a²/100>0. The tangent cross product of F_g points outward. Embedding the corners reconstructs the actual centroid-edge triangle.

All twelve embeddings agree at every shared labelled vertex. Because they are affine on each edge, agreement of its endpoints establishes agreement over the entire edge. The oriented boundaries cancel, each origin-cone tetrahedron has volume 2*a³/9, and the total enclosed volume is 8*a³/3.

Thus the atlas realizes the original convex tetrahedral positive geometry at each stage. Homothety by a>0 has positive Jacobian a³; the canonical simplex form and its boundary residues are transported by this orientation-preserving affine map.

## Original network stages

Let X contain the three corner roles of each spatial triangle, stacked into a 36-by-3 array. The local projector produces Y=L X. Each projected corner has the form

    q_g = alpha*v_g.

Recover alpha from the current q_g by v_g^dagger q_g/n, then apply F_g. The normal offset removed by projection is supplied explicitly by the atlas embedding; it is not silently treated as still present in q_g.

On the registered family,

    G Y=Y, N Y=Y.

Consequently every intermediate stage has twelve positively oriented chart triangles with consistent seams and a positive enclosed volume. The 576-arrow identity-feedback variant has the same witnesses.

## Compressed network stages

The gather map B=u^dagger/80 sends the corner array to the single shared reference chart. The intermediate state consists of:

- those three current complex chart corners;
- all twelve mode-frame embeddings and incidence labels.

It is NOT just an unannotated scalar. The shared chart plus its twelve embeddings is a complete realization of the spatial surface. The one-dimensional phase amplitude and the geometric chart samples are distinct fields of the declared stage state.

The middle identity wire preserves that chart. The scatter map A=u gives q_g=alpha*v_g for all patches, whose embeddings give the same positive surface.

No intermediate atlas must read the original spatial coordinate array. The checker constructs positions from the retained chart and mode-frame data, checks them, and only then compares against the source mesh as an independent oracle.

## Positivity-constrained bounds in this class

All 36 input columns and output rows of N are nonzero. A three-stage linear, no-bypass implementation with disjoint interfaces therefore needs at least

    36 first-stage arrows + 1 middle arrow + 36 final-stage arrows = 73.

The atlas-augmented construction attains this bound while satisfying stagewise positivity. Restricting to positive realizations cannot weaken the lower bound, and the admissible witness attains it. The analogous two-pass bound is 72.

This does not claim that the atlas is free under every physical cost model. If interpreting an embedding requires additional primitive interactions in the intended model, those operations must be specified and counted for both constructions. Nor does the witness derive the spatial carrier from phase processing: it gives positive coordinate presentations of a declared registered carrier.

## Executed tests

    python research/nima/checkers/check_stagewise_positive_atlas.py

For all four candidates, the checker validates every intermediate stage at scales 1/10, 1, 2 and 7/3. Linearity gives the extension to every a>0: coordinates scale by a, areas by a² and volumes by a³.

It verifies exact target-matrix equality on all phase inputs, positive chart areas, nondegenerate outward cells, supporting halfspaces, shared-vertex equality, boundary cancellation and positive volume. Independent negative controls reject:

- a zero-area chart;
- reversed chart orientation;
- individually positive cells whose shared vertices do not glue.

Artifact: `results/stagewise-positive-atlas.json`, including every patch embedding and every stage result.
