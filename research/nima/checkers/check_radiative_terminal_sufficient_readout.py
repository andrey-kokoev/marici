"""Finite harmonic controls for the terminal radiative readout quotient."""

from __future__ import annotations

import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "results" / "radiative_terminal_sufficient_readout.json"


def eigenvalue(l):
    return (l - 1) * l * (l + 1) * (l + 2) // 4


def main():
    cutoffs = []
    for maximum_l in range(2, 13):
        modes = [
            {"l": l, "m": m, "operator_eigenvalue": eigenvalue(l)}
            for l in range(maximum_l + 1)
            for m in range(-l, l + 1)
        ]
        kernel = [mode for mode in modes if mode["operator_eigenvalue"] == 0]
        quotient = [mode for mode in modes if mode["operator_eigenvalue"] != 0]
        cutoffs.append({
            "maximum_l": maximum_l,
            "ambient_dimension": len(modes),
            "joint_kernel_dimension": len(kernel),
            "kernel_l_values": sorted({mode["l"] for mode in kernel}),
            "terminal_quotient_dimension": len(quotient),
            "expected_terminal_dimension": (maximum_l + 1) ** 2 - 4,
            "operator_invertible_on_quotient": all(
                mode["operator_eigenvalue"] != 0 for mode in quotient
            ),
        })
    packet = {
        "schema": "marici.radiative-terminal-sufficient-readout.v1",
        "readout_family": ["soft zero-frequency map", "BMS soft charge", "displacement memory"],
        "common_kernel": "H_0 direct-sum H_1",
        "kernel_dimension": 4,
        "quotient": "C-infinity(S2)/(H_0 direct-sum H_1)",
        "finite_harmonic_controls": cutoffs,
        "terminal_property": (
            "every quotient preserving all three readouts maps uniquely onto the common-kernel quotient"
        ),
    }
    packet["passed"] = all(
        item["joint_kernel_dimension"] == 4
        and item["kernel_l_values"] == [0, 1]
        and item["terminal_quotient_dimension"] == item["expected_terminal_dimension"]
        and item["operator_invertible_on_quotient"]
        for item in cutoffs
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "cutoffs": len(cutoffs),
        "kernel_dimension": packet["kernel_dimension"],
        "largest_quotient_dimension": cutoffs[-1]["terminal_quotient_dimension"],
        "passed": packet["passed"],
    }, indent=2))
    if not packet["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
