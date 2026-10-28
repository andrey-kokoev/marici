# E/P edge exchange and the remaining construction frontier

This is a read-only audit of the current edge-ray construction, not a new
assignment step. Source: `edge-ray-model.mjs`, the native `simplex-components.mjs`
assembly, and the explicit symmetry in `edge-pair-symmetry.mjs`.

## Actual symmetry, not just a matching picture

For the tetrahedron formed at level k, use

    H_k(q0,q1,q2,q3) = (q2+k-7, q3, q0+7-k, q1).

H_k exchanges the starting E corner and the ray-end P corner, and exchanges
the two N corners. It is a proper half-turn fixing the line through the
midpoints of these opposite edge pairs. It is involutive, preserves distances
and oriented volume, and reverses E–P edge segment i to segment k+1-i.

The audit verifies for k=1..7 and both second-ray choices:

- every primitive cell maps to an actual cell inside the same growing region;
- every shared/exterior face retains its incidence multiplicity;
- octahedral groups map to octahedral groups, including their selected internal
  diagonals and individual wedge cells;
- completed assignment stages 2, 4–9 and all interior-closure rounds transform
  by E↔P and N↔N;
- each closure addition and each of its supporting face witnesses transforms
  to an addition/witness in the same round.

Step 3 alone contains only one of the two N corners and is not asserted to be
invariant. Neither the directed traversal history nor physical charge
conjugation is identified with this geometric map.

Although the fixed subdivision preserves only 8 of the outer tetrahedron's
24 vertex permutations (4 proper), this particular half-turn preserves it.
No retriangulation or silent diagonal change is needed for this comparison.

## Frontier after all currently enabled interior-closure rounds

| k | Unassigned E–P edge cell pairs | Fixed central cell | Assigned-face counts, in edge order |
|---|---|---|---|
| 2 | none | none | none |
| 3 | none | 132 | 2 |
| 4 | (132,127) | none | 1,1 |
| 5 | (132,119) | 127 | 1,0,1 |
| 6 | (132,108), (127,119) | none | 1,0,0,1 |
| 7 | (132,94), (127,108) | 119 | 1,0,0,0,1 |

These are actual existing cell IDs, not added fillers. All remaining edge
cells have exterior faces, so the existing *interior* two-face neutron rule
correctly does not assign them.

At k=4 the first unassigned cell from each end already has one assigned N
face-neighbor. These supports are exchanged by H_k. Neither cell yet has two
assigned-face supports. Thus the present local attachment rule stalls
symmetrically, rather than failing on one side or depending on processing order.

## Consequence and next boundary

Odd k has a central cell fixed by H_k. If a completed role assignment is
required to respect this combined geometric/species exchange, a fixed cell
cannot be E or P: its role would have to equal its opposite. N is the only
fixed role among the declared three. This is a conditional role-selection
argument, not permission to bypass the construction's attachment condition.
At k=3 the central cell already has two assigned faces; at k=5 and k=7 it does
not. Symmetry therefore distinguishes the central role without supplying the
missing inward attachments at larger k.

For even k, the central pair can be exchanged with opposite E/P roles, or
both be N, under symmetry alone. The next investigation is the missing second
attachment for the paired surface frontier, not an arbitrary parity label or
a global filling of all empty cells.

## Prior work used

- [Marked tetrahedron and edge handoff](../strominger/cmc-mcm-marked-tetrahedron.md):
  transport marks, shared edges, complementary faces and occurrence identities.
- [Tetrahedral field attachment](../strominger/tetrahedral-field-attachment-v1.md):
  opposite-edge axes and geometric action distinct from bare incidence.
- [Four-wedge octahedral ring](helium-ring-role-test-v1.md): subdivision and
  diagonal choices are real structure, not interchangeable regular cells.
- [Cross-branch coherence](cross-branch-coherence-v1.md): retain the actual
  supporting faces and filler boundaries, not just counts.

## Reproduce

    node scripts/check-edge-pair-symmetry.mjs
    node --test tests/edge-pair-symmetry.test.mjs

[Receipt](results/edge-pair-symmetry-v1.json): all 14 audits pass. The viewer and
its assignment rules were not changed by this audit.
