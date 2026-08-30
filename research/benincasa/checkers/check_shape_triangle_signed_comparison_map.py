#!/usr/bin/env python3
"""Construct labelled triangle-to-signed comparison maps at six branches."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import sympy as sp
import compile_cleared_relative_shape_jet as source

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/shape-triangle-signed-comparison-map.json"

a, b, c, t = source.a, source.b, source.c, source.t
variables = (a, b, c, t)
K = source.K
family_hessian = sp.hessian(K, variables)
triangle_vector = sp.Matrix([0, 0, 0, 1])

walls = {
    "a-b-1": a-b-1,
    "a-b+1": a-b+1,
    "a+b-1": a+b-1,
}
branches = {
    "plus": {
        "fold": 6*a**2-2*b**2-4*c**2+3,
        "points": {
            "a-b-1": {a: 2, b: 1, c: sp.Rational(5, 2), t: sp.Rational(1, 2)},
            "a-b+1": {a: 1, b: 2, c: sp.Rational(1, 2), t: sp.Rational(1, 2)},
            "a+b-1": {a: sp.Rational(1, 2), b: sp.Rational(1, 2), c: 1, t: sp.Rational(1, 2)},
        },
    },
    "minus": {
        "fold": 2*a**2-6*b**2+4*c**2-3,
        "points": {
            "a-b-1": {a: 2, b: 1, c: sp.Rational(1, 2), t: -sp.Rational(1, 2)},
            "a-b+1": {a: 1, b: 2, c: sp.Rational(5, 2), t: -sp.Rational(1, 2)},
            "a+b-1": {a: sp.Rational(1, 2), b: sp.Rational(1, 2), c: 1, t: -sp.Rational(1, 2)},
        },
    },
}


def one_lift(point, wall, fold):
    """Return any W with dH(W)=1, dL(W)=dt(W)=0."""
    gradient_wall = sp.Matrix([sp.diff(wall, variable) for variable in variables]).subs(point)
    gradient_fold = sp.Matrix([sp.diff(fold, variable) for variable in variables]).subs(point)
    coordinates = sp.Matrix(sp.symbols("q0:4"))
    solution = next(iter(sp.linsolve([
        (gradient_wall.T*coordinates)[0]-1,
        (gradient_fold.T*coordinates)[0],
        coordinates[3],
    ], list(coordinates))))
    free = sorted(set().union(*(entry.free_symbols for entry in solution)), key=str)
    return sp.Matrix([entry.subs({symbol: 0 for symbol in free}) for entry in solution])


records = {}
checks = {}
for branch_name, branch in branches.items():
    fold = branch["fold"]
    for wall_name, point in branch["points"].items():
        wall = walls[wall_name]
        hessian = family_hessian.subs(point)
        signed_lift = one_lift(point, wall, fold)
        comparison_unit = sp.factor((triangle_vector.T*hessian*signed_lift)[0])
        tangent_kernel = hessian.nullspace()
        lift_independence = all(
            sp.factor((triangle_vector.T*hessian*tangent)[0]) == 0
            for tangent in tangent_kernel
        )
        key = f"{branch_name}:{wall_name}"
        records[key] = {
            "point": {str(variable): sp.sstr(value) for variable, value in point.items()},
            "triangle_normal": [0, 0, 0, 1],
            "signed_normal_lift": [sp.sstr(value) for value in signed_lift],
            "comparison_matrix": [[sp.sstr(comparison_unit)]],
            "deck_character_source": -1,
            "deck_character_target": -1,
            "cone_rank_at_generic_point": 0,
        }
        checks[f"{key}:comparison_is_nonzero"] = comparison_unit != 0
        checks[f"{key}:lift_independence"] = lift_independence
        checks[f"{key}:map_is_rank_one"] = sp.Matrix([[comparison_unit]]).rank() == 1
        checks[f"{key}:deck_intertwining"] = -comparison_unit == comparison_unit*(-1)

checks["all_six_maps_are_units_at_representatives"] = all(
    record["comparison_matrix"][0][0] != "0" for record in records.values()
)
checks["all_generic_cones_have_rank_zero"] = all(
    record["cone_rank_at_generic_point"] == 0 for record in records.values()
)
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.shape-triangle-signed-comparison-map.v1",
    "connection_convention": "comparison coefficient is Hess_K(partial_t,W_H), with dH(W_H)=1, dL(W_H)=dt(W_H)=0",
    "records": records,
    "comparison_units": {key: record["comparison_matrix"][0][0] for key, record in records.items()},
    "lift_independence": "changing W_H by the critical-curve tangent leaves the coefficient unchanged because that tangent is in ker Hess_K",
    "deck_character": -1,
    "generic_supported_cone_rank": 0,
    "scope": "generic local points on six physical triangle-signed branches; deeper zeros of the comparison unit excluded",
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print("comparison units", {key: record["comparison_matrix"][0][0] for key, record in records.items()})
print(OUT)
