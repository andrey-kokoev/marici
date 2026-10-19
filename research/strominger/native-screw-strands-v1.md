# Native screw core: testing two strands

## Result

The screw-periodic cell core supports disjoint polygonal paths of the **same handedness**. Under the tested native-edge prescription, paths of opposite handedness intersect. Reversing one path's traversal gives opposite axial travel but does not remove those intersections or change geometric handedness.

Consequently this construction has **not yet produced the requested nonintersecting, oppositely handed pair**. A middle sheet cannot separate these intersecting paths without rerouting at least one of them.

## Exact test category

The input is the fresh, source-hash-checked receipt from `check_native_screw_patch.mjs`. Only actual vertices and edges of its occupied tetrahedra are used. No smoothed helix, fitted intermediate point or extra radial layer is added.

The tested prescription is:

1. use one of the four geometric vertex orbits represented by the root C0, C1, M0 and M1;
2. advance by the already-derived half-turn screw map in each block;
3. connect endpoints along native straight edges, with strictly increasing axial coordinate on every edge;
4. repeat the same edge motif under the screw map.

All occupied vertices belong to these four screw orbits. Axial coordinates are half-integers, and a block advances the axial coordinate by one. Therefore a strictly progressing path between a seed and its screw image can have at most one intermediate vertex. The endpoint pair itself is not a native edge. There are exactly two admissible two-edge paths per seed: **eight candidates** in total.

Each candidate is checked against the actual occupied edges throughout four blocks. Its intermediate vertex resolves the +pi versus -pi ambiguity left by the P-boundary half-turn samples alone. The sign of its successive transverse quarter-turns defines its geometric winding orientation relative to a fixed transverse basis.

These are geometric edge paths, **not newly derived field-transfer laws**. A two-edge geometric route is not a shortcut replacing the screw block's eight native transfers or its four-step realization-origin advance. Phase-continuous field propagation along these edge paths has not been established. Their role sequences mix C and M. The C-only and M-only occupied vertex sets lie in two different planes through the screw axis; treating either set alone as a nonplanar helix would be incorrect.

## Pairwise checks

The checker tests all 28 unordered candidate pairs using exact rational segment intersection, including interior crossings, shared vertices and collinear overlap.

Two blocks form a translational period. Comparing a fundamental period against neighboring translated copies checks periodic disjointness; bounded axial extents exclude more distant copies.

Results:

- 16 candidate pairs have opposite winding orientation;
- **none of those 16 is disjoint**;
- 8 candidate pairs are disjoint, and all have the same winding orientation.

Candidate pairs are counted as parametrized seed prescriptions, not as eight necessarily different topological pairs: changing the starting seed can describe the same periodic curve.

The finite four-block illustration also exhibits collisions for the displayed oppositely handed pair. Reversing one path's order produces opposite axial traversal but leaves the exact geometric intersection set unchanged.

## Separation gate

Two curves sharing a point cannot lie in disjoint regions separated by a sheet that avoids both curves. Thus adding a third curve or sheet to this particular intersecting pair cannot satisfy the requested separation condition by itself.

This does not rule out a different native path or a different layout. Options requiring new tests include a larger screw motif, nonmonotone edge routes, additional occupied radial layers, or curves through cell interiors. None is silently admitted here. In particular, arbitrary interior curves would no longer be a construction solely from the existing native edges.

No full A4 spatial realization, rung-12 field-metric binding, physical stability result or general impossibility theorem follows from this test.

## Reproduce

```
node research/strominger/checkers/check_native_screw_patch.mjs
python research/strominger/checkers/check_native_screw_strands.py
```

Outputs:

- `research/strominger/results/native-screw-strands/verification.json`
- `research/strominger/results/native-screw-strands/strand-comparison.svg`

The comparison drawing shows actual piecewise-linear native-edge paths. Production rules and the viewer are unchanged.
