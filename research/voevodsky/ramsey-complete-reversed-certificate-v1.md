# Complete reversed presentations pass with retained field readouts

Node: `T-seam-based-port-readout-binding`.

## Scope and correction of the previous comparison

Rather than renaming just the last context slot, this test reverses whole source presentations: every occurrence, reference basis, coefficient vector, edge, role, species and entry/exit boundary. Coordinates and the existing physical field carriers are retained.

The previous context-only mismatch is NOT an obstruction to this complete direction-indexed comparison. Likewise, a terminal E packet in the forward generator is not an obstruction to an experimental reversed certificate: its old exit becomes a reversed entry.

The admission policy used here is the explicit pullback pattern of the prior experimental reverse validator, implemented in a new owner-local checker for freshly generated three-packet chains. It is not a new rule installed in the native forward generator.

## Fresh complete geometric/reference certificates

Construct and validate P->N->E from each of24 seed markings. Each certificate retains all three packets, actual bodies/vertices/roles, both operations, all described contacts and complete entry/exit lists.

At origin0 use K=2 and occurrence reflection

    (role,index,vertex) -> (opposite role,K-index,vertex).

Reverse the ordered references as well as their occurrences. Every dual reference is exactly

    M0,C1,M1,C2,M2,

and every coefficient vector is Q times its old vector, Q=[4,3,2,1,0]. An edge permutation Pi is transformed to

    Pi_dual = Q Pi^-1 Q.

The reversed NE edge therefore uses PN's coefficient map, and the reversed PN edge uses NE's coefficient map. Packet coefficients satisfy every reversed edge. Reversing the entire certificate again recovers the original exactly.

All transformed local phase frames pass the actual native template audit. Geometry eligibility follows the explicitly transported negative-direction policy: dual E comes from regular old P; dual N retains split geometry; dual P may inherit regular or split old E. Transported contacts and full-boundary reachability pass.

The dual E endpoint is the OLD P packet. Its ordered window is M1,C1,C2, selected at outgoing-reference indices2,1,3. Its context is dual M2 at the old C0 vertex, with that provenance retained. No equation identifies old C0 with old native M2.

Six controls per marking reject missing entry, missing exit, inverse-without-Q rebasing, replacing dual M2 by old native M2, dropping a coefficient and freezing the original entry direction.

This is24 complete three-packet certificates, not a new multiple-exit isotope audit or an arbitrary-assembly theorem.

## Full44 field/readout compatibility

Use the saved co-moving joint-field candidate at the three original packets, with embeddings B_h and metric-adjoint readouts R_h. In the reversed references set

    B_h_dual = B_h Q,
    R_h_dual = Q R_h.

Keep the old physical field and its metric; traverse each field transport in reverse. Exact matrix checks establish on both reversed edges

    U_reverse B_source_dual = B_target_dual Pi_dual,
    R_target_dual U_reverse = Pi_dual R_source_dual.

The second identity is checked as a full5-by44 matrix equation. Every reversed packet recovers all five coefficients. Applying Q twice recovers the original binding. Inverse-only coefficient transport without Q fails a control.

These matrices are the one retained co-moving candidate and the two common coefficient maps used by all24 certificates. This does not newly prove geometric covariance of the candidate for arbitrary markings or assemblies, nor does it refit any embedding.

## What is now established

A **complete, direction-indexed, labelled reversal comparison** passes, including coefficient/reference binding, geometry/phase templates, contacts, boundaries, exact involution and retained-field readout squares. The previous proposed blockers based on an unchanged N reader, context-only relabelling or terminal forward E do not defeat this comparison.

## What is not identified by this test

The dual species name does not automatically change the physical carrier. In particular dual E is old P, whose retained preparation has zero in the old E8 coordinate block. That is an explicit coordinate fact, not a rank obstruction to a future carrier-changing comparison or proof that no E interpretation exists.

The earlier E observation on the transformed N field and this complete reversal's terminal dual E are different presentations/endpoints. Their native-field identifications must not be inferred merely from the shared E label.

Still separate are a direction-indexed carrier identification with the forward native species field laws, active native transition authority, larger retained assemblies and universal coherence. The positive certificate result does not assert those claims.

## Verification

    node research/voevodsky/checkers/check_ramsey_complete_reversed_reference.mjs
    python research/voevodsky/checkers/check_ramsey_reversed_certificate_fields.py

Both fresh checks pass. Receipts:

- `results/ramsey-complete-reversed-reference-v1.json`: all forward/dual certificates and controls.
- `results/ramsey-reversed-certificate-fields-v1.json`: exact binding/readout squares, reversed embeddings and source hashes.

Prior direct input pins are verified; no other-owner source or saved receipt was rewritten. No formal proof outcome, native generator rule, conjecture-net outcome or graph admission was changed.
