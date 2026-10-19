# Window-driven construction on the existing lattice

The default viewer now uses `window-construction-model.mjs`, not the centerline
or outward-distance selectors. Its protocol is imported from the retained
`carrier.mjs#trial` words/context marks. The reflected display coordinates are
not imported into the construction.

## Constructive transfer

The retained seed binding is:

```
C0 = (1,0,0,0)   M0 = (0,1,0,0)
C1 = (0,0,1,0)   M1 = (0,0,0,1)
P  = C0 M0 C1 [M1]
```

Entry is at the seed center from the inner dimension. Each call to `step()`
admits exactly one tetrahedral primitive:

1. P→N selects the ordered face **M0,C1,M1**. The unique adjacent primitive
   supplies the new context vertex **C2 = (-1,1,0,1)**. The neutron carrier is
   `M0 C1 M1 [C2]`.
2. N→E selects **M1,C1,C2**, the face opposite M0. The unique adjacent primitive
   supplies **M2 = (-1,0,1,1)**. The electron carrier is `M1 C1 C2 [M2]`.

These are existing primitive cell IDs **0, 13, 16**, not new caps or moved nodes.
The latter two cells belong to the existing octahedral subdivision. They are
nonregular tetrahedra; no regular-electron condition is silently imposed on
this lattice binding. Their interiors are positive and disjoint.

The P/N and N/E interfaces share exactly the globally identical C1/M1 edge.
The electron reverses its traversal, C1→M1 becoming M1→C1. No nearest-cell,
coordinate-order, radial direction, or chosen terminal coordinate selects the
attachment. An incompatible or already occupied interface is rejected instead
of repaired by changing a face or reusing a mark.

The final electron center is the exit into the next realization. Its coordinate
is produced by the transfers, not selected beforehand from the old Pb layout.
This implements the supplied finite P/N/E window chain; it does not invent a
recurrence after E or force a target particle count.

## Retained state

Every prefix retains:

- the same identity object;
- all globally bound marks, including outgoing C0 and M0;
- ordered active window and fourth context mark;
- the occurrence history `C0,M0,C1,M1,C1,C2`, including the repeated C1;
- attachment faces and one-item commit events;
- the declared source adapter's frame exchanges and symbolic branch/phase.

P→N records C0↔M1 and the forward target cycle. N→E records M0↔C2 and the
**inverse** target cycle. For an initial positive mode, the states are
`positive, phase 0 → positive, phase 1 → negative, phase 0`, with exponents
modulo three. All three source modes are tested. This records the historical
window adapter; it is not a native full-state particle-operator derivation or a
claim that its source metric becomes the spatial metric of these nonregular
cells. M2 remains new geometric context, not a sixth native spectral source.

## Viewer and tests

Select **Deuterium tunnel (trial)**, then **Next element** twice. The first step
constructs N; the second constructs E and reaches the exit. Global vertex labels
remain on their actual lattice nodes. Nuclear faces are opaque; the electron
has dotted edges and semi-transparent faces. No exit picker is needed.
Reselecting this mode starts a fresh run.

`check_window_construction.mjs` checks the exact source protocol, full-face
attachments, opposite-side apices, retained C1/M1 edge and reversal, untouched
prefixes, distinct new marks, history, shared identity, all three symbolic
modes, 24 supplied seed markings on the fixed subdivision, translation, and
membership in the existing primitive lattice. The full browser closure also
runs the original lattice non-overlap checker and tests one-cell stepping and
actual electron rendering.

Evidence: `results/window-construction/verification.json` and
`results/fiber-space/window-electron.png`.

## Global fiber coverage

The [entry–exit coverage test](entry-exit-fiber-coverage-v1.md) now verifies
reachability on admitted window states before projecting onto cells. The current
packet covers 3/343 primitive cells of the original space, not the full four
levels. Bare geometric adjacency is explicitly rejected as a substitute. The
viewer API retains this ambient coverage. Its current readout instead shows
coverage of the three-carrier [deuterium trial](deuterium-tunnel-trial-v1.md),
with reversible traversal controls after construction.

## Remaining boundary

This is a binding of the retained marked protocol, relative to the supplied
seed frame and existing octahedral subdivision. It does not derive that initial
physical C/M marking, identify native particle operations, or prove whole-space
witnessing.

The legacy Pb-208 layout has **not** been rebound: its 82 chains still fail the
recovered shared-edge condition. In particular its eight octahedral proton
assignments have no four-vertex seed binding in this constructor. No fresh
coordinate-sorted marking is assigned to those 82 separate proton sites to
pretend that a globally carried window has been constructed. Extending the
retained state through that whole assembly remains separate work.

## Full-layout rebinding audit

`check_pb_window_rebinding.mjs` holds the old 82 proton bodies and 44 witness
neutron bodies fixed, discards the old outward N/e assignments, and tests all
24 supplied seed markings at each four-vertex proton site. It does not choose
independent frames or treat this enumeration as sequential construction.

All 74 tetrahedral proton sites have multiple geometrically free P–N–e
embeddings; no site has a unique one. Their candidate cells do not conflict
between different sites, so geometric non-overlap alone does not select a
marking. This does not establish global frame/phase coherence. The remaining
eight proton sites are whole octahedra and have no binding in the current
four-vertex carrier constructor; no arbitrary child tetrahedron was substituted.

The missing data are the propagated marked state between particle instances
(a serial handoff or branching law), and the marked-carrier interpretation of
those eight sites. The supplied finite P→N→E packet does not itself specify
these. Full-layout status is **not constructed**, not an impossibility theorem.
Evidence: `results/pb-window-rebinding/verification.json`.
