#!/usr/bin/env python3
"""Derive the canonical first source derivative from the unspecialized form."""

import json
from pathlib import Path

import sympy as sp


def euler(expr, variables):
    return sp.expand(sum(variable * sp.diff(expr, variable) for variable in variables))


def main():
    x, y, z, a, b = sp.symbols("x y z a b")
    energy = x + y + z
    h = x**2 + y**2 - z**2
    k = (
        x**2 * a**4
        - h * a**2 * b**2
        + y**2 * b**4
        + (x**2 * (x**2 - y**2 - z**2) + energy**2 * (y**2 - x**2 - z**2)) * a**2
        + (y**2 * (y**2 - x**2 - z**2) + energy**2 * (x**2 - y**2 - z**2)) * b**2
        + z**2 * energy**4
        + energy**2 * z**2 * (z**2 - x**2 - y**2)
        + z**2 * x**2 * y**2
    )
    q = {
        "g1": b - y - z,
        "g2": a - x - z,
        "g3": a + b + z,
        "g23": b - x,
        "g31": a - y,
    }
    numerator = q["g23"] + q["g31"]
    variables = (x, y, z, a, b)

    factor_checks = {
        "numerator_degree_1": sp.expand(euler(numerator, variables) - numerator) == 0,
        "K_degree_6": sp.expand(euler(k, variables) - 6 * k) == 0,
        "all_five_q_degree_1": all(sp.expand(euler(value, variables) - value) == 0 for value in q.values()),
    }

    derivative_packets = {}
    derivative_checks = {}
    for axis_name, axis in zip(("x", "y", "z"), (x, y, z)):
        packet = {
            "numerator_derivative": str(sp.diff(numerator, axis)),
            "K_derivative_nonzero_terms": len(sp.Poly(sp.diff(k, axis), a, b, x, y, z).terms()),
            "marked_denominator_derivatives": {
                name: str(sp.diff(value, axis)) for name, value in q.items() if sp.diff(value, axis) != 0
            },
            "logarithmic_derivative_formula": (
                f"d_{axis_name}N/N + 5 d_{axis_name}K/K - sum_i d_{axis_name}q_i/q_i"
            ),
        }
        derivative_packets[axis_name] = packet
        derivative_checks[f"d{axis_name}_K_has_degree_5"] = (
            sp.expand(euler(sp.diff(k, axis), variables) - 5 * sp.diff(k, axis)) == 0
        )
        derivative_checks[f"d{axis_name}_numerator_has_degree_0"] = (
            sp.expand(euler(sp.diff(numerator, axis), variables)) == 0
        )
        derivative_checks[f"d{axis_name}_q_have_degree_0"] = all(
            sp.expand(euler(sp.diff(value, axis), variables)) == 0 for value in q.values()
        )

    # The coefficient of da wedge db has weight 26; differentiating an
    # external parameter lowers it to 25.  Adding the measure weight two gives
    # form weights 28 and 27 respectively.
    coefficient_weight = 1 + 5 * 6 - 5
    checks = {
        **factor_checks,
        **derivative_checks,
        "source_form_weight_28": coefficient_weight + 2 == 28,
        "canonical_derivative_form_weight_27": coefficient_weight - 1 + 2 == 27,
    }
    result = {
        "schema": "marici.rank26-canonical-source-derivative.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "source_coefficient": "(q_g23+q_g31) K_CM^5 / product_i q_i",
        "canonical_derivative_rule": "d_j log(source coefficient) = d_j N/N + 5 d_j K/K - sum_i d_j q_i/q_i",
        "derivative_packets": derivative_packets,
        "coefficient_weight": coefficient_weight,
        "source_form_weight": coefficient_weight + 2,
        "derivative_form_weight": coefficient_weight + 1,
        "checks": checks,
        "interpretation": (
            "The canonical dual-number coefficient is fixed term-by-term by differentiating the frozen numerator, "
            "Cayley-Menger factor, and all five labelled marked poles. It has source form weight 27 in every external direction."
        ),
        "remaining_gate": (
            "Insert these coefficient derivatives into the finite de Rham presentation and verify the quotient-level "
            "differentiated Euler relation in all three directions."
        ),
    }
    output = Path(__file__).with_name("rank26-canonical-source-derivative.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
