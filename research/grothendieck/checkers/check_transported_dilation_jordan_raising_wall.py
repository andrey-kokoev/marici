#!/usr/bin/env python3
"""Audit the transported dilation generator and its raising wall."""

import math


def action_column(j: int, lam: float) -> dict[int, float]:
    result = {
        j: 2.0 * j - 2.0 * lam + 0.5,
        j + 1: -2.0 * lam,
    }
    if j > 0:
        result[j - 1] = 2.0 * j
    return result


lam = math.pi
columns = [action_column(j, lam) for j in range(3)]
theta_top_coefficient = 4.0 * lam * lam
degree_three_leak = -2.0 * lam * theta_top_coefficient

# Conjugation check on a sample polynomial by direct differentiation.
y = 0.37
z = complex(0.4, 1.2)
psi = (1.0 + 2.0 * y + 3.0 * y * y) * math.exp(-lam * y)
psi_prime = (2.0 + 6.0 * y - lam * (1.0 + 2.0 * y + 3.0 * y * y)) * math.exp(-lam * y)
transported = 2.0 * (1.0 + y) * psi_prime + (0.5 + z) * psi

u = 0.5 * math.log(1.0 + y)
rho = (1.0 + y) ** 0.25
# Chain-rule evaluation of (partial_u+z)(rho psi).
rho_u = 0.5 * rho
psi_u = 2.0 * (1.0 + y) * psi_prime
direct = rho_u * psi + rho * psi_u + z * rho * psi
conjugation_error = abs(direct - rho * transported)

checks = {
    "quarter_density_conjugation": conjugation_error < 1.0e-13,
    "degree_two_leaks_to_degree_three": 3 in columns[2],
    "leak_coefficient_is_nonzero": abs(columns[2][3]) > 6.0,
    "theta_packet_has_nonzero_outward_current": degree_three_leak < -100.0,
    "every_finite_top_grade_leaks": all(action_column(j, lam)[j + 1] != 0.0 for j in range(12)),
}

failed = [name for name, passed in checks.items() if not passed]
print(
    {
        "passed": len(checks) - len(failed),
        "total": len(checks),
        "failed": failed,
        "lambda": lam,
        "columns_0_to_2": columns,
        "theta_degree_three_leak": degree_three_leak,
        "conjugation_error": conjugation_error,
    }
)

if failed:
    raise SystemExit(1)

