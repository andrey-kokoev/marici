"""WP276: exact sensor-kernel obstruction for measurement-based feedback."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    k1, k2 = sp.symbols("k1 k2", positive=True)
    sensor_one = sp.Matrix([[1, 0]])
    gain_column = sp.Matrix([[k1], [k2]])
    closed_one = -gain_column * sensor_one
    blind_direction = sp.Matrix([0, 1])
    gram_one = sensor_one.T * sensor_one

    complementary_sensor = sp.Matrix([[0, 1]])
    stacked_sensor = sensor_one.col_join(complementary_sensor)
    full_gain = sp.diag(k1, k2)
    closed_full = -full_gain * stacked_sensor
    gram_full = stacked_sensor.T * stacked_sensor

    checks = {
        "single_sensor_rank_one": sensor_one.rank() == 1,
        "single_sensor_gram_singular": gram_one.det() == 0,
        "blind_direction_is_unobserved": sensor_one * blind_direction == sp.zeros(1, 1),
        "blind_direction_is_uncontrolled_for_any_gain": closed_one * blind_direction == sp.zeros(2, 1),
        "single_sensor_closed_loop_has_zero_eigenvalue": closed_one.det() == 0,
        "complementary_sensor_restores_observation_rank": stacked_sensor.rank() == 2,
        "complementary_sensor_gram_positive": gram_full.det() == 1,
        "full_closed_loop_is_nonsingular": closed_full.det() == k1 * k2,
        "full_closed_loop_modes_decay": closed_full.eigenvals() == {-k1: 1, -k2: 1},
        "deliberate_gain_kills_sensor_kernel_claim_fails": closed_one * blind_direction == sp.zeros(2, 1),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP276",
        "theorem_domain": "two-dimensional flavor-deviation module with measurement-based linear feedback and zero uncontrolled drift",
        "single_sensor": [[int(value) for value in sensor_one.row(0)]],
        "single_sensor_gram": [[int(value) for value in gram_one.row(i)] for i in range(2)],
        "single_sensor_closed_loop": [[str(value) for value in closed_one.row(i)] for i in range(2)],
        "blind_direction": [int(value) for value in blind_direction],
        "stacked_sensor": [[int(value) for value in stacked_sensor.row(i)] for i in range(2)],
        "stacked_sensor_gram_determinant": str(gram_full.det()),
        "full_closed_loop": [[str(value) for value in closed_full.row(i)] for i in range(2)],
        "contextual_partition": "the one-port sensor identifies all deviations differing only along its kernel; the complementary source-derived port refines the partition to singleton vectors in this finite model",
        "classification": "rank-one feedback is neither a full deviation selector nor a complete physical instrument; a rank-two source-derived probe family restores formal observability, with actuator execution still separate",
        "first_nonfaithful_arrow": "physical deviation module -> sensor record",
        "smallest_exact_falsifier": "z=(0,1) has zero sensor record and zero feedback response for every positive gain pair",
        "remaining_physical_instrument_gate": "derive two independent flavor-sensitive sensor channels and actuator couplings in one common frame, then calibrate their noise, latency, bandwidth, reachability, and stabilization",
        "scope_limit": "formal observation rank is necessary but not sufficient for executable control; nonlinear dynamics and time-varying observability require separate audits",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp276_feedback_observability_kernel.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
