"""Minimal exact controls for extension blindness and torsion rationalization."""

from __future__ import annotations

import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "results" / "spectral_sequence_extension_blindness.json"


def order(element, add, zero):
    value = zero
    for candidate in range(1, 9):
        value = add(value, element)
        if value == zero:
            return candidate
    raise AssertionError("order bound exceeded")


def main():
    z4 = list(range(4))
    v4 = [(left, right) for left in range(2) for right in range(2)]
    z4_orders = sorted(order(x, lambda a, b: (a + b) % 4, 0) for x in z4)
    v4_orders = sorted(
        order(x, lambda a, b: ((a[0] + b[0]) % 2, (a[1] + b[1]) % 2), (0, 0))
        for x in v4
    )
    packet = {
        "schema": "marici.spectral-sequence-extension-blindness.v1",
        "nonsplit_filtered_group": {
            "group": "Z/4",
            "filtration": "0 < 2Z/4 < Z/4",
            "associated_graded_orders": [2, 2],
            "element_orders": z4_orders,
        },
        "split_filtered_group": {
            "group": "Z/2 direct-sum Z/2",
            "filtration": "0 < first Z/2 < (Z/2)^2",
            "associated_graded_orders": [2, 2],
            "element_orders": v4_orders,
        },
        "same_zero_differential_spectral_sequence": True,
        "filtered_objects_are_not_isomorphic": z4_orders != v4_orders,
        "torsion_rationalization": {
            "identity": "(Z/n) tensor_Z Q = 0 for n>0",
            "z4_rational_rank": 0,
            "v4_rational_rank": 0,
            "consequence": "rationalization erases torsion extension information rather than protecting it",
        },
    }
    packet["passed"] = (
        packet["same_zero_differential_spectral_sequence"]
        and packet["filtered_objects_are_not_isomorphic"]
        and packet["torsion_rationalization"]["z4_rational_rank"] == 0
        and packet["torsion_rationalization"]["v4_rational_rank"] == 0
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    if not packet["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
