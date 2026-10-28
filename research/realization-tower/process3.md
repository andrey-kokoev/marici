# Process 3 — geometric core and branch rules

Process 2 remains unchanged. Process 3 is an independent reconstruction; it
neither imports Process 2 assignments nor repairs counts by recoloring cells.
Select **Process 3 — diamond rules**. Progress persists separately.

## Current stages

| Step | Rule |
| --- | --- |
| 0 | E seed at V1 |
| 1 | Ray V1 → V3; P corner anchor |
| 2 | Ray V3 → V2; N corner anchor |
| 3 | Ray V2 → V1; retain E |
| 4 | Complete both corner PE/EP diamonds atomically |
| 5 | P in the unique tetrahedron containing the actual k-envelope centroid |
| 6 | If the four-vertex orientation is unique, leave the V1 branch neighbor unresolved and place P on the other three |

E is surface-only; the interior E13 trial has been removed without replacement.
At k=7, step 6 assigns P4/P7/P10 around P0 and leaves cell 13 unresolved. These IDs are consequences
of geometric selection, not placement constants.

## Collective-core trial (step 7)

After the bounded P core at step 6, step 7 assigns N corridors to the existing
surface E cells. All filler Ps must belong to the central full-face P component;
there is no individual or one-to-one P/E matching requirement. Further P packing
is deferred until these corridors are reserved.

Corridors use shortest full-face paths through unassigned cells or existing N.
They may include surface N and may end through the E's existing surface P partner
(`P-core → N… → P-surface → E`), preserving corner diamonds. Otherwise they end
directly at E. Existing assignments are never changed; E remains surface-only.
Equal-length paths use stable cell-ID order, a reproducible trial choice rather
than a uniquely derived physical rule. Corridors may share Ns. Missing routes
and disconnected filler Ps are reported explicitly; no roles are invented to
force a connection. This connects currently assigned surface Es only, not a
completed surface. The k=5 branch-orientation gate remains unchanged.

The audit lists the P component, route cell IDs, complete shared-face witnesses,
planned/assigned status and blocked targets. At step 7 dashed guides show these
assigned trial routes rather than the earlier four-vertex geometric guides.
Use `node scripts/inspect-process3.mjs --k 7 --step 7` to inspect them.

## Center and orientation, including k=5

Center selection uses barycentric containment of the current tetrahedron's
centroid, not a k=7-only deepest-cell lookup. At k=3,5,7 there is a unique central
tetrahedron. At k=1 it is the existing E seed; at even k the centroid lies in
multiple pieces of a central octahedron, requiring a separate anchoring rule.

For each central face-neighbor, compute shortest full-face adjacency distances
to all four corner cells, without passing back through the core. Enumerate the
24 bijections between neighbors and vertices and retain all minimum-cost choices.
At k=3 and k=7 the mapping is unique. At k=5 the central tetrahedron is reversed:
there are **nine tied mappings**, not one natural selection. P26 is still placed
and visible, but no shell orientation is invented. A branch-orientation choice
or additional rule is required before continuing there.

For a unique mapping, one representative shortest path per branch is exposed
in the audit and drawn dashed. Ties between paths use geometric deviation from
the center-to-corner line, then a stable tie-breaker. These are **geometric guides**:
every consecutive pair shares a full face, but intermediate particle roles,
information transport and role continuity have not been established. Paths do
not assign their cells and must not be read as verified physical channels.

## Constraints and invariants

- Validate complete batches against a prior snapshot; conflicts add nothing.
- A diamond consists of opposite charged roles sharing a full face.
- The central shell is a separate rule: central P plus three P; the V1-side neighbor remains unresolved.
- Existing roles are immutable within a replay; changing a trial rule rebuilds
  from its earlier stage, rather than overwriting an established N.
- Inner grouped layers admit P/N only, with an explicit per-cell constraint for the
  core P. There is no interior E exception. Remaining mixtures are unresolved.
- Grouped depth counts a whole octahedron once, not its triangulation pieces.
  Several cells can tie for deepest depth, so depth alone is not a center selector.
- Surface E audits expose partners and inward candidates. The corner E still
  has no fully interior face-neighbor; a universal hidden-partner claim needs a
  corner exception or a different relation.
- Particle counts are diagnostics, never optimization targets.

## Visual verification tools

Run `node scripts/inspect-process3.mjs --k 5,7 --step 6` (or
`pnpm normal-ray:inspect`). Optionally pass `--out DIRECTORY`.
The script builds locally, advances through enabled stages, and writes:

- overview and core close-up PNGs;
- X/Y/Z view PNGs;
- JSON containing assignments, centroid candidates, all orientation choices,
  face-path witnesses, conflicts, summary and counts.

It fails on browser errors or if inspection changes assignments. Artifacts go
to a printed temporary directory by default. Read the PNGs as well as the audit:
a passing geometry test does not verify visual appearance.

`NormalRayViewer.inspectView({cell, zoom:3, axis:'x'})` is the view-only inspection
hook used by this script. It focuses a valid cell and optionally changes viewing
axis; it never changes process assignments. Ordinary camera settings persist.
