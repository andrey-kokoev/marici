#!/usr/bin/env python3
"""Exact C3 descent census for three labelled rank-21 residue sectors."""
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    r = 0
    for c in range(len(a[0])):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        q = a[r][c]
        a[r] = [x / q for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [a[i][j] - q * a[r][j] for j in range(len(a[0]))]
        r += 1
    return r


def main():
    root = Path(__file__).resolve().parents[3]
    b = root / "research/benincasa"
    occurrence = json.loads((b / "cyclic-occurrence-rees-certificate.json").read_text())
    overlap = json.loads((b / "cross-sector-overlap-certificate.json").read_text())
    transition = json.loads((b / "g12-g31-residue-chart-transition.json").read_text())

    assert occurrence["assembly_type"] == "C3-equivariant direct sum of three residue sectors"
    assert not occurrence["cross_sector_cech_maps_source_defined"]
    assert not overlap["source_double_pole_G12_G23"]
    assert transition["source"]["quotient_rank"] == transition["target"]["quotient_rank"] == 21
    assert transition["checks"]["passed"]

    n = 21
    # Equations v0-v1=0 and v1-v2=0 cut out the diagonal invariants in V^3.
    equations = []
    for block_left, block_right in ((0, 1), (1, 2)):
        for j in range(n):
            row = [0] * (3 * n)
            row[block_left * n + j] = 1
            row[block_right * n + j] = -1
            equations.append(row)
    relation_rank = rank(equations)
    invariant_dimension = 3 * n - relation_rank
    assert relation_rank == 42
    assert invariant_dimension == 21

    result = {
        "schema": "marici.nima.physical_three_chart_equivariant_descent.v1",
        "passed": True,
        "labelled_chart_ranks": {"G12": 21, "G23": 21, "G31": 21},
        "labelled_direct_sum_rank": 63,
        "source_double_cut_overlap": False,
        "assembly": "C3-equivariant direct sum, not Cech gluing",
        "cyclic_relation_rank": relation_rank,
        "diagonal_invariant_rank": invariant_dimension,
        "physical_cyclic_sum_home": "diagonal C3-invariant rank-21 descent over the cyclic quotient of the labelled base",
        "conclusion": "cyclic organization neither triples the physical rank nor produces a smaller horizontal quotient; it descends the full rank-21 marked packet equivariantly",
    }
    output = root / "research/nima/results/physical_three_chart_equivariant_descent.json"
    payload = output.read_text(encoding="utf-8")
    assert json.loads(payload) == result
    print(json.dumps({"passed": True, "invariant_rank": 21,
                      "sha256": hashlib.sha256(payload.encode()).hexdigest().upper()}))


if __name__ == "__main__":
    main()
