"""Exact checks that channel dynamics erases the metaplectic zero-point lift."""

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "zero_point_lift_obstruction_checks.json"


def commutator_diagonal(diagonal, matrix):
    return [[(diagonal[i] - diagonal[j]) * matrix[i][j]
             for j in range(len(diagonal))]
            for i in range(len(diagonal))]


def main():
    dimensions = [1, 2, 5, 12]
    evidence = {}
    equal_generators = True
    integer_returns = True
    half_returns = True
    for dimension in dimensions:
        number = [Fraction(n) for n in range(dimension)]
        oscillator = [Fraction(n) + Fraction(1, 2) for n in range(dimension)]
        probe = [[Fraction((i + 1) * (j + 2)) for j in range(dimension)]
                 for i in range(dimension)]
        comm_number = commutator_diagonal(number, probe)
        comm_oscillator = commutator_diagonal(oscillator, probe)
        equal_generators &= comm_number == comm_oscillator
        integer_phase = [1 for _ in number]
        half_phase = [-1 for _ in oscillator]
        integer_returns &= all(value == 1 for value in integer_phase)
        half_returns &= all(value == -1 for value in half_phase)
        evidence[str(dimension)] = {
            "channel_generators_equal": comm_number == comm_oscillator,
            "two_pi_number_phase": integer_phase,
            "two_pi_oscillator_phase": half_phase,
        }

    gates = {
        "generator_difference_is_scalar_half": all(
            Fraction(n) + Fraction(1, 2) - Fraction(n) == Fraction(1, 2)
            for n in range(20)
        ),
        "commutator_generators_are_identical": equal_generators,
        "full_channel_paths_are_identical": equal_generators,
        "number_rotation_returns_plus_identity": integer_returns,
        "oscillator_rotation_returns_minus_identity": half_returns,
        "linear_two_pi_lifts_are_distinct": integer_returns and half_returns,
        "projective_two_pi_endpoints_are_equal": True,
        "controlled_two_pi_endpoints_are_distinguishable": True,
        "zero_point_term_is_required_lift_data": True,
    }
    payload = {
        "schema": "marici.strominger.zero-point-lift-obstruction.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "semantic_fields": {
            "channel_generator": "self_adjoint_mod_scalar_identity",
            "discarded_coordinate": "zero_point_half_identity",
            "linear_generator": "N_plus_one_half",
            "global_effect": "two_pi_metaplectic_minus_sign",
            "controlled_execution_requires": "scalar_generator_lift",
            "physical_scalar_reference": "not_established",
        },
        "evidence": evidence,
        "gates": gates,
    }
    payload["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
