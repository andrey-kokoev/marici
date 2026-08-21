#!/usr/bin/env python3
"""Typed capability matrix for the proposed Carrier-to-BMS orientation bridge."""

import json
from pathlib import Path


links = {
    "carrier_to_marked_theta_circuit_ward": True,
    "carrier_relation_generator_to_physical_cut": False,
    "carrier_scalar_first_jet_to_physical_ward_coefficients": False,
    "gravitational_amplitude_to_weinberg_soft_residue": True,
    "weinberg_soft_residue_to_bms_ward": True,
    "bms_ward_to_memory": True,
    "marked_theta_circuit_ward_is_bms_ward": False,
    "carrier_relation_to_gravitational_soft_residue": False,
}

typed_path = (
    links["carrier_relation_to_gravitational_soft_residue"]
    and links["weinberg_soft_residue_to_bms_ward"]
    and links["bms_ward_to_memory"]
)

assert not links["marked_theta_circuit_ward_is_bms_ward"]
assert not typed_path

result = {
    "status": "PASS",
    "links": links,
    "complete_typed_bridge_exists": typed_path,
    "first_missing_link": "carrier relation cell -> gravitational soft residue",
    "warning": "Ward/circuit and BMS Ward are distinct typed objects",
}

out = Path(__file__).resolve().parents[1] / "results" / "orientation_bridge_factorization_gate.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
