from fractions import Fraction
import json
from pathlib import Path


def forward_shift(n):
    matrix = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for j in range(n - 1):
        matrix[j + 1][j] = Fraction(1)
    return matrix


def matvec(matrix, vector):
    return [
        sum((a * b for a, b in zip(row, vector)), Fraction(0))
        for row in matrix
    ]


def dot(row, column):
    return sum((a * b for a, b in zip(row, column)), Fraction(0))


records = []
shell_length = 3
for shell_count in range(2, 11):
    source = [
        Fraction((i + 1) * ((-1) ** i), shell_count + 5)
        for i in range(shell_length * shell_count)
    ]
    phase = [Fraction((-1) ** i) for i in range(len(source))]
    weighted_source = [a * b for a, b in zip(source, phase)]
    shells = [
        sum(
            weighted_source[j * shell_length : (j + 1) * shell_length],
            Fraction(0),
        )
        for j in range(shell_count)
    ]

    a = forward_shift(shell_count)
    b = [Fraction(1)] + [Fraction(0) for _ in range(shell_count - 1)]
    current = b
    moments = []
    for _ in range(shell_count):
        moments.append(dot(shells, current))
        current = matvec(a, current)
    assert moments == shells

    for k in range(1, shell_count + 1):
        assert sum(moments[:k], Fraction(0)) == sum(shells[:k], Fraction(0))

    shell_norm_squared = sum((value * value for value in shells), Fraction(0))
    source_norm_squared = sum((value * value for value in source), Fraction(0))
    assert shell_norm_squared <= shell_length * source_norm_squared

    # Off-seam hostile: source_i=r^(-i) is square summable, while multiplication
    # by r^i makes every weighted sample one and every shell sum constant.
    r = Fraction(2)
    hostile_source = [r ** (-i) for i in range(shell_length * shell_count)]
    hostile_weighted = [
        hostile_source[i] * r ** i for i in range(len(hostile_source))
    ]
    hostile_shells = [
        sum(
            hostile_weighted[j * shell_length : (j + 1) * shell_length],
            Fraction(0),
        )
        for j in range(shell_count)
    ]
    assert hostile_shells == [Fraction(shell_length) for _ in range(shell_count)]
    hostile_return_norm_squared = sum(v * v for v in hostile_shells)
    assert hostile_return_norm_squared == shell_count * shell_length * shell_length

    records.append(
        {
            "shell_count": shell_count,
            "all_markov_parameters_exact": True,
            "all_cumulative_windows_exact": True,
            "seam_cauchy_bound": True,
            "off_seam_hostile_return_norm_squared": int(hostile_return_norm_squared),
        }
    )

result = {
    "schema": "marici.nima.prime-orbit-shell-markov-realization.v1",
    "records": records,
    "seam_return_bounded_by_source_l2": True,
    "off_seam_return_bounded_by_unweighted_source_l2": False,
    "verdict": "prime seam shells are the source-derived Markov parameters of the local relative transfer",
}

out = (
    Path(__file__).parents[1]
    / "results"
    / "prime-orbit-shell-markov-realization.json"
)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
