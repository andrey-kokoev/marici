"""WP277: exact actuator-reachability obstruction after full observation."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    k1, k2 = sp.symbols("k1 k2", positive=True)
    sensor = sp.eye(2)
    actuator_one = sp.Matrix([1, 0])
    controller = sp.Matrix([[k1, k2]])
    closed_one = -actuator_one * controller * sensor
    left_blind = sp.Matrix([[0, 1]])
    zero_drift = sp.zeros(2)
    controllability_one = actuator_one.row_join(zero_drift * actuator_one)

    initial = sp.Matrix([0, 1])
    initial_derivative = closed_one * initial
    invariant_derivative = sp.simplify((left_blind * initial_derivative)[0])

    actuator_full = sp.eye(2)
    full_controller = sp.diag(k1, k2)
    closed_full = -actuator_full * full_controller * sensor
    controllability_full = actuator_full.row_join(zero_drift * actuator_full)

    checks = {
        "sensor_is_fully_observing": sensor.rank() == 2,
        "single_actuator_rank_one": actuator_one.rank() == 1,
        "single_actuator_controllability_rank_one": controllability_one.rank() == 1,
        "left_blind_covector_annihilates_actuator": left_blind * actuator_one == sp.zeros(1, 1),
        "second_state_coordinate_is_feedback_invariant": invariant_derivative == 0,
        "single_actuator_closed_loop_has_zero_determinant": closed_one.det() == 0,
        "full_actuator_restores_reachability_rank": controllability_full.rank() == 2,
        "full_closed_loop_nonsingular": closed_full.det() == k1 * k2,
        "full_closed_loop_modes_decay": closed_full.eigenvals() == {-k1: 1, -k2: 1},
        "deliberate_full_sensor_implies_control_claim_fails": sensor.rank() == 2 and controllability_one.rank() == 1,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP277",
        "theorem_domain": "fully observed two-dimensional flavor-deviation module with zero uncontrolled drift and measurement-based linear feedback",
        "sensor": [[int(value) for value in sensor.row(i)] for i in range(2)],
        "single_actuator": [int(value) for value in actuator_one],
        "single_actuator_closed_loop": [[str(value) for value in closed_one.row(i)] for i in range(2)],
        "left_blind_covector": [int(value) for value in left_blind.row(0)],
        "hostile_initial_state": [int(value) for value in initial],
        "hostile_initial_derivative": [str(value) for value in initial_derivative],
        "full_actuator_closed_loop": [[str(value) for value in closed_full.row(i)] for i in range(2)],
        "contextual_partition": "the rank-one actuator preserves the second-coordinate leaves even under faithful sensing; a second source-derived actuator refines reachability to the whole finite module",
        "classification": "full observation without full actuator reachability is neither a complete selector nor an executable preparation instrument; complementary control must be source-derived",
        "first_nonfaithful_arrow": "controller command -> physical flavor-state displacement",
        "smallest_exact_falsifier": "from z=(0,1), arbitrary feedback changes the first coordinate by -k2 but leaves the second derivative exactly zero",
        "remaining_physical_instrument_gate": "derive two independent actuator couplings on the same physical flavor substrate and calibrate authority, reachability, energy, noise, latency, reset, and degradation",
        "scope_limit": "nonzero drift can enlarge controllability through commutators; any such drift must be source-derived and checked through the full controllability matrix",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp277_feedback_actuator_reachability.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
