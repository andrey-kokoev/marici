from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/nima/results/six-point-nmhv-generic-projective-identity.json"
y = sp.symbols("y1:6")
c = sp.symbols("c1:6")
Y = sp.Matrix(y)
Z = {i + 1: sp.eye(5).col(i) for i in range(5)}
Z[6] = sp.Matrix(c)
LEFT = [(1,2,3,4,5), (1,2,3,5,6), (1,3,4,5,6)]
RIGHT = [(1,2,3,4,6), (1,2,4,5,6), (2,3,4,5,6)]
ALL_FACETS = tuple(combinations(range(1, 7), 4))


def bracket(columns):
    return sp.det(sp.Matrix.hstack(*columns))


def parity_to_sorted(values):
    inversions = sum(values[i] > values[j] for i in range(len(values)) for j in range(i + 1, len(values)))
    return -1 if inversions % 2 else 1


def simplex_data(vertices):
    a,b,d,e,f = vertices
    cyclic = [(a,b,d,e), (b,d,e,f), (d,e,f,a), (e,f,a,b), (f,a,b,d)]
    denominator_sign = sp.prod(parity_to_sorted(face) for face in cyclic)
    facets = {tuple(sorted(face)) for face in cyclic}
    numerator = sp.expand(bracket([Z[i] for i in vertices]) ** 4)
    return numerator / denominator_sign, facets


def common_numerator(signed_cells):
    facet_forms = {face: sp.expand(bracket([Y] + [Z[i] for i in face])) for face in ALL_FACETS}
    total = 0
    for sign, cell in signed_cells:
        numerator, facets = simplex_data(cell)
        complement = [facet_forms[face] for face in ALL_FACETS if face not in facets]
        total += sign * numerator * sp.prod(complement)
    return sp.Poly(sp.expand(total), *(y + c)), facet_forms


def main():
    signed = [(1, cell) for cell in LEFT] + [(-1, cell) for cell in RIGHT]
    residual, facets = common_numerator(signed)
    mutated = signed[:]
    mutated[0] = (-1, mutated[0][1])
    mutation, _ = common_numerator(mutated)
    ordered_minors = {"".join(map(str, cell)): str(sp.factor(bracket([Z[i] for i in cell]))) for cell in combinations(range(1, 7), 5)}
    expected_signs = {"12345": "1", "12346": "c5", "12356": "-c4", "12456": "c3", "13456": "-c2", "23456": "c1"}
    checks = {
        "generic_common_numerator_zero": residual.is_zero,
        "orientation_mutation_nonzero": not mutation.is_zero,
        "ordered_minor_gauge_matches": ordered_minors == expected_signs,
        "all_fifteen_facet_forms_nonzero": len(facets) == 15 and all(form != 0 for form in facets.values())
    }
    out = {
        "schema": "marici.nima.six_point_nmhv_generic_projective_identity.result.v1",
        "status": "passed" if all(checks.values()) else "failed",
        "checks": checks,
        "projective_gauge": "Z1,...,Z5 are the standard basis and Z6=(c1,...,c5)",
        "positive_chamber": "c1>0, c2<0, c3>0, c4<0, c5>0",
        "ordered_five_brackets": ordered_minors,
        "common_numerator_term_count": 0 if residual.is_zero else len(residual.terms()),
        "orientation_mutation_term_count": len(mutation.terms()),
        "claim_boundary": "Exact generic identity on the projective chart where Z1,...,Z5 form a basis and all declared denominators are nonzero. This proves the bosonic simplex-form equality in that chart, not the supersymmetric numerator or physical boundary semantics."
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    if out["status"] != "passed": raise SystemExit(1)


if __name__ == "__main__": main()
