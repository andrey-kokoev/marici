"""Deterministic compatibility ideals for singular C8 linear-reduction branches."""

import json
from pathlib import Path

import sympy as sp

from eight_site_companion_nlsat import SP as LOWER, SQ_SP, companion, eliminate_positive_linear, square_reduce


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results" / "eight-site-base-reduced-companion-models.json"
TARGET = ROOT / "results" / "eight-site-companion-exceptional-compatibility.json"


def audit(model: dict, kind: str) -> dict:
    equations = [square_reduce(sp.sympify(text, locals=LOWER)) for text in model["cover_equations"]]
    wall = square_reduce(companion(sp.sympify(model["jacobian_determinant"], locals=LOWER)))
    if kind == "A":
        for name in ("C", "D"):
            equations, _ = eliminate_positive_linear(equations, name)
        linear = [equations[1], wall]
        unknowns = [SQ_SP["A"], SQ_SP["Z"]]
    else:
        equations, _ = eliminate_positive_linear(equations, "D")
        linear = [equations[1], equations[2], wall]
        unknowns = [SQ_SP["A"], SQ_SP["C"], SQ_SP["Z"]]
    matrix, right = sp.linear_eq_to_matrix(linear, unknowns)
    generators = [sp.expand(matrix.det())]
    for column in range(len(unknowns)):
        replaced = matrix.copy()
        replaced[:, column] = right
        generators.append(sp.expand(replaced.det()))
    basis = sp.groebner(generators, SQ_SP["B"], SQ_SP["k"], SQ_SP["l"], order="lex")
    return {
        "model": model["name"],
        "compatibility_generators": [str(sp.factor(value)) for value in generators],
        "groebner_basis": [str(sp.factor(poly.as_expr())) for poly in basis.polys],
        "elimination_polynomials_kl": [
            str(sp.factor(poly.as_expr())) for poly in basis.polys if not poly.as_expr().has(SQ_SP["B"])
        ],
    }


def main() -> None:
    models = json.loads(SOURCE.read_text())["models"]
    results = [audit(models[0], "A"), audit(models[3], "B4")]
    TARGET.write_text(json.dumps({"schema": "marici.eight_site_companion_exceptional_compatibility.v1", "models": results}, indent=2) + "\n")
    print(json.dumps({item["model"]: {"basis": len(item["groebner_basis"]), "elimination": len(item["elimination_polynomials_kl"])} for item in results}))


if __name__ == "__main__":
    main()
