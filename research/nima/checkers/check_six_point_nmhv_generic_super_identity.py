from __future__ import annotations

import json
from collections import Counter
from itertools import combinations, combinations_with_replacement
from math import factorial
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/nima/results/six-point-nmhv-generic-super-identity.json"
a = sp.symbols("a1:5")
b = sp.symbols("b1:5")
Z = {i + 1: sp.eye(4).col(i) for i in range(4)}
Z[5], Z[6] = sp.Matrix(a), sp.Matrix(b)
LEFT = [(1,2,3,4,5), (1,2,3,5,6), (1,3,4,5,6)]
RIGHT = [(1,2,3,4,6), (1,2,4,5,6), (2,3,4,5,6)]
FACETS = tuple(combinations(range(1, 7), 4))


def bracket(indices):
    return sp.det(sp.Matrix.hstack(*(Z[i] for i in indices)))


def parity_to_sorted(values):
    inversions = sum(values[i] > values[j] for i in range(len(values)) for j in range(i + 1, len(values)))
    return -1 if inversions % 2 else 1


def cell_data(vertices, facet_forms):
    x0,x1,x2,x3,x4 = vertices
    cyclic = [(x0,x1,x2,x3),(x1,x2,x3,x4),(x2,x3,x4,x0),(x3,x4,x0,x1),(x4,x0,x1,x2)]
    denominator_sign = sp.prod(parity_to_sorted(face) for face in cyclic)
    sorted_facets = {tuple(sorted(face)) for face in cyclic}
    complement = sp.prod(facet_forms[face] for face in FACETS if face not in sorted_facets)
    q = {
        x0: bracket(cyclic[1]),
        x1: bracket(cyclic[2]),
        x2: bracket(cyclic[3]),
        x3: bracket(cyclic[4]),
        x4: bracket(cyclic[0]),
    }
    return sp.expand(complement / denominator_sign), q


def multiplicity(labels):
    counts = Counter(labels)
    out = factorial(4)
    for count in counts.values(): out //= factorial(count)
    return out


def main():
    facet_forms = {face: sp.expand(bracket(face)) for face in FACETS}
    signed_cells = [(1, cell) for cell in LEFT] + [(-1, cell) for cell in RIGHT]
    data = [(sign, *cell_data(cell, facet_forms)) for sign, cell in signed_cells]
    mutation_data = data[:]
    mutation_data[0] = (-data[0][0], data[0][1], data[0][2])
    zero_components = 0
    mutation_nonzero_ordered = 0
    first_mutation = None
    representatives = list(combinations_with_replacement(range(1, 7), 4))
    for labels in representatives:
        residual = 0
        mutation = 0
        for sign, complement, q in data:
            coefficient = sp.prod(q.get(label, 0) for label in labels)
            residual += sign * complement * coefficient
        for sign, complement, q in mutation_data:
            coefficient = sp.prod(q.get(label, 0) for label in labels)
            mutation += sign * complement * coefficient
        residual = sp.Poly(sp.expand(residual), *(a + b))
        mutation = sp.Poly(sp.expand(mutation), *(a + b))
        if residual.is_zero: zero_components += multiplicity(labels)
        if not mutation.is_zero:
            mutation_nonzero_ordered += multiplicity(labels)
            if first_mutation is None:
                first_mutation = {"labels": labels, "term_count": len(mutation.terms())}
    checks = {
        "all_1296_grassmann_components_zero": zero_components == 6**4,
        "orientation_mutation_nonzero": mutation_nonzero_ordered > 0,
        "fifteen_generic_four_brackets_present": len(facet_forms) == 15 and all(value != 0 for value in facet_forms.values())
    }
    out = {
        "schema": "marici.nima.six_point_nmhv_generic_super_identity.result.v1",
        "status": "passed" if all(checks.values()) else "failed",
        "checks": checks,
        "projective_gauge": "Z1,...,Z4 are the standard basis, Z5=a, Z6=b",
        "multiset_component_representatives_checked": len(representatives),
        "ordered_grassmann_components_certified_zero": zero_components,
        "orientation_mutation_nonzero_ordered_components": mutation_nonzero_ordered,
        "first_mutation_witness": first_mutation,
        "claim_boundary": "Exact generic polynomial proof of the six-term super five-bracket identity on the projective chart with nonzero declared denominators. This uses an authored standard five-bracket convention and does not supply primary-source normalization or physical boundary semantics."
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    if out["status"] != "passed": raise SystemExit(1)


if __name__ == "__main__": main()
