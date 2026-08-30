#!/usr/bin/env python3
"""Capability gate from the scalar-scaffolded YM conductor to gravity."""

import json
from pathlib import Path

packet = {
    "polarity_odd_relative_normal_symbol": True,
    "ordered_conormal_orientation": True,
    "three_gluon_scalarized_residue_polynomial": True,
    "physical_brst_chain_map": False,
    "helicity_or_polarization_line": False,
    "bcj_jacobi_numerator_basis": False,
    "second_gauge_copy": False,
    "typed_state_pairing": False,
    "soft_leg_map": False,
}
required = ("bcj_jacobi_numerator_basis", "second_gauge_copy", "typed_state_pairing", "soft_leg_map")
double_copy_ready = all(packet[key] for key in required)
assert not double_copy_ready

result = {
    "status": "PASS",
    "packet": packet,
    "canonical_gravitational_double_copy_ready": double_copy_ready,
    "first_missing_structure": "polarization/BCJ coefficient enrichment before double copy",
    "conclusion": "the existing scalarized YM conductor cannot yet define a gravitational soft residue",
}
out = Path(__file__).resolve().parents[1] / "results" / "carrier_gravitational_soft_double_copy_gate.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
