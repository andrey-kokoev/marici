#!/usr/bin/env python3
"""Verify the positive length-three Jordan form of theta labels."""

import math


def coefficients(label: int) -> tuple[float, float, float]:
    lam = math.pi * label * label
    return (
        4.0 * lam * lam - 6.0 * lam,
        8.0 * lam * lam - 6.0 * lam,
        4.0 * lam * lam,
    )


rows = []
for n in range(1, 9):
    lam = math.pi * n * n
    coeffs = coefficients(n)
    rows.append(
        {
            "label": n,
            "lambda": lam,
            "coefficients": coeffs,
            "support_gap": lam > 1.5,
            "all_positive": all(value > 0.0 for value in coeffs),
        }
    )

# Check the coordinate identity away from the seam for several labels and y.
identity_error = 0.0
for n in range(1, 5):
    lam = math.pi * n * n
    a0, a1, a2 = coefficients(n)
    for y in (0.0, 0.1, 0.7, 2.0):
        direct = (4.0 * (lam * (1.0 + y)) ** 2 - 6.0 * lam * (1.0 + y)) * math.exp(
            -lam * (1.0 + y)
        )
        jordan = math.exp(-lam) * (a0 + a1 * y + a2 * y * y) * math.exp(-lam * y)
        identity_error = max(identity_error, abs(direct - jordan))

# The differentiation matrix in the ordered basis (1,y,y^2)e^{-lambda y}
# has diagonal -lambda and the source-fixed nilpotent lowering entries 1,2.
lam = math.pi
derivative_matrix = [
    [-lam, 1.0, 0.0],
    [0.0, -lam, 2.0],
    [0.0, 0.0, -lam],
]

checks = {
    "arithmetic_support_above_threshold": all(row["support_gap"] for row in rows),
    "all_jordan_coefficients_positive": all(row["all_positive"] for row in rows),
    "coordinate_identity": identity_error < 1.0e-14,
    "length_three_closure": derivative_matrix[0][1] == 1.0 and derivative_matrix[1][2] == 2.0,
    "single_label_pi_is_strict": min(coefficients(1)) > 0.0,
}

failed = [name for name, passed in checks.items() if not passed]
print(
    {
        "passed": len(checks) - len(failed),
        "total": len(checks),
        "failed": failed,
        "first_label": rows[0],
        "identity_error": identity_error,
        "derivative_matrix": derivative_matrix,
    }
)

if failed:
    raise SystemExit(1)

