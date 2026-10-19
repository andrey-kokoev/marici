# Selecting a boundary-contraction rule

## Question

Does terminality alone isolate the successful P->E support contraction, or does
it permit a much broader collection of neutron-removing operations?

## Finite test

Enumerate all simple native paths of length 2 through 4 in the complete
origin-4 universe (192 packets). Require a terminal E endpoint, exclusively N
internal readers, and internal N bodies distinct from both endpoint bodies.
Check the existing endpoint and full-support role/species/contact guards.
No occupancy contraction is admitted during this classification.

Results:

- 219 paths examined;
- 203 pass both endpoint and full-support guards;
- 64 are the direct PN->NE composition;
- 139 are other compatible paths involving realization advances.

| Representative path | Shared endpoint vertices | Origin increment | Compatible instances |
|---|---:|---:|---:|
| P->N->E | 2 (edge) | 0 | 64 |
| P->N->N->E | 1 | 1 | 29 |
| P->N->N->N->E | 2 (edge) | 2 | 12 |
| P->N->same-N reader->E | 2 (edge) | 1 | 29 |
| N->N->E | 2 (edge) | 1 | 29 |
| N->N->N->E | 3 (face) | 2 | 12 |

Other longer reader/NN combinations account for the remainder. Sixteen paths
fail the existing occupancy/role/contact guards; these are not contraction
candidates. Table counts are operation/reader paths, not distinct particle
arrangements.

## What distinguishes the proposed P/E edge?

**Terminality is insufficient. Edge sharing is insufficient too.** Other paths
also end at a terminal electron and share an edge, but span realization steps.

Within the tested family, adding **zero realization increment** selects exactly
the 64 PN->NE paths. Every one has:

- P/E endpoints sharing C1/M1;
- one intervening reference N body;
- unchanged absolute origin;
- full coefficient permutation `[3,4,2,0,1]`;
- compatible reference roles before and after removing occupied N support.

The result suggests a narrowly stated candidate rule:

> Contract occupied support only for the grade-zero terminal reference pair;
> do not erase realization-advance history merely because its endpoint is E.

This selects the same kind of shortcut that repairs the tested H-1, N-14 and
Ne-21 cases. It is a motivated rule definition, not a derivation that such
support contraction must occur. Grade-zero native transfers still require
occupied N in the current production grammar.

## Geometry is not enough to identify the map

Twenty geometric endpoint-pair groups contain different composite permutations
across their reader paths. A single connection determined solely by the two
occupied shapes would therefore discard reader/history information.

When grouping by the exact source packet, target chart and target origin,
there are zero conflicting composite maps in this finite test. This supports
retaining the full marked reference and occurrence data. It does not prove
unbounded path independence or establish a geometry-only edge law.

## Structural synthesis

A disciplined proposal now has separate conditions:

1. Terminal boundary role, covariant with direction reversal.
2. A grade-zero native reference pair, not an arbitrary multi-step path.
3. Exact shared edge, reference marks and full coefficient-map composition.
4. Explicit permission to leave its intermediate N unoccupied.
5. Original whole-assembly compatibility, contact and rooted-path checks.

Items 1-3 isolate a specific candidate; item 4 remains the substantive new
occupancy assumption. Item 5 tests the resulting assembly rather than assuming
local eligibility is enough. This avoids treating all unoccupied reference
geometry as universally available for arbitrary shortcuts.

Production/viewer and existing isotope receipts were unchanged.

## Reproduction

```sh
node research/strominger/checkers/probe_boundary_contractions.mjs
```

Evidence: `results/boundary-contractions/verification.json`, with all paths,
composite permutations, guard results, endpoint ambiguity groups and hashes.
