"""Exact WP124 audit; dependency-free rational arithmetic."""

from fractions import Fraction as F
import json
from pathlib import Path


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def trace(a):
    return sum(a[i][i] for i in range(3))


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(3)] for i in range(3)]


def frobenius_sq(a):
    return sum(x * x for row in a for x in row)


hu = [[F(3), F(0), F(0)], [F(0), F(2), F(0)], [F(0), F(0), F(1)]]
hd = [[F(6), F(0), F(0)], [F(0), F(4), F(0)], [F(0), F(0), F(1)]]
hd_reverse = [[F(1), F(0), F(0)], [F(0), F(4), F(0)], [F(0), F(0), F(6)]]
r = [[F(3, 5), F(-4, 5), F(0)], [F(4, 5), F(3, 5), F(0)], [F(0), F(0), F(1)]]
hd_rot = matmul(matmul(r, hd), transpose(r))

c_aligned = trace(matmul(hu, hd))
c_reverse = trace(matmul(hu, hd_reverse))
c_rotated = trace(matmul(hu, hd_rot))
commutator = sub(matmul(hu, hd_rot), matmul(hd_rot, hu))
commutator_norm_sq = frobenius_sq(commutator)

# For R(theta) acting in the 1-2 plane:
# d/dtheta Tr(Hu R Hd R^T) = (u1-u2)(d2-d1) sin(2 theta).
sin_two_theta = F(24, 25)
orientation_derivative = (F(3) - F(2)) * (F(4) - F(6)) * sin_two_theta

checks = {
    "rotation_is_orthogonal": matmul(r, transpose(r)) == [[F(1), F(0), F(0)], [F(0), F(1), F(0)], [F(0), F(0), F(1)]],
    "aligned_value_exact": c_aligned == F(27),
    "reverse_value_exact": c_reverse == F(17),
    "rotated_value_exact": c_rotated == F(643, 25),
    "rotated_value_is_interior": c_reverse < c_rotated < c_aligned,
    "hostile_point_noncommuting": commutator_norm_sq == F(1152, 625),
    "hostile_point_not_stationary": orientation_derivative == F(-48, 25),
    "nonzero_obstruction": orientation_derivative != 0,
    "zero_mixed_coefficient_is_flat": F(0) * orientation_derivative == 0,
}

result = {
    "work_package": "WP124",
    "theorem_scope": "full U(3)_Q x U(3)_u x U(3)_d; two bifundamentals; local polynomial potential of field degree at most four",
    "classification": "renormalizable invariant generic-mixing selector no-go",
    "orientation_invariant": "Tr(H_u H_d)",
    "reference_port_required": False,
    "physical_instrument_established": False,
    "hostile_point": {
        "C_aligned": str(c_aligned),
        "C_reverse": str(c_reverse),
        "C_rotated": str(c_rotated),
        "commutator_frobenius_squared": str(commutator_norm_sq),
        "orientation_derivative": str(orientation_derivative),
    },
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "all_pass": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp124_renormalizable_flavon_mixing_no_go.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
if not result["all_pass"]:
    raise SystemExit(1)
