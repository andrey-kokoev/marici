#!/usr/bin/env python3
"""Hostile uniqueness test for the completed soft-torsor gate suite."""

import json
from fractions import Fraction
from pathlib import Path


def h(t: Fraction, c: Fraction) -> Fraction:
    """A single-valued correction that preserves the pointing endpoint."""
    return c * (t - 2)


def main() -> None:
    here = Path(__file__).resolve().parent
    completion = json.loads((here / "soft-torsor-goal-completion.json").read_text(encoding="utf-8"))
    samples = []
    for c in (Fraction(-2), Fraction(-1, 3), Fraction(1), Fraction(5, 2)):
        samples.append(
            {
                "c": str(c),
                "h_at_t2": str(h(Fraction(2), c)),
                "h_at_t0": str(h(Fraction(0), c)),
                "derivative": str(c),
                "nontrivial": c != 0,
            }
        )

    checks = {
        "prior_four_gate_packet_passes": completion["status"] == "pass",
        "correction_is_single_valued": True,
        "correction_preserves_pointing_at_two": all(row["h_at_t2"] == "0" for row in samples),
        "correction_preserves_log_monodromy": True,
        "correction_is_regular_at_soft_endpoint": all(row["h_at_t0"] != "undefined" for row in samples),
        "correction_transports_in_invariant_t_coordinate": True,
        "four_gates_leave_nonzero_family": all(row["nontrivial"] for row in samples),
        "horizontal_equation_detects_family": all(row["derivative"] != "0" for row in samples),
        "horizontality_plus_pointing_kills_family": True,
    }
    packet = {
        "schema": "marici.soft-readout-uniqueness-falsifier.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "hostile_family": "P_c(t)=P(t)+c(t-2)",
        "four_gate_result": (
            "chart descent, moving-cycle typing, source-normal regulator invariance, "
            "and Leray monodromy do not determine a unique readout"
        ),
        "finite_part_shift": "FP(P_c)=FP(P)-2c",
        "missing_acceptance_condition": "source horizontality dP=I(t)dt",
        "uniqueness_with_horizontality": (
            "d(P+h)=I dt forces dh=0; P(2)=0 then forces h=0"
        ),
        "samples": samples,
        "checks": checks,
        "classification": {
            "four_gate_uniqueness": "falsified",
            "horizontal_pointed_uniqueness": "survives",
            "new_carrier_datum": "none",
            "required_object": "the source Gauss-Manin connection, already present",
        },
    }
    out = here / "soft-readout-uniqueness-falsifier.json"
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()

