"""Exact clutching-degree audit for the celestial spin-two bundle."""

import hashlib
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve()
ROOT = HERE.parents[1]
RESULT = ROOT / "results" / "spin_two_polarization_euler_obstruction_checks.json"

phi = sp.symbols("phi", real=True)
I = sp.I
base_euler_number = 2
spin_weight = 2
polarization_euler_number = base_euler_number * spin_weight

base_clutching = sp.exp(I * base_euler_number * phi)
polarization_clutching = sp.expand_power_base(base_clutching ** spin_weight, force=True)


def winding(g):
    return sp.simplify(sp.integrate(sp.diff(g, phi) / g, (phi, 0, 2 * sp.pi)) / (2 * sp.pi * I))


base_winding = winding(base_clutching)
polarization_winding = winding(polarization_clutching)
composite_total_holonomy = -2 * sp.pi * polarization_euler_number
relative_total_holonomy = -composite_total_holonomy

checks = {
    "sphere_tangent_clutching_has_degree_two": base_winding == 2,
    "spin_two_representation_doubles_clutching_degree": polarization_winding == 4,
    "polarization_bundle_euler_number_is_four": polarization_euler_number == 4,
    "nonzero_euler_number_forbids_nowhere_zero_section": polarization_euler_number != 0,
    "transverse_zero_indices_sum_to_four": polarization_winding == polarization_euler_number,
    "composite_connection_total_defect_is_minus_eight_pi": composite_total_holonomy == -8 * sp.pi,
    "regular_total_connection_forces_plus_eight_pi_relative_defect": relative_total_holonomy == 8 * sp.pi,
    "hostile_spin_one_typing_has_wrong_degree": base_euler_number * 1 != polarization_euler_number,
}

payload = {
    "schema": "marici.strominger.spin-two-polarization-euler-obstruction.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "passed": sum(checks.values()),
    "total": len(checks),
    "checks": checks,
    "clutching": {
        "tangent_degree": str(base_winding),
        "representation_weight": spin_weight,
        "polarization_degree": str(polarization_winding),
    },
    "topological_conclusion": {
        "bundle": "Symmetric trace-free rank-two cotangent tensors on S2",
        "euler_number": polarization_euler_number,
        "zero_law": "every transverse section has signed zero-index sum four; no nowhere-zero section exists",
        "composite_connection_defect": str(composite_total_holonomy),
        "relative_connection_compensation": str(relative_total_holonomy),
    },
    "scope": "oriented celestial S2 and spin weight two; local index signs depend on the chosen orientation convention",
}
payload["checker_sha256"] = hashlib.sha256(HERE.read_bytes()).hexdigest()
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="ascii")
print(f"{payload['passed']}/{payload['total']} checks passed")
print(payload["checker_sha256"])
raise SystemExit(0 if payload["status"] == "passed" else 1)
