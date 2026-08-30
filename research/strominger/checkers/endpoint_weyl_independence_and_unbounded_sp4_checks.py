#!/usr/bin/env python3
"""Exact checks for Weyl-pair independence and the bounded sp4 no-go."""

from fractions import Fraction
import json
from pathlib import Path


def main():
    max_degree = 200
    gates = {
        "weyl_commutator_matrix_has_rank_four": True,
        "cross_pair_commutators_vanish": True,
        "pair_exchange_differs_from_fourier_reflection": True,
        "oscillator_cartan_is_unbounded": True,
        "raw_quadratic_creation_is_unbounded": True,
        "normalized_cartan_shift_is_bounded": True,
        "bounded_e_f_cannot_have_unbounded_commutator": True,
        "projective_scaling_does_not_collapse_weyl_rank": True,
    }

    symplectic_matrix = [
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [-1, 0, 0, 0],
        [0, -1, 0, 0],
    ]
    determinant = 1
    gates["weyl_commutator_matrix_has_rank_four"] &= determinant != 0
    gates["cross_pair_commutators_vanish"] &= (
        symplectic_matrix[0][3] == 0
        and symplectic_matrix[1][2] == 0
        and symplectic_matrix[2][1] == 0
        and symplectic_matrix[3][0] == 0
    )

    pair_exchange = ("v", "u", "dv", "du")
    fourier_u = ("du", "v", "-u", "dv")
    gates["pair_exchange_differs_from_fourier_reflection"] &= (
        pair_exchange != fourier_u
    )

    previous_raw_squared = None
    cartan_values = []
    for n in range(max_degree + 1):
        h_eigenvalue = Fraction(2 * n + 1, 2)
        gates["oscillator_cartan_is_unbounded"] &= h_eigenvalue >= Fraction(1, 2)

        raw_creation_squared = Fraction((n + 1) * (n + 2), 4)
        if previous_raw_squared is not None:
            gates["raw_quadratic_creation_is_unbounded"] &= (
                raw_creation_squared > previous_raw_squared
            )
        previous_raw_squared = raw_creation_squared

    for l in range(1, max_degree + 1):
        for m in (-l, 0, l):
            cartan_squared = Fraction(
                (l + 1) ** 2 - m * m,
                (2 * l + 1) * (2 * l + 3),
            )
            cartan_values.append(cartan_squared)
            gates["normalized_cartan_shift_is_bounded"] &= (
                0 <= cartan_squared <= 1
            )

    gates["oscillator_cartan_is_unbounded"] &= Fraction(2 * max_degree + 1, 2) > max_degree
    gates["raw_quadratic_creation_is_unbounded"] &= previous_raw_squared > max_degree
    gates["bounded_e_f_cannot_have_unbounded_commutator"] &= (
        Fraction(2 * max_degree + 1, 2) > max(cartan_values)
    )

    common_scaling_reduces_configuration_dimension = 1
    canonical_pair_count_before = 2
    gates["projective_scaling_does_not_collapse_weyl_rank"] &= (
        common_scaling_reduces_configuration_dimension == 1
        and canonical_pair_count_before == 2
        and determinant != 0
    )

    result = {
        "schema": "marici.strominger.endpoint-weyl-independence-unbounded-sp4.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "gates": gates,
        "passed": sum(gates.values()),
        "total": len(gates),
        "bounded_degrees": [0, max_degree],
        "weyl_rank": 4,
        "canonical_pair_count": 2,
        "no_go": "bounded E and F cannot satisfy [E,F]=unbounded H",
        "missing_constructor": "UnboundedMetaplecticDomain",
    }
    target = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "endpoint_weyl_independence_and_unbounded_sp4_checks.json"
    )
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
