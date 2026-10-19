# Sequential construction with entry and exit boundaries

Historical centerline proposal, superseded in the viewer by
[window-driven construction](window-driven-lattice-construction-v1.md).
The centerline selects geometry without the retained P/N/E window and cannot
serve as its attachment law. Its tests and module remain a separate experiment.
The exit-picker UI described below is no longer active.

## Boundary contract

The first cell is entered **at its center from the inner dimension**. The last
cell exits **at its center into the next realization**. These are endpoint
conditions for the whole sequence, not incoming/outgoing spatial faces of an
isolated seed.

`createSequentialConstruction({exitCell})` accepts the last cell as boundary
data. It does not invent its location or infer it from target particle counts.
With no exit supplied, it returns `needs-exit`: missing boundary data, **not a
construction obstruction**. The center entry and exit retain one identity.
An incoming-face argument for seed admission is rejected.

## Explicit candidate rule

The current proposal follows the straight segment between the two centers.
At each step it intersects that segment with the active cell's boundary,
selects the first forward face crossing, and admits its neighboring lattice
item. Exactly one item is committed per successful call. Earlier geometry
and the endpoints stay unchanged. Reaching the specified last cell completes
the transition at its center; another step cannot add a cell past the exit.

This is a boundary-conditioned kinematic proposal, not a derived particle law.
It requires no coordinate-order preference, global matching, target counts,
precomputed final path, or backtracking. Geometry comes from local honeycomb
items in `lattice-items.mjs`, not from the Pb assembly. The same rule commutes
with all 24 structural-coordinate permutations.

If the segment crosses an edge or vertex, several face crossings coincide.
That **particular straight-segment proposal** reports the ambiguity without
choosing a face by index. It does not prove that construction between the
endpoints is impossible; a richer transport rule may resolve it.

The old isolated-seed symmetry calculation remains a statement about missing
state only. Its four equivalent faces cannot be used as an obstruction after
an exit condition is supplied. `resumeFaceContinuation()` retains the earlier
local face-normal diagnostic separately; it is not the endpoint constructor.

## Viewer

The default **Sequential construction** starts with only the seed and reports
“Exit cell not set”. To supply an endpoint:

1. Select **Lead-208 (layout)**.
2. Click a particle to select its P–N–e chain.
3. Click **Use electron as exit**. This explicitly supplies that electron's
   cell geometry as the boundary for a new construction experiment.
4. Use **Next element** to admit one element at a time.

Only committed cells are drawn as solids. The exit label marks boundary data,
not a pre-added cell. Meshes are deduplicated by primitive coordinates, and the
camera zooms out as necessary without changing the geometry. The identity
label reaches the last cell's center on completion. No species assignment is
inferred for intermediate cells in this sequence.

The endpoint can also be supplied directly through
`FiberSpaceViewer.setSequentialExit({kind, origin, inverted})`. No particular
Pb electron is selected by default. Existing layouts remain comparisons, not
sequential derivations of Pb-208 or full-structure witnessing.

## Verification and limits

`node research/strominger/checkers/check_sequential_space.mjs` checks:

- explicit center entry and terminal center exit;
- one-item commits, unchanged prefixes, fixed boundary conditions;
- preservation of the same identity object through the exit;
- 24 coordinate-permutation covariance checks;
- positive, non-overlapping lattice primitives in every admitted prefix;
- no mutation on missing-boundary, singular-path, or completed states.

Its explicit test endpoint `[2,1,-1,-2]` (upright tetrahedral origin) is reached
in six commits; it is a test fixture, not a default or hidden construction goal.
Evidence: `results/sequential-space/verification.json`.

The separate Pb checker audits all 82 existing electron cells as supplied
endpoints: this version completes 8 centerline paths and reports edge/vertex
ambiguities for 74. These are **not** 82 sequentially derived electron
attachments. Details: `results/lead208-loadout/verification.json`.

Browser checks cover endpoint selection, one-item stepping, reaching an exit,
hiding uncommitted geometry, species-layout isolation, and responsive layout.
