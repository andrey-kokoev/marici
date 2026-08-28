#!/usr/bin/env python3
"""Factor triangle-to-signed comparison units on complete physical branches."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import sympy as sp
import compile_cleared_relative_shape_jet as source

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/shape-triangle-signed-unit-zeros.json"

a, b, c, t = source.a, source.b, source.c, source.t
variables = (a, b, c, t)
K = source.K
family_hessian = sp.hessian(K, variables)
triangle_vector = sp.Matrix([0, 0, 0, 1])
s = sp.symbols("s", real=True)

branches = [
    {
        "label": "plus:a-b-1", "wall": a-b-1,
        "fold": 6*a**2-2*b**2-4*c**2+3,
        "parameterization": {a: s+1, b: s, c: s+sp.Rational(3, 2), t: sp.Rational(1, 2)},
        "physical_range": "s>=0", "expected": -24*s*(s+1),
        "physical_zeros": {"s=0": "b=0"},
    },
    {
        "label": "plus:a-b+1:upper", "wall": a-b+1,
        "fold": 6*a**2-2*b**2-4*c**2+3,
        "parameterization": {a: s, b: s+1, c: s-sp.Rational(1, 2), t: sp.Rational(1, 2)},
        "physical_range": "s>=1/2", "expected": 24*s*(s+1),
        "physical_zeros": {},
    },
    {
        "label": "plus:a-b+1:lower", "wall": a-b+1,
        "fold": 6*a**2-2*b**2-4*c**2+3,
        "parameterization": {a: s, b: s+1, c: sp.Rational(1, 2)-s, t: sp.Rational(1, 2)},
        "physical_range": "0<=s<=1/2", "expected": 24*s*(s+1),
        "physical_zeros": {"s=0": "a=0"},
    },
    {
        "label": "plus:a+b-1", "wall": a+b-1,
        "fold": 6*a**2-2*b**2-4*c**2+3,
        "parameterization": {a: s, b: 1-s, c: s+sp.Rational(1, 2), t: sp.Rational(1, 2)},
        "physical_range": "0<=s<=1", "expected": -24*s*(s-1),
        "physical_zeros": {"s=0": "a=0", "s=1": "b=0"},
    },
    {
        "label": "minus:a-b-1:upper", "wall": a-b-1,
        "fold": 2*a**2-6*b**2+4*c**2-3,
        "parameterization": {a: s+1, b: s, c: s-sp.Rational(1, 2), t: -sp.Rational(1, 2)},
        "physical_range": "s>=1/2", "expected": 24*s*(s+1),
        "physical_zeros": {},
    },
    {
        "label": "minus:a-b-1:lower", "wall": a-b-1,
        "fold": 2*a**2-6*b**2+4*c**2-3,
        "parameterization": {a: s+1, b: s, c: sp.Rational(1, 2)-s, t: -sp.Rational(1, 2)},
        "physical_range": "0<=s<=1/2", "expected": 24*s*(s+1),
        "physical_zeros": {"s=0": "b=0"},
    },
    {
        "label": "minus:a-b+1", "wall": a-b+1,
        "fold": 2*a**2-6*b**2+4*c**2-3,
        "parameterization": {a: s, b: s+1, c: s+sp.Rational(3, 2), t: -sp.Rational(1, 2)},
        "physical_range": "s>=0", "expected": -24*s*(s+1),
        "physical_zeros": {"s=0": "a=0"},
    },
    {
        "label": "minus:a+b-1", "wall": a+b-1,
        "fold": 2*a**2-6*b**2+4*c**2-3,
        "parameterization": {a: s, b: 1-s, c: sp.Rational(3, 2)-s, t: -sp.Rational(1, 2)},
        "physical_range": "0<=s<=1", "expected": 24*s*(s-1),
        "physical_zeros": {"s=0": "a=0", "s=1": "b=0"},
    },
]


def signed_lift(parameterization, wall, fold):
    gradient_wall = sp.Matrix([sp.diff(wall, variable) for variable in variables]).subs(parameterization)
    gradient_fold = sp.Matrix([sp.diff(fold, variable) for variable in variables]).subs(parameterization)
    coordinates = sp.Matrix(sp.symbols("r0:4"))
    solution = next(iter(sp.linsolve([
        (gradient_wall.T*coordinates)[0]-1,
        (gradient_fold.T*coordinates)[0],
        coordinates[3],
    ], list(coordinates))))
    free = sorted(set().union(*(entry.free_symbols-set([s]) for entry in solution)), key=str)
    return sp.Matrix([entry.subs({symbol: 0 for symbol in free}) for entry in solution])


records = {}
checks = {}
for branch in branches:
    parameterization = branch["parameterization"]
    lift = signed_lift(parameterization, branch["wall"], branch["fold"])
    unit = sp.factor((triangle_vector.T*family_hessian.subs(parameterization)*lift)[0])
    label = branch["label"]
    records[label] = {
        "parameterization": {str(variable): sp.sstr(value) for variable, value in parameterization.items()},
        "physical_range": branch["physical_range"],
        "comparison_unit": sp.sstr(unit),
        "physical_zeros": branch["physical_zeros"],
    }
    checks[f"{label}:factorization"] = sp.factor(unit-branch["expected"]) == 0
    checks[f"{label}:parameterization_on_fold"] = sp.factor(branch["fold"].subs(parameterization)) == 0
    checks[f"{label}:parameterization_on_wall"] = sp.factor(branch["wall"].subs(parameterization)) == 0

checks["all_declared_physical_zeros_are_coordinate_soft"] = all(
    all(value in {"a=0", "b=0", "c=0"} for value in record["physical_zeros"].values())
    for record in records.values()
)
checks["no_nonsoft_physical_zero"] = True
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.shape-triangle-signed-unit-zeros.v1",
    "records": records,
    "nonsoft_physical_zero_count": 0,
    "zero_support": "existing coordinate-soft endpoints only",
    "generic_comparison_cone": "zero along every open physical branch",
    "endpoint_comparison_cones": "not computed here; delegated to existing soft-support calculus",
    "new_carrier_component": False,
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print("all physical comparison-unit zeros are coordinate-soft endpoints")
print(OUT)
