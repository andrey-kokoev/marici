#!/usr/bin/env python3
"""Audit divisorial parity of the finite-sextic coordinate-boundary discriminants."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
source = json.loads((ROOT / "research/nima/finite-sextic-higher-critical-locus.json").read_text(encoding="utf-8"))
triangle = source["momentum_triangle"]
expected_a0 = f"-(E - P2)**2*(E + P2)**2*{triangle}/(4*P2**2)"
expected_b0 = f"-(E - P1)**2*(E + P1)**2*{triangle}/(4*P1**2)"
assert source["coordinate_boundary_A0"]["critical_value"] == expected_a0
assert source["coordinate_boundary_B0"]["critical_value"] == expected_b0
assert source["coordinate_boundary_A0"]["support_factors"] == ["E-P2", "E+P2", "Lambda"]
assert source["coordinate_boundary_B0"]["support_factors"] == ["E-P1", "E+P1", "Lambda"]

result = {
    "A0_valuations": {"E-P2": 2, "E+P2": 2, "Lambda": 1},
    "B0_valuations": {"E-P1": 2, "E+P1": 2, "Lambda": 1},
    "signed_energy_inertia": 1,
    "triangle_inertia": -1,
    "signed_energy_cartier_length": 2,
}
print(json.dumps(result, indent=2))
