#!/usr/bin/env python3
"""Compare the predeclared rank-26 derivative-word relations at two twists."""
from __future__ import annotations

import importlib
import itertools
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
NCHK = ROOT / "research" / "nima" / "checkers"
sys.path.insert(0, str(NCHK))
census = importlib.import_module("check_rank26_physical_source_covariant_jet_census")

P = census.P
MAX_ORDER = int(os.environ.get("MARICI_MAX_JET_ORDER", "4"))
OUT = ROOT / "research" / "benincasa" / "results" / (
    f"rank26-twist-word-kernel-transport-k{census.K_DEPTH}-p{P}.json"
)


def rank(rows: list[list[int]]) -> int:
    a = [[x % P for x in row] for row in rows if any(x % P for x in row)]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], P - 2, P)
        a[r] = [(inv * x) % P for x in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [(x - q * y) % P for x, y in zip(a[i], a[r])]
        r += 1
        if r == m:
            break
    return r


def kernel_basis(matrix: list[list[int]]) -> list[list[int]]:
    """Kernel of a row-action matrix: matrix times column vector equals zero."""
    if not matrix:
        return []
    a = [[x % P for x in row] for row in matrix]
    m, n = len(a), len(a[0])
    pivots: list[int] = []
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], P - 2, P)
        a[r] = [(inv * x) % P for x in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [(x - q * y) % P for x, y in zip(a[i], a[r])]
        pivots.append(c)
        r += 1
        if r == m:
            break
    free = [c for c in range(n) if c not in pivots]
    out = []
    for f in free:
        v = [0] * n
        v[f] = 1
        for i, c in enumerate(pivots):
            v[c] = (-a[i][f]) % P
        out.append(v)
    return out


def word_packet(gamma: int, words: list[tuple[int, ...]]):
    census.GAMMA = gamma
    census.charts.GAMMA = gamma
    census.charts.AMBIENT = 14
    census.charts.CUTOFF = 7
    census.charts.K_DEPTH = census.K_DEPTH
    pres = census.charts.presentation(census.FIBER, census.POINT, census.NAMES)
    free = list(pres["free_low"])
    free_index = {column: i for i, column in enumerate(free)}
    k, q = census.source_polynomials()
    kd = [{e: census.pder(poly, a) for e, poly in k.items()} for a in range(3)]
    qd = [
        {name: {e: census.pder(poly, a) for e, poly in qp.items()} for name, qp in q.items()}
        for a in range(3)
    ]
    connections = {
        (column, axis): census.connection_poly(label, axis, pres, kd[axis], qd[axis])
        for column, label in enumerate(pres["ordered_columns"])
        for axis in range(3)
    }
    numerator = {e: dict(poly) for e, poly in q[census.NUMERATOR_NAMES[0]].items()}
    for e, poly in q[census.NUMERATOR_NAMES[1]].items():
        census.padd(numerator.setdefault(e, {}), poly)
    root_label = (0, 1, 1, 1, 1, 1)
    root = {pres["columns"][(*root_label, e)]: poly for e, poly in numerator.items()}
    raws = {(): root}
    for order in range(MAX_ORDER):
        for word in [w for w in words if len(w) == order]:
            for axis in range(3):
                raws[word + (axis,)] = census.differentiate_raw(
                    raws[word], axis, pres, connections
                )
    vectors = []
    for word in words:
        reduced = census.evaluate_reduce(raws[word], pres, set(free))
        row = [0] * len(free)
        for column, value in reduced.items():
            row[free_index[column]] = value
        vectors.append(row)
    # Evaluation W -> H has these word vectors as columns.
    evaluation = [[vectors[j][i] for j in range(len(words))] for i in range(len(free))]
    return vectors, kernel_basis(evaluation)


def sparse(v: list[int], words: list[tuple[int, ...]]):
    return [
        {"word": list(words[i]), "coefficient": x if x <= P // 2 else x - P}
        for i, x in enumerate(v)
        if x
    ]


def main() -> None:
    words = [()] + [
        word
        for order in range(1, MAX_ORDER + 1)
        for word in itertools.product(range(3), repeat=order)
    ]
    half = (-pow(2, P - 2, P)) % P
    generic_vectors, generic_kernel = word_packet(5, words)
    physical_vectors, physical_kernel = word_packet(half, words)
    rg = rank(generic_vectors)
    rp = rank(physical_vectors)
    joint_kernel_rank = rank(generic_kernel + physical_kernel)
    intersection = len(generic_kernel) + len(physical_kernel) - joint_kernel_rank
    equal = (
        len(generic_kernel) == len(physical_kernel) == intersection
    )
    payload = {
        "schema": "marici.rank26-twist-word-kernel-transport.v1",
        "prime": P,
        "chart": census.CHART,
        "point": census.POINT,
        "k_pole_depth": census.K_DEPTH,
        "max_word_order": MAX_ORDER,
        "word_count": len(words),
        "word_order": [list(w) for w in words],
        "generic_rank": rg,
        "physical_rank": rp,
        "generic_kernel_dimension": len(generic_kernel),
        "physical_kernel_dimension": len(physical_kernel),
        "kernel_intersection_dimension": intersection,
        "kernels_equal": equal,
        "identity_on_words_descends": all(
            rank(physical_kernel + [v]) == len(physical_kernel)
            for v in generic_kernel
        ),
        "generic_only_relation": next(
            (sparse(v, words) for v in generic_kernel if rank(physical_kernel + [v]) > len(physical_kernel)),
            None,
        ),
        "physical_only_relation": next(
            (sparse(v, words) for v in physical_kernel if rank(generic_kernel + [v]) > len(generic_kernel)),
            None,
        ),
        "expected_generic_source_orbit_rank": 26 if MAX_ORDER >= 4 else 19,
        "expected_physical_source_orbit_rank": 19,
        "passed": rg == (26 if MAX_ORDER >= 4 else 19) and rp == 19,
        "interpretation": (
            "The common derivative-word presentation transports canonically."
            if equal
            else "The two rank-26 fibers have different derivative-word relation kernels; identity on words does not descend."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    if not payload["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
