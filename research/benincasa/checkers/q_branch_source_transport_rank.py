"""Rank audit for the two frozen physical source summands.

This does not choose a face projection or a period covector.  It asks whether
the labelled source vectors and their two covariant derivatives acquire a
cohomological rank defect at a supplied kinematic point.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa"))
import physical_four_mark_residue_twisted_derham as m

P = m.PRIME
POINT = tuple(int(x) % P for x in os.environ.get("MARICI_EXTERNAL_POINT", "2,3,4").split(","))
AMBIENT = int(os.environ.get("MARICI_AMBIENT_DEGREE", "12"))
CUTOFF = int(os.environ.get("MARICI_CUTOFF_DEGREE", "6"))
GAMMA = (P - 1) // 2
NAMES = ("g1", "g2", "g3", "g23", "g31")
ORIGINAL_FIBER_DATA = m.fiber_data


def add_scaled(target, vector, scale=1):
    for column, value in vector.items():
        m.add_value(target, column, scale * value)


def rank(rows):
    pivots = {}
    for row in rows:
        m.add_pivot(dict(row), pivots)
    return len(pivots)


def parameter_derivative_data(axis):
    weights = (1, -8, 0, 8, -1)
    inv12 = pow(12, P - 2, P)
    kout, qout = {}, {}
    for offset, weight in zip((-2, -1, 0, 1, 2), weights):
        point = list(POINT)
        point[axis] = (point[axis] + offset) % P
        kval, qval = ORIGINAL_FIBER_DATA(*point)
        for exponent, coefficient in kval.items():
            kout[exponent] = (kout.get(exponent, 0) + weight * coefficient) % P
        for name, polynomial in qval.items():
            target = qout.setdefault(name, {})
            for exponent, coefficient in polynomial.items():
                target[exponent] = (target.get(exponent, 0) + weight * coefficient) % P
    kout = {e: c * inv12 % P for e, c in kout.items() if c}
    qout = {
        name: {e: c * inv12 % P for e, c in polynomial.items() if c}
        for name, polynomial in qout.items()
    }
    return kout, qout


def main():
    m.fiber_data = lambda _x, _y, _z: ORIGINAL_FIBER_DATA(*POINT)
    m.parameter_derivative_data = parameter_derivative_data
    low, columns, pivots, free = m.presentation(
        NAMES, GAMMA, AMBIENT, CUTOFF, minimum_q_level=0
    )
    labels = {columns[label]: label for label in low}

    def quotient(label):
        return m.quotient_coordinates(label, columns, pivots, free)

    def connection(vector, axis):
        image = {}
        for column, coefficient in vector.items():
            add_scaled(
                image,
                m.connection_image(labels[column], NAMES, GAMMA, axis, columns),
                coefficient,
            )
        reduced = m.reduce_row(image, pivots)
        return {column: reduced[column] for column in free if column in reduced}

    source_labels = {
        "g23": (0, 1, 1, 1, 1, 0, (0, 0)),
        "g31": (0, 1, 1, 1, 0, 1, (0, 0)),
    }
    sources = {name: quotient(label) for name, label in source_labels.items()}
    derivatives = {
        name: [connection(vector, axis) for axis in (0, 1)]
        for name, vector in sources.items()
    }
    source_sum = {}
    for vector in sources.values():
        add_scaled(source_sum, vector)
    derivative_sum = []
    for axis in (0, 1):
        row = {}
        for name in source_labels:
            add_scaled(row, derivatives[name][axis])
        derivative_sum.append(row)

    x, y, z = POINT
    e = (x + y + z) % P
    # A=ell_1 ell_2=-(E-2X1)(E-2X2), while
    # B=ell_3 ell_4=(E-2X3)E in the frozen signed-letter convention.
    a = (-(e - 2 * x) * (e - 2 * y)) % P
    b = ((e - 2 * z) * e) % P
    q = (4 * a * b - (a + b - e * e) ** 2) % P

    packet = {
        "schema": "marici.benincasa.q-branch-source-transport-rank.v1",
        "prime": P,
        "point": list(POINT),
        "Q_mod_prime": q,
        "ambient": AMBIENT,
        "cutoff": CUTOFF,
        "common_dimension": len(free),
        "source_rank": rank(list(sources.values())),
        "source_plus_derivative_rank_by_channel": {
            name: rank([sources[name], *derivatives[name]]) for name in source_labels
        },
        "derivative_rank_by_channel": {
            name: rank(derivatives[name]) for name in source_labels
        },
        "all_four_derivatives_rank": rank(
            derivatives["g23"] + derivatives["g31"]
        ),
        "assembled_source_and_derivatives_rank": rank([source_sum, *derivative_sum]),
        "branchwise_derivatives_add_to_assembled": all(
            derivative_sum[axis] == connection(source_sum, axis) for axis in (0, 1)
        ),
    }
    packet["passed"] = packet["branchwise_derivatives_add_to_assembled"]
    print(json.dumps(packet, indent=2))
    if not packet["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
