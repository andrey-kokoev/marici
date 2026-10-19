# Empty structured space: discrete Y and linked planar frames

Historical untyped construction. The current signed C/M role display and R
(realization) naming are specified in `vacuum-space-typed-R-v2.md`.

## Question

Visualize the operator's proposed empty space in the existing Three.js work: one discrete normal Y axis and three coplanar axes whose admitted orientation depends on the preceding frame. The operator rejected the earlier fixed C/M-layer account because it privileges a planar direction through a 2+1 main-space/codimension split.

## Claim boundary

This is an editable geometric candidate, not a selected vacuum energy law or a completed particle constructor. Applicable SCC obligations: forward geometric realization and adjacent-frame attachment transport.

At level n in Z, the display frame has angle theta_n = alpha + n delta, with three signed axes at theta_n + 120j degrees for j=0,1,2. Its sites have coordinates q a_n + r b_n + n h Y, with integer q,r and bounded hexagonal patch radius 3. The patches are triangular lattices: all nearest-neighbor edges have length one. Every axis uses the same rotation rule, and negative levels use its inverse. Y indexes structure, not physical time.

The chosen constant-turn family is one explicit way to make the next frame depend on the previous frame. It does not determine the full set of admitted rotations. Initial delta=30 degrees and h=1.1 are editable display inputs, not source-derived constants. The planes stay parallel; frames rotate within them around Y. No main-space/codimension roles are assigned, so the operator's original symmetry problem is exposed for further construction rather than declared solved.

The view contains no occupants, particle windows, C/M labels, identity modes or particle trajectories. Dashed links join corresponding signed frame tips. Colors retain axis identity even when a 60/120-degree turn preserves the unlabeled planar lattice. The highlighted level is a selection, not a distinct species or preferred structural level.

## Disposition

Implemented under `research/strominger/demos/particle-overlap-tetrahedron/` as `vacuum.html`, `vacuum-model.mjs`, `vacuum-app.js` and `vacuum.css`. The existing experiment links to it. The owned publisher mirrors these assets to both public roots.

Route: `/experiments/particle-overlap-tetrahedron/vacuum.html`.

Checker: `node research/strominger/checkers/check_vacuum_space_viewer.mjs`.
SCC: `python research/aspect/scc/scc.py check vacuum-space-viewer-v1 --verbose`.
Receipt and desktop/mobile screenshots: `research/strominger/results/vacuum-space-viewer/`.

The first fresh execution passed 26 checks, including unit edge lengths, equivalent axes, discrete Y rejection controls, signed/zero rotation controls, cyclic frame permutation, WebGL output, responsive layout, interactive level selection and preservation of the existing carrier view. The unoccupied geometry is implemented; the source-selected rotational law and C/M transition binding remain unconstructed. The live server at `http://127.0.0.1:8766` and the SCC owner-local check each passed the same 26 checks in fresh runs (`structured_command_execution:e_24480_1792166481261634900_3`, `structured_command_execution:e_24480_1792166484077469800_4`).

Operator stimulus and bounded result were admitted under proposal `ep_5e66f1ae-ad83-4c18-a254-12f380c388ad`, ledger head `b1ad78473c19e0019b5a2b5ddd81302bfa5683765324fe533f840861bac06536`. Changes and admitted graph records remain uncommitted; no deployment was performed.
