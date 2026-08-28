#!/usr/bin/env python3
"""Construct the labelled local coefficient complex at four external-soft A3 points."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import sympy as sp
import compile_cleared_relative_shape_jet as source

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/shape-external-soft-a3-complex.json"

a, b, c, t = source.a, source.b, source.c, source.t
K = source.K

points = [
    {
        "label": "t=1:b=1", "fixed": {t: 1, b: 1},
        "morse": a, "quartic_soft": c,
    },
    {
        "label": "t=1:b=2", "fixed": {t: 1, b: 2},
        "morse": c, "quartic_soft": a,
    },
    {
        "label": "t=-1:a=1", "fixed": {t: -1, a: 1},
        "morse": b, "quartic_soft": c,
    },
    {
        "label": "t=-1:a=2", "fixed": {t: -1, a: 2},
        "morse": c, "quartic_soft": b,
    },
]

# In the ordered A3 basis (1,x,x^2), restriction to the soft divisor x=0
# and inclusion of its first two normal grades are canonical.
restriction = sp.Matrix([[1, 0, 0]])
jet_inclusion = sp.Matrix([[0, 0], [1, 0], [0, 1]])
generic_inclusion = sp.Matrix([[1], [0], [0]])
assembly = generic_inclusion.row_join(jet_inclusion)

records = {}
checks = {
    "restriction_rank_is_one": restriction.rank() == 1,
    "soft_jet_inclusion_rank_is_two": jet_inclusion.rank() == 2,
    "restriction_kills_soft_jet_image": restriction * jet_inclusion == sp.zeros(1, 2),
    "assembly_is_isomorphism": assembly == sp.eye(3) and assembly.rank() == 3,
    "assembled_comparison_cone_rank_is_zero": 3 - assembly.rank() == 0,
}

for datum in points:
    polynomial = sp.factor(K.subs(datum["fixed"]))
    morse = datum["morse"]
    x = datum["quartic_soft"]
    derivative_morse = sp.factor(sp.diff(polynomial, morse))
    morse_unit = sp.factor(derivative_morse / (2*morse))
    morse_unit_at_origin = sp.factor(morse_unit.subs({morse: 0, x: 0}))
    reduced_polynomial = sp.factor(polynomial.subs(morse, 0))
    reduced_derivative = sp.factor(sp.diff(reduced_polynomial, x))
    quartic_coefficient = sp.factor(sp.diff(reduced_polynomial, x, 4).subs(x, 0) / sp.factorial(4))
    key = datum["label"]
    records[key] = {
        "slice_polynomial": sp.sstr(polynomial),
        "morse_variable": str(morse),
        "morse_unit_at_origin": sp.sstr(morse_unit_at_origin),
        "quartic_soft_variable": str(x),
        "reduced_polynomial": sp.sstr(reduced_polynomial),
        "reduced_jacobian_generator": sp.sstr(reduced_derivative),
        "local_jacobian_algebra": f"Q[{x}]/({x}^3)",
        "basis": ["1", str(x), f"{x}^2"],
        "generic_line_class": "1",
        "soft_normal_grades": [str(x), f"{x}^2"],
        "deck_character": -1,
    }
    checks[f"{key}:morse_unit_is_invertible"] = morse_unit_at_origin != 0
    checks[f"{key}:null_slice_is_pure_quartic"] = sp.factor(
        reduced_polynomial - quartic_coefficient*x**4
    ) == 0
    checks[f"{key}:quartic_coefficient_is_nonzero"] = quartic_coefficient != 0
    checks[f"{key}:jacobian_generator_is_cubic"] = sp.factor(
        reduced_derivative - 4*quartic_coefficient*x**3
    ) == 0

assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.shape-external-soft-a3-complex.v1",
    "records": records,
    "exact_sequence": "0 -> span(x,x^2) -> Q[x]/(x^3) -> span(1) -> 0",
    "restriction_matrix": [[int(value) for value in row] for row in restriction.tolist()],
    "soft_jet_inclusion_matrix": [[int(value) for value in row] for row in jet_inclusion.tolist()],
    "generic_plus_soft_assembly_matrix": [[int(value) for value in row] for row in assembly.tolist()],
    "local_cone_rank": 0,
    "raw_A3_excess_rank": 2,
    "excess_generated_by_existing_soft_grades": True,
    "deck_character": -1,
    "physical_betti_comparison": "not constructed; result is algebraic/de Rham associated-grade closure",
    "new_carrier_component": False,
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print("four A3 algebras close as generic line plus two labelled soft grades")
print(OUT)
