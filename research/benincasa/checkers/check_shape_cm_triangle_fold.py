#!/usr/bin/env python3
"""Classify the Cayley-Menger degeneration at the external triangle wall."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import sympy as sp
import compile_cleared_relative_shape_jet as source

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/shape-cm-triangle-fold.json"

a, b, c, t = source.a, source.b, source.c, source.t
K = source.K
P1, P2, P3 = 1 + t, 1 - t, sp.Integer(1)
triangle = sp.factor(
    (P1 + P2 + P3)
    * (-P1 + P2 + P3)
    * (P1 - P2 + P3)
    * (P1 + P2 - P3)
)

walls = {
    "plus": {
        "t": sp.Rational(1, 2),
        "L": 6*a**2 - 2*b**2 - 4*c**2 + 3,
        "generic_point": {a: 1, b: sp.Rational(4, 3), c: sp.Rational(7, 6)},
    },
    "minus": {
        "t": -sp.Rational(1, 2),
        "L": 2*a**2 - 6*b**2 + 4*c**2 - 3,
        "generic_point": {a: sp.Rational(4, 3), b: 1, c: sp.Rational(7, 6)},
    },
}

signed_support = sp.factor(
    (a-b-1)*(a-b+1)*(a+b-1)*(a+b+1)
)
records = {}
checks = {
    "external_triangle_discriminant_is_3_times_1_minus_4t2": sp.expand(triangle - 3*(1-4*t**2)) == 0,
}
for label, datum in walls.items():
    value = datum["t"]
    L = datum["L"]
    specialized = sp.factor(K.subs(t, value))
    Kt = sp.factor(sp.diff(K, t).subs(t, value))
    resultant = sp.factor(sp.resultant(L, Kt, c))
    point = datum["generic_point"]
    point_with_t = dict(point)
    point_with_t[t] = value
    generic_Kt = sp.factor(sp.diff(K, t).subs(point_with_t))
    records[label] = {
        "parameter_value": sp.sstr(value),
        "square_factor": sp.sstr(L),
        "specialized_K": sp.sstr(specialized),
        "generic_positive_point": {str(variable): sp.sstr(coordinate) for variable, coordinate in point.items()},
        "normal_derivative_at_generic_point": sp.sstr(generic_Kt),
        "nontransverse_resultant": sp.sstr(resultant),
    }
    checks[f"{label}_specialization_is_square"] = sp.factor(specialized - L**2/16) == 0
    checks[f"{label}_generic_point_lies_on_fold"] = sp.factor(L.subs(point)) == 0
    checks[f"{label}_generic_point_is_positive"] = all(coordinate > 0 for coordinate in point.values())
    checks[f"{label}_normal_derivative_is_nonzero"] = generic_Kt != 0
    checks[f"{label}_deeper_support_is_existing_signed_arrangement"] = sp.factor(
        resultant - 144*signed_support**2
    ) == 0

assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.shape-cm-triangle-fold.v1",
    "external_triangle_polynomial": sp.sstr(triangle),
    "triangle_parameter_values": ["1/2", "-1/2"],
    "fold_records": records,
    "generic_local_type": "transverse rank-one fold: normal^2 plus triangle-parameter times a unit",
    "generic_nearby_cycle_rank": 1,
    "support_classification": "existing external triangle divisor",
    "deeper_nontransverse_support": [
        "a-b-1=0", "a-b+1=0", "a+b-1=0", "a+b+1=0"
    ],
    "new_carrier_component": False,
    "scope": "geometric and nearby-cycle rank classification; no global physical period asserted",
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print("triangle fold is generic rank one; deeper failure lies on signed support")
print(OUT)
