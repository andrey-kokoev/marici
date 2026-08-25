import math


def constant_eigenvalue(n: int, a: float = 1.0) -> float:
    return 1.0 - 0.5 * a * math.log(n)


assert constant_eigenvalue(2) > 0
assert constant_eigenvalue(7) > 0
assert constant_eigenvalue(8) < 0
assert all(constant_eigenvalue(n) >= 0 for n in range(1, 8))

# Direct step-function verification of
# R_v = v D_v - integral_0^v D_q dq.
z = 0.37 + 0.11j
v = math.log(11.0)


def chi(n: int) -> complex:
    return n ** (-0.5 - 1j * z)


direct_repair = sum(math.log(n) * chi(n) for n in range(1, 12))
integral_d = 0j
for n in range(1, 12):
    left = math.log(n)
    right = v if n == 11 else math.log(n + 1)
    integral_d += (right - left) * sum(chi(k) for k in range(1, n + 1))
summation_by_parts = v * sum(chi(n) for n in range(1, 12)) - integral_d
assert abs(direct_repair - summation_by_parts) < 1e-12

print(
    {
        "status": "passed",
        "prime_two_margin": constant_eigenvalue(2),
        "last_nonnegative_integer_horizon": 7,
        "first_negative_integer_horizon": 8,
        "n8_constant_eigenvalue": constant_eigenvalue(8),
        "summation_by_parts_residual": abs(direct_repair - summation_by_parts),
        "disposition": "universal_volterra_orientation_falsified",
    }
)
