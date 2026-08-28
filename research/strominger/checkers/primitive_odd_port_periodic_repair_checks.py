#!/usr/bin/env python3
"""Exact bounded checks for the primitive reflection-odd repair port."""

from __future__ import annotations

import json
import math
from pathlib import Path


def ports(x: int, y: int, n: int) -> tuple[int, int, int]:
    return ((3 * x - 2 * y) % n, (3 * y - 2 * x) % n, (x - y) % n)


def main() -> None:
    cases = []
    gates = {
        "joint_kernel_has_gcd_n_5_elements": True,
        "joint_packet_has_n_squared_over_gcd_n_5_images": True,
        "primitive_odd_port_restores_injectivity": True,
        "odd_port_is_redundant_off_exceptional_spins": True,
        "odd_port_separates_exceptional_kernel": True,
        "exceptional_spins_are_four_modulo_five": True,
        "spin_four_kernel_and_repair_match_prediction": True,
        "all_scalar_repair_ports_obey_u_minus_v_criterion": True,
    }

    for s in range(1, 21):
        n = 4 * s - 1
        joint_fibres: dict[tuple[int, int], list[tuple[int, int]]] = {}
        augmented = set()
        for x in range(n):
            for y in range(n):
                left, right, odd = ports(x, y, n)
                joint_fibres.setdefault((left, right), []).append((x, y))
                augmented.add((left, right, odd))

        kernel = joint_fibres[(0, 0)]
        divisor = math.gcd(n, 5)
        gates["joint_kernel_has_gcd_n_5_elements"] &= len(kernel) == divisor
        gates["joint_packet_has_n_squared_over_gcd_n_5_images"] &= len(joint_fibres) == n * n // divisor
        gates["primitive_odd_port_restores_injectivity"] &= len(augmented) == n * n
        gates["exceptional_spins_are_four_modulo_five"] &= (divisor == 5) == (s % 5 == 4)

        if divisor == 1:
            inv5 = pow(5, -1, n)
            for x in range(n):
                for y in range(n):
                    left, right, odd = ports(x, y, n)
                    gates["odd_port_is_redundant_off_exceptional_spins"] &= odd == inv5 * (left - right) % n
        else:
            odd_values = {ports(x, y, n)[2] for x, y in kernel}
            gates["odd_port_separates_exceptional_kernel"] &= len(odd_values) == 5

        cases.append({
            "spin": s,
            "modulus": n,
            "joint_kernel_size": len(kernel),
            "joint_image_size": len(joint_fibres),
            "augmented_image_size": len(augmented),
            "extra_port_required": divisor == 5,
        })

    spin_four_kernel = [tuple(v) for v in [(0, 0), (3, 12), (6, 9), (9, 6), (12, 3)]]
    computed = []
    for x in range(15):
        for y in range(15):
            if ports(x, y, 15)[:2] == (0, 0):
                computed.append((x, y))
    gates["spin_four_kernel_and_repair_match_prediction"] &= computed == spin_four_kernel
    gates["spin_four_kernel_and_repair_match_prediction"] &= len({ports(x, y, 15)[2] for x, y in computed}) == 5
    for u in range(15):
        for v in range(15):
            observed = {(u * x + v * y) % 15 for x, y in computed}
            predicted_faithful = (u - v) % 5 != 0
            gates["all_scalar_repair_ports_obey_u_minus_v_criterion"] &= (len(observed) == 5) == predicted_faithful

    result = {
        "theorem": "one primitive reflection-odd port is required exactly when spin is 4 modulo 5",
        "range": {"spin_min": 1, "spin_max": 20},
        "gates": gates,
        "passed": sum(gates.values()),
        "total": len(gates),
        "all_passed": all(gates.values()),
        "cases": cases,
        "spin_four_kernel": [list(v) for v in computed],
        "spin_four_odd_values": sorted({ports(x, y, 15)[2] for x, y in computed}),
    }
    target = Path(__file__).resolve().parents[1] / "results" / "primitive_odd_port_periodic_repair_checks.json"
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("passed", "total", "all_passed", "spin_four_kernel", "spin_four_odd_values")}, indent=2))

    if not result["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
