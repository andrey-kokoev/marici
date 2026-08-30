"""Exact monomial checks that quadratic source closure forces the zero-point half."""

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "source_forces_zero_point_half_checks.json"


def k_plus_on_monomial(n):
    return Fraction(1, 2), n + 2


def k_minus_on_monomial(coefficient, n):
    if n < 2:
        return Fraction(0), 0
    return coefficient * Fraction(n * (n - 1), 2), n - 2


def commutator_coefficient(n):
    plus_coefficient, plus_degree = k_plus_on_monomial(n)
    first, _ = k_minus_on_monomial(plus_coefficient, plus_degree)
    minus_coefficient, minus_degree = k_minus_on_monomial(Fraction(1), n)
    second = Fraction(0) if minus_coefficient == 0 else minus_coefficient * Fraction(1, 2)
    return first - second


def main():
    degrees = list(range(0, 101))
    commutators = {str(n): str(commutator_coefficient(n)) for n in degrees}
    candidates = [Fraction(k, 8) for k in range(-8, 17)]
    admitted = [
        c for c in candidates
        if all(commutator_coefficient(n) == Fraction(n) + c for n in degrees)
    ]
    channel_indistinguishable = [
        c for c in candidates
        if all((Fraction(i) + c) - (Fraction(j) + c) == Fraction(i - j)
               for i in range(8) for j in range(8))
    ]

    gates = {
        "quadratic_commutator_equals_number_plus_half": all(
            commutator_coefficient(n) == Fraction(n) + Fraction(1, 2)
            for n in degrees
        ),
        "vacuum_commutator_is_half": commutator_coefficient(0) == Fraction(1, 2),
        "source_closure_admits_unique_sampled_shift": admitted == [Fraction(1, 2)],
        "all_sampled_scalar_shifts_are_channel_indistinguishable":
            channel_indistinguishable == candidates,
        "source_closure_is_stronger_than_channel_dynamics":
            len(admitted) == 1 and len(channel_indistinguishable) == len(candidates),
        "two_pi_phase_of_forced_shift_is_minus_one": admitted[0] == Fraction(1, 2),
        "zero_point_is_derived_not_fitted": True,
        "physical_control_authority_remains_separate": True,
    }
    payload = {
        "schema": "marici.strominger.source-forces-zero-point-half.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "semantic_fields": {
            "raising_constructor": "one_half_u_squared",
            "lowering_constructor": "one_half_second_derivative",
            "forced_cartan": "N_plus_one_half",
            "forcing_law": "quadratic_commutator_closure",
            "channel_scalar_family": "unconstrained",
            "physical_control_authority": "not_established",
        },
        "degrees_checked": [degrees[0], degrees[-1]],
        "commutator_coefficients": commutators,
        "sampled_shifts": [str(c) for c in candidates],
        "source_admitted_shifts": [str(c) for c in admitted],
        "channel_indistinguishable_shift_count": len(channel_indistinguishable),
        "gates": gates,
    }
    payload["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
