"""WP366: exact gain-calibrated common-perturbation response audit."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    p, q, gx, gy = sp.symbols("p q g_x g_y", nonzero=True)
    ax, ay = sp.symbols("a_x a_y", positive=True)
    alpha = sp.symbols("alpha", real=True)

    measured_x = gx * p
    measured_y = gy * q
    raw_ratio = sp.simplify(measured_x / measured_y)
    calibrated_ratio = sp.simplify((gy / gx) * raw_ratio)
    response_jacobian = sp.Matrix([measured_x, measured_y])

    transformed_gx = ax * gx
    transformed_gy = ay * gy
    transformed_measured_x = ax * measured_x
    transformed_measured_y = ay * measured_y
    transformed_calibrated_ratio = sp.simplify(
        (transformed_gy / transformed_gx)
        * (transformed_measured_x / transformed_measured_y)
    )

    hostile_a_raw = raw_ratio.subs({p: 1, q: 1, gx: 2, gy: 1})
    hostile_b_raw = raw_ratio.subs({p: 2, q: 1, gx: 1, gy: 1})
    hostile_a_calibrated = calibrated_ratio.subs({p: 1, q: 1, gx: 2, gy: 1})
    hostile_b_calibrated = calibrated_ratio.subs({p: 2, q: 1, gx: 1, gy: 1})
    ward_residual = alpha * q - p

    checks = {
        "calibrated_ratio_recovers_physical_response_ratio": calibrated_ratio == p / q,
        "calibrated_ratio_is_detector_unit_invariant": transformed_calibrated_ratio == calibrated_ratio,
        "response_jacobian_has_rank_one": response_jacobian.rank() == 1,
        "raw_hostile_pair_collides": hostile_a_raw == hostile_b_raw == 2,
        "gain_calibration_separates_hostile_pair": (
            hostile_a_calibrated == 1 and hostile_b_calibrated == 2
        ),
        "ward_residual_vanishes_exactly_at_alpha_equal_p_over_q": (
            sp.simplify(ward_residual.subs(alpha, p / q)) == 0
        ),
        "deliberate_wrong_ward_scale_is_detected": (
            ward_residual.subs({alpha: 1, p: 2, q: 1}) != 0
        ),
        "uncalibrated_ratio_retains_gain_kernel": sp.diff(raw_ratio, gx) != 0 and sp.diff(raw_ratio, gy) != 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}

    result = {
        "work_package": "WP366",
        "admitted_state_domain": "one controlled perturbation epsilon with nonzero local responses p=dx/depsilon and q=dy/depsilon, and independently calibrated nonzero detector gains gx and gy",
        "faithful_quotient_coordinate": "the gain- and unit-invariant response ratio s_det=p/q for the relational two-port experiment; full physical16 remains projected to x=J^2",
        "source_authorized_probe_family": "common-perturbation slopes at both ports plus independent detector-gain calibration",
        "contextual_partition": "without gain calibration packets sharing (gx/gy)*(p/q) collide; with calibration the classes are equality of p/q, provided q is resolvably nonzero",
        "classification": "candidate physical instrument for relational scale identification and Ward falsification; neither a numerical selector nor a rank-two source identifier",
        "response_jacobian": str(response_jacobian),
        "response_rank": 1,
        "raw_ratio": str(raw_ratio),
        "calibrated_ratio": str(calibrated_ratio),
        "ward_residual": str(ward_residual),
        "hostile_pair": {
            "packet_a": {"p_over_q": 1, "gx_over_gy": 2, "raw_ratio": 2, "calibrated_ratio": 1},
            "packet_b": {"p_over_q": 2, "gx_over_gy": 1, "raw_ratio": 2, "calibrated_ratio": 2},
        },
        "smallest_exact_falsifier": "distinct physical response ratios 1 and 2 give the same raw detector ratio 2 when gains are uncalibrated",
        "remaining_physical_instrument_gate": "derive one source operation with nonzero causal responses in both J^2 and Q/M2, independently calibrate gains, freeze threshold and scheme, and bound uncertainty away from q=0",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp366_common_perturbation_port_calibration.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
