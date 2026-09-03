#!/usr/bin/env python3
"""Independence of readout descent from strict attachment transport coherence."""

import json
from pathlib import Path

ATTACHMENTS = ("a", "b")
RECORDS = (0, 1)
# One realization arrow R -> S. Contravariant attachment and record transport are identities.
attachment_pullback = {item: item for item in ATTACHMENTS}
record_pullback = {item: item for item in RECORDS}
readout_S = {"a": 0, "b": 1}
readout_R_good = {"a": 0, "b": 1}
readout_R_bad = {"a": 1, "b": 0}

def descent_failures(readout_R):
    return tuple(item for item in ATTACHMENTS if readout_R[attachment_pullback[item]] != record_pullback[readout_S[item]])

def identity_law(mapping): return all(mapping[item] == item for item in mapping)

good_failures = descent_failures(readout_R_good)
bad_failures = descent_failures(readout_R_bad)
checks = {
    "attachment_transport_is_strict_identity": identity_law(attachment_pullback),
    "record_transport_is_strict_identity": identity_law(record_pullback),
    "attachment_unit_law_holds": identity_law(attachment_pullback),
    "attachment_compositor_is_strict": all(attachment_pullback[attachment_pullback[item]] == attachment_pullback[item] for item in ATTACHMENTS),
    "good_readout_satisfies_descent": len(good_failures) == 0,
    "bad_readout_fails_descent": len(bad_failures) == 2,
    "bad_readout_preserves_attachment_transport": identity_law(attachment_pullback),
    "bad_readout_preserves_internal_coherence": all(attachment_pullback[attachment_pullback[item]] == item for item in ATTACHMENTS),
    "unit_laws_do_not_detect_readout_failure": identity_law(attachment_pullback) and bool(bad_failures),
    "readout_descent_is_independent_gate": not good_failures and bool(bad_failures),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.fourth-coherence-face-readout-descent.v1", "status": "passed", "checks": checks, "good_descent_failure_count": len(good_failures), "bad_descent_failures": bad_failures, "claim_boundary": "Finite independence model; it establishes a readout naturality gate, not a canonical geometric tetrahedron."}
output = Path(__file__).parents[1] / "results" / "fourth_coherence_face_readout_descent.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "bad_failures": len(bad_failures)}, sort_keys=True))
