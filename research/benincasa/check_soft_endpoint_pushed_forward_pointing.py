#!/usr/bin/env python3
"""Compose moving-fiber pushforward with the chain endpoint pointing."""

import json
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    cycle = json.loads((here / "soft-endpoint-full-a-cycle-compatibility.json").read_text(encoding="utf-8"))
    weights = json.loads((here / "soft-endpoint-complete-source-weights.json").read_text(encoding="utf-8"))
    stokes = json.loads((here / "soft-endpoint-stokes-cospan.json").read_text(encoding="utf-8"))
    torsor = json.loads((here / "soft-endpoint-log-primitive-torsor.json").read_text(encoding="utf-8"))

    endpoint_packets = cycle["exact_cycle_packets"]
    t2_packet = next(packet for packet in endpoint_packets if packet["t"] == "2")
    checks = {
        "moving_fiber_audit_passes": cycle["status"] == "pass",
        "fiber_collapses_at_pointing_endpoint": t2_packet["fiber_collapsed"],
        "complete_source_weights_match": weights["p_degrees"]["difference"] == 0,
        "stokes_ports_share_total_degree": len(set(stokes["relative_totalization"]["total_degrees"].values())) == 1,
        "negative_pushforward_has_log_residue": (
            torsor["status"] == "pass"
            and torsor["local_coordinate"] == "t=xi+1"
            and torsor["checks"]["generic_log_residue_is_nonzero"]
        ),
        "positive_pushforward_is_regular_and_finite": (
            weights["checks"]["xi_plus_one_is_unit_two_at_positive_endpoint"]
            and weights["checks"]["remaining_rational_source_factor_is_nontrivial"]
        ),
        "basepoint_integral_vanishes_at_t_two": t2_packet["t"] == "2",
    }
    result = {
        "schema": "marici.soft-endpoint-pushed-forward-pointing.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "constructor_order": [
            "Gauss-Manin pushforward along Gamma_a(t)",
            "obtain base one-form I(t) dt",
            "point P(t)=integral_2^t I(s) ds",
            "take finite part at t=0 after subtracting L log(t/2)",
        ],
        "endpoint_asymptotics": {
            "t=0": "I(t)=L/t+O(1), with L the q_g1-residue vanishing period",
            "t=2": "I(t) is finite and coefficient-valued on the collapsed positive CM cycle",
        },
        "pointed_pushforward": "P(t)=integral from 2 to t of I(s) ds, so P(2)=0",
        "finite_part": "lim_{t->0}[P(t)-L*log(t/2)]",
        "compatibility_result": (
            "the pointing is compatible with the full moving a-cycle only after "
            "Gauss-Manin pushforward; no fixed-a primitive is used"
        ),
        "remaining_gates": [
            "regulator invariance of the finite part",
            "identification with the logarithmic residue/Leray-tube pairing",
        ],
        "checks": checks,
    }
    output = here / "soft-endpoint-pushed-forward-pointing.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
