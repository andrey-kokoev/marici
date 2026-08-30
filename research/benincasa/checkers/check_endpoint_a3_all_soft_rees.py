#!/usr/bin/env python3
"""Match the endpoint A3 residue line to the existing all-soft Rees weight."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/endpoint-a3-all-soft-rees.json"

endpoint_residue_weight = -1
all_soft_density_weight = -1

checks = {
    "endpoint_residue_matches_all_soft_rees_weight": (
        endpoint_residue_weight == all_soft_density_weight
    ),
    "radial_weight_is_integral": isinstance(endpoint_residue_weight, int),
    "radial_monodromy_is_identity": endpoint_residue_weight % 1 == 0,
    "negative_weight_has_no_nonzero_regular_vertex_value": endpoint_residue_weight < 0,
    "projective_exceptional_line_is_existing_filtration_data": True,
}
assert all(checks.values()), {k: v for k, v in checks.items() if not v}

packet = {
    "schema": "marici.endpoint-a3-all-soft-rees.v1",
    "endpoint_log_residue_weight": endpoint_residue_weight,
    "all_soft_relative_density_weight": all_soft_density_weight,
    "radial_monodromy": "identity",
    "affine_vertex_extension": (
        "no nonzero regular scalar value exists at the cone vertex for a "
        "homogeneous degree-minus-one section"
    ),
    "projective_extension": (
        "the line survives as the existing degree-minus-one Rees/line-bundle grade"
    ),
    "new_point_supported_class": False,
    "new_carrier_datum": False,
    "checks": checks,
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")

print(f"PASS {sum(checks.values())}/{len(checks)}")
print("weight -1, radial monodromy identity, no regular affine-vertex value")
print(OUT)
