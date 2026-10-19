# Local field lift: a closed metric interface route, with distinct constraint seams

## Construction before comparison

The source-axis rule is retained from the previous packet. The new checker reconstructs all eighteen triangle modes and their intrinsic plane metrics directly from ordered triangle geometry, using the unchanged source mode formula. It reproduces the original36 numerator coordinates and denominators exactly.

For a local mode w, let c=<w,bar(w)> in its actual metric. On an axially reversed triangle define

    J w = bar(w),
    J bar(w) = (c/bar(c)) w.

These two vectors span the local complex plane. Their Gram matrices determine this pointed extension and prove metric unitarity. Positive triangles use identity. The target signs, target selected numerators and saved global adapter are not used to construct the blocks.

Only after assembly does the checker load the prior opposite-branch comparisons. The direct sum of the local blocks equals the saved full36-coordinate cycle adapter exactly. It intertwines L/G/N, native C3, local cycle inversion and the full native Hamiltonian. All21 target seam projectors are independently rebuilt from the generated modes and tested against the corresponding source projectors. Extending by identity on all16 bank coordinates intertwines all18 framed pulse projectors.

Thus the axial preparation and the pointed local metric rule jointly reproduce the previously verified global field construction. This is not a factorization fitted from that global matrix. Both the axial coupling and this pointed metric completion remain declared uniform constructor rules, not uniquely selected physical laws.

## The six actual face interfaces lift

Each shared edge of the six coarse belt faces selects one small centroid-edge triangle on either side. These six actual pairs have equal mode norms and equal normalized conjugate-eigenline Gram overlap.

For a source port a and target port b, with modes w_a,w_b and c_a=<w_a,bar(w_a)>, construct

    B_ba w_a = w_b,
    B_ba bar(w_a) = (c_a/c_b) bar(w_b).

For these ports |c_a/c_b|=1. The resulting complete two-plane map is metric-unitary and intertwines the real native cycles. The corresponding opposite-branch map is obtained from the independently local J blocks; its square with the original interface commutes exactly. No scalar phase flip is substituted for polarization conversion.

A coarse face label is not itself a triangle port. Entering and leaving one face uses two DIFFERENT small triangles. The checker therefore constructs six additional within-face port maps by the same rule. These twelve lateral ports have equal Gram shape. The resulting twelve-step route closes exactly on both branches:

    B_12 ... B_1 = I.

The native coordinate labels, intermediate port changes and full plane maps remain retained. This establishes more than closure of the six sign labels.

## Why not every energy seam is an isometric identification

For a triangle define

    kappa = |<w,bar(w)>|² / ||w||^4.

Any unitary intertwiner of two simple-spectrum triangle cycles must preserve the absolute normalized overlap of their two eigenlines, hence kappa. Reversing the cycle exchanges the two lines and leaves this invariant unchanged.

On12 of the21 admitted energy seams these invariants differ. An explicit example is original triangles0 and1:

    kappa_0 = 823849/1423249,
    kappa_1 = 3806401/4405801.

Therefore no full-plane metric-unitary cycle intertwiner exists on those seams. This is stronger than one chosen map failing. These are within-face shape changes, not failures of the six cross-face interface maps above.

The raw eigenframe transport [w_b,bar(w_b)] [w_a,bar(w_a)]^-1 is flat and cycle-intertwining, but fails metric isometry on18 of21 seams. Correcting the complementary-line phase repairs the lateral-port route; it cannot repair unequal kappa. Exact checks of648 frame-composition squares separate flatness from metric compatibility.

The original amplitude-mismatch projectors across the unequal planes still transport under the local branch conversion. A constraint comparing amplitudes is not a claim that its two full planes are isometrically identical. Thus the global energy result survives, while the stronger proposal to interpret EVERY energy seam as an invertible metric gluing is rejected. None of the other six triangle planes or16 bank coordinates is discarded to obtain the successful12-port route.

## Synthesis

The construction now has three explicitly different operations:

1. Local branch conversion within each triangle: full metric isometry, reproducing the global adapter.
2. Transport through the six face interfaces and six lateral port changes: full metric isometries with identity loop composition.
3. The broader21-seam amplitude constraints: preserved under branch conversion, but not all realizable as full-plane isometric transports.

This is a conditional local-to-global field synthesis, not a seam-free ordinary signed geometric chain or a proof that WG uniquely chooses its axial rule. It supplies a field-level realization for the previously co-generated polarity interface, with the necessary extra port data and phases retained.

## Verification

Protocol: `inputs/belt-local-field-lift-protocol-v1.json`.
Checker: `checkers/check_belt_local_field_lift.py`.
Receipt with full local/global adapter, six cross-face maps, actual12-port route and all seam invariants: `results/belt-local-field-lift/verification.json`.

Twelve exact groups, targeted SCC check and frozen challenge pass at `91f1311d98f73b45`. Earlier freezes retain the successive audit refinements: global LGN/C3 replay, separation of cross-face ports from all energy seams, then explicit within-face completion of the route. No failed invariant was weakened or source rule changed to remove the12 Gram obstructions.

    python research/strominger/checkers/check_belt_local_field_lift.py
    python research/aspect/scc/scc.py check belt-local-field-lift
    python research/aspect/scc/scc.py challenge belt-local-field-lift research/strominger/checkers/check_belt_local_field_lift.py survives

Sources remain read-only and hash-checked. No Agda compilation, physical calibration, commit or push is claimed.
