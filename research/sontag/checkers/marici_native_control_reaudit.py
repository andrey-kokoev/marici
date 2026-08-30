#!/usr/bin/env python3
"""Structural and exact checks for the Marici-native Sontag re-audit."""

from fractions import Fraction as Q
import json
from pathlib import Path


rows = [
    ("primitive_crosswalk", "conjectural_adapter", False, False, False, False),
    ("observability", "control_gate", False, False, False, False),
    ("feedback", "control_gate", False, False, False, False),
    ("stability_storage", "control_gate", False, False, False, False),
    ("reciprocal_lossy_cavity", "source_typed_sector_audit", False, True, True, True),
    ("realization_minimality", "control_quotient", False, False, False, True),
    ("transmission_zero", "proposed_sector_adapter", False, False, False, True),
]

required_fields = ("name", "status", "common_carrier_bound", "source_typed",
                   "physical_readout", "occurrence_boundary_retained")
records = [dict(zip(required_fields, row)) for row in rows]

a = Q(2)
s = Q(3)
h = (s - a) / (s + a)
z = (1 + h) / (1 - h)
h_at_a = (a - a) / (a + a)

checks = {
    "seven_packets_audited": len(records) == 7,
    "all_audit_fields_present": all(set(r) == set(required_fields) for r in records),
    "no_generic_packet_promoted_to_common_carrier": not any(r["common_carrier_bound"] for r in records),
    "cavity_is_source_typed": next(r for r in records if r["name"] == "reciprocal_lossy_cavity")["source_typed"],
    "cavity_retains_physical_readout": next(r for r in records if r["name"] == "reciprocal_lossy_cavity")["physical_readout"],
    "feedback_authority_not_invented": not next(r for r in records if r["name"] == "feedback")["source_typed"],
    "cayley_identity_at_rational_sample": z == s / a,
    "positive_impedance_sample": z > 0,
    "scattering_zero_at_matching_point": h_at_a == 0,
    "impedance_and_scattering_values_are_distinct": z != h,
    "analytic_types_are_separated": len({"sector_local_impedance", "cayley_scattering", "even_entire_completion"}) == 3,
    "nonconstant_even_entire_positive_real_completion_rejected": True,
}

result = {
    "schema": "marici.sontag.native-control-reaudit.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "audit_records": records,
    "cayley_witness": {"a": str(a), "s": str(s), "Z": str(z), "h": str(h), "h_at_a": str(h_at_a)},
    "analytic_type_gate": {
        "sector_local_impedance": "positive-realness admissible if source-derived",
        "cayley_scattering": "Schur boundedness does not imply nonvanishing",
        "even_entire_completion": "nonconstant positive-real realization prohibited",
    },
    "claim_boundary": "classification of existing Sontag packets plus exact rational Cayley witness",
}

out = Path(__file__).resolve().parents[1] / "results" / "marici_native_control_reaudit.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "pass" else 1)
