#!/usr/bin/env python3
"""Audit reciprocal Green identities and the surviving bulk current."""

import cmath


z = complex(0.3, 0.8)
a = z.real

# Exact source f(q)=exp(-q).
g_plus_0 = 1.0 / (1.0 - z)
g_minus_0 = 1.0 / (1.0 + z)
norm_plus = 0.5 * abs(g_plus_0) ** 2
norm_minus = 0.5 * abs(g_minus_0) ** 2
pair_plus = 0.5 * g_plus_0.conjugate()
pair_minus = 0.5 * g_minus_0.conjugate()

green_plus_left = -abs(g_plus_0) ** 2 + 2.0 * a * norm_plus
green_plus_right = -2.0 * pair_plus.real
green_minus_left = abs(g_minus_0) ** 2 + 2.0 * a * norm_minus
green_minus_right = 2.0 * pair_minus.real

bulk_from_tails = 2.0 * (pair_minus - pair_plus).real
summed_green = 2.0 * a * (norm_plus + norm_minus) + abs(g_minus_0) ** 2 - abs(g_plus_0) ** 2

# The zero condition is anti-diagonal and therefore cancels the oriented seam
# quadratic form independently of whether this hostile source has a zero.
sample_endpoint = complex(0.7, -1.1)
anti_endpoint = -sample_endpoint
oriented_seam = abs(anti_endpoint) ** 2 - abs(sample_endpoint) ** 2

checks = {
    "plus_green_identity": abs(green_plus_left - green_plus_right) < 1.0e-13,
    "minus_green_identity": abs(green_minus_left - green_minus_right) < 1.0e-13,
    "summed_bulk_identity": abs(summed_green - bulk_from_tails) < 1.0e-13,
    "zero_state_seam_cancellation": abs(oriented_seam) < 1.0e-15,
    "generic_bulk_current_survives": abs(bulk_from_tails) > 0.05,
}

failed = [name for name, passed in checks.items() if not passed]
print(
    {
        "passed": len(checks) - len(failed),
        "total": len(checks),
        "failed": failed,
        "bulk_current": bulk_from_tails,
        "summed_green": summed_green,
        "oriented_seam": oriented_seam,
    }
)

if failed:
    raise SystemExit(1)
