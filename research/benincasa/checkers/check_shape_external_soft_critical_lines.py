#!/usr/bin/env python3
"""Classify critical lines and A3 enhancements at external-soft parameters."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import sympy as sp
import compile_cleared_relative_shape_jet as source

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/shape-external-soft-critical-lines.json"

a, b, c, t = source.a, source.b, source.c, source.t
K = source.K

branches = {
    "plus": {
        "parameter": {t: 1},
        "line_variable": b,
        "transverse": (a, c),
        "line_ideal": {a: 0, c: 0, t: 1},
        "enhancements": [
            {
                "value": 1,
                "point": {a: 0, b: 1, c: 0, t: 1},
                "null_variable": c,
                "morse_variable": a,
            },
            {
                "value": 2,
                "point": {a: 0, b: 2, c: 0, t: 1},
                "null_variable": a,
                "morse_variable": c,
            },
        ],
    },
    "minus": {
        "parameter": {t: -1},
        "line_variable": a,
        "transverse": (b, c),
        "line_ideal": {b: 0, c: 0, t: -1},
        "enhancements": [
            {
                "value": 1,
                "point": {a: 1, b: 0, c: 0, t: -1},
                "null_variable": c,
                "morse_variable": b,
            },
            {
                "value": 2,
                "point": {a: 2, b: 0, c: 0, t: -1},
                "null_variable": b,
                "morse_variable": c,
            },
        ],
    },
}

records = {}
checks = {}
for branch_name, branch in branches.items():
    line_variable = branch["line_variable"]
    x, y = branch["transverse"]
    line_substitution = branch["line_ideal"]
    specialized = sp.expand(K.subs(branch["parameter"]))
    quadratic_x = sp.factor(sp.diff(specialized, x, 2).subs({x: 0, y: 0}) / 2)
    quadratic_y = sp.factor(sp.diff(specialized, y, 2).subs({x: 0, y: 0}) / 2)
    transverse_determinant = sp.factor(quadratic_x * quadratic_y)
    records[branch_name] = {
        "parameter_value": str(branch["parameter"][t]),
        "critical_line": {str(variable): str(value) for variable, value in line_substitution.items()},
        "line_parameter": str(line_variable),
        "transverse_quadratic_coefficients": [sp.sstr(quadratic_x), sp.sstr(quadratic_y)],
        "transverse_quadratic_determinant": sp.sstr(transverse_determinant),
        "generic_transverse_milnor_rank": 1,
        "enhancements": [],
    }
    checks[f"{branch_name}:critical_line_lies_on_K"] = sp.factor(K.subs(line_substitution)) == 0
    checks[f"{branch_name}:critical_line_annihilates_gradient"] = all(
        sp.factor(sp.diff(K, variable).subs(line_substitution)) == 0
        for variable in (a, b, c)
    )
    checks[f"{branch_name}:generic_transverse_quadratic_is_nonzero"] = transverse_determinant != 0

    for enhancement in branch["enhancements"]:
        point = enhancement["point"]
        null_variable = enhancement["null_variable"]
        morse_variable = enhancement["morse_variable"]
        slice_polynomial = sp.factor(
            K.subs({t: point[t], line_variable: enhancement["value"]})
        )
        hessian = sp.hessian(slice_polynomial, branch["transverse"]).subs({
            branch["transverse"][0]: 0,
            branch["transverse"][1]: 0,
        })
        null_restriction = sp.factor(slice_polynomial.subs(morse_variable, 0))
        quartic_coefficient = sp.factor(
            sp.diff(null_restriction, null_variable, 4).subs(null_variable, 0) / sp.factorial(4)
        )
        record = {
            "line_parameter_value": enhancement["value"],
            "point": {str(variable): str(value) for variable, value in point.items()},
            "slice_polynomial": sp.sstr(slice_polynomial),
            "transverse_hessian_rank": hessian.rank(),
            "null_variable": str(null_variable),
            "quartic_coefficient": sp.sstr(quartic_coefficient),
            "singularity_type": "A3",
            "transverse_milnor_rank": 3,
            "rank_excess_over_generic_line": 2,
        }
        records[branch_name]["enhancements"].append(record)
        key = f"{branch_name}:{enhancement['value']}"
        checks[f"{key}:physical_point"] = all(point[variable] >= 0 for variable in (a, b, c))
        checks[f"{key}:transverse_hessian_corank_one"] = hessian.rank() == 1
        checks[f"{key}:null_restriction_starts_quartic"] = (
            sp.diff(null_restriction, null_variable, order).subs(null_variable, 0) == 0
            for order in range(4)
        )
        checks[f"{key}:quartic_coefficient_nonzero"] = quartic_coefficient != 0

# Materialize generator-valued checks before assertion.
for key, value in list(checks.items()):
    if not isinstance(value, bool) and not isinstance(value, sp.logic.boolalg.Boolean):
        try:
            checks[key] = all(value)
        except TypeError:
            pass

assert all(bool(value) for value in checks.values()), {
    key: value for key, value in checks.items() if not bool(value)
}

packet = {
    "schema": "marici.shape-external-soft-critical-lines.v1",
    "records": records,
    "physical_A3_point_count": 4,
    "generic_transverse_rank": 1,
    "A3_transverse_rank": 3,
    "rank_excess_per_A3_point": 2,
    "support_classification": "external-soft parameter intersected with existing double coordinate-soft line",
    "new_carrier_component": False,
    "supported_comparison_maps": "not constructed in this packet",
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print("two external-soft critical lines with four physical A3 enhancements")
print(OUT)
