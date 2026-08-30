from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


def reconstruct(records: dict[str, F]) -> tuple[F, F]:
    return (records["XX"] - records["YY"]) / 4, -(records["XY"] + records["YX"]) / 4


def first_jet_record(records: dict[str, F], setting: str, time: F, omega: F) -> F:
    derivative = {
        "XX": records["XY"],
        "YY": -records["YX"],
        "XY": -records["XX"],
        "YX": records["YY"],
    }[setting]
    return records[setting] + omega * time * derivative


def main() -> None:
    # Universal cancellation coefficients for the reconstructed x and y jets.
    # Independence of XX, YY, XY, YX forces every effective time to zero.
    coefficient_support = {
        "t_XX multiplies XY in dx": F(1, 4),
        "t_YY multiplies YX in dx": F(1, 4),
        "t_XY multiplies XX in dy": F(1, 4),
        "t_YX multiplies YY in dy": F(-1, 4),
    }
    assert all(value != 0 for value in coefficient_support.values())
    universal_single_sample_solution = {setting: F(0) for setting in ("XX", "YY", "XY", "YX")}

    records = {"XX": F(2, 25), "YY": F(-1, 25), "XY": F(-9, 100), "YX": F(-7, 100)}
    true_vector = reconstruct(records)
    assert true_vector == (F(3, 100), F(1, 25))
    boundary_product = F(1, 400)
    assert true_vector[0] ** 2 + true_vector[1] ** 2 == boundary_product

    times = {"XX": F(-3), "YY": F(-1), "XY": F(1), "YX": F(3)}
    omega = F(1, 100)
    sequential = {
        setting: first_jet_record(records, setting, times[setting], omega)
        for setting in records
    }
    sequential_vector = reconstruct(sequential)
    sequential_residual = sequential_vector[0] ** 2 + sequential_vector[1] ** 2 - boundary_product
    assert sequential_vector == (F(617, 20000), F(81, 2000))
    assert sequential_residual == F(36789, 400000000)
    assert sequential_residual > 0

    # Minimal universal first-jet repair: average each setting at opposite
    # effective times. The affine phase term cancels setting by setting.
    magnitudes = {"XX": F(4), "YY": F(3), "XY": F(2), "YX": F(1)}
    paired = {}
    for setting, magnitude in magnitudes.items():
        negative = first_jet_record(records, setting, -magnitude, omega)
        positive = first_jet_record(records, setting, magnitude, omega)
        paired[setting] = (negative + positive) / 2
    assert paired == records
    paired_vector = reconstruct(paired)
    paired_residual = paired_vector[0] ** 2 + paired_vector[1] ** 2 - boundary_product
    assert paired_residual == 0

    result = {
        "schema": "marici.aspect.within-block-phase-drift-no-go.v1",
        "status": "pass",
        "first_jet_derivatives": {
            "dXX/dphase": "XY",
            "dYY/dphase": "-YX",
            "dXY/dphase": "-XX",
            "dYX/dphase": "YY",
        },
        "universal_single_sample_solution": {key: str(value) for key, value in universal_single_sample_solution.items()},
        "single_sample_nonzero_time_schedule_possible": False,
        "hostile_times": {key: str(value) for key, value in times.items()},
        "hostile_phase_slope": str(omega),
        "hostile_false_npt_residual": str(sequential_residual),
        "paired_samples_per_setting": 2,
        "paired_total_correlation_samples": 8,
        "paired_first_jet_residual": str(paired_residual),
        "verdict": "No four-sample sequential order universally cancels affine within-block phase drift; opposite-time pairing of every setting is the minimal record-independent first-jet repair.",
        "claim_boundary": "first jet in phase; one drifting analyzer frame; arbitrary labelled X-state correlations; second-order phase curvature, gain drift, and finite counts excluded",
    }
    output = Path(__file__).parents[1] / "results" / "within_block_phase_drift_no_go.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
