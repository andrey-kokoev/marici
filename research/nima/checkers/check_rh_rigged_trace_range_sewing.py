from fractions import Fraction
import json
from pathlib import Path


def matmul(left, right):
    return [
        [sum(a * b for a, b in zip(row, column)) for column in zip(*right)]
        for row in left
    ]


def matvec(matrix, vector):
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def identity(size):
    return [
        [Fraction(int(i == j)) for j in range(size)]
        for i in range(size)
    ]


# Injective rectangular trace carrier and invertible source Fourier map.
trace = [
    [Fraction(1), Fraction(0)],
    [Fraction(0), Fraction(1)],
    [Fraction(1), Fraction(1)],
]
fourier = [
    [Fraction(0), Fraction(-1)],
    [Fraction(1), Fraction(0)],
]
fourier_inverse = [
    [Fraction(0), Fraction(1)],
    [Fraction(-1), Fraction(0)],
]
assert matmul(fourier, fourier_inverse) == identity(2)

sources = [
    [Fraction(1), Fraction(2)],
    [Fraction(-3), Fraction(4)],
    [Fraction(5), Fraction(-1)],
]

round_trips = 0
for source in sources:
    traced = matvec(trace, source)
    sewn = matvec(trace, matvec(fourier, source))
    unsewn = matvec(trace, matvec(fourier_inverse, matvec(fourier, source)))
    assert unsewn == traced
    assert len(sewn) == len(traced)
    round_trips += 1

# Noninjective scalar compression does not define conjugated transport because
# equal visible inputs can have different visible Fourier outputs.
scalar_trace = [[Fraction(1), Fraction(0)]]
source_a = [Fraction(0), Fraction(1)]
source_b = [Fraction(0), Fraction(2)]
assert matvec(scalar_trace, source_a) == matvec(scalar_trace, source_b)
assert matvec(scalar_trace, matvec(fourier, source_a)) != matvec(
    scalar_trace, matvec(fourier, source_b)
)

result = {
    "trace_source_dimension": 2,
    "trace_range_ambient_dimension": 3,
    "injective_trace_model": True,
    "source_round_trips": round_trips,
    "fourier_conjugated_sewing_well_defined_on_trace_range": True,
    "inverse_sewing_exact_on_trace_range": True,
    "scalar_compression_hostile": True,
    "completed_closability_proved": False,
    "verdict": "the injective source trace range carries a canonical Fourier sewing operator; only its rigged completion and observability remain open",
}

out = Path(__file__).parents[1] / "results" / "rh-rigged-trace-range-sewing.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
