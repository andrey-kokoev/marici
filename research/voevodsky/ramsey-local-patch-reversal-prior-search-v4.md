# Prior research for the marked face/patch/sector reversal

Target: revision30's open `T-seam-marked-face-patch-sector-transport`. This search follows local geometric field conversion and its retained phases, not another abstract coefficient conjugation.

## Strongest new lead: source-local full-plane conversion already exists

Sources:

- `research/strominger/belt-local-field-lift-v1.md`
- `research/strominger/checkers/check_belt_local_field_lift.py`
- `research/strominger/opposite-branch-canonical-compatibility-v1.md`
- `research/strominger/checkers/check_opposite_branch_cycle_lift.py`

The local-field checker reconstructs all18 triangle modes and their metrics from the unchanged ordered geometry, reproducing the36 native numerator coordinates. For a selected two-component mode w, it computes c=<w,conjugate(w)> in the actual metric and constructs the complex-linear map

    L w = conjugate(w),
    L conjugate(w) = (c/conjugate(c)) w.

The eigenframe is a basis and c is nonzero on the tested planes. Gram equality proves metric unitarity. The complementary phase is determined by this pointed completion, not fitted from the saved global matrix. Positive-branch triangles use identity. The direct sum is built before loading the independent target and global adapter, and then matches them exactly.

The resulting full36-coordinate conversion intertwines L/G/return projectors, native C3, the branch-indexed local cycle and native energy. All21 seam projectors are independently reconstructed and transported. Identity extension over the separate16-coordinate bank transports all18 framed pulse projectors.

This is materially closer to the requested action on patch modes and phases than an arbitrary joint44 isometry. It is still a declared axial/pointed construction on an opposite-circulation belt branch, not an existing T-seam occurrence adapter. The bank here has16 coordinates, not the8-coordinate E field of the joint44 candidate.

## Based inverse, not one involution

The cycle-lift implementation independently constructs its backward map from the target mode. It is exactly the metric adjoint and backward-after-forward is identity. The same forward map squared is NOT identity: negative triangles retain the phase c/conjugate(c).

The occurrence map J_r squares to identity at fixed r, so its field realization must distinguish the two based directions or explicitly address this phase. Erasing it to assert involution would contradict the prior control.

The complex-linear lift sends the selected mode to its conjugate but is not conjugation on arbitrary vectors. It therefore does not contradict the prior obstruction to intertwining antiunitary whole-field transport with complex-linear coefficient bindings. A diagonal adapter also agrees on selected modes but differs transversely and does not supply the same cycle-level transport. Selected-mode equality alone does not select the full map.

## Actual face ports and complementary phases are available

The local-field checker identifies six genuine cross-face interfaces by shared edges of actual centroid-edge triangles. For equal-norm compatible ports a,b it constructs

    B_ba w_a = w_b,
    B_ba conjugate(w_a) = (c_a/c_b) conjugate(w_b).

All six cross-face maps are full-plane metric-unitary and cycle-intertwining. Their branch-conversion squares commute.

Crucially, arriving at and departing from a coarse face uses DIFFERENT triangle ports. The checker supplies six within-face port changes as well. The actual12-port loop has identity composition on both branches, with all intermediate labels and maps retained. This supplies a concrete port-aware route interface, not simply a closed six-face label cycle.

This loop is not the earlier N-reader chart-overlap loop: the latter concerns identifications of belt vertices with one fixed tetrahedron. The two outcomes must not be substituted for each other.

## A precise early rejection test: normalized eigenline Gram shape

The invariant

    kappa = |<w,conjugate(w)>|^2 / ||w||^4

must agree for a full-plane metric-unitary intertwiner of the simple-spectrum cycles, including cycle reversal. The source finds12 of21 energy seams with unequal kappa. For example the retained values include823849/1423249 and3806401/4405801.

Raw eigenframe transport is flat and cycle-intertwining but fails metric isometry on18 of21 seams. Its648 composition squares do not repair that defect. The six cross-face interfaces and completed12-port route pass the stronger metric test because their port shapes match.

Thus the next marked T-seam comparison should check the actual selected source/target ports and their Gram invariants before trying to assemble a global field map. These failures are not a universal obstruction to branch conversion or the existing amplitude constraints.

## Where the branch signs originate, and what remains chosen

`belt-axial-witness-v1.md` derives an axis line from the source C3 projector (I+R+R^2)/3 and its direction from the ordered source seeds. The declared axial contraction then produces the alternating face signs before the target branch is loaded. Swapping seed roles reverses those signs; the unpointed rotation and unordered seeds do not select a direction.

`belt-relative-assembly-v1.md` shows that polarization-label transitions can retain a root sign and close coherently, but all64 sign assignments generate such flat connections. Flatness does not select the alternating branch. It also tests that scalar multiplication by -1 does not reverse a mode's oriented bivector, while conjugation does. A sign label is not a full-field converter.

These are useful constructor provenance and type controls. Nothing inspected identifies this axial branch selection with T-seam occurrence reflection or its five-slot outgoing reference.

## Adjacent patch transport is useful but not a substitute

`native-patch-mode-transport-v1.md` supplies exact internal two-component patch maps from native modes and a six-component conditional PN face map. Real rotations plus scalar phases cannot match P/N patch invariants; changing unequal patch weights additionally requires inter-patch mixing. Its explicit phase/axis choices and minimal-mixing convention remain inputs, and it does not give the full joint-field seam binding.

## Sharper next question

Can the actual T-seam occurrence reversal select matching ports and based directions in this existing local-field construction, while inducing the required active-sector/context action on the five-column N seed?

The concrete missing comparison is:

1. Map J_r-transformed reader faces and their uv-incident context patches to the actual belt triangle ports, preserving occurrence labels and ordering.
2. Compare source/target mode norms, Gram invariants and inherited phases; identify whether the required operation is this branch conversion, a port map, or neither.
3. Track the based forward/backward maps, active sectors, context columns and full complement; test the resulting labelled readout against Q.
4. Only then propagate through the existing PN pullback and joint NE exchange.

The inspected local-field and cycle-lift implementations do not consume the T-seam basis record or the full-five embedding. There is no located completed adapter between them. This is a bounded source search, not a proof of repository-wide absence. The marked transport conjecture remains open.

## Evidence status

Read the cited reports and the local-field implementation, and inspected the cycle-lift inverse/square checks. No scientific suite was rerun. Fresh direct-pin checks found no mismatches:

| Receipt under research/strominger/results/ | Direct pins |
|---|---:|
| belt-local-field-lift/verification.json |13|
| belt-axial-witness/verification.json |8|
| belt-relative-assembly/verification.json |10|
| opposite-branch-cycle-lift/verification.json |11|
| native-patch-mode-transport/verification.json |5|

These are direct recorded hash checks, not transitive verification or fresh replay of the scientific claims. No native source, owner receipt, admission policy or conjecture-net status was changed.
