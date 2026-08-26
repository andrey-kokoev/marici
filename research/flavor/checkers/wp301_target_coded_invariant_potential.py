"""WP301: exact authority audit for a convex invariant selector potential."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def stationary_point(hessian, linear_source):
    return hessian.inv() * linear_source


def potential(hessian, linear_source, point):
    return sp.simplify((point.T * hessian * point)[0] / 2 - (linear_source.T * point)[0])


def main():
    hessian = sp.diag(2, 3)
    target_a = sp.Matrix([1, 2])
    target_b = sp.Matrix([2, 1])
    source_a = hessian * target_a
    source_b = hessian * target_b
    selected_a = stationary_point(hessian, source_a)
    selected_b = stationary_point(hessian, source_b)
    x1, x2 = sp.symbols("x1 x2", real=True)
    point = sp.Matrix([x1, x2])
    gradient_a = sp.Matrix([sp.diff(potential(hessian, source_a, point), variable) for variable in (x1, x2)])
    displacement = point - selected_a
    completion_identity = sp.simplify(
        potential(hessian, source_a, point)
        - potential(hessian, source_a, selected_a)
        - (displacement.T * hessian * displacement)[0] / 2
    )

    checks = {
        "hessian_is_positive_definite": all(value > 0 for value in hessian.eigenvals()),
        "first_stationary_point_equals_encoded_target": selected_a == target_a,
        "second_stationary_point_equals_encoded_target": selected_b == target_b,
        "same_quadratic_architecture_selects_different_points": selected_a != selected_b,
        "linear_source_is_exactly_hessian_times_target": source_a == hessian * target_a and source_b == hessian * target_b,
        "gradient_vanishes_at_first_target": gradient_a.subs({x1: target_a[0], x2: target_a[1]}) == sp.zeros(2, 1),
        "completion_of_square_proves_unique_global_minimum": completion_identity == 0,
        "zero_linear_source_selects_only_origin": stationary_point(hessian, sp.zeros(2, 1)) == sp.zeros(2, 1),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP301",
        "theorem_domain": "two weak-basis-invariant local physical16 coordinates with convex quadratic source action V(x)=x^T A x/2-b^T x and positive-definite A",
        "selector_formula": "x_star=A^{-1}b",
        "authority_identity": "b=A*x_star",
        "shared_architecture": {"A": [[str(value) for value in hessian.row(i)] for i in range(2)]},
        "rival_sources": [
            {"b": [str(value) for value in source_a], "selected_point": [str(value) for value in selected_a]},
            {"b": [str(value) for value in source_b], "selected_point": [str(value) for value in selected_b]},
        ],
        "descent": "conditional: if x consists of declared weak-basis invariants, V is a quotient function; this does not authorize its coefficients",
        "classification": "genuine convex point selector only conditional on independent source authority for A and b; otherwise the numerical target is encoded in b",
        "smallest_exact_falsifier": "the same A=diag(2,3) selects (1,2) for b=(2,6) and (2,1) for b=(4,3)",
        "anti_circularity_gate": "derive b from source fields, symmetry, normalization, and matching before consulting the fitted physical16 point",
        "remaining_physical_instrument_gate": "construct a UV source whose invariant effective action produces A and b independently, certify stability and RG/threshold transport, and measure relaxation into the predicted physical16 image",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp301_target_coded_invariant_potential.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
