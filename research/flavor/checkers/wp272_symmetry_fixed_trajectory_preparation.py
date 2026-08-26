"""WP272: exact symmetry-versus-fixed-trajectory preparation audit."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    time = sp.symbols("time", nonnegative=True)
    amplitude = sp.symbols("amplitude", real=True)
    trajectory = amplitude * sp.exp(-time)
    reflected = -trajectory
    beta = lambda value: -value

    flow_residual = sp.simplify(sp.diff(trajectory, time) - beta(trajectory))
    reflected_residual = sp.simplify(sp.diff(reflected, time) - beta(reflected))
    equivariance_residual = sp.simplify(beta(-trajectory) + beta(trajectory))

    quotient_coordinate = sp.simplify(trajectory**2)
    matching_quotient = quotient_coordinate.subs(time, 0)
    amplitude_one = matching_quotient.subs(amplitude, 1)
    amplitude_two = matching_quotient.subs(amplitude, 2)

    # Group averaging of the pair gives zero mean but retains a nonzero second
    # moment, so it is not the delta state at the fixed trajectory.
    averaged_mean = sp.simplify((trajectory + reflected) / 2)
    averaged_second_moment = sp.simplify((trajectory**2 + reflected**2) / 2)
    fixed_second_moment = sp.Rational(0)

    checks = {
        "trajectory_solves_flow": flow_residual == 0,
        "reflected_trajectory_solves_same_flow": reflected_residual == 0,
        "flow_is_z2_equivariant": equivariance_residual == 0,
        "z2_quotient_removes_sign": sp.simplify(trajectory**2 - reflected**2) == 0,
        "z2_quotient_retains_amplitude_magnitude": matching_quotient == amplitude**2,
        "inequivalent_magnitudes_survive_quotient": amplitude_one == 1 and amplitude_two == 4,
        "group_average_has_zero_mean": averaged_mean == 0,
        "group_average_is_not_fixed_delta_state": averaged_second_moment != fixed_second_moment,
        "deliberate_symmetric_law_implies_fixed_state_claim_fails": averaged_second_moment == amplitude**2 * sp.exp(-2 * time),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP272",
        "theorem_domain": "Z2-equivariant attractive trajectory dz/dt=-z with t increasing toward the UV",
        "symmetry": "z -> -z",
        "trajectory_family": "z_A(t)=A*exp(-t)",
        "quotient_coordinate": str(quotient_coordinate),
        "finite_matching_quotient": str(matching_quotient),
        "hostile_amplitudes": [
            {"A": "1", "quotient_at_matching": str(amplitude_one)},
            {"A": "2", "quotient_at_matching": str(amplitude_two)},
        ],
        "group_averaged_state": {
            "mean": str(averaged_mean),
            "second_moment": str(averaged_second_moment),
            "fixed_trajectory_second_moment": str(fixed_second_moment),
        },
        "contextual_partition": "Z2 identifies A with -A but leaves distinct classes labelled by |A|; averaging an orbit erases the mean but not its fluctuation record",
        "classification": "the symmetry quotient removes sign redundancy but does not select the fixed trajectory or eliminate the invariant amplitude; it is neither a selector nor a flavor texture rigidifier",
        "first_nonfaithful_arrow": "symmetry of the source law -> preparation of a symmetry-fixed state",
        "smallest_exact_falsifier": "A=1 and A=2 are both Z2-compatible UV-attractive trajectories but have quotient records 1 and 4 at the matching scale",
        "remaining_authority_gate": "derive a unique unbroken symmetric vacuum, dissipative preparation channel, boundary condition, or superselection rule that kills |A| rather than only its sign",
        "scope_limit": "a source with a proven unique symmetric state or an executable projection onto the fixed sector can close this gate; law equivariance alone cannot",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp272_symmetry_fixed_trajectory_preparation.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
