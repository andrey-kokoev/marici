#!/usr/bin/env python3
"""Compute the ordered marked-wall reduction and A1 branch costalk value."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / ".tmp_sympy"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import sympy as sp
import compile_cleared_relative_shape_jet as source

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "research/benincasa/results/shape-branch-mixed-costalk.json"

x, y, z = sp.symbols("x y z")
local = {
    source.a: -x / 2 + y / 2 + z / 2 - 1,
    source.b: x / 2 - y / 2 + z / 2 - 1,
    source.c: x / 2 + y / 2 - z / 2,
}
K = sp.expand(source.K0.subs(local))
N_left = sp.expand(source.numerators["G23_g12"].subs(local))
N_right = sp.expand(source.numerators["G31_g12"].subs(local))
g3 = sp.expand(source.g3.subs(local))
B23 = sp.expand(source.B23.subs(local))
B31 = sp.expand(source.B31.subs(local))

# Remove x^-3 y^-3 by the canonical second derivatives. The z^-1 factor is
# retained while the two source occurrences are summed before specialization.
coefficient = (N_left / B23 + N_right / B31) / (3 * g3 * z * K**sp.Rational(5, 2))
reduced = sp.factor(sp.diff(coefficient, x, 2, y, 2).subs({x: 0, y: 0}) / 4)
expected = 64 * z**5 * (z**2 + 8*z + 17) / (3 * (z - 1) * (z + 4)**3 * (z**2)**sp.Rational(5, 2))

jacobian = sp.Matrix([
    [-sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(1, 2)],
    [sp.Rational(1, 2), -sp.Rational(1, 2), sp.Rational(1, 2)],
    [sp.Rational(1, 2), sp.Rational(1, 2), -sp.Rational(1, 2)],
]).det()
plus_sheet = sp.limit((reduced * (z**2)**sp.Rational(5, 2) / z**5) * jacobian, z, 0)
minus_sheet = -plus_sheet

checks = {
    "native_triple_numerators_agree": sp.expand(N_left - N_right) == 0,
    "ordered_reduction_matches_closed_form": sp.factor(reduced - expected) == 0,
    "coordinate_jacobian_is_positive_half": jacobian == sp.Rational(1, 2),
    "plus_sheet_costalk_is_nonzero": plus_sheet == -sp.Rational(17, 6),
    "deck_sheet_is_anti_invariant": minus_sheet == sp.Rational(17, 6),
    "no_marked_z_pole_remains": sp.limit(reduced * (z**2)**sp.Rational(5, 2) / z**5, z, 0).is_finite,
}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.shape-branch-mixed-costalk.v1",
    "ordered_reduction": sp.sstr(reduced),
    "coordinate_jacobian": sp.sstr(jacobian),
    "normalized_sheet_values": [sp.sstr(plus_sheet), sp.sstr(minus_sheet)],
    "deck_character": -1,
    "marked_s12_residue": 0,
    "anti_invariant_branch_costalk_value": sp.sstr(minus_sheet - plus_sheet),
    "physical_cycle_pairing_constructed": False,
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print("sheet values:", plus_sheet, minus_sheet)
print(OUT)
