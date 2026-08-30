"""WP278: exact dynamic observability and reachability from one port."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    drift = sp.Matrix([[0, 1], [-1, 0]])
    actuator = sp.Matrix([1, 0])
    sensor = sp.Matrix([[1, 0]])

    observability = sensor.col_join(sensor * drift)
    controllability = actuator.row_join(drift * actuator)

    z1, z2 = sp.symbols("z1 z2", real=True)
    state = sp.Matrix([z1, z2])
    score_tower = sp.Matrix([(sensor * state)[0], (sensor * drift * state)[0]])
    reconstructed = sp.simplify(observability.inv() * score_tower)

    # One-input state feedback u=-Kz. Choose K=(2,0), yielding a repeated
    # stable eigenvalue -1.
    feedback = sp.Matrix([[2, 0]])
    closed_loop = drift - actuator * feedback
    characteristic = sp.factor(closed_loop.charpoly().as_expr())

    # One-output observer injection with L=(2,0)^T has the same stable error
    # polynomial for A-LC.
    observer_gain = sp.Matrix([2, 0])
    observer_error = drift - observer_gain * sensor
    observer_characteristic = sp.factor(observer_error.charpoly().as_expr())

    checks = {
        "instantaneous_sensor_rank_one": sensor.rank() == 1,
        "instantaneous_actuator_rank_one": actuator.rank() == 1,
        "two_score_observability_rank_two": observability.rank() == 2,
        "drift_actuator_controllability_rank_two": controllability.rank() == 2,
        "score_tower_reconstructs_state_exactly": reconstructed == state,
        "single_actuator_feedback_stabilizes": characteristic == (sp.Symbol("lambda") + 1) ** 2,
        "single_sensor_observer_stabilizes": observer_characteristic == (sp.Symbol("lambda") + 1) ** 2,
        "drift_is_nonsingular_rotation_generator": drift.det() == 1 and drift.T == -drift,
        "deliberate_instantaneous_rank_bounds_dynamic_rank_claim_fails": sensor.rank() == 1 and observability.rank() == 2,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP278",
        "theorem_domain": "two-dimensional linear deviation dynamics with source drift A, one sensor C, and one actuator B",
        "drift": [[int(value) for value in drift.row(i)] for i in range(2)],
        "sensor": [[int(value) for value in sensor.row(0)]],
        "actuator": [int(value) for value in actuator],
        "observability_tower": [[int(value) for value in observability.row(i)] for i in range(2)],
        "controllability_tower": [[int(value) for value in controllability.row(i)] for i in range(2)],
        "score_readout": [str(value) for value in score_tower],
        "reconstructed_state": [str(value) for value in reconstructed],
        "closed_loop": [[int(value) for value in closed_loop.row(i)] for i in range(2)],
        "closed_loop_characteristic": str(characteristic),
        "observer_error_characteristic": str(observer_characteristic),
        "contextual_partition": "the instantaneous sensor has one-dimensional fibers, while the source-generated first time score refines them to singleton states in this finite model",
        "classification": "conditional positive architecture: one physical sensor and actuator become jointly faithful and stabilizing through a source-derived drift; neither algebraic span nor an added reference port is needed once the time-resolved instrument exists",
        "smallest_exact_falsifier": "if the drift entry A_12 vanishes, both observability and controllability towers lose their second independent column/row",
        "remaining_physical_instrument_gate": "derive an actual dynamical flavon drift with this mixing action, a time-resolved flavor sensor, an actuator coupling, clock, bandwidth, noise model, and repeatable stabilization on physical16",
        "scope_limit": "this is a finite linear architecture theorem, not evidence that Standard Model Yukawa parameters possess the required dynamical substrate or executable ports",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp278_dynamic_single_port_closure.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
