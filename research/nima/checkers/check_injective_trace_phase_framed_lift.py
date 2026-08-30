import json
from fractions import Fraction
from pathlib import Path


def matmul(left, right):
    rows = len(left)
    columns = len(right[0])
    middle = len(right)
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(middle))
            for j in range(columns)
        ]
        for i in range(rows)
    ]


def matvec(matrix, vector):
    return [
        sum(entry * value for entry, value in zip(row, vector))
        for row in matrix
    ]


tau = [
    [Fraction(1), Fraction(0)],
    [Fraction(0), Fraction(1)],
    [Fraction(1), Fraction(1)],
]
left_inverse = [
    [Fraction(1), Fraction(0), Fraction(0)],
    [Fraction(0), Fraction(1), Fraction(0)],
]
fourier = [
    [Fraction(0), Fraction(1)],
    [Fraction(1), Fraction(0)],
]

j_on_ambient = matmul(matmul(tau, fourier), left_inverse)
assert matmul(j_on_ambient, tau) == matmul(tau, fourier)

source_vectors = [
    [Fraction(a), Fraction(b)]
    for a in range(-2, 3)
    for b in range(-2, 3)
]
for source in source_vectors:
    trace = matvec(tau, source)
    induced = matvec(j_on_ambient, trace)
    transformed_trace = matvec(tau, matvec(fourier, source))
    assert induced == transformed_trace

minus_fourier = [[-entry for entry in row] for row in fourier]
minus_j = matmul(matmul(tau, minus_fourier), left_inverse)
assert minus_j != j_on_ambient

# Noninjective trace with a kernel not preserved by Fourier.
tau_bad = [[Fraction(1), Fraction(0)]]
zero_source = [Fraction(0), Fraction(0)]
kernel_source = [Fraction(0), Fraction(1)]
assert matvec(tau_bad, zero_source) == matvec(tau_bad, kernel_source) == [0]
assert matvec(tau_bad, matvec(fourier, zero_source)) == [0]
assert matvec(tau_bad, matvec(fourier, kernel_source)) == [1]

result = {
    "schema": "marici.injective-trace-phase-framed-lift.v1",
    "injective_trace_shape": [3, 2],
    "source_vectors_checked": len(source_vectors),
    "intertwining_identity_exact": True,
    "representative_independence_exact": True,
    "opposite_phase_operator_lifts_distinct": True,
    "noninjective_hostile_same_trace": [0],
    "noninjective_hostile_transformed_traces": [[0], [1]],
    "noninjective_descent_fails": True,
    "verdict": "injective trace supplies an algebraic phase-framed lift but not a physical controlled implementation",
}

output = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "injective-trace-phase-framed-lift.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
