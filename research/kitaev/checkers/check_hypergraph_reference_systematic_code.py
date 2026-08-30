#!/usr/bin/env python3
"""Exact finite audit for hypergraph parity comparisons."""

import hashlib
import json
from itertools import combinations
from pathlib import Path

from sympy import Matrix


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/hypergraph-reference-systematic-code.json"


def bits(number, width):
    return tuple((number >> i) & 1 for i in range(width))


def matvec(rows, x):
    return tuple(sum(a * b for a, b in zip(row, x)) % 2 for row in rows)


def weight(x):
    return sum(x)


def distance(rows, n):
    return min(weight(x) + weight(matvec(rows, x)) for i in range(1, 1 << n) for x in [bits(i, n)])


def residual(rows, x, e):
    hx = matvec(rows, x)
    return tuple(a ^ b for a, b in zip(hx, e))


def errors_of_weight_at_most(length, t):
    yield (0,) * length
    for size in range(1, t + 1):
        for support in combinations(range(length), size):
            value = [0] * length
            for i in support:
                value[i] = 1
            yield tuple(value)


def one_fault_collision_free(rows, n):
    m = len(rows)
    seen = {}
    for z in errors_of_weight_at_most(n + m, 1):
        r = residual(rows, z[:n], z[n:])
        if r in seen and seen[r] != z:
            return False
        seen[r] = z
    return True


def parity_set_value(hyperedges, subset):
    chosen = set(subset)
    return sum(len(chosen.intersection(edge)) % 2 for edge in hyperedges)


def main():
    matrices_checked = 0
    correction_checks = 0
    for n in range(1, 4):
        for m in range(1, 4):
            for mask in range(1 << (n * m)):
                rows = tuple(
                    tuple((mask >> (i * n + j)) & 1 for j in range(n))
                    for i in range(m)
                )
                d = distance(rows, n)
                # [I;H] is injective independently of H.
                generator = Matrix.vstack(Matrix.eye(n), Matrix(rows))
                assert generator.rank() == n
                # Directly verify ker R is precisely {(x,Hx)}.
                kernel = []
                for xi in range(1 << n):
                    x = bits(xi, n)
                    for ei in range(1 << m):
                        e = bits(ei, m)
                        if not any(residual(rows, x, e)):
                            kernel.append((x, e))
                assert set(kernel) == {(bits(i, n), matvec(rows, bits(i, n))) for i in range(1 << n)}
                assert min(weight(x) + weight(e) for x, e in kernel if any(x) or any(e)) == d
                assert one_fault_collision_free(rows, n) == (d >= 3)
                matrices_checked += 1
                correction_checks += 1

    hostile_rows = ((1, 1, 0), (1, 1, 1), (0, 0, 1))
    hostile_d = distance(hostile_rows, 3)
    singleton_bound = 1 + min(sum(row[j] for row in hostile_rows) for j in range(3))
    witness = (1, 1, 0)
    assert matvec(hostile_rows, witness) == (0, 0, 0)
    assert hostile_d == 2 and singleton_bound == 3

    ternary = ({0, 1, 2},)
    s = {0, 1}
    t = {1, 2}
    lhs = parity_set_value(ternary, s) + parity_set_value(ternary, t)
    rhs = parity_set_value(ternary, s & t) + parity_set_value(ternary, s | t)
    assert lhs == 0 and rhs == 2 and lhs < rhs

    payload = {
        "schema": "marici.kitaev.hypergraph_reference_systematic_code.v1",
        "status": "pass",
        "strength": "finite-cutoff theorem",
        "field": "F2",
        "binary_matrices_checked": matrices_checked,
        "one_fault_collision_checks": correction_checks,
        "hostile_degree_witness": {
            "matrix": [list(row) for row in hostile_rows],
            "command": list(witness),
            "output": list(matvec(hostile_rows, witness)),
            "actual_distance": hostile_d,
            "singleton_prediction": singleton_bound,
            "residual": singleton_bound - hostile_d,
        },
        "submodularity_falsifier": {
            "hyperedge": [0, 1, 2],
            "S": sorted(s),
            "T": sorted(t),
            "lhs": lhs,
            "rhs": rhs,
            "residual": rhs - lhs,
        },
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope_exclusions": [
            "efficient decoding", "correlated noise", "quantum commutation",
            "physical comparison implementation"
        ],
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
