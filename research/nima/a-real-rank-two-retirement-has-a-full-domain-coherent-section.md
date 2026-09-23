# A real rank-two retirement has a full-domain coherent section

## Delivered integration

The owning `one-sided-audit-evidence` retirement now has a certified full-domain triangular section. This is a real rank-two public domain, not a producer-declared subdomain or an approximate scalar-band witness.

The attachment checks six source vertices, six Farkas coverage implications and a four-triangle cover. Twelve interpolated source answers pass fresh replay. Fifteen refusal controls pass, including a missing domain sliver and a fine-admitted but incoherent shared-edge lift.

## Owning migration and its polygon

The existing migration has m=3 and retires audit 0. Its old fine frames successively bound that atom by 30, 20 and 10. The remaining public coordinates are

    U=t0+t1+t2,
    V=t0+t1/128+t2/16384.

The expected fine source therefore has bounds

    0<=t0<=10,  0<=t1<=102,  0<=t2<=104.

Its public image is the rank-two hexagon obtained by observing these source corners, in counterclockwise order:

    (0,0,0), (0,0,104), (0,102,104),
    (10,102,104), (10,102,0), (10,0,0).

The implementation does not assume that this description is the retired runtime domain. It replays the owning migration certificate, then establishes both inclusions against that exact migration context.

## Coverage is an implication from expected runtime rows

For every oriented edge a->b of the proposed counterclockwise polygon, the attachment constructs the target halfspace

    (b_y-a_y)*U + (a_x-b_x)*V
        <= (b_y-a_y)*a_x + (a_x-b_x)*a_y.

A nonnegative rational combination of the expected runtime source/evidence rows must have exactly that normal and a sufficient upper bound. Source rows come from the owning verifier's model; candidate-supplied source inequalities are not accepted as authority.

These six implications establish runtime-domain inclusion in the polygon. The reverse inclusion follows from admitted fine source lifts over a complete mesh: convex interpolation preserves all original source bounds and old fine evidence, and projects exactly to the public triangle.

## Exact mesh and source continuity

The checker admits a strictly convex two-dimensional polygon and a finite mesh of nondegenerate counterclockwise triangles. It checks:

- containment of every mesh vertex in the polygon;
- absence of pairwise interior overlap;
- equality of total triangle area and polygon area;
- each mesh vertex's source lift against the verified migration's fine context;
- equality of interpolated SOURCE vectors at every vertex of every pairwise triangle intersection.

Containment, disjoint interiors and equal area certify full coverage for this finite closed mesh. Agreement at intersection vertices certifies affine agreement along the entire shared segment.

A shared source-lift array is useful but not sufficient on its own. The checker also accepts a coherent nonconforming mesh with a T-junction and rejects an incoherent version of the same mesh.

For that control, the midpoint of the origin-to-opposite-corner diagonal initially has source lift (5,51,52). Perturb it by

    (1,-129,128)/1000.

This perturbation preserves both public coordinates and remains inside every old fine bound. Thus the altered vertex lift is individually valid. But it disagrees with the unsplit neighboring triangle's affine lift along their common edge. The full attachment rejects it on continuity, not on source admission.

## Restriction-only reuse

The session stores the accepted attachment as an immutable serialized proof and publishes a fresh handle only after all checks pass. Queries first check current source/runtime/public inequalities, then locate a triangle by exact barycentric tests and interpolate its checked source lifts. No solver is called to locate a cell or construct a source answer.

After appending U<=162, the old hexagon mesh is no longer literally a mesh of the smaller domain. Its RESTRICTION still covers the entire current domain, because the session permits only public evidence appends and the fine context is unchanged.

The point three quarters of the way to the opposite corner returns source lift

    (15/2,153/2,78).

The old opposite corner, with U=216, is refused. The successful source-vertex check count remains six; the service does not recheck vertices that have become ineligible under the new public frame.

This capability is retained fine lifting, not archival re-exposure. The workload bootstraps with lift capability and without archive capability. Re-exposure is refused, as are unsupported domain-widening operations.

## Refusal controls and replay

The controls reject missing coverage implications, negative multipliers, wrong source lifts, a foreign migration binding, missing or overlapping triangles, a smaller admitted polygon that omits runtime points, incoherent shared-edge lifts, outside-domain or wrong-arity queries, an excluded old vertex, a stale handle, archive escalation, domain widening and attachment without fine-lift capability.

The smaller-polygon control is important: every proposed lift is individually admitted, but that does not prove full runtime coverage. Its scaled coverage implications fail against the real expected rows.

`verify_full_polygon_checkpoint.py` freshly replays the owning migration, complete attachment, reported interpolation answers and verified public restriction. It uses the same attachment kernel rather than a separately implemented geometric verifier.

The scalar-envelope certificate verifier and the existing rank-one full-segment workload also pass. Their contracts remain distinct: scalar bands can represent approximate lifts; this attachment certifies exact lifts into the retained fine history.

## Scope and retained costs

The adapter requires exactly two public coordinates and no surviving audits. It supports triangular meshes of strictly convex polygons, including coherent T-junctions. It does not implement higher-dimensional complexes, nonconvex domains or arbitrary changes to the fine source.

Point location currently scans the triangles. Pairwise intersection checks are quadratic in the triangle count. Source-lift arrays, mesh geometry and Farkas multipliers remain retained information. Receipts charge the full polygon encoding separately from the live descriptor, lift context and archive.

Work counters describe successful attachments and returned interpolations; failed attempts, separate producer checks, owning import-time replay and fresh verification are additional work. Encoded lengths are not complete heap accounting. This remains a trusted in-process prototype, with no new observation-authentication or archival authority.

## Reproduction

    uv run --with sympy python research/nima/checkers/check_full_polygon_checkpoint.py
    uv run --with sympy python research/nima/checkers/verify_full_polygon_checkpoint.py

Implementation: `research/nima/checkers/full_polygon_checkpoint.py`.

Artifacts: `research/nima/results/full-polygon-checkpoint*.json`.

Predecessor coverage gate: `research/voevodsky/a-real-retired-domain-now-has-full-two-cell-section-coverage.md`.
