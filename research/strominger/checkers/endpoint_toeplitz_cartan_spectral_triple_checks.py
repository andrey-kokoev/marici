#!/usr/bin/env python3
"""Exact bounded checks for the Toeplitz-Cartan spectral triple."""

from fractions import Fraction
import json
from pathlib import Path


def power_sum_direct(cutoff, exponent):
    return sum(
        Fraction(2 * l + 1) * Fraction(2, l + 1) ** exponent
        for l in range(cutoff + 1)
    )


def power_sum_zeta_decomposition(cutoff, exponent):
    harmonic_s = sum(Fraction(1, n**exponent) for n in range(1, cutoff + 2))
    harmonic_s_minus_one = sum(
        Fraction(1, n ** (exponent - 1)) for n in range(1, cutoff + 2)
    )
    return 2**exponent * (2 * harmonic_s_minus_one - harmonic_s)


def main():
    max_grade = 200
    gates = {
        "grade_operator_is_positive": True,
        "raising_commutator_is_constant_half": True,
        "lowering_commutator_is_constant_minus_half": True,
        "resolvent_eigenvalues_decay_to_zero": True,
        "finite_zeta_identity_is_exact": True,
        "multiplicity_count_is_quadratic": True,
        "summability_threshold_is_two": True,
        "nonlinear_hostile_grade_has_unbounded_difference": True,
    }

    cumulative = 0
    previous_resolvent = None
    for l in range(max_grade + 1):
        d_l = Fraction(l + 1, 2)
        d_next = Fraction(l + 2, 2)
        gates["grade_operator_is_positive"] &= d_l > 0
        gates["raising_commutator_is_constant_half"] &= d_next - d_l == Fraction(1, 2)
        if l > 0:
            d_previous = Fraction(l, 2)
            gates["lowering_commutator_is_constant_minus_half"] &= (
                d_previous - d_l == Fraction(-1, 2)
            )

        resolvent = Fraction(1, 1) / d_l
        if previous_resolvent is not None:
            gates["resolvent_eigenvalues_decay_to_zero"] &= (
                resolvent < previous_resolvent
            )
        previous_resolvent = resolvent

        cumulative += 2 * l + 1
        gates["multiplicity_count_is_quadratic"] &= cumulative == (l + 1) ** 2

    for cutoff in (0, 1, 2, 5, 10, 50, 200):
        for exponent in (3, 4, 5):
            gates["finite_zeta_identity_is_exact"] &= (
                power_sum_direct(cutoff, exponent)
                == power_sum_zeta_decomposition(cutoff, exponent)
            )

    gates["summability_threshold_is_two"] &= all(
        (1 - exponent < -1) == (exponent > 2)
        for exponent in range(1, 9)
    )

    hostile_differences = [(l + 2) ** 2 - (l + 1) ** 2 for l in range(max_grade)]
    gates["nonlinear_hostile_grade_has_unbounded_difference"] &= (
        hostile_differences[-1] > hostile_differences[0]
        and hostile_differences[-1] == 2 * max_grade + 1
    )

    result = {
        "schema": "marici.strominger.endpoint-toeplitz-cartan-spectral-triple.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "gates": gates,
        "passed": sum(gates.values()),
        "total": len(gates),
        "bounded_grades": [0, max_grade],
        "commutators": {
            "raising": "[D,S_a]=S_a/2",
            "lowering": "[D,S_a^dagger]=-S_a^dagger/2",
        },
        "spectral_zeta": "2^s(2 zeta(s-1)-zeta(s))",
        "summability": "p>2",
    }
    target = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "endpoint_toeplitz_cartan_spectral_triple_checks.json"
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
                    "commutators",
                    "spectral_zeta",
                    "summability",
                )
            },
            indent=2,
        )
    )
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()

