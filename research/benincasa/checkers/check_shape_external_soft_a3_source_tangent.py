#!/usr/bin/env python3
"""Reduce the source external-soft normal in each labelled A3 Jacobian algebra."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import sympy as sp
import compile_cleared_relative_shape_jet as source

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/shape-external-soft-a3-source-tangent.json"

a, b, c, t = source.a, source.b, source.c, source.t
K = source.K

points = [
    ("t=1:b=1", {t: 1, b: 1}, a, c, -1, "P2=1-t"),
    ("t=1:b=2", {t: 1, b: 2}, c, a, -1, "P2=1-t"),
    ("t=-1:a=1", {t: -1, a: 1}, b, c, 1, "P1=1+t"),
    ("t=-1:a=2", {t: -1, a: 2}, c, b, 1, "P1=1+t"),
]

records = {}
checks = {}
for label, fixed, morse, x, normal_sign, source_normal in points:
    raw = sp.factor(normal_sign * sp.diff(K, t).subs(fixed))
    reduced = sp.factor(raw.subs(morse, 0))
    jacobian_class = sp.rem(sp.Poly(reduced, x), sp.Poly(x**3, x)).as_expr()
    coeffs = [sp.factor(jacobian_class.coeff(x, degree)) for degree in range(3)]
    addressed = [degree for degree, value in enumerate(coeffs) if value != 0]
    normal_jet = []
    for order in range(1, 5):
        jet_raw = sp.factor(
            normal_sign**order
            * sp.diff(K, t, order).subs(fixed)
            / sp.factorial(order)
        )
        jet_reduced = sp.factor(jet_raw.subs(morse, 0))
        jet_class = sp.rem(sp.Poly(jet_reduced, x), sp.Poly(x**3, x)).as_expr()
        normal_jet.append([
            sp.sstr(sp.factor(jet_class.coeff(x, degree)))
            for degree in range(3)
        ])
    first_visible_order = next(
        (
            order for order, values in enumerate(normal_jet, start=1)
            if any(value != "0" for value in values)
        ),
        None,
    )
    jet_matrix = sp.Matrix([
        [sp.sympify(value) for value in values]
        for values in normal_jet
    ]).T
    records[label] = {
        "source_normal": source_normal,
        "source_normal_sign_times_dK_dt": sp.sstr(raw),
        "after_morse_elimination": sp.sstr(reduced),
        "jacobian_class_basis_1_x_x2": [sp.sstr(value) for value in coeffs],
        "addressed_grades": addressed,
        "normal_jet_orders_1_through_4": normal_jet,
        "first_visible_normal_order": first_visible_order,
        "normal_jet_image_rank": jet_matrix.rank(),
        "normal_jet_image_is_even_plane": (
            jet_matrix.rank() == 2
            and all(jet_matrix[1, column] == 0 for column in range(jet_matrix.cols))
        ),
        "soft_variable": str(x),
    }
    checks[f"{label}:source_tangent_is_defined"] = raw != 0
    checks[f"{label}:normal_jet_image_is_even_plane"] = (
        records[label]["normal_jet_image_is_even_plane"]
    )

packet = {
    "schema": "marici.shape-external-soft-a3-source-tangent.v1",
    "basis": ["1", "x", "x^2"],
    "records": records,
    "zero_jacobian_classes": [
        label for label, record in records.items()
        if all(value == "0" for value in record["jacobian_class_basis_1_x_x2"])
    ],
    "nonzero_jacobian_classes": [
        label for label, record in records.items()
        if any(value != "0" for value in record["jacobian_class_basis_1_x_x2"])
    ],
    "interpretation": (
        "The frozen external-soft parameter supplies a canonical algebraic tangent "
        "class. This does not by itself construct a Betti relative-chain map."
    ),
    "all_checks_pass": all(checks.values()),
    "checks": checks,
}
assert packet["all_checks_pass"], {key: value for key, value in checks.items() if not value}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
for label, record in records.items():
    print(label, record["jacobian_class_basis_1_x_x2"])
print(OUT)
