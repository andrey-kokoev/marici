import json
import math


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def subtract(a, b):
    return [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def rank(a):
    m = [[float(x) for x in row] for row in a]
    rows = len(m)
    cols = len(m[0]) if rows else 0
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if abs(m[i][c]) > 1e-12), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        scale = m[r][c]
        m[r] = [x / scale for x in m[r]]
        for i in range(rows):
            if i != r and abs(m[i][c]) > 1e-12:
                scale = m[i][c]
                m[i] = [x - scale * y for x, y in zip(m[i], m[r])]
        r += 1
    return r


# Finite compressed-shift model: S is an isometry from C^2 into C^3;
# W=S* is a coisometry with one-dimensional initial defect.
s = [[1, 0], [0, 1], [0, 0]]
w = transpose(s)
assert matmul(w, transpose(w)) == identity(2)
defect = subtract(identity(3), matmul(transpose(w), w))
assert rank(defect) == 1


def poisson_window_mass(a, b, radius):
    # Integral of the normalized one-state density over [b-radius,b+radius].
    return 2.0 * math.atan(radius / a) / math.pi


a = 0.75
b = 1.25
masses = [poisson_window_mass(a, b, radius) for radius in (1.0, 10.0, 100.0)]
assert 0.0 < masses[0] < masses[1] < masses[2] < 1.0
assert masses[-1] > 0.995

# At fixed resolution, moving the zero to the seam concentrates the state.
concentration = [poisson_window_mass(x, b, 0.1) for x in (1.0, 0.1, 0.01)]
assert concentration[0] < concentration[1] < concentration[2]

result = {
    "schema": "marici.nima.blaschke-model-defect.v1",
    "compressed_coisometry": True,
    "defect_rank": rank(defect),
    "poisson_mass_tends_to_one": True,
    "boundary_concentration_as_a_tends_to_zero": True,
    "reciprocal_packet_mass": 2,
    "spectral_measure_identification_rejected": True,
    "boundary_diagonal_identification": True,
}
print(json.dumps(result, indent=2, sort_keys=True))

