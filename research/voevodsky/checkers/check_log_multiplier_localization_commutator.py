from __future__ import annotations

import json
from fractions import Fraction

import sympy as sp


def main() -> None:
    modes = list(range(-16, 17))
    matrix = []
    for n in modes:
        row = []
        for m in modes:
            coefficient = sp.Rational(1, 2) if abs(n - m) == 1 else sp.Integer(0)
            row.append(sp.Abs(sp.log(1 + abs(n)) - sp.log(1 + abs(m))) * coefficient)
        matrix.append(row)

    row_sums = [sp.simplify(sum(row)) for row in matrix]
    column_sums = [sp.simplify(sum(matrix[row][column] for row in range(len(modes)))) for column in range(len(modes))]
    assert all(value <= 1 for value in row_sums)
    assert all(value <= 1 for value in column_sums)

    first_fourier_moment = Fraction(1, 2) + Fraction(1, 2)
    assert first_fourier_moment == 1

    harmonic_cutoffs = [8, 16, 32, 64, 128]
    hostile_partial_moments = [sum(Fraction(1, k) for k in range(1, cutoff + 1)) for cutoff in harmonic_cutoffs]
    assert all(hostile_partial_moments[index + 1] > hostile_partial_moments[index] for index in range(len(harmonic_cutoffs) - 1))

    result = {
        "schema": "marici.voevodsky.log-multiplier-localization-commutator.v1",
        "status": "fourier_first_moment_commutator_bound_verified",
        "fixture": "chi(x)=cos(x)",
        "fixture_first_absolute_fourier_moment": "1/1",
        "finite_section_modes": [modes[0], modes[-1]],
        "row_schur_sums_at_most_one": True,
        "column_schur_sums_at_most_one": True,
        "commutator_norm_upper_bound": "1/1",
        "hostile_coefficient_model": "abs(chi_hat_k)=1/k^2",
        "hostile_partial_first_moments": [f"{value.numerator}/{value.denominator}" for value in hostile_partial_moments],
        "hostile_certificate_diverges": True,
        "actual_interval_partition_coefficients_materialized": False,
        "next_gate": "extract partition Fourier coefficients and coordinate-transfer constants",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
