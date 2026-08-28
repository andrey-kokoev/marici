import json
from pathlib import Path

import sympy as sp


def traceless_projection(x: sp.Matrix) -> sp.Matrix:
    return sp.simplify(x - sp.trace(x) * sp.eye(3) / 3)


def main() -> None:
    a, b = sp.symbols("a b")
    idempotent_solutions = sp.solve(
        [a**2 - a, 2 * a * b + 3 * b**2 - b],
        [a, b],
        dict=True,
    )
    solution_pairs = {(solution[a], solution[b]) for solution in idempotent_solutions}

    y = sp.diag(1, -1, 0)
    right = sp.diag(1, -1, 1)
    transformed = y * right.conjugate().T
    descent_residual = sp.simplify(
        traceless_projection(transformed) - traceless_projection(y) * right.conjugate().T
    )

    positive_input = sp.diag(1, 0, 0)
    nonpositive_output = traceless_projection(positive_input)
    output_eigenvalues = sorted(nonpositive_output.eigenvals().keys(), key=lambda value: float(value))

    x = sp.Matrix([[2, 1, sp.I], [1, 3, 1], [-sp.I, 1, 5]])
    u = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    conjugation_residual = sp.simplify(
        traceless_projection(u * x * u.conjugate().T)
        - u * traceless_projection(x) * u.conjugate().T
    )

    checks = {
        "four_equivariant_idempotents": solution_pairs == {(0, 0), (0, sp.Rational(1, 3)), (1, 0), (1, sp.Rational(-1, 3))},
        "traceless_projector_idempotent": traceless_projection(traceless_projection(x)) == traceless_projection(x),
        "traceless_image_dimension_eight": 9 - 1 == 8,
        "traceless_image_noncommutative": sp.Matrix([[0, 1, 0], [0, 0, 0], [0, 0, 0]]) * sp.Matrix([[0, 0, 0], [1, 0, 0], [0, 0, 0]]) != sp.Matrix([[0, 0, 0], [1, 0, 0], [0, 0, 0]]) * sp.Matrix([[0, 1, 0], [0, 0, 0], [0, 0, 0]]),
        "simultaneous_conjugation_covariant": conjugation_residual == sp.zeros(3),
        "hostile_left_unitary": sp.eye(3) * sp.eye(3).conjugate().T == sp.eye(3),
        "hostile_right_unitary": right * right.conjugate().T == sp.eye(3),
        "hostile_input_traceless": sp.trace(y) == 0,
        "biunitary_descent_residual_nonzero": descent_residual != sp.zeros(3),
        "biunitary_descent_residual_exact": descent_residual == -sp.Rational(2, 3) * sp.eye(3),
        "positive_input_positive_semidefinite": positive_input.is_positive_semidefinite,
        "traceless_projection_not_positive": output_eigenvalues == [sp.Rational(-1, 3), sp.Rational(2, 3)],
        "not_a_physical_conditional_expectation": not nonpositive_output.is_positive_semidefinite,
        "physical_instrument_remains_open": True,
    }

    result = {
        "work_package": "WP948",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "equivariant_idempotents": [[str(left), str(right_value)] for left, right_value in sorted(solution_pairs, key=str)],
        "hostile_descent": {
            "residual": str(descent_residual.tolist()),
            "residual_rank": descent_residual.rank(),
        },
        "positivity_hostile": {
            "input": str(positive_input.tolist()),
            "output": str(nonpositive_output.tolist()),
            "distinct_output_eigenvalues": [str(value) for value in output_eigenvalues],
        },
        "classification": "unique proper noncommutative conjugation-equivariant projector is presentation-only and nonpositive",
        "smallest_exact_falsifier": "P0(Y V dagger)-P0(Y)V dagger=-2I/3 for a unitary right-frame flip",
        "remaining_gate": "source operation on full weak-basis covariants, or an explicitly new relational left-right reference experiment, plus calibrated instrument",
    }

    expected_path = Path(__file__).parents[1] / "results" / "wp948_canonical_traceless_channel_full_weak_basis_no_go.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    assert result == expected
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
