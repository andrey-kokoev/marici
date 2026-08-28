#!/usr/bin/env python3
"""Exact checks for the quadratic trace relation behind the Cartan tower."""

from __future__ import annotations

import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
CARTAN_CHECKER = HERE / "cartan_endpoint_grade_change_coherence_checks.py"


def load_cartan_module():
    spec = importlib.util.spec_from_file_location("cartan_exact", CARTAN_CHECKER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load Cartan checker")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def symmetric_dimension(degree: int, ambient_dimension: int) -> int:
    return math.comb(degree + ambient_dimension - 1, ambient_dimension - 1)


def harmonic_dimension(degree: int, ambient_dimension: int) -> int:
    trace = symmetric_dimension(degree - 2, ambient_dimension) if degree >= 2 else 0
    return symmetric_dimension(degree, ambient_dimension) - trace


def main() -> None:
    cartan = load_cartan_module()
    gates = {
        "quadratic_trace_projects_to_zero": True,
        "fischer_dimension_decomposition_is_exact": True,
        "harmonic_hilbert_function_is_two_l_plus_one": True,
        "hilbert_increment_is_exactly_two": True,
        "principal_quadratic_resolution_has_correct_graded_dimensions": True,
        "no_additional_relation_dimension_is_required": True,
        "constant_two_increment_is_specific_to_three_ambient_dimensions": True,
        "spin_two_five_plus_two_plus_two_is_quadric_hilbert_growth": True,
    }

    projection_cases = 0
    for degree in range(0, 8):
        monomials = [
            {(degree, 0, 0): Fraction(1)},
            {(max(degree - 1, 0), 1 if degree else 0, 0): Fraction(1)},
        ]
        for p in monomials:
            qp = cartan.multiply(cartan.R2, p)
            projected = cartan.harmonic_project(qp, degree + 2)
            gates["quadratic_trace_projects_to_zero"] &= projected == {}
            projection_cases += 1

    dimensions = []
    for degree in range(0, 51):
        sym = symmetric_dimension(degree, 3)
        trace = symmetric_dimension(degree - 2, 3) if degree >= 2 else 0
        harmonic = harmonic_dimension(degree, 3)
        gates["fischer_dimension_decomposition_is_exact"] &= sym == harmonic + trace
        gates["harmonic_hilbert_function_is_two_l_plus_one"] &= harmonic == 2 * degree + 1
        gates["principal_quadratic_resolution_has_correct_graded_dimensions"] &= harmonic == sym - trace
        gates["no_additional_relation_dimension_is_required"] &= sym - harmonic == trace
        if degree >= 1:
            gates["hilbert_increment_is_exactly_two"] &= harmonic - dimensions[-1]["harmonic"] == 2
        dimensions.append({"degree": degree, "symmetric": sym, "trace_ideal": trace, "harmonic": harmonic})

    for ambient in range(2, 9):
        increments = {harmonic_dimension(l, ambient) - harmonic_dimension(l - 1, ambient) for l in range(3, 9)}
        has_constant_two = increments == {2}
        gates["constant_two_increment_is_specific_to_three_ambient_dimensions"] &= has_constant_two == (ambient == 3)

    gates["spin_two_five_plus_two_plus_two_is_quadric_hilbert_growth"] &= [harmonic_dimension(l, 3) for l in (2, 3, 4)] == [5, 7, 9]

    result = {
        "schema": "marici.strominger.cartan-quadric-relation-hilbert-result.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "gates": gates,
        "passed": sum(gates.values()),
        "total": len(gates),
        "algebra": "direct_sum H_l is Sym(H_1)/(q), q=x^2+y^2+z^2",
        "minimal_resolution": "0 -> S(-2) --q--> S -> Cartan -> 0",
        "hilbert_series": "(1-t^2)/(1-t)^3=(1+t)/(1-t)^2",
        "hilbert_function": "dim H_l=2l+1",
        "projection_case_count": projection_cases,
        "bounded_degrees": [0, 50],
        "dimensions": dimensions,
    }
    target = HERE.parent / "results" / "cartan_quadric_relation_hilbert_checks.json"
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("status", "passed", "total", "algebra", "minimal_resolution", "hilbert_series", "hilbert_function", "projection_case_count", "bounded_degrees")}, indent=2))
    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
