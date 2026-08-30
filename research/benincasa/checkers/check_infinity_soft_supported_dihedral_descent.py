#!/usr/bin/env python3
"""Reflection and full dihedral descent of the supported infinity line."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/infinity-soft-supported-dihedral-descent.json"

reflection_packet = json.loads(
    (ROOT / "research/benincasa/g12-g31-residue-chart-transition.json")
    .read_text(encoding="utf-8")
)
cyclic_packet = json.loads(
    (ROOT / "research/benincasa/results/infinity-soft-supported-cyclic-descent.json")
    .read_text(encoding="utf-8")
)

# Occurrence order: G12@P3-soft, G23@P1-soft, G31@P2-soft.
rho = sp.Matrix(cyclic_packet["cyclic_matrix"])
reflection_permutation = sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])

residue_orientation_sign = reflection_packet["transition"]["orientation_sign"]
cut_orientation_sign = -1  # t -> 1/t reverses the oriented gap interval.
deck_pairing_sign = (-1) * (-1)  # odd coefficient paired with odd cycle.
total_internal_sign = residue_orientation_sign * cut_orientation_sign * deck_pairing_sign
sigma = total_internal_sign * reflection_permutation

identity = sp.eye(3)
invariant_vector = sp.Matrix([1, 1, 1])
joint_constraints = (rho - identity).col_join(sigma - identity)
dihedral_invariant_rank = 3 - joint_constraints.rank()

checks = {
    "residue_reflection_sign_is_minus": residue_orientation_sign == -1,
    "reciprocal_cut_orientation_is_minus": cut_orientation_sign == -1,
    "odd_coefficient_odd_cycle_pairing_is_even": deck_pairing_sign == 1,
    "combined_reflection_character_is_even": total_internal_sign == 1,
    "reflection_is_involutive": sigma**2 == identity,
    "dihedral_relation_holds": sigma * rho * sigma == rho**2,
    "cyclic_generator_survives_reflection": sigma * invariant_vector == invariant_vector,
    "full_dihedral_invariant_rank_is_one": dihedral_invariant_rank == 1,
}
checks = {key: bool(value) for key, value in checks.items()}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.infinity_soft_supported_dihedral_descent.v1",
    "occurrence_basis": cyclic_packet["occurrence_basis"],
    "reflection": "sigma_23: G12@P3-soft <-> G31@P2-soft, G23@P1-soft fixed",
    "sign_factors": {
        "poincare_residue_orientation": residue_orientation_sign,
        "reciprocal_cut_orientation": cut_orientation_sign,
        "deck_odd_coefficient_times_deck_odd_cycle": deck_pairing_sign,
        "combined": total_internal_sign,
    },
    "reflection_matrix": [list(map(int, row)) for row in sigma.tolist()],
    "dihedral_relations": ["rho^3=1", "sigma^2=1", "sigma*rho*sigma=rho^-1"],
    "dihedral_invariant_generator": [1, 1, 1],
    "dihedral_invariant_rank": dihedral_invariant_rank,
    "verdict": (
        "The residue and cut-orientation signs cancel. The supported cyclic "
        "line is reflection-even and descends through the full D3 occurrence "
        "stabilizer without cancellation."
    ),
    "new_carrier_datum": False,
    "checks": checks,
    "all_checks_pass": True,
}

OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {sum(checks.values())}/{len(checks)}")
print("full dihedral invariant rank 1")
print(OUT)
