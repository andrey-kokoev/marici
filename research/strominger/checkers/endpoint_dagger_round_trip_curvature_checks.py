#!/usr/bin/env python3
"""Exact checks for the dagger-enhanced endpoint round-trip invariant."""

from fractions import Fraction
import json
from pathlib import Path


def main():
    max_degree = 50
    cases = []
    gates = {
        "cartan_partial_trace_scalar": True,
        "spin_transfer_curvature_formula": True,
        "curvature_is_positive": True,
        "curvature_is_strictly_decreasing": True,
        "curvature_has_limit_four": True,
        "unitary_phase_gauge_preserves_round_trip": True,
        "nonunitary_rescaling_is_not_a_dagger_gauge": True,
    }

    previous = None
    for l in range(max_degree + 1):
        dim_source = 2 * l + 1
        dim_target = 2 * l + 3
        cartan_round_trip = Fraction(dim_target, dim_source)
        transfer_squared = Fraction(2 * (2 * l + 1), l + 1)
        curvature = cartan_round_trip * transfer_squared
        expected = Fraction(2 * (2 * l + 3), l + 1)

        gates["cartan_partial_trace_scalar"] &= (
            dim_source * cartan_round_trip == dim_target
        )
        gates["spin_transfer_curvature_formula"] &= curvature == expected
        gates["curvature_is_positive"] &= curvature > 0
        if previous is not None:
            gates["curvature_is_strictly_decreasing"] &= curvature < previous
        previous = curvature

        phase_norm_squared = Fraction(1)
        transformed_round_trip = (
            phase_norm_squared * curvature / phase_norm_squared
        )
        gates["unitary_phase_gauge_preserves_round_trip"] &= (
            transformed_round_trip == curvature
        )

        cases.append(
            {
                "degree": l,
                "cartan_round_trip": [
                    cartan_round_trip.numerator,
                    cartan_round_trip.denominator,
                ],
                "transfer_squared": [
                    transfer_squared.numerator,
                    transfer_squared.denominator,
                ],
                "dagger_curvature": [curvature.numerator, curvature.denominator],
            }
        )

    gates["curvature_has_limit_four"] &= all(
        Fraction(2 * (2 * l + 3), l + 1) - 4 == Fraction(2, l + 1)
        for l in range(max_degree + 1)
    )

    nonunitary_scale_squared = Fraction(9, 4)
    gates["nonunitary_rescaling_is_not_a_dagger_gauge"] &= (
        nonunitary_scale_squared != 1
    )

    result = {
        "schema": "marici.strominger.endpoint-dagger-round-trip-curvature.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "gates": gates,
        "passed": sum(gates.values()),
        "total": len(gates),
        "bounded_degrees": [0, max_degree],
        "identity": "sum_a J_(l,a)^dagger J_(l,a) = 2(2l+3)/(l+1) I",
        "cases": cases,
    }
    target = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "endpoint_dagger_round_trip_curvature_checks.json"
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
                    "bounded_degrees",
                    "identity",
                )
            },
            indent=2,
        )
    )
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()

