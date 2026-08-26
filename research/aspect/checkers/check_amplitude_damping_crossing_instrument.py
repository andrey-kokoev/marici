from __future__ import annotations

import json
from pathlib import Path

from sympy import Rational as Q
from sympy import simplify, sqrt


def records(alpha_squared, beta_squared, p):
    b = p * (1 - p) * beta_squared
    c = b
    z = (1 - p) * sqrt(alpha_squared * beta_squared)
    return b, c, z


def delta(alpha_squared, beta_squared, p):
    b, c, z = records(alpha_squared, beta_squared, p)
    return simplify(z**2 - b * c)


def npt_lower(b, c, z, population_radius, quadrature_radius):
    return simplify((z - quadrature_radius) ** 2 - (b + population_radius) * (c + population_radius))


def ppt_upper(b, c, z, population_radius, quadrature_radius):
    return simplify((z + quadrature_radius) ** 2 - (b - population_radius) * (c - population_radius))


def main() -> None:
    theta_1 = (Q(1, 4), Q(3, 4))
    theta_2 = (Q(3, 4), Q(1, 4))
    population_radius = Q(1, 1000)
    quadrature_radius = Q(1, 200)

    p_crossing_squared = simplify(theta_1[0] / theta_1[1])
    assert p_crossing_squared == Q(1, 3)
    assert simplify(delta(*theta_1, 1 / sqrt(3))) == 0

    below, above = Q(1, 2), Q(2, 3)
    theta_1_below = delta(*theta_1, below)
    theta_1_above = delta(*theta_1, above)
    assert theta_1_below == Q(3, 256)
    assert theta_1_above == Q(-1, 144)

    b_below, c_below, z_below = records(*theta_1, below)
    b_above, c_above, z_above = records(*theta_1, above)
    below_safe_lower = npt_lower(
        b_below, c_below, z_below, population_radius, quadrature_radius
    )
    above_safe_upper = ppt_upper(
        b_above, c_above, z_above, population_radius, quadrature_radius
    )
    assert below_safe_lower > 0
    assert above_safe_upper < 0

    # The swapped equal-concurrence control has its formal zero at p=sqrt(3),
    # outside the physical damping interval. It remains NPT for every p<1.
    theta_2_formal_crossing_squared = simplify(theta_2[0] / theta_2[1])
    assert theta_2_formal_crossing_squared == 3
    p_control = Q(9, 10)
    theta_2_control_delta = delta(*theta_2, p_control)
    b_control, c_control, z_control = records(*theta_2, p_control)
    control_safe_lower = npt_lower(
        b_control, c_control, z_control, population_radius, quadrature_radius
    )
    assert theta_2_control_delta > 0
    assert control_safe_lower > 0

    # Near complete damping, the control is still mathematically NPT but this
    # frozen instrument becomes inconclusive as the signal vanishes.
    p_near_endpoint = Q(99, 100)
    b_endpoint, c_endpoint, z_endpoint = records(*theta_2, p_near_endpoint)
    endpoint_delta = delta(*theta_2, p_near_endpoint)
    endpoint_safe_lower = npt_lower(
        b_endpoint, c_endpoint, z_endpoint, population_radius, quadrature_radius
    )
    assert endpoint_delta > 0
    assert endpoint_safe_lower < 0

    result = {
        "schema": "marici.aspect.amplitude-damping-crossing-instrument.v1",
        "status": "pass",
        "source_formula": "Delta=(1-p)^2 |beta|^2 (|alpha|^2-p^2|beta|^2)",
        "theta_1_weights": [str(value) for value in theta_1],
        "theta_1_crossing": "1/sqrt(3)",
        "theta_1_below": {
            "p": str(below),
            "exact_delta": str(theta_1_below),
            "safe_npt_lower": str(below_safe_lower),
        },
        "theta_1_above": {
            "p": str(above),
            "exact_delta": str(theta_1_above),
            "safe_ppt_upper": str(above_safe_upper),
        },
        "theta_2_weights": [str(value) for value in theta_2],
        "theta_2_formal_crossing": "sqrt(3), outside physical p interval",
        "theta_2_control": {
            "p": str(p_control),
            "exact_delta": str(theta_2_control_delta),
            "safe_npt_lower": str(control_safe_lower),
        },
        "theta_2_near_endpoint": {
            "p": str(p_near_endpoint),
            "exact_delta_positive": True,
            "safe_lower": str(endpoint_safe_lower),
            "instrument_inconclusive": True,
        },
        "population_radius": str(population_radius),
        "quadrature_radius": str(quadrature_radius),
        "verdict": "The calibrated determinant instrument resolves the source-predicted Theta_1 crossing at frozen bracketing points and distinguishes the Theta_2 no-finite-crossing control until endpoint signal loss overwhelms calibration.",
        "claim_boundary": "source-derived dual local amplitude-damping law; exact state family; deterministic calibration box; no fitted trajectory or differential phase-drift repair",
    }
    output = Path(__file__).parents[1] / "results" / "amplitude_damping_crossing_instrument.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
