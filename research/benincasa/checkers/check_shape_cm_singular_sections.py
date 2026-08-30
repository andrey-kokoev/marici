#!/usr/bin/env python3
"""Resolve the physical singular scheme of the shape Cayley-Menger family."""

import itertools
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import sympy as sp
import compile_cleared_relative_shape_jet as source

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/shape-cm-singular-sections.json"

a, b, c, t = source.a, source.b, source.c, source.t
variables = (a, b, c)
K, K0, K1, K2 = source.K, source.K0, source.K1, source.K2

# Classify the nonnegative singular scheme at t=0 using A=a^2, B=b^2,
# C=c^2 and the factorization K_a=2a(2A-B-C-1), cyclically.
A = sp.symbols("A0:3")
square_K = A[0]**2 + A[1]**2 + A[2]**2 - A[0]*A[1] - A[0]*A[2] - A[1]*A[2] - sum(A) + 1
physical_square_solutions = []
for size in range(4):
    for active in itertools.combinations(range(3), size):
        active = set(active)
        equations = []
        for index in active:
            equations.append(sp.Eq(2*A[index] - sum(A[j] for j in range(3) if j != index) - 1, 0))
        for index in range(3):
            if index not in active:
                equations.append(sp.Eq(A[index], 0))
        solutions = sp.solve(equations, A, dict=True)
        for solution in solutions:
            values = tuple(sp.factor(solution[value]) for value in A)
            if all(value >= 0 for value in values) and sp.factor(square_K.subs(solution)) == 0:
                physical_square_solutions.append(values)
physical_square_solutions = sorted(set(physical_square_solutions), key=str)

sections = [
    {a: 1-t, b: 1+t, c: 0},
    {a: 1, b: 0, c: 1+t},
    {a: 0, b: 1, c: 1-t},
]
base_points = [{variable: sp.factor(sp.sympify(expression).subs(t, 0)) for variable, expression in section.items()}
               for section in sections]
velocities = [sp.Matrix([sp.diff(sp.sympify(section[variable]), t).subs(t, 0) for variable in variables])
              for section in sections]

H0 = sp.hessian(K0, variables)
grad_K1 = sp.Matrix([sp.diff(K1, variable) for variable in variables])
records = []
for index, (section, point, velocity) in enumerate(zip(sections, base_points, velocities)):
    hessian = sp.simplify(H0.subs(point))
    gradient_k1 = sp.simplify(grad_K1.subs(point))
    raw_k2 = sp.factor(K2.subs(point))
    effective_k2 = sp.factor(raw_k2 - (gradient_k1.T * hessian.inv() * gradient_k1)[0])
    family_hessian_det = sp.factor(sp.hessian(K, variables).subs(section).det())
    records.append({
        "index": index,
        "section": {str(variable): sp.sstr(expression) for variable, expression in section.items()},
        "base_point": {str(variable): sp.sstr(value) for variable, value in point.items()},
        "velocity": [sp.sstr(value) for value in velocity],
        "K1_value": sp.sstr(K1.subs(point)),
        "raw_K2_value": sp.sstr(raw_k2),
        "effective_second_critical_value": sp.sstr(effective_k2),
        "family_hessian_determinant": sp.sstr(family_hessian_det),
    })

checks = {
    "nonnegative_singular_scheme_has_three_points": physical_square_solutions == [
        (sp.Integer(0), sp.Integer(1), sp.Integer(1)),
        (sp.Integer(1), sp.Integer(0), sp.Integer(1)),
        (sp.Integer(1), sp.Integer(1), sp.Integer(0)),
    ],
    "all_sections_lie_on_full_family": all(sp.factor(K.subs(section)) == 0 for section in sections),
    "all_sections_are_critical": all(
        all(sp.factor(sp.diff(K, variable).subs(section)) == 0 for variable in variables)
        for section in sections
    ),
    "all_base_singularities_are_morse": all(sp.factor(H0.subs(point).det()) == -288 for point in base_points),
    "first_shape_class_vanishes_locally": all(sp.factor(K1.subs(point)) == 0 for point in base_points),
    "critical_velocities_solve_first_transport_equation": all(
        sp.simplify(H0.subs(point) * velocity + grad_K1.subs(point)) == sp.zeros(3, 1)
        for point, velocity in zip(base_points, velocities)
    ),
    "raw_second_symbols_are_nonzero": [sp.factor(K2.subs(point)) for point in base_points] == [24, 8, 8],
    "effective_second_classes_vanish": all(record["effective_second_critical_value"] == "0" for record in records),
    "generic_sections_remain_morse": all(record["family_hessian_determinant"] != "0" for record in records),
}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.shape-cm-singular-sections.v1",
    "physical_square_singular_points": [[sp.sstr(value) for value in point] for point in physical_square_solutions],
    "critical_sections": records,
    "local_deformation_result": "analytically trivial along each generic critical section through second order, and exactly critical in the full family",
    "exceptional_parameter_support": {
        "t=1 or t=-1": "external soft support",
        "t=1/2 or t=-1/2": "external triangle-degeneration support",
    },
    "carrier_classification": "existing coordinate-soft and triangle support only",
    "residual_supported_class": 0,
    "scope": "nonnegative singular scheme of the homogeneous shape family",
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print("three exact critical sections; effective second class zero")
print(OUT)
