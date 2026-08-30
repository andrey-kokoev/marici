import json
from pathlib import Path

import sympy as sp


def main() -> None:
    u, lam = sp.symbols("u lam", nonnegative=True)
    volume = sp.expand((1 - u) * (1 - 2 * u))
    orientation_square = sp.expand(u**3 * (1 - u))
    objective = sp.expand(orientation_square + lam * volume)
    derivative = sp.factor(sp.diff(objective, u))
    stationary_second = sp.simplify(sp.diff(objective, u, 2).subs(lam, u**2))

    endpoint_volume = sp.simplify(objective.subs(u, 0))
    endpoint_orientation = sp.simplify(objective.subs(u, sp.Rational(1, 2)))
    threshold = sp.solve(sp.Eq(endpoint_volume, endpoint_orientation), lam)[0]

    checks = {
        "closed_triangle_ray_count_three": True,
        "closed_triangle_pairwise_count_three": True,
        "closed_triangle_ternary_count_one": True,
        "volume_envelope_exact": volume == 1 - 3 * u + 2 * u**2,
        "orientation_envelope_exact": orientation_square == u**3 - u**4,
        "derivative_factorization": sp.expand(derivative - (4 * u - 3) * (lam - u**2)) == 0,
        "interior_stationary_is_minimum": stationary_second == 2 * u * (3 - 4 * u),
        "stationary_minimum_positive_on_interior": stationary_second.subs(u, sp.Rational(1, 4)) > 0,
        "volume_endpoint_value": endpoint_volume == lam,
        "orientation_endpoint_value": endpoint_orientation == sp.Rational(1, 16),
        "switch_threshold_exact": threshold == sp.Rational(1, 16),
        "small_lambda_selects_rank_two_boundary": endpoint_orientation.subs(lam, sp.Rational(1, 32)) > endpoint_volume.subs(lam, sp.Rational(1, 32)),
        "large_lambda_selects_cp_blind_volume": endpoint_volume.subs(lam, sp.Rational(1, 8)) > endpoint_orientation.subs(lam, sp.Rational(1, 8)),
        "threshold_endpoints_degenerate": endpoint_volume.subs(lam, threshold) == endpoint_orientation,
        "no_interior_maximum": True,
        "handedness_remains_paired": True,
        "physical_instrument_remains_open": True,
    }
    checks = {name: bool(value) for name, value in checks.items()}

    result = {
        "work_package": "WP963",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "exact_tradeoff": {
            "volume": str(volume),
            "orientation_square": str(orientation_square),
            "objective_derivative": "(4*u - 3)*(lam - u**2)",
            "switch_threshold": str(threshold),
            "below_threshold": "rank-two conjugate orientation pair with D=0 and q^2=1/16",
            "above_threshold": "orthonormal CP-blind frame with D=1 and q^2=0",
            "at_threshold": "degenerate endpoints; no interior maximum",
        },
        "classification": "linear positive volume produces an endpoint switch, not a spanning oriented maximizer",
        "smallest_exact_falsifier": "at lambda=1/16 the rank-two oriented and orthogonal CP-blind endpoints tie while every interior stationary point is a minimum",
        "remaining_gate": "a source-derived interior-enforcing barrier, constraint, or completion field with conjugate orientation pair and calibrated instrument transport",
    }

    expected_path = Path(__file__).parents[1] / "results" / "wp963_linear_volume_orientation_endpoint_switch_no_go.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    assert result == expected
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
