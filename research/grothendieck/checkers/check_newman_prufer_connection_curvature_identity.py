from fractions import Fraction as F


def connection(jets):
    a, b, c, d, _ = map(F, jets)
    gram = a * a + b * b
    omega_x = (a * c - b * b) / gram
    omega_lambda = (b * c - a * d) / gram
    return omega_x, omega_lambda


def closure_numerators(jets):
    a, b, c, d, e = map(F, jets)
    gram = a * a + b * b
    nx = a * c - b * b
    nl = -c * c - a * e + 2 * b * d
    gram_l = -2 * a * c - 2 * b * d
    ml = b * c - a * d
    mx = c * c - a * e
    gram_x = 2 * a * b + 2 * b * c
    return nl * gram - nx * gram_l, mx * gram - ml * gram_x


fixtures = (
    (1, 2, 3, 4, 5),
    (3, -1, 7, -2, 11),
    (-2, 5, -3, 13, -7),
    (8, 0, -1, 4, 9),
)

for jets in fixtures:
    omega_x, omega_lambda = connection(jets)
    assert omega_x == F(jets[0] * jets[2] - jets[1] ** 2,
                        jets[0] ** 2 + jets[1] ** 2)
    assert omega_lambda == F(jets[1] * jets[2] - jets[0] * jets[3],
                             jets[0] ** 2 + jets[1] ** 2)
    lhs, rhs = closure_numerators(jets)
    assert lhs == rhs

# At a simple real zero, the spatial phase density is exactly -1.
for slope in (-9, -2, 1, 6):
    omega_x, _ = connection((0, slope, 17, 3, 5))
    assert omega_x == -1

print("newman_prufer_connection_curvature_identity: 16/16 gates passed")
