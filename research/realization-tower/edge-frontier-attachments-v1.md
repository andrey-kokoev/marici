# Missing attachments on the paired E/P edge frontier

Read-only continuation of [the symmetry audit](edge-pair-symmetry-v1.md).
No assignment rule or viewer state has been changed.

## k=4 after step 10

| Edge cell | Existing assigned face support | Missing second support | Assigned face supports of that missing cell |
|---|---|---|---|
| 132 | N cell 339 | cell 333 | 0 |
| 127 | N cell 313 | cell 331 | 0 |

The half-turn exchanges both rows, including their actual attachment faces.
The missing cells 333 and 331 belong to the same existing octahedral assembly
(group 53, primitive cells 331,332,333,334). All four are unassigned, and none
has an assigned external face-neighbor. Its other two wedges, 332 and 334,
have exterior faces on the two surfaces meeting the E/P edge.

There is therefore no sequence of applications of the current two-assigned-face
interior rule that starts this block. Counting the symmetry-related cells as
already assigned supports would introduce a circular construction.

## The block is not unattached: its attachments are edges

The complete six-vertex octahedron shares one elementary edge with N cell 339
and the opposite elementary edge with N cell 313. These are the only assigned
edge contacts. Their four endpoints average to the octahedron's center, and
the existing half-turn exchanges the two contacts. These are genuine lattice
edges, not the inserted long subdivision diagonal.

This is the constructive next object to examine: an **octahedral filler between
two existing, symmetry-related N edges**, rather than a tetrahedron attached
across two already assigned triangular faces. The two attachment kinds must
not be conflated.

The geometry identifies the block and its boundary contacts. The current
rules do not yet license admitting this whole block or select the roles of
its two exterior wedges. Such a group-attachment rule should carry the two
edge witnesses, all exterior/internal faces and the retained diagonal. It
must then be checked against the unique-opposite-partner condition and the
existing symmetry, not introduced by declaring four arbitrary N cells.

## Reproduce

    node scripts/check-edge-frontier-attachments.mjs
    node --test tests/edge-frontier-attachments.test.mjs

[Receipt](results/edge-frontier-attachments-v1.json) records the dependencies
for k=2..7 and both continuation branches. Tests retain the k=4 edge-versus-face
distinction explicitly. No new particle assignments are made.
