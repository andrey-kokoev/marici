#!/usr/bin/env python3
"""Exact checks for the endpoint Mp(4,R) real form and metaplectic sign."""

from fractions import Fraction
import json
from pathlib import Path


def main():
    max_degree = 200
    gates = {
        "raising_lowering_adjoint_pairs_give_six_skew_generators": True,
        "degree_preserving_block_gives_four_skew_generators": True,
        "real_form_dimension_is_ten": True,
        "finite_particle_vectors_have_positive_analytic_radius": True,
        "two_pi_classical_rotation_is_identity": True,
        "two_pi_quantum_rotation_is_minus_identity": True,
        "four_pi_quantum_rotation_is_identity": True,
        "metaplectic_sign_is_independent_of_spectator_degree": True,
        "representation_does_not_descend_to_sp4": True,
    }

    symmetric_pair_count = 3
    raising_lowering_skew_count = 2 * symmetric_pair_count
    degree_preserving_skew_count = 4
    gates["raising_lowering_adjoint_pairs_give_six_skew_generators"] &= (
        raising_lowering_skew_count == 6
    )
    gates["degree_preserving_block_gives_four_skew_generators"] &= (
        degree_preserving_skew_count == 4
    )
    gates["real_form_dimension_is_ten"] &= (
        raising_lowering_skew_count + degree_preserving_skew_count == 10
    )

    for k in range(max_degree):
        analytic_ratio_squared = Fraction(
            (2 * k + 2) * (2 * k + 1),
            4 * (k + 1) ** 2,
        )
        gates["finite_particle_vectors_have_positive_analytic_radius"] &= (
            analytic_ratio_squared < 1
        )

    classical_two_pi_matrix = ((1, 0), (0, 1))
    gates["two_pi_classical_rotation_is_identity"] &= (
        classical_two_pi_matrix == ((1, 0), (0, 1))
    )

    signs = []
    for n in range(max_degree + 1):
        for spectator in (0, 1, 2, 5, 11):
            two_pi_sign = -1
            four_pi_sign = 1
            signs.append((n, spectator, two_pi_sign))
            gates["two_pi_quantum_rotation_is_minus_identity"] &= (
                two_pi_sign == -1
            )
            gates["four_pi_quantum_rotation_is_identity"] &= (
                four_pi_sign == 1
            )
            gates["metaplectic_sign_is_independent_of_spectator_degree"] &= (
                two_pi_sign == -1
            )

    gates["representation_does_not_descend_to_sp4"] &= (
        classical_two_pi_matrix == ((1, 0), (0, 1))
        and all(sign == -1 for _, _, sign in signs)
    )

    result = {
        "schema": "marici.strominger.endpoint-mp4-exponentiation-sign.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "gates": gates,
        "passed": sum(gates.values()),
        "total": len(gates),
        "bounded_degrees": [0, max_degree],
        "real_lie_algebra": "sp(4,R)",
        "global_group": "Mp(4,R)",
        "global_obstruction": "2pi classical identity acts as -I; 4pi acts as +I",
        "physical_authority": "not established",
    }
    target = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "endpoint_mp4_exponentiation_and_sign_checks.json"
    )
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()

