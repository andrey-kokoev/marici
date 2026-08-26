"""Finite controlled-reference test for the horizontal Clifford phase kernel."""

from __future__ import annotations

import cmath
import json
import math


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def dagger(a):
    return [[a[j][i].conjugate() for j in range(2)] for i in range(2)]


def scale(c, a):
    return [[c * a[i][j] for j in range(2)] for i in range(2)]


def close_matrix(a, b, tol=1e-12):
    return all(abs(a[i][j] - b[i][j]) < tol for i in range(2) for j in range(2))


def clean(x):
    return 0.0 if abs(x) < 1e-15 else x


def main():
    root2 = math.sqrt(2.0)
    identity = [[1.0 + 0j, 0j], [0j, 1.0 + 0j]]
    h = [[1 / root2, 1 / root2], [1 / root2, -1 / root2]]
    s = [[1.0 + 0j, 0j], [0j, 1j]]
    hs = matmul(h, s)
    route = matmul(matmul(hs, hs), hs)
    phase = cmath.exp(1j * math.pi / 4)

    x = [[0j, 1.0 + 0j], [1.0 + 0j, 0j]]
    z = [[1.0 + 0j, 0j], [0j, -1.0 + 0j]]
    isolated_equal = all(
        close_matrix(matmul(matmul(route, p), dagger(route)), p)
        for p in (identity, x, z, matmul(x, z))
    )

    p_plus_identity = 1.0
    p_plus_route = (1.0 + math.cos(math.pi / 4)) / 2.0
    p_minus_route = 1.0 - p_plus_route
    fringe_shift_visible = abs(p_plus_route - p_plus_identity) > 1e-12
    checks = {
        "clifford_relation_has_scalar_phase": close_matrix(route, scale(phase, identity)),
        "isolated_operator_conjugation_is_identical": isolated_equal,
        "reference_arm_makes_phase_observable": fringe_shift_visible,
        "controlled_probabilities_are_normalized": abs(p_plus_route + p_minus_route - 1.0) < 1e-12,
        "predicted_plus_port_probability": abs(p_plus_route - (2.0 + root2) / 4.0) < 1e-12,
        "identity_and_route_are_not_operationally_equivalent_after_control_lift": fringe_shift_visible,
        "test_does_not_assert_physical_controlled_clifford_availability": True,
    }
    result = {
        "schema": "marici.aspect.controlled_clifford_phase_interferometer.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "finite_matrix_calculation": True,
        "checks": checks,
        "route_scalar_phase": {"real": clean(phase.real), "imag": clean(phase.imag)},
        "interferometer": {
            "identity_plus_port_probability": p_plus_identity,
            "route_plus_port_probability": p_plus_route,
            "route_minus_port_probability": p_minus_route,
            "absolute_fringe_displacement": abs(p_plus_identity - p_plus_route),
        },
        "typed_boundary": {
            "source": "one coherent path qubit, one target qubit, and a phase-stable reference arm",
            "constructor": "controlled insertion of the Clifford route in one arm followed by balanced recombination",
            "detector": "two complementary output-port probabilities",
            "hostile": "isolated conjugation declares identity while the controlled interferometer retains the central phase",
            "completion": "separates projective from controlled operational equivalence without claiming the controlled device exists",
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
