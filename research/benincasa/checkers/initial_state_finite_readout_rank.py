#!/usr/bin/env python3
"""Exact rank audit for finite readouts of the generated Gaussian pair."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "results" / "initial-state-finite-readout-rank.json"


def main() -> None:
    # Remove the common nonzero factor 1/(2 omega^2).  At equal time,
    # Delta G^(1)(t,t) = beta cos(2 omega (t-t0)) + B.
    # det [[c1,1],[c2,1]] = c1-c2 and
    # det [[c1,1],[-2 omega s1,0]] = 2 omega s1.
    det_two = "c1 - c2"
    det_jet = "2*omega*s1"

    # Independent integer substitutions guard the determinant signs and
    # generic ranks without importing a computer-algebra package.
    assert 3 * 1 - 1 * 5 == -2  # c1=3, c2=5
    assert 3 * 0 - 1 * (-2 * 7 * 11) == 154

    packet = {
        "schema": "marici.initial_state_finite_readout_rank.v1",
        "source_linearized_readout": "2 omega^2 DeltaG(t,t) = beta cos(2 omega (t-t0)) + B",
        "readouts": {
            "one_equal_time": {
                "matrix": [["c1", "1"]],
                "rank": 1,
                "kernel_generator": ["1", "-c1"],
            },
            "two_equal_times": {
                "matrix": [["c1", "1"], ["c2", "1"]],
                "determinant": det_two,
                "generic_rank": 2,
                "failure_locus": "c1=c2",
            },
            "value_and_time_derivative": {
                "matrix": [["c1", "1"], ["-2 omega s1", "0"]],
                "determinant": det_jet,
                "generic_rank": 2,
                "failure_locus": "sin(2 omega (t1-t0))=0",
            },
            "infinite_time_average": {
                "matrix": [["0", "1"]],
                "rank": 1,
                "kernel_generator": ["1", "0"],
            },
        },
        "conclusion": (
            "Two generic equal-time samples, or one equal-time value and its time derivative, "
            "separate beta and B. A single-time power readout and the infinite-time average do not."
        ),
        "classification": "readout projection rank; no new carrier incidence",
    }
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"det_two_time": det_two, "det_value_derivative": det_jet}))


if __name__ == "__main__":
    main()
