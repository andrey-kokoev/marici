#!/usr/bin/env python3
"""SCC checker for the cross-level calibration naturality candidate."""
from __future__ import annotations
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ASPECT = HERE.parent
CONTRACT = ASPECT / "contracts" / "interaction-net-cross-level-calibration.v1.json"
RESULT = ASPECT / "results" / "interaction_net_cross_level_calibration.json"

def saturate(q, level):
    return (q[0], q[1], min(q[2], level), min(q[3], level), min(q[4], 2 * level))

def raw(q, gains, offsets):
    return tuple(gains[j] * q[j] + offsets[j] for j in range(5))

def transfer(high_raw, high_gains, high_offsets, low_gains, low_offsets, low_level, wrong_v=False):
    q = tuple((high_raw[j] - high_offsets[j]) / high_gains[j] for j in range(5))
    vcap = low_level if wrong_v else 2 * low_level
    restricted = (q[0], q[1], min(q[2], low_level), min(q[3], low_level), min(q[4], vcap))
    return raw(restricted, low_gains, low_offsets)

def residual_norm2(left, right):
    return sum((a - b) ** 2 for a, b in zip(left, right))

def transfer_jacobian(q, high_gains, low_gains, low_level):
    caps = (None, None, low_level, low_level, 2 * low_level)
    diagonal = []
    for j in range(5):
        active = 1.0 if caps[j] is None or q[j] < caps[j] else 0.0
        diagonal.append(active * low_gains[j] / high_gains[j])
    return tuple(diagonal)

def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    states = [
        (0, 0, 0, 0, 0), (1, 3, 1, 1, 2), (2, 17, 2, 1, 4),
        (0, 31, 4, 3, 8), (1, 9, 6, 5, 12)
    ]
    calibrations = {
        r: {
            "g": tuple(1.0 + 0.03 * r for _ in range(5)),
            "b": tuple(0.1 * r - 0.02 * j for j in range(5))
        } for r in range(6)
    }
    squares = []
    for low in range(5):
        high = low + 1
        lo, hi = calibrations[low], calibrations[high]
        errors = []
        for q in states:
            direct = raw(saturate(q, low), lo["g"], lo["b"])
            high_readout = raw(saturate(q, high), hi["g"], hi["b"])
            errors.append(residual_norm2(direct, transfer(
                high_readout, hi["g"], hi["b"], lo["g"], lo["b"], low
            )))
        squares.append({"low": low, "high": high, "max_squared_residual": max(errors),
                        "closed": max(errors) < 1e-20})

    lo, hi = calibrations[3], calibrations[4]
    witness = (0, 0, 2, 0, 4)
    direct = raw(saturate(witness, 3), lo["g"], lo["b"])
    high_readout = raw(saturate(witness, 4), hi["g"], hi["b"])
    wrong_clip_error = residual_norm2(direct, transfer(
        high_readout, hi["g"], hi["b"], lo["g"], lo["b"], 3, wrong_v=True
    ))
    drifted_high = tuple(g * (1.0 + 0.02 * (j + 1)) for j, g in enumerate(hi["g"]))
    drift_error = residual_norm2(direct, transfer(
        raw(saturate(witness, 4), drifted_high, hi["b"]),
        hi["g"], hi["b"], lo["g"], lo["b"], 3
    ))
    jet_probe = (0.25, 0.5, 1.25, 0.75, 2.5)
    predicted_jet = transfer_jacobian(jet_probe, hi["g"], lo["g"], 3)
    epsilon = 1e-6
    finite_difference = []
    base_high = raw(jet_probe, hi["g"], hi["b"])
    base_low = transfer(base_high, hi["g"], hi["b"], lo["g"], lo["b"], 3)
    for j in range(5):
        perturbed = list(base_high)
        perturbed[j] += epsilon
        moved = transfer(tuple(perturbed), hi["g"], hi["b"], lo["g"], lo["b"], 3)
        finite_difference.append((moved[j] - base_low[j]) / epsilon)
    jet_error = residual_norm2(predicted_jet, finite_difference)
    omitted_jet_error = residual_norm2(predicted_jet, (1.0,) * 5)
    hostiles = {
        "wrong_v_clipping_detected": wrong_clip_error > 1e-6,
        "post_standard_gain_drift_detected": drift_error > 1e-6,
        "test_packet_refit_rejected": contract["calibration"]["test_packet_excluded_from_fit"],
        "diagonal_only_covariance_rejected": "full paired-route covariance" in contract["required_packet"],
        "adaptive_level_choice_rejected": "level chosen after target observation" in contract["hostiles"],
        "first_jet_transport_closed": jet_error < 1e-16,
        "omitted_derivative_transport_detected": omitted_jet_error > 1e-6,
        "synthetic_fixture_not_promoted": not contract["authority"]["physical_square_closed"]
    }
    passed = all(s["closed"] for s in squares) and all(hostiles.values())
    out = {
        "schema": "marici.aspect.interaction-net-cross-level-calibration-result.v1",
        "passed": passed,
        "ideal_synthetic_squares": squares,
        "wrong_clip_squared_residual": wrong_clip_error,
        "gain_drift_squared_residual": drift_error,
        "first_jet_squared_residual": jet_error,
        "omitted_jet_squared_residual": omitted_jet_error,
        "hostiles": hostiles,
        "physical_status": "not_run",
        "verdict": "checker_validated_candidate_awaiting_independent_calibrated_packet"
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))
    raise SystemExit(0 if passed else 1)

if __name__ == "__main__":
    main()
