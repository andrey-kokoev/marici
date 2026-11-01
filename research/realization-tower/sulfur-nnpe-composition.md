# Su-32: NNPE composition

A Three.js view based on cyclic-operad composition, independent of the channel
geometry, wires and folding experiments. Reference: Doherty–Hackney,
*Models for cyclic infinity operads*, arXiv:2506.15622v2, Definitions 3.2 and 4.1,
and the Segal-core discussion in §4.2.

## Explicit trial conventions

- There are sixteen labelled generators S1–S16.
- NNPE is represented by one N centre and three attachment ports N, P, E.
- Each generator is **assigned** additive inventory (N:1, P:1). This grading is
  a modelling convention, not inferred from the paper or from external ports.
- Attachment labels are not additional particles. N is self-dual; P and E are
  dual. E is an attachment type here, not an independently counted electron.
- Joining consumes two compatible boundary ports but retains both generator
  inventories. No inventory is annihilated by a P/E attachment.
- Only different connected components may compose: assemblies are trees, not
  arbitrary graphs with cycles. An occupied port cannot be reused.

Thus the initial sixteen generators carry the target 16N/16P inventory, but no
unique connecting tree is asserted. The operator chooses the joins.

## Half-cube representation

Each generator is displayed as a cube cut diagonally in half by x=y, retaining
y≤x. This is a triangular prism: only its three rectangular side surfaces are
shown, coloured blue, red and white. The white surface is the diagonal cut;
the two triangular end caps are omitted. There are no labels, axes, port balls
or central marker.

The geometry uses the main Three.js scene and its rotation, zoom, pan, opacity,
outline and shape controls. Invisible attachment targets lie on the coloured
surfaces and track the camera projection. Collapsed components use the same
simple half-cube representation. Internal labels, joins and histories remain
in the model; simplifying the display does not change the counting convention.

## Interaction and retained data

Select two ports to compose. Invalid colour matches, occupied ports and
loop-producing joins are rejected. Undo removes the most recent join; Reset
returns to sixteen separate stars. Collapse composites displays each connected
component as one corolla with its remaining boundary ports. The decorated
binary composition history and all sixteen original generator identities remain
stored, including when collapsed.

Boundary order follows cyclic grafting: remove the two joined ports and splice
the remaining cyclic orders. A complete sixteen-generator tree has fifteen
joins and eighteen boundary ports. Its inventory remains 16N/16P even though
its boundary labels have changed. Joins and collapse state persist locally.

## Verification

- `node --test tests/sulfur-nnpe-composition.test.mjs tests/sulfur-nnpe-layout.test.mjs`
- `node scripts/test-sulfur-nnpe-composition.mjs`

Checks include full-tree composition, inventory/history retention, boundary
counts, invalid join rejection, collapse, undo/reset, persistence and returning
to Channels / cutaway without rendering errors.
