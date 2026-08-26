"""WP345: exact quotient identification for the symmetric two-branch mediator."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    center, displacement, variance = sp.symbols("pbar d s", real=True)
    u1 = center
    u2 = center**2 + displacement**2
    u3 = center**3 + 3 * center * displacement**2
    quotient_u2 = center**2 + variance
    quotient_response = sp.Matrix([
        [sp.diff(readout, parameter) for parameter in (center, variance)]
        for readout in (u1, quotient_u2)
    ])
    original_response = sp.Matrix([
        [sp.diff(readout, parameter) for parameter in (center, displacement)]
        for readout in (u1, u2)
    ])
    reconstructed_center = u1
    reconstructed_variance = sp.simplify(u2 - u1**2)
    third_consistency = sp.simplify(u3 - (3 * u1 * u2 - 2 * u1**3))
    checks = {
        "branch_exchange_preserves_all_three_moments": all(sp.simplify(moment.subs(displacement, -displacement) - moment) == 0 for moment in (u1, u2, u3)),
        "quotient_response_has_unit_determinant": quotient_response.det() == 1,
        "first_two_moments_reconstruct_center": reconstructed_center == center,
        "first_two_moments_reconstruct_variance": reconstructed_variance == displacement**2,
        "original_coordinate_determinant_vanishes_only_at_branch_collision": original_response.det() == 2 * displacement,
        "third_moment_is_forced_by_first_two": third_consistency == 0,
        "opposite_displacements_are_same_quotient_point": (center, displacement**2) == (center, (-displacement) ** 2),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP345",
        "admitted_state_domain": "equal-weight two-branch shared-mediator laws with probabilities pbar-d and pbar+d, quotiented by branch exchange d~-d",
        "faithful_quotient_coordinate": "(pbar,s) with s=d^2, subject to the probability-support inequalities",
        "candidate_probe_family": "calibrated first and second normalized domain coincidences; third order retained as a grammar-consistency control",
        "quotient_response_jacobian": [[str(value) for value in row] for row in quotient_response.tolist()],
        "quotient_determinant": str(quotient_response.det()),
        "inverse_map": {"pbar": "u1", "s": "u2-u1^2"},
        "third_order_identity": "u3=3*u1*u2-2*u1^3",
        "contextual_partition": "first and second moments have singleton fibers on the branch-exchange quotient; literal d and -d remain one relational source point",
        "classification": "second order is sufficient for the physical symmetric-mediator quotient, while third order tests the frozen grammar; neither moment selects the quotient values",
        "smallest_exact_falsifier": "a measured residual u3-3*u1*u2+2*u1^3 different from zero rejects the equal-weight two-branch mediator grammar",
        "reference_rule": "a mediator branch label would split d and -d only by adding a branch-resolved reference port and changing the experiment to the branch stabilizer groupoid",
        "remaining_physical_instrument_gate": "calibrate first through third coincidences, propagate contrast-conditioned errors, and derive equal branch weights and a single shared mediator from the source history",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp345_symmetric_mediator_quotient.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
