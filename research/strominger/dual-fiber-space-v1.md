# Dual-incidence space and one transported identity

Historical capacity-only stage. The active Pb-208 loadout and simplified UI
are now described in [Explicit outward chains](lead208-outward-chains-v1.md):
82 P–N–e chains plus 44 witness neutrons, with distinct positive shapes.
The fiber and layer-item cards and context/route controls were removed.

The active `vacuum.html` now loads `fiber-space-app.js`, backed by
`fiber-space-model.mjs`. It replaces the prior cell-only viewer. The geometric
assembly remains 1/4/44/126 items and 343 disjoint tetrahedral components.

## State and incidence

The dual graph has one node per assembled item and an edge precisely when two
items share a triangular face. Internal octahedron subdivision faces are not
dual connections. A single `identity` object is retained through transport.

For this executable realization, local frame parity is construction-layer
parity. This is a chart convention, not a geometric derivation of C/M roles.
An edge transports the local representative by XOR of endpoint frame parities.
Changing the global perspective changes the representative but not the identity,
occupancy, matching, or geometry. Transport around every tested fundamental
loop is trivial in the canonical frame. This is an explicitly flat transport
model; it does not claim to establish a unique physical connection.

The full-space spanning-tree traversal visits all 175 items and returns to
the seed, then exits through the output interface. Input/output are represented
in the state readout, not extra geometric glyphs. A cell-edge highlight marks
the single transported state; no separate pointer sphere is added.

H/D/He views instead use a local route joining the occupied items. Context is
limited to that route plus its face-adjacent neighborhood. Route and context
are off by default; the camera fits the occupied solid cells automatically.
Clicking a visible cell selects it only if it belongs to the active route;
orbit drags do not trigger selection.

## Loadout

The default Pb-208 candidate uses actual shared-face matching:
44 distinct outer witnesses cover the 44 inner items. The neutron, witness,
and proton controls select roles on the same outer items, not 208 separately
occupied cells. Each primitive retains exactly one opaque solid mesh.
Decorative rings, dots, glyphs and transparent fills have been removed.
The panel uses short labels rather than repeating counts and color legends. Electron placement is unassigned for this nuclear capacity model.
Hydrogen, deuterium, and helium presets remain available as cell occupancies.

## Verification

`node research/strominger/checkers/check_fiber_space.mjs` checks geometry,
matching, state identity, frame swaps, closed-loop transport, full traversal,
channel toggles, atomic presets, and browser/mobile operation. Results and
screenshots: `research/strominger/results/fiber-space/`.

The old `check_simplex_space.mjs` targets the replaced UI and is historical;
the component and atomic model checkers are still included in the active test.
