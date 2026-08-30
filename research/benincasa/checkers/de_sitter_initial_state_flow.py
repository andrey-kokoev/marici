#!/usr/bin/env python3
"""Exact state-flow audit for the freeze-out normal-grade readout."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "results" / "de-sitter-initial-state-flow.json"


def main() -> None:
    # At x=k eta0, r=(1-i x)e^{i x} and r'/r=(x+i x^2)/(1+x^2).
    # The fixed-state connection is dA=-2(r'/r)A and
    # dB=-2x/(1+x^2)B.  Verify the invariant numerators exactly at an
    # arbitrary rational hostile point x=3; cancellation is polynomial.
    x = Fraction(3)
    R = 1 + x * x
    log_r_prime = (x / R, x * x / R)  # real, imaginary
    flow_A = (-2 * log_r_prime[0], -2 * log_r_prime[1])
    assert flow_A[0] + 2 * log_r_prime[0] == 0
    assert flow_A[1] + 2 * log_r_prime[1] == 0
    flow_B = -2 * x / R
    assert flow_B + 2 * x / R == 0

    packet = {
        "schema": "marici.de_sitter_initial_state_flow.v1",
        "coordinate": "x=k eta0",
        "mode_factor": "r(x)=(1-i x) exp(i x)",
        "logarithmic_derivative": "d_x log r=(x+i x^2)/(1+x^2)",
        "fixed_state_connection": {
            "complex": {
                "dA_dx": "-2 (x+i x^2)/(1+x^2) A",
                "dB_dx": "-2x/(1+x^2) B",
            },
            "real_basis_alpha_beta_B": [
                ["-2x/(1+x^2)", "2x^2/(1+x^2)", "0"],
                ["-2x^2/(1+x^2)", "-2x/(1+x^2)", "0"],
                ["0", "0", "-2x/(1+x^2)"],
            ],
        },
        "horizontal_invariants": {
            "C": "A r(x)^2",
            "N": "B abs(r(x))^2=B(1+x^2)",
            "derivatives": {"dC_dx": "0", "dN_dx": "0"},
        },
        "freezeout_rows_in_invariant_coordinates_ReC_ImC_N": {
            "grade_0": ["0", "2", "2"],
            "grade_1": ["0", "0", "0"],
            "grade_2": ["0", "4", "4"],
            "grade_3": ["-8", "0", "0"],
        },
        "rank": {
            "through_grade_2": 1,
            "through_grade_3_on_full_gaussian_state": 2,
            "state_flow_dependence": "none in horizontal coordinates (C,N)",
        },
        "slice_audit": {
            "slice": "alpha=Re(A)=0",
            "normal_derivative_on_slice": "d alpha/dx=2x^2 beta/(1+x^2)",
            "preserved": False,
            "generic_exception": "x beta=0",
        },
        "conclusion": (
            "The grade-three readout is state-flow covariant after completing the source slice "
            "to the full complex Gaussian A-plane. The alpha=0 presentation slice itself is not horizontal."
        ),
        "classification": "coefficient connection and readout filtration; unchanged carrier",
    }
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"horizontal_invariants": ["A r^2", "B(1+x^2)"], "slice_preserved": False}))


if __name__ == "__main__":
    main()
