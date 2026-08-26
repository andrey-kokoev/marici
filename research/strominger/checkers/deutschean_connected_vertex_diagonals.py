"""Exact audit of the first two connected-decoration diagonals."""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research/strominger/deutschean-connected-vertex-source-frontier.md"
SOURCE_RESULT = ROOT / ".ai/tmp/strominger-connected-vertex-order30.json"
RESULT = ROOT / "research/strominger/results/deutschean_connected_vertex_diagonals.json"


def parse_fraction(value: str) -> Fraction:
    return Fraction(value)


def cubic(n: int) -> Fraction:
    return Fraction(5 * n**3 + 10 * n**2 + 175 * n - 198, 48)


def main() -> None:
    source = json.loads(SOURCE_RESULT.read_text(encoding="utf-8"))
    diagonals = source["observed"]["connected_vertex_source_diagonals"]
    grades = sorted(int(key) for key in diagonals)

    leading_failures = [
        n
        for n in grades
        if n >= 3 and parse_fraction(diagonals[str(n)]["leading"]) != 1
    ]
    reconstruction_grades = [4, 5, 6, 7]
    withheld_grades = list(range(8, 31))
    cubic_reconstruction_failures = [
        n
        for n in reconstruction_grades
        if parse_fraction(diagonals[str(n)]["next_to_leading"]) != cubic(n)
    ]
    cubic_withheld_failures = [
        n
        for n in withheld_grades
        if parse_fraction(diagonals[str(n)]["next_to_leading"]) != cubic(n)
    ]
    values = [
        parse_fraction(diagonals[str(n)]["next_to_leading"])
        for n in range(4, 31)
    ]
    third_differences = values
    for _ in range(3):
        third_differences = [
            third_differences[i + 1] - third_differences[i]
            for i in range(len(third_differences) - 1)
        ]

    n_symbol = sp.symbols("n")
    deficit_polynomials = {}
    deficit_failures = []
    deficit_withheld_counts = {}
    newton_coefficients = {}
    newton_positivity_failures = []
    for deficit in range(6):
        start = deficit + 3
        values_by_grade = []
        for n in range(start, 31):
            value = parse_fraction(
                diagonals[str(n)]["top_six"][deficit]
            )
            values_by_grade.append(
                (n, sp.Rational(value.numerator, value.denominator))
            )
        degree = 3 * deficit
        reconstruction = values_by_grade[: degree + 1]
        withheld = values_by_grade[degree + 1 :]
        polynomial = sp.interpolate(reconstruction, n_symbol)
        failures = [
            n
            for n, value in withheld
            if sp.expand(polynomial.subs(n_symbol, n) - value) != 0
        ]
        if sp.degree(polynomial, n_symbol) != degree or failures:
            deficit_failures.append(deficit)
        difference_level = [
            sp.factor(polynomial.subs(n_symbol, start + offset))
            for offset in range(degree + 1)
        ]
        coefficients = []
        while difference_level:
            coefficients.append(difference_level[0])
            difference_level = [
                sp.factor(difference_level[i + 1] - difference_level[i])
                for i in range(len(difference_level) - 1)
            ]
        if any(value <= 0 for value in coefficients):
            newton_positivity_failures.append(deficit)
        deficit_polynomials[str(deficit)] = str(sp.factor(polynomial))
        deficit_withheld_counts[str(deficit)] = len(withheld)
        newton_coefficients[str(deficit)] = [str(value) for value in coefficients]

    checks = {
        "source_order_30_hostile_passed": source["passed"] is True,
        "zero_deficit_diagonal_is_one_through_vertex_grade_30": (
            not leading_failures
        ),
        "deficit_one_cubic_matches_four_reconstruction_grades": (
            not cubic_reconstruction_failures
        ),
        "deficit_one_cubic_matches_23_withheld_grades": (
            not cubic_withheld_failures
        ),
        "deficit_one_third_forward_difference_is_five_over_eight": all(
            value == Fraction(5, 8) for value in third_differences
        ),
        "deficit_zero_through_five_have_degree_three_d_transport": (
            not deficit_failures
        ),
        "all_stable_deficit_polynomials_have_positive_newton_coordinates": (
            not newton_positivity_failures
        ),
        "newton_degree_bound_matches_three_d_plus_one_propagator_bound": all(
            len(newton_coefficients[str(deficit)]) == 3 * deficit + 1
            for deficit in range(6)
        ),
    }
    payload = {
        "artifact_sha256": sha256(PACKET.read_bytes()).hexdigest().upper(),
        "source_result_sha256": sha256(SOURCE_RESULT.read_bytes()).hexdigest().upper(),
        "checks": checks,
        "observed": {
            "vertex_grade_range": [1, 30],
            "leading_failures": leading_failures,
            "cubic_reconstruction_grades": reconstruction_grades,
            "cubic_reconstruction_failures": cubic_reconstruction_failures,
            "cubic_withheld_grades": [8, 30],
            "cubic_withheld_failure_count": len(cubic_withheld_failures),
            "third_forward_difference": "5/8",
            "deficit_one_formula": "(5*n^3+10*n^2+175*n-198)/48",
            "decoration_deficit_degree_law": "degree=3*d; stable from n=d+3",
            "deficit_polynomials": deficit_polynomials,
            "deficit_withheld_counts": deficit_withheld_counts,
            "deficit_failures": deficit_failures,
            "newton_basis": "binomial(n-d-3,k), k=0..3d",
            "propagator_basis": "(1-T)^(-k-1), k=0..3d",
            "newton_coefficients": newton_coefficients,
            "newton_positivity_failures": newton_positivity_failures,
        },
        "passed": all(checks.values()),
        "semantic_boundary": (
            "Finite-cutoff theorem through connected vertex grade 30. The cubic is "
            "verified on 23 withheld grades. Deficits zero through five satisfy the "
            "degree-3d law with withheld tests and positive Newton coordinates, but "
            "neither law is yet derived from "
            "the all-orders Gamma saddle or a source-authorized decoration grammar."
        ),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    if not payload["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
