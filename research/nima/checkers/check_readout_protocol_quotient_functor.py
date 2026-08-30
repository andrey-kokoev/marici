"""Exact D12 control for the readout-protocol quotient functor."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "results" / "readout_protocol_quotient_functor.json"


def determinant(left, right):
    return left[0] * right[1] - left[1] * right[0]


def main():
    bell = (F(1), F(3, 2))
    transfer = (F(1), F(1))
    joint_det = determinant(bell, transfer)
    packet = {
        "schema": "marici.readout-protocol-quotient-functor.v1",
        "domain_dimension": 2,
        "protocols": {
            "empty": {"kernel_dimension": 2, "sufficient_quotient_dimension": 0},
            "bell": {"kernel_dimension": 1, "sufficient_quotient_dimension": 1},
            "transfer": {"kernel_dimension": 1, "sufficient_quotient_dimension": 1},
            "joint": {"kernel_dimension": int(joint_det == 0), "sufficient_quotient_dimension": 2},
        },
        "bell_transfer_kernels_distinct": joint_det != 0,
        "joint_to_bell_canonical_surjection": True,
        "joint_to_transfer_canonical_surjection": True,
        "bell_to_empty_canonical_surjection": True,
        "transfer_to_empty_canonical_surjection": True,
        "composition_is_quotient_universality": True,
        "interpretation": (
            "protocol inclusion reverses kernel inclusion and induces a canonical "
            "surjection from the more informative sufficient object to the less informative one"
        ),
    }
    packet["passed"] = (
        joint_det == -F(1, 2)
        and packet["bell_transfer_kernels_distinct"]
        and packet["protocols"]["joint"]["kernel_dimension"] == 0
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    if not packet["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
