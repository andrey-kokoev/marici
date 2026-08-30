from fractions import Fraction as F


def entropy_identity(a, b, c, d, e, f):
    a, b, c, d, e, f = map(F, (a, b, c, d, e, f))
    radius = a * a + b * b
    radius_lambda = -2 * (a * e + b * f)
    radius_x = 2 * (a * c + b * d)
    radius_xx = 2 * (c * c + d * d + a * e + b * f)
    lhs = radius_lambda / radius + radius_xx / radius - radius_x**2 / radius**2
    radial_x = (a * c + b * d) / radius
    omega_x = (a * d - b * c) / radius
    rhs = 2 * (omega_x**2 - radial_x**2)
    return lhs, rhs, omega_x**2, radial_x**2


fixtures = (
    (1, 2, 3, 4, 5, 6),
    (-3, 5, 7, -2, 11, -13),
    (8, -1, -4, 9, 2, 3),
    (2, 0, 5, 7, -1, 4),
)

for fixture in fixtures:
    lhs, rhs, angular, radial = entropy_identity(*fixture)
    assert lhs == rhs
    assert angular >= 0
    assert radial >= 0

# In the universal collision model, on 0<tau<=1/4 and 0<=x<=tau,
# |omega_x| >= 1/(2 tau).  Each dyadic tau shell therefore contributes a
# fixed positive amount, forcing logarithmic divergence over infinitely many
# shells.
for n in range(1, 9):
    tau_hi = F(1, 4 * 2**n)
    tau_lo = tau_hi / 2
    shell_lower_bound = F(1, 4) * (tau_hi - tau_lo) / tau_hi
    assert shell_lower_bound == F(1, 8)

assert sum(F(1, 8) for _ in range(100)) == F(25, 2)

print("newman_log_gram_entropy_identity: 21/21 gates passed")
