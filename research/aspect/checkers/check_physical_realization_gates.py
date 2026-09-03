#!/usr/bin/env python3
"""Typed certificate diagnostic for realization, record, and physical-time gates."""

import json
from pathlib import Path

APPARATUS_FIELDS = {"source_realization", "apparatus_realization", "source_apparatus_interface", "incidence_transport", "coherence_transport"}
RECORD_FIELDS = {"physical_state_map", "effect_source", "effect", "positive_pairing", "detector_response", "stable_record_map"}
TIME_FIELDS = {"carrier_order_type", "physical_time_object", "tau", "orientation_authority", "order_compatibility", "clock_calibration", "valid_sector"}


def gate(certificate, required):
    return required <= certificate.keys() and all(certificate[field] not in (None, "") for field in required)


full = {
    "source_realization": "P(S)",
    "apparatus_realization": "P(S,D)",
    "source_apparatus_interface": "iota",
    "incidence_transport": "Phi_B",
    "coherence_transport": "Phi_kappa",
    "physical_state_map": "state_compare",
    "effect_source": "detector_channel_spec",
    "effect": "E0",
    "positive_pairing": "p0",
    "detector_response": "response0",
    "stable_record_map": "rec0",
    "carrier_order_type": "composition_category",
    "physical_time_object": "T_phys",
    "tau": "tau_calibrated",
    "orientation_authority": "clock_orientation",
    "order_compatibility": "monotone_tau",
    "clock_calibration": "calibration0",
    "valid_sector": "laboratory_sector",
}
missing_interface = {key: value for key, value in full.items() if key != "source_apparatus_interface"}
probability_only = {"positive_pairing": "p0", "effect": "E0"}
composition_order_only = {"carrier_order_type": "composition_category"}
missing_orientation = {key: value for key, value in full.items() if key != "orientation_authority"}
record_without_time = {key: value for key, value in full.items() if key not in TIME_FIELDS}
checks = {
    "full_certificate_passes_apparatus_gate": gate(full, APPARATUS_FIELDS),
    "full_certificate_passes_record_gate": gate(full, RECORD_FIELDS),
    "full_certificate_passes_time_gate": gate(full, TIME_FIELDS),
    "missing_interface_rejects_apparatus_claim": not gate(missing_interface, APPARATUS_FIELDS),
    "probability_alone_rejects_record_claim": not gate(probability_only, RECORD_FIELDS),
    "composition_order_alone_rejects_physical_time": not gate(composition_order_only, TIME_FIELDS),
    "time_map_without_orientation_authority_is_rejected": not gate(missing_orientation, TIME_FIELDS),
    "physical_record_does_not_imply_physical_time": gate(record_without_time, RECORD_FIELDS) and not gate(record_without_time, TIME_FIELDS),
    "apparatus_gate_does_not_imply_record_gate": gate({key: full[key] for key in APPARATUS_FIELDS}, APPARATUS_FIELDS) and not gate({key: full[key] for key in APPARATUS_FIELDS}, RECORD_FIELDS),
    "gate_requirements_are_pairwise_distinct": APPARATUS_FIELDS != RECORD_FIELDS and RECORD_FIELDS != TIME_FIELDS and APPARATUS_FIELDS != TIME_FIELDS,
    "all_required_fields_are_nonempty_in_full_certificate": all(full[field] not in (None, "") for field in APPARATUS_FIELDS | RECORD_FIELDS | TIME_FIELDS),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.physical-realization-gates.v1", "status": "passed", "checks": checks, "required_fields": {"apparatus": sorted(APPARATUS_FIELDS), "record": sorted(RECORD_FIELDS), "physical_time": sorted(TIME_FIELDS)}, "claim_boundary": "Schema-level gate diagnostic; the synthetic certificate is not evidence of a physical realization."}
output = Path(__file__).parents[1] / "results" / "physical_realization_gates.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "apparatus_fields": len(APPARATUS_FIELDS), "record_fields": len(RECORD_FIELDS), "time_fields": len(TIME_FIELDS)}, sort_keys=True))
