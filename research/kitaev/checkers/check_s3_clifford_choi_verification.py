#!/usr/bin/env python3
"""Exact verified-cat schedules for the required encoded Clifford Choi states."""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from check_s3_five_rail_code_freeze import QUBIT, QUTRIT, certify, weight  # noqa: E402


def verification_schedule(name, logical_x_weight, logical_z_weight, gate):
    if gate == "fourier":
        # X_A tensor Z_B and Z_A^-1 tensor X_B.
        weights = [logical_x_weight + logical_z_weight] * 2
        blocks = 2
    elif gate == "sum":
        # X1 -> X1 X2, Z1 -> Z1, X2 -> X2, Z2 -> Z1^-1 Z2.
        weights = [
            3 * logical_x_weight,
            2 * logical_z_weight,
            2 * logical_x_weight,
            3 * logical_z_weight,
        ]
        blocks = 4
    else:
        raise ValueError(gate)
    rounds = 3
    return {
        "resource": name,
        "encoded_blocks": blocks,
        "logical_stabilizer_weights": weights,
        "logical_stabilizer_generators": len(weights),
        "verification_rounds": rounds,
        "cat_data_contacts": rounds * sum(weights),
        "cat_verification_checks": rounds * sum(w - 1 for w in weights),
        "fresh_cat_rails_prepared": rounds * sum(weights),
        "maximum_cat_length": max(weights),
        "unique_logical_state_after_stabilizer_projection": True,
    }


def component(name, q, stabilizers):
    certificate = certify(name, q, stabilizers)
    wx = weight(tuple(certificate["logical_x"]))
    wz = weight(tuple(certificate["logical_z"]))
    assert wx == wz == 3
    return {
        "logical_x_weight": wx,
        "logical_z_weight": wz,
        "fourier_choi": verification_schedule(f"{name}_fourier_choi", wx, wz, "fourier"),
        "sum_choi": verification_schedule(f"{name}_sum_choi", wx, wz, "sum"),
    }


def main():
    qubit = component("qubit", 2, QUBIT)
    qutrit = component("qutrit", 3, QUTRIT)
    for item in (qubit, qutrit):
        assert item["fourier_choi"]["logical_stabilizer_weights"] == [6, 6]
        assert item["sum_choi"]["logical_stabilizer_weights"] == [9, 6, 6, 9]

    result = {
        "schema": "marici.kitaev.s3-clifford-choi-verification.v1",
        "components": {"qubit": qubit, "qutrit": qutrit},
        "preparation_protocol": [
            "prepare individually error-corrected encoded blocks",
            "measure the listed independent logical Choi stabilizers with fresh adjacent-verified generalized cats",
            "repeat every logical stabilizer three times and majority-decode",
            "apply a logical Pauli frame to set all stabilizer eigenvalues to +1",
            "perform a final component-code recovery before coupling the resource to data",
        ],
        "peak_width_boundary": "Counts are consumed fresh-cat rails. Sequential stabilizer measurement reduces peak cat width to the listed maximum cat length plus its verification rails.",
        "verdict": "The H, F3, qubit-SUM, and qutrit-SUM Choi resources have explicit verified preparation schedules. Fourier resources use weights [6,6] and 36 cat-data contacts; SUM resources use [9,6,6,9] and 90 contacts, before final code recovery.",
    }
    output = Path(__file__).parents[1] / "results" / "s3-clifford-choi-verification.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
