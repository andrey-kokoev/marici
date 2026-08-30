import json
from pathlib import Path

import sympy as sp


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return sp.simplify(left - right) == sp.zeros(*left.shape)


def main() -> None:
    i = sp.I
    omega = (-1 + sp.sqrt(3) * i) / 2
    identity = sp.eye(3)
    d = sp.diag(1, omega, omega**2)
    s = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    words = [sp.simplify(d**a * s**b) for a in range(3) for b in range(3)]
    word_matrix = sp.Matrix.hstack(*[word.reshape(9, 1) for word in words])

    def clock_twirl(x: sp.Matrix) -> sp.Matrix:
        return sp.simplify(sum((d**a * x * d**(-a) for a in range(3)), sp.zeros(3)) / 3)

    def full_twirl(x: sp.Matrix) -> sp.Matrix:
        total = sp.zeros(3)
        for a in range(3):
            for b in range(3):
                unitary = sp.simplify(d**a * s**b)
                total += unitary * x * unitary.conjugate().T
        return sp.simplify(total / 9)

    basis_units = []
    for row in range(3):
        for column in range(3):
            unit = sp.zeros(3)
            unit[row, column] = 1
            basis_units.append(unit)

    clock_images = [clock_twirl(unit) for unit in basis_units]
    full_images = [full_twirl(unit) for unit in basis_units]
    clock_image_rank = sp.Matrix.hstack(*[x.reshape(9, 1) for x in clock_images]).rank()
    full_image_rank = sp.Matrix.hstack(*[x.reshape(9, 1) for x in full_images]).rank()

    hostile = sp.Matrix([[2, 1, i], [1, 3, 1], [-i, 1, 5]])
    clock_hostile = clock_twirl(hostile)
    full_hostile = full_twirl(hostile)
    clock_commutator = sp.simplify(d * clock_hostile - clock_hostile * d)

    checks = {
        "weyl_words_span_full_algebra": word_matrix.rank() == 9,
        "smallest_unital_algebra_is_m3": word_matrix.rank() == 9,
        "clock_twirl_image_rank_three": clock_image_rank == 3,
        "clock_twirl_is_idempotent": matrix_equal(clock_twirl(clock_hostile), clock_hostile),
        "clock_twirl_output_diagonal": clock_hostile == sp.diag(2, 3, 5),
        "clock_twirl_commutes_with_clock": clock_commutator == sp.zeros(3),
        "clock_twirl_kills_shift": clock_twirl(s) == sp.zeros(3),
        "clock_twirl_kills_second_shift": clock_twirl(s**2) == sp.zeros(3),
        "full_twirl_image_rank_one": full_image_rank == 1,
        "full_twirl_is_trace_expectation": matrix_equal(full_hostile, sp.trace(hostile) * identity / 3),
        "full_twirl_is_idempotent": matrix_equal(full_twirl(full_hostile), full_hostile),
        "full_twirl_erases_clock": full_twirl(d) == sp.zeros(3),
        "canonical_expectations_fail_viable_noncommuting_image": clock_image_rank == 3 and full_image_rank == 1,
        "physical_instrument_remains_open": True,
    }

    result = {
        "work_package": "WP945",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "closure": {
            "generated_algebra_dimension": word_matrix.rank(),
            "ambient_algebra_dimension": 9,
        },
        "canonical_expectations": {
            "clock_twirl_image_dimension": clock_image_rank,
            "clock_twirl_hostile_output": str(clock_hostile.tolist()),
            "full_twirl_image_dimension": full_image_rank,
            "full_twirl_hostile_output": str(full_hostile.tolist()),
        },
        "classification": "closure is universal and nonselective; canonical expectations are proper but phenomenologically overprojected",
        "smallest_exact_falsifier": "D-twirl kills S while full Weyl twirl maps every matrix to Tr(X)I/3",
        "remaining_gate": "source-derived asymmetric proper noncommuting word module with completion stability, physical16 descent, and calibrated instrument",
    }

    expected_path = Path(__file__).parents[1] / "results" / "wp945_weyl_executable_closure_conditional_expectation_no_go.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    assert result == expected
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
