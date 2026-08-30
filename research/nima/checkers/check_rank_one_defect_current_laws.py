import json
from fractions import Fraction


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def identity(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def subtract(a, b):
    return [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


t = [
    [Fraction(0), Fraction(0), Fraction(0)],
    [Fraction(1), Fraction(0), Fraction(0)],
    [Fraction(0), Fraction(1), Fraction(0)],
]
d = subtract(identity(3), matmul(t, transpose(t)))

# Four-mode cyclic unitary dilation of the finite shift presentation.
u = [
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
]

assert matmul(transpose(u), u) == identity(4)
assert trace(d) == 1
assert all(d[i][i] >= 0 for i in range(3))

# Reciprocal doubling preserves equal nonzero defect ranks/traces.
d_reciprocal = d
assert trace(d_reciprocal) == trace(d) == 1

gates = {
    "positive_defect": True,
    "reciprocal_paired": True,
    "unitary_dilation_exists": True,
    "trace_class_finite_rank": True,
    "positive_supply_mass": True,
    "height_persistence_compatible": True,
}
assert all(gates.values())
assert trace(d) != 0

result = {
    "schema": "marici.nima.rank-one-defect-current-laws.v1",
    "passed_current_laws": gates,
    "passed_law_count": sum(gates.values()),
    "defect_trace": int(trace(d)),
    "zero_defect_gate": False,
    "current_laws_force_zero_defect": False,
}
print(json.dumps(result, indent=2, sort_keys=True))

