# Coherent change of anchor, without an anchor-free Boolean normalization

`agda/ObserverAnchorChange.agda` generalizes the previous record equivalence to every anchor a: RecordAt(a) ≃ Fibre(a), with both roundtrips.

Reanchoring along an actual comparison a=b is transport of this record family and is an equivalence. Identity and composition laws are checked, and normalization is equivariant: normalizing after reanchoring equals transporting the previous normalized value in the fibre family. These are explicit path equalities, not strict definitional equalities or a separately proved infinite hierarchy of higher coherence laws.

Forgetting the comparison leaves the reply and dependent value unchanged up to a checked path under reanchoring. Nevertheless the concrete turn loop flips the normalized Boolean. Thus valid anchor-relative equivalence does not imply a globally invariant Boolean presentation.

A stronger obstruction is explicit: the reflexive true record and the held-true turned record have definitionally equal forgotten reply/value pairs but normalize to true and false. No function from the unanchored reply/value space to Bool can agree with normalization for every original record. This is failure of the requested faithful factorization, not absence of all functions or all observations on the unanchored space.

## Verification

Fresh safe Cubical Agda --ignore-interfaces -Werror passes: results/agda-anchor-change.log. The aggregate includes this module. A fresh check_transport_gate.py run passes local/whole ordinary/whole strict checks with source bytes unchanged: results/transport-gate.json.

## Next

Connect this obstruction back to the internal first-order access-code language. Characterize exactly which coded observations of the anchored value descend after forgetting comparison paths: test constructive descent for result-only codes and impossibility for rule-sensitive codes. Preserve the distinction between an existing uninformative observation and faithful access to anchored content. The cover remains a mathematical example, not a physical causality or universal computation model.
