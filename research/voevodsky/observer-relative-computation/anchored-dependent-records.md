# Dependent observed records normalize relative to their retained anchor

`agda/ObserverAnchoredRecords.agda` packages a reply y, an actual path base=y, and an observed value in the fibre over y. The comparison path is retained as data, not truncated or replaced by its mere existence.

Transporting the value backwards along that comparison defines an anchored Boolean readout. Embedding a Boolean at the anchor and this normalization have BOTH checked roundtrips, giving Record ≃ Bool. Path induction proves the full-record roundtrip; this does not assert that all stored comparisons are equal in a fixed-reply fibre.

The existing finite comparison codes now select manifestations of a supplied anchored value. Every such manifestation faithfully normalizes back to that value.

## Checked contrasting examples

- (base, refl, true) and (base, turn, false) are equal as complete dependent records: the reply/value move coherently. Different endpoint Boolean presentations do not imply different anchored content.
- (base, refl, true) and (base, turn, true) are unequal as complete records. Keeping the visible Boolean true while changing the comparison represents the other anchored value; the second record equals the reflexive embedding of false.

This is an equivalence of the mathematical record type, not literal serialization equality and not a claim that comparison fields can be dropped without changing what is recoverable. It also does not contradict the previous impossibility of a constant Boolean extension on the certificate space alone: the present input includes a dependent value and uses a different, anchored readout.

## Verification

Fresh safe Cubical Agda --ignore-interfaces -Werror: results/agda-anchored-records.log. The aggregate includes the module. A fresh check_transport_gate.py run passes local/whole ordinary/whole strict checks with inventoried source bytes unchanged: results/transport-gate.json.

## Next

Investigate coherent change of anchor rather than silently fixing a global frame. Establish transport-equivariance and identity/composition behavior for reanchoring. Test whether the anchored Boolean normalization can descend after forgetting the comparison path, and use the loop example to separate a valid frame-relative equivalence from an unsupported anchor-independent value assignment. No physical or causal interpretation is established by these checks.
