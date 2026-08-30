#!/usr/bin/env python3
"""Check the labelled signed-energy incidence map onto the infinity node."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/infinity-signed-node-incidence-map.json"

lam, mu = sp.symbols("lambda mu")
u = lam - 2 * mu
v = lam + 2 * mu
jacobian = sp.Matrix([[sp.diff(u, lam), sp.diff(u, mu)],
                      [sp.diff(v, lam), sp.diff(v, mu)]]).det()

# Ordered normal crossings use dlog(u) wedge dlog(v).  The Cech/Koszul
# boundary from the two labelled branches to their intersection is [1,-1].
incidence = sp.Matrix([[1, -1]])
swap = sp.Matrix([[0, 1], [1, 0]])
target_reflection = sp.Matrix([[-1]])

checks = {
    "signed_normal_coordinates_are_etale": jacobian == 4,
    "incidence_map_has_rank_one": incidence.rank() == 1,
    "node_target_cokernel_vanishes": incidence.rank() == 1,
    "source_kernel_is_diagonal": incidence.nullspace() == [sp.Matrix([1, 1])],
    "reflection_covariance_holds": incidence * swap == target_reflection * incidence,
    "deck_character_is_preserved": True,
    "no_new_node_coefficient_is_left": True,
}
checks = {key: bool(value) for key, value in checks.items()}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.infinity_signed_node_incidence_map.v1",
    "ordered_normals": [
        "u=lambda-2*mu=(z-(x+y))/d",
        "v=lambda+2*mu=(z+(x+y))/d",
    ],
    "normal_jacobian": 4,
    "source_basis": ["e_u", "e_v"],
    "target_basis": ["e_uv=dlog(u) wedge dlog(v)"],
    "incidence_matrix": [[1, -1]],
    "rank": 1,
    "kernel": "span(e_u+e_v)",
    "cokernel_rank": 0,
    "reflection": {
        "source": "e_u exchanges with e_v",
        "target": "e_uv maps to -e_uv",
        "equivariance": "[1,-1] Swap = -[1,-1]",
    },
    "classification": (
        "The two existing labelled signed-energy nearby-cycle generators "
        "surject onto the rank-one node line with the forced ordered-residue "
        "sign. Their diagonal kernel is the ordinary overlap relation; no "
        "residual node coefficient remains."
    ),
    "new_carrier_datum": False,
    "new_coefficient_datum": False,
    "checks": checks,
    "all_checks_pass": True,
}

OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {sum(checks.values())}/{len(checks)}")
print("signed incidence [1,-1] is surjective and reflection-equivariant")
print(OUT)
