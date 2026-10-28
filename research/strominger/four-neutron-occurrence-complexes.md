# Four reflected N occurrence complexes

The live double-ESD7 viewer now preserves the four source N seed occurrences independently:

- `original:tet-61` (−N)
- `clone:tet-67` (−N)
- `original:tet-134` (+N)
- `clone:tet-134` (+N)

Each owns a separate instance of the native six-cell annular carrier, with its C6 shared-face graph. There are 24 internal carrier cells. The 350 parent cells remain as the reference complex and retain their labels and face incidence. Internal cells are not additional particle assignments.

The four carriers are uniformly scaled into their parent inspheres for display. This is an internal-fiber presentation, not a claimed tetrahedral volume replacement or a completed conforming face refinement. External arrows remain on the parent reference. Each of its four face ports is retained verbatim, with the child-port map explicitly null. No guessed external arrow is attached to a child. Every child has precisely two internal shared-face neighbors.

The previous single large belt and its 42 rim fan-out links have been removed from the live process. Its standalone construction code remains research evidence, not the live simplex attachment.

Graph mode includes 350 parent-reference nodes plus 24 internal nodes. Parents with a local carrier use wireframe node markers. The viewer control is **Four N occurrence complexes**. Teal/violet distinguish the source circulation signs, not particle roles.

Still required for a true replacement: an incidence-preserving map from parent face ports to child ports with no more than four arrows per tetrahedral child. This is not supplied by identifying coarse rim edges with many parent subsegments.

Verification:

```
node --test tests/neutron-occurrence-refinements.test.mjs
node scripts/test-neutron-belt.mjs
node scripts/test-double-esd7.mjs
```
