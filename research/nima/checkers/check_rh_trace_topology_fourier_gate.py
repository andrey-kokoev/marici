from fractions import Fraction
import json
from pathlib import Path


def matmul(left, right):
    return [
        [sum(a * b for a, b in zip(row, column)) for column in zip(*right)]
        for row in left
    ]


def inverse_diagonal(matrix):
    return [
        [Fraction(1, matrix[0][0]), Fraction(0)],
        [Fraction(0), Fraction(1, matrix[1][1])],
    ]


fourier = [
    [Fraction(0), Fraction(-1)],
    [Fraction(1), Fraction(0)],
]

cutoffs = [1, 2, 4, 8, 16]
operator_growth = []
for cutoff in cutoffs:
    trace_observer = [
        [Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(1, cutoff)],
    ]
    observed_fourier = matmul(
        matmul(trace_observer, fourier),
        inverse_diagonal(trace_observer),
    )
    # Matrix is [[0,-N],[1/N,0]], so its Euclidean operator norm is N.
    assert observed_fourier == [
        [Fraction(0), Fraction(-cutoff)],
        [Fraction(1, cutoff), Fraction(0)],
    ]
    operator_growth.append(cutoff)

assert operator_growth[-1] > operator_growth[0]

# Restoring both source coordinates gives the source-pulled topology and a
# uniformly norm-one Fourier action.
restored_observer = [
    [Fraction(1), Fraction(0)],
    [Fraction(0), Fraction(1)],
]
restored_fourier = matmul(
    matmul(restored_observer, fourier),
    inverse_diagonal(restored_observer),
)
assert restored_fourier == fourier

result = {
    "cutoffs": cutoffs,
    "weakened_topology_fourier_norms": operator_growth,
    "each_finite_sewing_defined": True,
    "uniform_fourier_bound_in_weakened_topology": False,
    "source_pulled_topology_fourier_norm": 1,
    "restored_observation_repairs_uniformity": True,
    "singular_theta_boundary_topology_verified": False,
    "verdict": "source-pulled topology makes Fourier sewing automatic, while any enlarged boundary completion must independently preserve both Fourier directions",
}

out = Path(__file__).parents[1] / "results" / "rh-trace-topology-fourier-gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
