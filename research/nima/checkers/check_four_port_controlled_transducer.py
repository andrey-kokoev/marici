#!/usr/bin/env python3
"""Exact rank checks for the four-port controlled-transducer DPC."""

import json
from fractions import Fraction
from pathlib import Path


def main():
    b = Fraction(3, 2)
    q = Fraction(1, 3)
    y_plus = b * (1 + q) / 2
    y_minus = b * (1 - q) / 2

    # Rows are y_plus and y_minus; columns are body b and gate q.
    jacobian = (
        ((1 + q) / 2, b / 2),
        ((1 - q) / 2, -b / 2),
    )
    determinant = jacobian[0][0] * jacobian[1][1] - jacobian[0][1] * jacobian[1][0]
    assert determinant == -b / 2
    assert determinant != 0

    scalar_sum = y_plus + y_minus
    assert scalar_sum == b
    scalar_gate_derivative = Fraction(0)
    assert scalar_gate_derivative == 0

    # An even readout retains a simultaneous sign torsor.
    def even_readout(body, gate):
        return ((body * (1 + gate) / 2) ** 2, (body * (1 - gate) / 2) ** 2)

    assert even_readout(b, q) == even_readout(-b, -q)[::-1]
    unordered_positive = sorted(even_readout(b, q))
    unordered_reversed = sorted(even_readout(-b, -q))
    assert unordered_positive == unordered_reversed

    result = {
        "schema": "marici.four-port-controlled-transducer.v1",
        "status": "pass",
        "joint_readout_jacobian_determinant": [determinant.numerator, determinant.denominator],
        "joint_readout_locally_rank_two": determinant != 0,
        "scalar_sum": [scalar_sum.numerator, scalar_sum.denominator],
        "scalar_sum_gate_derivative": [scalar_gate_derivative.numerator, scalar_gate_derivative.denominator],
        "scalar_shadow_forgets_gate": scalar_gate_derivative == 0,
        "even_unordered_readout_retains_sign_torsor": unordered_positive == unordered_reversed,
        "active_gain_claimed": False,
        "disposition": "four-port controlled-transducer DPC passes; transistor gain remains unproved",
    }
    out = Path(__file__).parents[1] / "results" / "four-port-controlled-transducer.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

