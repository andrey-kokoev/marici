from fractions import Fraction
import json
from pathlib import Path


def identity(n):
    return [
        [Fraction(1 if i == j else 0) for j in range(n)]
        for i in range(n)
    ]


def multiply(left, right):
    rows = len(left)
    inner = len(right)
    columns = len(right[0])
    return [
        [
            sum(
                (left[i][k] * right[k][j] for k in range(inner)),
                Fraction(0),
            )
            for j in range(columns)
        ]
        for i in range(rows)
    ]


def trace(matrix):
    return sum((matrix[i][i] for i in range(len(matrix))), Fraction(0))


def power(matrix, exponent):
    result = identity(len(matrix))
    for _ in range(exponent):
        result = multiply(result, matrix)
    return result


def shift(n):
    return [
        [Fraction(1 if j == i + 1 else 0) for j in range(n)]
        for i in range(n)
    ]


def weighted_cycle(n, q):
    matrix = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for i in range(n - 1):
        matrix[i][i + 1] = Fraction(1)
    matrix[n - 1][0] = q
    return matrix


acyclic_records = []
coarse_cycle_records = []
for n in range(2, 9):
    transport = shift(n)
    traces = [trace(power(transport, k)) for k in range(1, 2 * n + 1)]
    assert all(value == 0 for value in traces)
    assert power(transport, n) == [
        [Fraction(0) for _ in range(n)] for _ in range(n)
    ]
    acyclic_records.append({"dimension": n, "all_cyclic_traces_zero": True})

    q = Fraction(2, 5)
    cycle = weighted_cycle(n, q)
    cycle_traces = [trace(power(cycle, k)) for k in range(1, 2 * n + 1)]
    for k, value in enumerate(cycle_traces, start=1):
        expected = Fraction(0) if k % n else n * q ** (k // n)
        assert value == expected
    assert cycle_traces[0] != q
    coarse_cycle_records.append(
        {
            "dimension": n,
            "first_nonzero_trace_depth": n,
            "reproduces_primitive_one_cycle_grammar": False,
        }
    )

prime_weights = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 5)]
primitive_loop = [
    [prime_weights[i] if i == j else Fraction(0) for j in range(3)]
    for i in range(3)
]
primitive_traces = []
for k in range(1, 9):
    observed = trace(power(primitive_loop, k))
    expected = sum((q ** k for q in prime_weights), Fraction(0))
    assert observed == expected
    primitive_traces.append(str(observed))

result = {
    "schema": "marici.nima.euler-feedback-loop-necessity.v1",
    "acyclic_records": acyclic_records,
    "coarse_cycle_records": coarse_cycle_records,
    "primitive_loop_traces_through_grade_eight": primitive_traces,
    "feed_forward_cut_has_euler_cyclic_grades": False,
    "primitive_one_cycle_per_prime_has_correct_grammar": True,
    "verdict": "Euler attachment requires source-authorized primitive feedback loops",
}

out = Path(__file__).parents[1] / "results" / "euler-feedback-loop-necessity.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
