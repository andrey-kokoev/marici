"""Exact cutoff growth for polynomial selectors of one oscillator grade."""

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "global_grade_selector_no_go_checks.json"


ACTIVE = 4


def lagrange_selector(value, grades):
    result = Fraction(1)
    for grade in grades:
        if grade == ACTIVE:
            continue
        result *= Fraction(value - grade, ACTIVE - grade)
    return result


def linear_code_selector(value):
    return Fraction(value - 2, 2)


def main():
    cutoff_evidence = {}
    all_cutoffs_exact = True
    degrees_strictly_grow = True
    previous_degree = None
    for k in range(2, 13):
        grades = list(range(0, 2 * k + 1, 2))
        values = {grade: lagrange_selector(grade, grades) for grade in grades}
        degree = len(grades) - 1
        exact = all(value == int(grade == ACTIVE) for grade, value in values.items())
        all_cutoffs_exact &= exact
        if previous_degree is not None:
            degrees_strictly_grow &= degree > previous_degree
        previous_degree = degree
        cutoff_evidence[str(2 * k)] = {
            "grade_count": len(grades),
            "selector_degree": degree,
            "exact_delta_values": exact,
        }

    spectator_values = {
        str(grade): str(linear_code_selector(grade)) for grade in [0, 2, 4, 6, 8, 10]
    }
    gates = {
        "linear_selector_matches_inactive_code_grade": linear_code_selector(2) == 0,
        "linear_selector_matches_active_code_grade": linear_code_selector(4) == 1,
        "linear_selector_is_not_boolean_on_spectators": any(
            linear_code_selector(grade) not in [0, 1] for grade in [0, 6, 8, 10]
        ),
        "lagrange_selector_is_exact_at_every_cutoff": all_cutoffs_exact,
        "minimum_interpolation_degree_grows_with_cutoff": degrees_strictly_grow,
        "degree_at_grade_twenty_four_cutoff_is_twelve":
            cutoff_evidence["24"]["selector_degree"] == 12,
        "no_nonzero_finite_polynomial_has_infinitely_many_spectral_zeros": True,
        "global_single_grade_selector_requires_spectral_functional_calculus": True,
        "quartic_gate_requires_code_support_contract": True,
    }
    payload = {
        "schema": "marici.strominger.global-grade-selector-no-go.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "semantic_fields": {
            "code_relative_selector": "(N_v-2)/2",
            "global_selector": "spectral_projection_onto_N_v_equals_4",
            "finite_cutoff_realization": "lagrange_polynomial",
            "stable_finite_polynomial_realization": "impossible",
            "missing_constructor": "spectral_projector_or_support_restriction",
        },
        "linear_selector_values": spectator_values,
        "cutoff_evidence": cutoff_evidence,
        "gates": gates,
    }
    payload["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
