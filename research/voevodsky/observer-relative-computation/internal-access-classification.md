# Complete information classification of internal access codes

`agda/ObserverAccessClassification.agda` classifies every finite compositional code of ObserverInternalInterface. The decision returns a ResultOnly witness or a RuleAccess witness; the two alternatives are proved incompatible.

For each code, its admissible image is the reply paired with propositional truncation of an origin history and its readout equality. Only origin membership is truncated. The actual reply remains visible.

Checked equivalences, with both roundtrips:

- ResultOnly code: admissible image is equivalent to Unit.
- RuleAccess code: admissible image is equivalent to the original History, hence Bool.
- Every code therefore normalizes to one of these two information types.

In particular, both(rule,rule) has admissible image equivalent to Bool, not an arbitrary independent Bool pair. The candidate reply (true,false) is proved inadmissible: both components read the SAME supplied history. Repeating access creates presentation redundancy, not an additional independently varying witness. This does not apply to separate histories or independent probes.

The result is specific to the two-history fixture and the current result/rule/both code language. Constant observations still exist; their inability to distinguish these histories is not nonexistence of observation. No geometric area, physical authority, resource cost, or universal computation classification follows.

## Verification

Fresh safe Cubical Agda --ignore-interfaces -Werror check passes: results/agda-access-classification.log. The aggregate import list now includes the module, and a fresh check_transport_gate.py run passes its local, whole ordinary, and whole -Werror checks with inventoried source bytes unchanged: results/transport-gate.json. Older aggregate audit receipts remain historical.

## Next

Internalize restriction itself as a first-order code transformation language, rather than adding arbitrary reply callbacks. Prove these transformations preserve shared-origin manifestations, establish when restriction exists, and test whether different projection choices agree on admissible images even though they can disagree on impossible reply combinations. This adds coherent internal comparison to the object-level information classification.
