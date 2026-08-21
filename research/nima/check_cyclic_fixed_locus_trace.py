"""Exact C3 trace/transfer audit on the equal-energy cosmological locus.

This joins the source cyclic base map and horizontal Gysin transition of
Entry 764 with the two physical occurrence orbits of Entry 356.  The purpose
is to decide whether cyclic covariance becomes an in-place descent packet at
the source-fixed equal-energy point.
"""

from fractions import Fraction as Q
import json
from pathlib import Path


OCCURRENCE = Path("research/benincasa/cyclic-occurrence-rees-certificate.json")
CONNECTION = Path("research/benincasa/independent-three-chart-gysin-connections.json")
OUTPUT = Path("research/nima/results/cyclic_fixed_locus_trace.json")


def rho(point):
    u, v = point
    return 2 * u / (u - v), 2 * (2 - v) / (u - v)


def matmul(a, b, modulus=None):
    out = [[sum(a[i][k] * b[k][j] for k in range(len(b)))
            for j in range(len(b[0]))] for i in range(len(a))]
    if modulus is not None:
        out = [[x % modulus for x in row] for row in out]
    return out


def rank_mod(matrix, prime):
    a = [[x % prime for x in row] for row in matrix]
    rows, cols = len(a), len(a[0])
    rank = 0
    for col in range(cols):
        pivot = next((i for i in range(rank, rows) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, prime)
        a[rank] = [(inv * x) % prime for x in a[rank]]
        for i in range(rows):
            if i != rank and a[i][col]:
                c = a[i][col]
                a[i] = [(x - c * y) % prime for x, y in zip(a[i], a[rank])]
        rank += 1
    return rank


def main():
    occurrence = json.loads(OCCURRENCE.read_text())
    connection = json.loads(CONNECTION.read_text())
    assert occurrence["rho_order"] == 3
    assert occurrence["all_source_signs"] == 1
    assert occurrence["cyclic_orbits"] == [
        ["12|23", "23|31", "31|12"],
        ["12|31", "23|12", "31|23"],
    ]
    assert connection["passed"]

    fixed = (Q(3), Q(1))
    assert rho(fixed) == fixed
    u, v = fixed
    x = (Q(1), (u + v) / 2 - 1, (u - v) / 2)
    assert x == (Q(1), Q(1), Q(1))
    scale = (u - v) / 2
    weights = (-2, -1, 1, 1)
    gauge = [scale ** w for w in weights]
    assert gauge == [Q(1)] * 4

    # Basis order follows the two source C3 orbits listed above.
    transfer = [
        [1, 0], [1, 0], [1, 0],
        [0, 1], [0, 1], [0, 1],
    ]
    trace = [
        [1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1],
    ]
    norm = matmul(transfer, trace)
    trace_transfer = matmul(trace, transfer)
    norm_squared = matmul(norm, norm)
    assert trace_transfer == [[3, 0], [0, 3]]
    assert norm_squared == [[3 * x for x in row] for row in norm]

    norm_mod_3 = [[x % 3 for x in row] for row in norm]
    assert matmul(norm_mod_3, norm_mod_3, 3) == [[0] * 6 for _ in range(6)]
    assert rank_mod(norm_mod_3, 3) == 2

    physical_source = [[1], [1], [1], [1], [1], [1]]
    orbit_readout = matmul(trace, physical_source)
    assert orbit_readout == [[3], [3]]

    out = {
        "schema": "marici.cosmology.cyclic_fixed_locus_trace.v1",
        "base_fixed_point": {"u": 3, "v": 1},
        "equal_energy_locus": {"X1": 1, "X2": 1, "X3": 1},
        "gysin_transition_scale": 1,
        "gysin_transition_diagonal": [1, 1, 1, 1],
        "physical_occurrence_orbits": occurrence["cyclic_orbits"],
        "trace_transfer": [[3, 0], [0, 3]],
        "norm_rank_mod_3": 2,
        "norm_square_mod_3": "zero",
        "all_positive_orbit_readout": [3, 3],
        "conclusion": (
            "On the equal-energy fixed locus the source cyclic relabeling is "
            "an in-place horizontal C3 action on two regular occurrence "
            "orbits. The all-positive physical occurrence sum is their "
            "integral trace, and trace after transfer is multiplication by 3."
        ),
        "typing_boundary": (
            "This establishes characteristic-three degeneration for the "
            "source occurrence trace at the cyclic fixed locus. It does not "
            "identify the three occurrences as one generic-base deck cover."
        ),
        "inputs": [str(OCCURRENCE), str(CONNECTION)],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
