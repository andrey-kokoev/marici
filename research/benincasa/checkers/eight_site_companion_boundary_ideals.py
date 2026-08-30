"""Exact boundary-ideal audit for the two unresolved reduced C8 companion models."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results" / "eight-site-base-reduced-companion-models.json"
TARGET = ROOT / "results" / "eight-site-companion-boundary-ideals.json"
LOWER_NAMES = ("a", "b", "c", "d", "z", "k", "l")
UPPER_NAMES = ("A", "B", "C", "D", "Z", "k", "l")
LOWER = dict(zip(LOWER_NAMES, sp.symbols(" ".join(LOWER_NAMES))))
UPPER = dict(zip(UPPER_NAMES, sp.symbols(" ".join(UPPER_NAMES))))


def companion(det: sp.Expr) -> sp.Expr:
    supports = [(len(sp.Add.make_args(factor)), factor) for factor, _ in sp.factor_list(det)[1]]
    largest = max(size for size, _ in supports)
    candidates = [factor for size, factor in supports if size == largest]
    if len(candidates) != 1:
        raise RuntimeError(f"non-unique companion: {supports}")
    return candidates[0]


def square_reduce(value: sp.Expr) -> sp.Expr:
    result = 0
    for powers, coefficient in sp.Poly(value, *(LOWER[name] for name in LOWER_NAMES)).terms():
        if any(power % 2 for power in powers[:5]):
            raise RuntimeError("edge expression is not deck-even")
        term = coefficient
        for name, power in zip(UPPER_NAMES[:5], powers[:5]):
            term *= UPPER[name] ** (power // 2)
        term *= UPPER["k"] ** powers[5] * UPPER["l"] ** powers[6]
        result += term
    return sp.expand(result)


def audit(model: dict, substitutions: dict, variables: tuple[str, ...]) -> dict:
    equations = [square_reduce(sp.sympify(text, locals=LOWER)) for text in model["cover_equations"]]
    wall = square_reduce(companion(sp.sympify(model["jacobian_determinant"], locals=LOWER)))
    reduced = [sp.factor(expression.subs(substitutions)) for expression in equations + [wall]]
    generators = [UPPER[name] for name in variables]
    basis = sp.groebner(reduced, *generators, order="grevlex")
    factored_basis = [str(sp.factor(poly.as_expr())) for poly in basis.polys]
    return {
        "model": model["name"],
        "substitutions": {str(key): str(value) for key, value in substitutions.items()},
        "variables": variables,
        "reduced_generators": [str(value) for value in reduced],
        "groebner_basis": factored_basis,
        "unit_ideal": any(poly.as_expr().is_nonzero and poly.as_expr().is_number for poly in basis.polys),
    }


def main() -> None:
    models = json.loads(SOURCE.read_text())["models"]
    results = [
        audit(models[0], {UPPER["B"]: 0, UPPER["l"]: 2 * UPPER["k"]}, ("A", "C", "D", "Z", "k")),
        audit(models[3], {UPPER["B"]: 0, UPPER["l"]: -1}, ("A", "C", "D", "Z", "k")),
    ]
    packet = {"schema": "marici.eight_site_companion_boundary_ideals.v1", "models": results}
    TARGET.write_text(json.dumps(packet, indent=2) + "\n")
    print(json.dumps({item["model"]: {"unit_ideal": item["unit_ideal"], "basis_length": len(item["groebner_basis"])} for item in results}))


if __name__ == "__main__":
    main()
