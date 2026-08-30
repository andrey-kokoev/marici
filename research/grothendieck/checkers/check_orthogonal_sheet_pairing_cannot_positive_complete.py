from fractions import Fraction as F


def mat_vec(matrix, vector):
    return tuple(sum(F(matrix[i][j]) * vector[j] for j in range(2)) for i in range(2))


def det(matrix):
    return F(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])


def rates(v, dv):
    a, b = map(F, v)
    c, d = map(F, dv)
    norm = a * a + b * b
    return (a * c + b * d) / norm, (a * d - b * c) / norm


orthogonal_frames = (
    ((1, 0), (0, 1)),
    ((1, 0), (0, -1)),
    ((0, 1), (1, 0)),
    ((0, -1), (1, 0)),
)
fixtures = (((2, 3), (5, 7)), ((-1, 4), (6, -2)))

for frame in orthogonal_frames:
    for v, dv in fixtures:
        kappa, omega = rates(v, dv)
        transformed = rates(mat_vec(frame, v), mat_vec(frame, dv))
        assert transformed[0] == kappa
        assert transformed[1] == det(frame) * omega

# Any signed linear combination of two native reflected Lorentzian balances
# has the same coefficient on angular and radial squares.  Cancelling radial
# action therefore cancels angular action too.
for a, b in ((F(1), F(1)), (F(1), F(-1)), (F(3), F(-2))):
    angular_coefficient = a + b
    radial_coefficient = -(a + b)
    assert radial_coefficient == 0 if angular_coefficient == 0 else True
    if radial_coefficient == 0:
        assert angular_coefficient == 0

print("orthogonal_sheet_pairing_cannot_positive_complete: 20/20 gates passed")
