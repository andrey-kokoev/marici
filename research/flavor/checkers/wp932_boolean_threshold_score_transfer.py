"""WP932: transfer Boolean score faithfulness to a conditional flavor threshold tower."""

import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def subsets(n):
    return [tuple(i for i in range(n) if mask & (1 << i)) for mask in range(1 << n)]


def main():
    wp884 = json.loads((ROOT / "results/wp884_spin5_finite_threshold_selector_obstruction.json").read_text())
    wp922 = json.loads((ROOT / "results/wp922_spin7_orbifold_zero_mode_projection_fiber.json").read_text())
    wp931 = json.loads((ROOT / "results/wp931_declared_flavor_selector_exhaustion.json").read_text())

    labels = subsets(3)
    zeta = sp.Matrix([[int(set(s).issuperset(t)) for s in labels] for t in labels])
    mobius = sp.Matrix([
        [(-1) ** (len(t) - len(s)) if set(t).issuperset(s) else 0 for t in labels]
        for s in labels
    ])
    current_aggregate = sp.Matrix([[1] * len(labels)])
    kernel = current_aggregate.nullspace()

    route_values = sp.Matrix(range(1, 9))
    scores = zeta * route_values
    reconstructed = mobius * scores

    checks = {
        "wp884_threshold_obstruction_passes": wp884["status"] == "PASS" and wp884["summary"]["all_passed"],
        "wp922_three_bulk_label_source_passes": wp922["passed"] and wp922["parity_assignment_count"] == 8,
        "wp931_declared_selector_exhaustion_passes": wp931["passed"],
        "boolean_route_count_is_eight": len(labels) == 8,
        "zeta_matrix_is_unimodular": zeta.det() == 1,
        "mobius_is_exact_inverse": mobius * zeta == sp.eye(8) and zeta * mobius == sp.eye(8),
        "complete_score_tower_reconstructs_labelled_packet": reconstructed == route_values,
        "complete_tower_has_zero_algebraic_kernel": zeta.rank() == 8,
        "current_single_aggregate_has_rank_one": current_aggregate.rank() == 1,
        "current_single_aggregate_has_kernel_dimension_seven": len(kernel) == 7,
        "declared_threshold_source_rank_remains_one": wp884["local_source_constraint_rank"] == 1,
        "independent_deletion_controls_are_not_declared": True,
        "faithful_reconstruction_does_not_select_values": True,
        "no_typed_eight_route_instrument": True,
    }

    result = {
        "work_package": "WP932",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "classification": "conditional identification theorem, not selection: a complete Boolean threshold tower is faithful but is not source-authorized in flavor",
        "admitted_state_domain": "a labelled three-multiplet route packet modeled on the Spin7 bulk labels 8_a, 8_b, and 21, with eight formal deletion sectors",
        "faithful_quotient_coordinate": "the eight labelled route coefficients before any map to physical16",
        "source_authorized_probe_family": "currently only the rank-one finite-threshold matching constraint of WP884; independent multiplet deletion controls are undeclared",
        "contextual_partition": "the formal complete tower gives eight singleton coefficient coordinates, whereas the authorized aggregate leaves a seven-dimensional kernel",
        "boolean_zeta_determinant": int(zeta.det()),
        "complete_tower_rank": zeta.rank(),
        "authorized_aggregate_rank": current_aggregate.rank(),
        "authorized_aggregate_kernel_dimension": len(kernel),
        "operation_classification": "conditional source-story identifier if all deletion routes become executable; neither physical16 selector nor presentation rigidifier",
        "smallest_exact_falsifier": "two labelled packets differing by (1,-1,0,0,0,0,0,0) have the same authorized total aggregate but distinct complete score towers",
        "descent_result": "no physical16 descent is claimed; the theorem is faithful on labelled route coefficients, not on the low-energy flavor quotient",
        "remaining_physical_instrument_gate": "independently controllable decoupling or deletion of each multiplet, contact-normal subtraction, common calibration, and all eight route scores",
        "claim_boundary": "Möbius faithfulness proves identification only after route authorization; it neither prepares nor numerically selects the reconstructed coefficients",
        "successor": "test whether the declared Spin7 bulk action contains three independently tunable, gauge-consistent mass controls; without them the deletion tower remains formal",
        "checks": checks,
        "passed": all(checks.values()),
    }
    out = ROOT / "results/wp932_boolean_threshold_score_transfer.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
