"""WP270: exact hostile trajectories sharing one UV-attractive fixed point."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    time = sp.symbols("time", nonnegative=True)
    fixed = sp.Rational(1)
    amplitudes = [sp.Rational(0), sp.Rational(1)]
    trajectories = [fixed + amplitude * sp.exp(-time) for amplitude in amplitudes]
    beta = lambda value: -value + fixed
    residuals = [sp.simplify(sp.diff(value, time) - beta(value)) for value in trajectories]
    uv_limits = [sp.limit(value, time, sp.oo) for value in trajectories]
    matching_values = [value.subs(time, 0) for value in trajectories]
    selected_points = [sp.simplify(1 / (2 * value)) for value in matching_values]
    trajectory_difference = sp.simplify(trajectories[1] - trajectories[0])

    # A finite experimental resolution delta forgets the trajectory amplitude
    # sufficiently far in the UV although it remains nonzero at finite time.
    delta = sp.Rational(1, 100)
    blind_time = sp.log(100)
    difference_at_blind_time = sp.simplify(trajectory_difference.subs(time, blind_time))

    checks = {
        "both_trajectories_solve_same_beta_function": all(residual == 0 for residual in residuals),
        "both_share_same_uv_fixed_point": uv_limits == [fixed, fixed],
        "finite_matching_values_are_distinct": matching_values == [1, 2],
        "finite_selected_points_are_distinct": selected_points == [sp.Rational(1, 2), sp.Rational(1, 4)],
        "trajectory_amplitude_survives_at_finite_scale": trajectory_difference == sp.exp(-time),
        "trajectory_difference_vanishes_only_asymptotically": sp.limit(trajectory_difference, time, sp.oo) == 0 and trajectory_difference.subs(time, 0) != 0,
        "finite_resolution_collapses_trajectories_in_uv": difference_at_blind_time == delta,
        "deliberate_uv_limit_implies_ir_uniqueness_claim_fails": matching_values[0] != matching_values[1],
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP270",
        "theorem_domain": "finite-scale trajectories of dc/dt=-c+1 with common UV limit c*=1",
        "hostile_trajectories": [
            {"amplitude": str(amplitudes[i]), "trajectory": str(trajectories[i]), "uv_limit": str(uv_limits[i]), "c_at_matching_scale": str(matching_values[i]), "selected_x": str(selected_points[i])}
            for i in range(2)
        ],
        "trajectory_difference": str(trajectory_difference),
        "finite_resolution_witness": {"delta": str(delta), "time": str(blind_time), "difference": str(difference_at_blind_time)},
        "contextual_partition": "the UV-limit readout identifies both trajectories, while the finite matching-scale readout separates their integration constants",
        "classification": "the attractive fixed point selects an asymptotic boundary class but not a unique finite-scale flavor coefficient; trajectory amplitude is an exact remaining source coordinate",
        "first_nonfaithful_arrow": "common UV fixed-point limit -> unique finite matching trajectory",
        "smallest_exact_falsifier": "c_0(t)=1 and c_1(t)=1+exp(-t) solve the same beta function and share UV limit 1, but at t=0 select x=1/2 and x=1/4",
        "remaining_authority_gate": "derive the RG trajectory amplitude from a renormalized boundary condition, finite threshold match, or zero-dimensional UV critical surface, then transport it to the physical matching scale",
        "scope_limit": "a UV completion with no free trajectory directions or an independently fixed finite-scale matching condition can close this kernel",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp270_uv_limit_trajectory_kernel.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
