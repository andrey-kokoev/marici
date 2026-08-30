#!/usr/bin/env python3
"""Exact checks for the endpoint dagger-curvature spectral law."""

from fractions import Fraction
import json
from pathlib import Path


def main():
    max_grade = 200
    gates = {
        "defect_recovers_grade": True,
        "multiplicity_is_two_l_plus_one": True,
        "cumulative_multiplicity_is_square": True,
        "threshold_counting_law_is_exact": True,
        "defect_eigenvalues_strictly_decay": True,
        "reciprocal_is_order_one_grade_operator": True,
        "critical_power_has_harmonic_growth": True,
        "supercritical_power_has_decaying_tail": True,
    }

    cumulative = 0
    previous = None
    cases = []
    for l in range(max_grade + 1):
        n = l + 1
        defect = Fraction(2, n)
        multiplicity = 2 * l + 1
        recovered_grade = Fraction(2, 1) / defect - 1
        reciprocal = Fraction(1, 1) / defect

        gates["defect_recovers_grade"] &= recovered_grade == l
        gates["multiplicity_is_two_l_plus_one"] &= multiplicity == 2 * n - 1
        cumulative += multiplicity
        gates["cumulative_multiplicity_is_square"] &= cumulative == n * n
        gates["reciprocal_is_order_one_grade_operator"] &= reciprocal == Fraction(n, 2)
        if previous is not None:
            gates["defect_eigenvalues_strictly_decay"] &= defect < previous
        previous = defect

        critical_term = multiplicity * defect * defect
        gates["critical_power_has_harmonic_growth"] &= (
            critical_term >= Fraction(4, n)
            and critical_term <= Fraction(8, n)
        )
        cubic_term = multiplicity * defect * defect * defect
        gates["supercritical_power_has_decaying_tail"] &= (
            cubic_term <= Fraction(16, n * n)
        )

        if l in (0, 1, 2, 4, 9, 24, 49, 99, 199):
            cases.append(
                {
                    "grade": l,
                    "defect": [defect.numerator, defect.denominator],
                    "multiplicity": multiplicity,
                    "cumulative_count": cumulative,
                    "reciprocal": [reciprocal.numerator, reciprocal.denominator],
                }
            )

    for denominator in range(1, 101):
        epsilon = Fraction(2, denominator)
        counted = sum(
            2 * l + 1
            for l in range(max_grade + 1)
            if Fraction(2, l + 1) >= epsilon
        )
        gates["threshold_counting_law_is_exact"] &= counted == denominator * denominator

    result = {
        "schema": "marici.strominger.endpoint-dagger-spectral-dimension.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "gates": gates,
        "passed": sum(gates.values()),
        "total": len(gates),
        "bounded_grades": [0, max_grade],
        "spectral_law": "delta_l=2/(l+1), multiplicity=2l+1",
        "counting_law": "N_delta(epsilon)=floor(2/epsilon)^2",
        "schatten_threshold": "p>2",
        "cases": cases,
    }
    target = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "endpoint_dagger_spectral_dimension_checks.json"
    )
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(
        json.dumps(
            {
                key: result[key]
                for key in (
                    "status",
                    "passed",
                    "total",
                    "bounded_grades",
                    "spectral_law",
                    "counting_law",
                    "schatten_threshold",
                )
            },
            indent=2,
        )
    )
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()

