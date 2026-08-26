from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


def lower_square(estimate: F, radius: F) -> F:
    lower_magnitude = max(abs(estimate) - radius, F(0))
    return lower_magnitude**2


def determinant_lower(
    b_hat: F,
    c_hat: F,
    x_hat: F,
    y_hat: F,
    population_radius: F,
    quadrature_radius: F,
) -> F:
    return (
        lower_square(x_hat, quadrature_radius)
        + lower_square(y_hat, quadrature_radius)
        - (b_hat + population_radius) * (c_hat + population_radius)
    )


def main() -> None:
    correlation_radius = F(1, 100)
    population_radius = F(1, 1000)
    quadrature_radius = correlation_radius / 2
    assert quadrature_radius == F(1, 200)

    b, c = F(1, 100), F(9, 100)
    x, y = F(3, 100), F(4, 100)
    robust_lower = determinant_lower(
        b, c, x, y, population_radius, quadrature_radius
    )
    assert robust_lower == F(849, 1000000)
    assert robust_lower > 0

    # At a true boundary point, adversarial plug-in estimates can look NPT.
    boundary_b, boundary_c = F(1, 100), F(9, 100)
    boundary_x, boundary_y = F(3, 100), F(0)
    assert boundary_x**2 + boundary_y**2 - boundary_b * boundary_c == 0
    b_hat = boundary_b - population_radius
    c_hat = boundary_c - population_radius
    x_hat = boundary_x + quadrature_radius
    y_hat = boundary_y + quadrature_radius
    naive_plugin = x_hat**2 + y_hat**2 - b_hat * c_hat
    safe_lower = determinant_lower(
        b_hat,
        c_hat,
        x_hat,
        y_hat,
        population_radius,
        quadrature_radius,
    )
    assert naive_plugin == F(449, 1000000)
    assert naive_plugin > 0
    assert safe_lower == 0

    # A common calibrated phase rotation preserves the exact determinant.
    rotated_x, rotated_y = -y, x
    assert x**2 + y**2 - b * c == rotated_x**2 + rotated_y**2 - b * c

    result = {
        "schema": "marici.aspect.robust-x-state-determinant-instrument.v1",
        "status": "pass",
        "correlation_radius_each_of_XX_YY_XY_YX": str(correlation_radius),
        "derived_quadrature_radius": str(quadrature_radius),
        "population_radius_each_of_b_c": str(population_radius),
        "certificate": "max(|x_hat|-r_z,0)^2 + max(|y_hat|-r_z,0)^2 - (b_hat+r_p)(c_hat+r_p)",
        "hostile_robust_lower": str(robust_lower),
        "boundary_naive_plugin": str(naive_plugin),
        "boundary_safe_lower": str(safe_lower),
        "common_phase_rotation_preserves_exact_residual": True,
        "verdict": "The one-sided interval certificate survives the asymmetric hostile and prevents a false NPT claim at the exact boundary.",
        "claim_boundary": "componentwise calibrated deterministic error box; no covariance gain, finite-count derivation, or phase-frame drift model",
    }
    output = Path(__file__).parents[1] / "results" / "robust_x_state_determinant_instrument.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
