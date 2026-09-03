"""Exact point-interval probe of the apparent Chart-1 weak Dq locus."""
import json
from fractions import Fraction as F
from theta_fixedpoint_interval import FixedDual, cancellation_free_residual_quotient

Q0, Q1 = F(39, 100), F(41, 100)
Y0, Y1 = F(3, 100), F(7, 200)
N = 40
best = None
for i in range(N + 1):
    q0 = Q0 + (Q1 - Q0) * F(i, N)
    for j in range(N + 1):
        y0 = Y0 + (Y1 - Y0) * F(j, N)
        value = cancellation_free_residual_quotient(
            FixedDual(q0, dq=1), FixedDual(y0, dy=1))
        row = (value.dq.lo, value.dq.hi, value.dy.lo, value.dy.hi, q0, y0)
        if best is None or row[0] < best[0]:
            best = row
result = {
    "points": (N + 1) ** 2,
    "minimum_dq_lower_scaled": str(best[0]),
    "dq_upper_scaled": str(best[1]),
    "dy_lower_scaled": str(best[2]),
    "dy_upper_scaled": str(best[3]),
    "q": str(best[4]),
    "y": str(best[5]),
}
print(json.dumps(result, indent=2))
assert best[0] > 0 and best[3] < 0
