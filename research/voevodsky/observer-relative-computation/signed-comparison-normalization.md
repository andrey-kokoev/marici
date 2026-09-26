# Signed codes normalize by actual path equality

`agda/ObserverSignedNormalization.agda` transfers Cubical's checked circle-loop/integer isomorphism to the programme's actual Reply index (Unit paired with the existing circle). The forward/backward loop maps and both roundtrips are explicit. Consequently the fixed-base comparison-loop type is equivalent to Integers in this particular model.

The resulting integer classifier preserves composition. The first-order signed evaluator assigns0 to stay, +1 to up, -1 to down, and integer addition to composition. It is proved equal to the classifier of each interpreted code path. Reconstructing the integer normal form yields the ORIGINAL path up to a checked path equality.

For signed codes, equal evaluated integers are necessary AND sufficient for equality of interpreted comparison paths. Both up/down cancellation orders are also checked directly. This does not identify the original syntax trees: distinct expressions may denote the same path.

## Scope

The loop/integer equivalence covers fixed-base loops of this concrete circle index, not arbitrary observation spaces or machine histories. Comparison reversal is not a proof of a reverse admitted machine run. The library-derived classifier and the earlier separately defined integer-cover diagnostic are not claimed to have an additional checked function-alignment theorem in this leaf; each existing use retains its own proved contract.

The result supplies semantic completeness that finite observer agreement alone did not provide. Extending finite-probe separation to arbitrary signed winding still requires a separate bridge; it is not inferred simply from successful integer normalization.

## Verification

Fresh safe Cubical Agda --ignore-interfaces -Werror passes: results/agda-signed-normalization.log. Aggregate imports include the module. Fresh check_transport_gate.py passes local/whole ordinary/whole strict checks with inventoried source bytes unchanged: results/transport-gate.json.

## Next

Use signed normalization to extend the finite-observer boundary from nonnegative powers to bounded signed winding. Prove actual finite-cover recovery/separation with an explicit signed bound, including inverse-loop behavior, and distinguish pair-dependent finite separation from any fixed finite family's unbounded completeness.
