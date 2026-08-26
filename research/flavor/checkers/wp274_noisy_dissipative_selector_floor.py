"""WP274: exact noise-floor audit for dissipative flavor preparation."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    time = sp.symbols("time", nonnegative=True)
    rate, diffusion, initial_variance = sp.symbols("rate diffusion initial_variance", positive=True)
    variance = sp.simplify(
        initial_variance * sp.exp(-2 * rate * time)
        + diffusion / rate * (1 - sp.exp(-2 * rate * time))
    )
    variance_residual = sp.simplify(sp.diff(variance, time) - (-2 * rate * variance + 2 * diffusion))
    stationary_variance = sp.limit(variance, time, sp.oo)

    tolerance = sp.Rational(1, 100)
    tolerance_variance = tolerance**2

    # Passing packet: stationary standard deviation 1/200 below tolerance.
    passing = {rate: 1, diffusion: sp.Rational(1, 40000), initial_variance: 1}
    passing_floor = stationary_variance.subs(passing)
    passing_time = sp.log(13333) / 2
    passing_terminal = sp.simplify(variance.subs(passing).subs(time, passing_time))

    # Borderline packet: the stationary variance equals tolerance squared, so
    # any finite time remains strictly above tolerance from v0=1.
    borderline = {rate: 1, diffusion: sp.Rational(1, 10000), initial_variance: 1}
    borderline_floor = stationary_variance.subs(borderline)
    borderline_excess = sp.factor(variance.subs(borderline) - tolerance_variance)

    # Failing packet: stationary floor already exceeds tolerance.
    failing = {rate: 1, diffusion: sp.Rational(1, 5000), initial_variance: 1}
    failing_floor = stationary_variance.subs(failing)

    checks = {
        "variance_ode_solution_exact": variance_residual == 0,
        "stationary_variance_is_D_over_gamma": stationary_variance == diffusion / rate,
        "passing_noise_floor_below_tolerance": passing_floor == sp.Rational(1, 40000) and passing_floor < tolerance_variance,
        "passing_runtime_exact": passing_terminal == tolerance_variance,
        "borderline_floor_equals_tolerance": borderline_floor == tolerance_variance,
        "borderline_packet_never_passes_at_finite_time": borderline_excess == sp.Rational(9999, 10000) * sp.exp(-2 * time),
        "failing_floor_exceeds_tolerance": failing_floor == sp.Rational(1, 5000) and failing_floor > tolerance_variance,
        "deliberate_damping_alone_implies_point_selector_claim_fails": stationary_variance > 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP274",
        "theorem_domain": "Ornstein-Uhlenbeck deviation dynamics dz=-gamma*z*dt+sqrt(2D)*dW with mean-square preparation tolerance epsilon^2",
        "variance_exact": str(variance),
        "stationary_variance": str(stationary_variance),
        "necessary_strict_finite_time_condition": "D/gamma < epsilon^2",
        "tolerance": str(tolerance),
        "packets": {
            "passing": {"gamma": "1", "D": "1/40000", "v0": "1", "floor": str(passing_floor), "runtime": str(passing_time), "terminal_variance": str(passing_terminal)},
            "borderline": {"gamma": "1", "D": "1/10000", "v0": "1", "floor": str(borderline_floor), "finite_time_excess": str(borderline_excess)},
            "failing": {"gamma": "1", "D": "1/5000", "v0": "1", "floor": str(failing_floor)},
        },
        "contextual_partition": "the noisy channel converges to a Gaussian tolerance class with variance D/gamma, not to a distinguished point",
        "classification": "finite noisy dissipation is a conditional approximate distribution selector only when an independently calibrated noise floor lies strictly below tolerance",
        "first_nonfaithful_arrow": "unique deterministic vacuum -> point preparation under source noise",
        "smallest_exact_falsifier": "D=1/10000 and gamma=1 put the variance floor exactly at epsilon^2=1/10000, so every finite time remains above tolerance from v0=1",
        "remaining_physical_instrument_gate": "derive and calibrate damping, diffusion, initial-domain variance, tolerance metric, runtime, post-preparation stabilization, and readout in one flavor substrate",
        "scope_limit": "active cooling, squeezed/non-Gaussian reservoirs, feedback, error correction, or zero-temperature limits require separate source and resource typing",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp274_noisy_dissipative_selector_floor.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
