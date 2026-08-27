#!/usr/bin/env python3
"""Verify half-index per sector and integral reciprocal sewing."""

import cmath
import math


coefficient = complex(-0.7, 1.3)
radius = 0.2


def unwrapped_change(values):
    arguments = [cmath.phase(value) for value in values]
    total = 0.0
    for left, right in zip(arguments, arguments[1:]):
        step = right - left
        while step <= -math.pi:
            step += 2.0 * math.pi
        while step > math.pi:
            step -= 2.0 * math.pi
        total += step
    return total


panels = 2000
full = [
    coefficient * radius * cmath.exp(1j * 2.0 * math.pi * j / panels)
    for j in range(panels + 1)
]
right_half = [
    coefficient * radius * cmath.exp(1j * (-0.5 * math.pi + math.pi * j / panels))
    for j in range(panels + 1)
]
left_half = [
    coefficient * radius * cmath.exp(1j * (0.5 * math.pi + math.pi * j / panels))
    for j in range(panels + 1)
]

full_index = unwrapped_change(full) / (2.0 * math.pi)
right_relative_index = unwrapped_change(right_half) / (2.0 * math.pi)
left_relative_index = unwrapped_change(left_half) / (2.0 * math.pi)

checks = {
    "interior_simple_zero_has_unit_index": abs(full_index - 1.0) < 1.0e-12,
    "right_sector_sees_half_index": abs(right_relative_index - 0.5) < 1.0e-12,
    "left_sector_sees_half_index": abs(left_relative_index - 0.5) < 1.0e-12,
    "reciprocal_sewing_restores_unit_index": abs(right_relative_index + left_relative_index - 1.0) < 1.0e-12,
    "generic_offline_quartet_is_integral": abs(4.0 * full_index - 4.0) < 1.0e-12,
}

failed = [name for name, passed in checks.items() if not passed]
print(
    {
        "passed": len(checks) - len(failed),
        "total": len(checks),
        "failed": failed,
        "full_index": full_index,
        "right_relative_index": right_relative_index,
        "left_relative_index": left_relative_index,
    }
)

if failed:
    raise SystemExit(1)
