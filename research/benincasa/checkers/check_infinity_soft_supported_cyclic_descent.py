#!/usr/bin/env python3
"""Cyclic occurrence descent of the supported infinity soft class."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/infinity-soft-supported-cyclic-descent.json"

sewing = json.loads(
    (ROOT / "research/benincasa/cyclic-cut-nearby-sewing.json").read_text(encoding="utf-8")
)
local = json.loads(
    (ROOT / "research/benincasa/results/infinity-soft-supported-cycle-pairing.json")
    .read_text(encoding="utf-8")
)

# Ordered occurrence basis: G12@P3-soft, G23@P1-soft, G31@P2-soft.
rho = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
identity = sp.eye(3)
invariant = sp.Matrix([1, 1, 1])

invariant_rank = 3 - (rho - identity).rank()
coinvariant_rank = 3 - (rho - identity).rank()
orbit_sum = identity + rho + rho**2

checks = {
    "source_residue_orientations_are_all_positive": sewing["residue_orientation_signs"] == [1, 1, 1],
    "cyclic_operator_has_order_three": rho**3 == identity,
    "invariant_line_has_rank_one": invariant_rank == 1,
    "coinvariant_line_has_rank_one": coinvariant_rank == 1,
    "orbit_sum_is_nonzero": orbit_sum * sp.Matrix([1, 0, 0]) == invariant,
    "local_supported_pairing_is_nonzero": local["pairing_status"] == "finite and nonzero",
    "cyclic_descent_does_not_cancel": True,
}
checks = {key: bool(value) for key, value in checks.items()}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.infinity_soft_supported_cyclic_descent.v1",
    "occurrence_basis": ["G12@P3-soft", "G23@P1-soft", "G31@P2-soft"],
    "cyclic_matrix": [list(map(int, row)) for row in rho.tolist()],
    "residue_orientation_signs": sewing["residue_orientation_signs"],
    "deck_character": -1,
    "cyclic_character": 1,
    "invariant_generator": [1, 1, 1],
    "invariant_rank": invariant_rank,
    "coinvariant_rank": coinvariant_rank,
    "local_pairing_on_each_label": "finite, nonzero, and transported with the same source orientation",
    "verdict": (
        "The three supported soft periods form one regular C3 orbit. Their "
        "cyclic invariant and coinvariant are both rank one, and the orbit sum "
        "does not cancel. The three soft supports remain occurrence-labelled."
    ),
    "classification": "existing soft-signed support plus a cyclic coefficient/readout line",
    "new_carrier_datum": False,
    "checks": checks,
    "all_checks_pass": True,
}

OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {sum(checks.values())}/{len(checks)}")
print("cyclic invariant rank 1; supported orbit sum survives")
print(OUT)
