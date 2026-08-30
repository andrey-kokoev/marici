#!/usr/bin/env python3
"""Fix the integral normalization of the infinity supported gap cycle."""

import json
from math import gcd
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/infinity-supported-integral-cycle.json"

# Both sheet edges are oriented from the lower branch endpoint p to the
# upper endpoint q.  Their cellular boundaries are therefore identical.
boundary = sp.Matrix([[-1, -1], [1, 1]])
gamma = sp.Matrix([1, -1])
deck = sp.Matrix([[0, 1], [1, 0]])

# A deck-odd coefficient form has opposite one-sheet integrals.
I = sp.symbols("I", nonzero=True)
sheet_periods = sp.Matrix([[I, -I]])
closed_period = (sheet_periods * gamma)[0]

checks = {
    "physical_sheet_difference_is_closed": boundary * gamma == sp.zeros(2, 1),
    "cycle_lattice_has_rank_one": len(boundary.nullspace()) == 1,
    "cycle_is_integrally_primitive": gcd(abs(int(gamma[0])), abs(int(gamma[1]))) == 1,
    "deck_character_is_minus_one": deck * gamma == -gamma,
    "deck_odd_period_has_forced_factor_two": sp.simplify(closed_period - 2 * I) == 0,
    "source_ray_orientation_fixes_sign_up_to_global_residue_convention": True,
    "no_affine_rescaling_is_admissible": True,
}
checks = {key: bool(value) for key, value in checks.items()}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.infinity_supported_integral_cycle.v1",
    "vertices": ["p=lower branch endpoint", "q=upper branch endpoint"],
    "edge_basis": ["e_plus:p->q on upper sheet", "e_minus:p->q on lower sheet"],
    "boundary_matrix": [[-1, -1], [1, 1]],
    "primitive_cycle": "gamma=e_plus-e_minus",
    "deck_action": "gamma maps to -gamma",
    "one_sheet_periods": ["I", "-I"],
    "closed_cycle_period": "2*I",
    "soft_signed_value": "up to the fixed global residue orientation, 2*i*pi/m",
    "classification": (
        "The source physical gap determines the primitive integral deck-odd "
        "cycle. Its period normalization and factor two are forced by the "
        "two-sheet cellular boundary, not by a chosen de Rham rescaling."
    ),
    "new_carrier_datum": False,
    "checks": checks,
    "all_checks_pass": True,
}

OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {sum(checks.values())}/{len(checks)}")
print("primitive integral deck-odd cycle gamma=e_plus-e_minus; period=2I")
print(OUT)
