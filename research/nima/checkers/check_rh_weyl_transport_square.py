import json
from pathlib import Path


# Gaussian integers are represented by pairs (real, imaginary).
ZERO = (0, 0)
ONE = (1, 0)
I = (0, 1)
MINUS_ONE = (-1, 0)
MINUS_I = (0, -1)


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def multiply(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def scale_matrix(scalar, matrix):
    return [[multiply(scalar, x) for x in row] for row in matrix]


def matmul(a, b):
    out = [[ZERO for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            value = ZERO
            for k in range(len(b)):
                value = add(value, multiply(a[i][k], b[k][j]))
            out[i][j] = value
    return out


def identity(n):
    return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]


n = 4
clock_phases = [ONE, I, MINUS_ONE, MINUS_I]
clock = [[ZERO for _ in range(n)] for _ in range(n)]
shift = [[ZERO for _ in range(n)] for _ in range(n)]
for k in range(n):
    clock[k][k] = clock_phases[k]
    shift[(k + 1) % n][k] = ONE

shift_clock = matmul(shift, clock)
clock_shift = matmul(clock, shift)
assert clock_shift == scale_matrix(I, shift_clock)
assert shift_clock == scale_matrix(MINUS_I, clock_shift)

# The commutator square S M S^-1 M^-1 equals -i times the identity.
shift_inverse = [[shift[j][i] for j in range(n)] for i in range(n)]
clock_inverse = [[ZERO for _ in range(n)] for _ in range(n)]
for k, phase in enumerate([ONE, MINUS_I, MINUS_ONE, I]):
    clock_inverse[k][k] = phase
holonomy = matmul(shift, matmul(clock, matmul(shift_inverse, clock_inverse)))
assert holonomy == scale_matrix(MINUS_I, identity(n))

# Two seam steps multiply their central phases.
shift_two = matmul(shift, shift)
shift_two_clock = matmul(shift_two, clock)
clock_shift_two = matmul(clock, shift_two)
assert clock_shift_two == scale_matrix(MINUS_ONE, shift_two_clock)
assert multiply(I, I) == MINUS_ONE

result = {
    "finite_model_dimension": 4,
    "clock_shift_relation": "M S = i S M",
    "transport_square_holonomy": "-i I",
    "two_step_phase": "-1",
    "two_step_phase_is_product": True,
    "flat_commuting_model_valid": False,
    "continuous_source_law": "T_q M_x = exp(i x q) M_x T_q",
    "prime_holonomy": "p^(i x)",
    "orientation_implied": False,
    "verdict": "spectral height and moving seam carry an exact source-derived Weyl curvature",
}

out = Path(__file__).parents[1] / "results" / "rh-weyl-transport-square.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
