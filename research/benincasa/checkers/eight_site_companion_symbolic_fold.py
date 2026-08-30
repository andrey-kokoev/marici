"""Symbolic corank-one and kernel-transversality packets for C8 companions."""

import json
from pathlib import Path

import sympy as sp

from eight_site_companion_nlsat import SP as LOWER, companion


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results" / "eight-site-base-reduced-companion-models.json"
TARGET = ROOT / "results" / "eight-site-companion-symbolic-fold.json"
VARIABLES = [LOWER[name] for name in ("a", "b", "c", "d")]


def audit(model: dict) -> dict:
    equations = [sp.sympify(text, locals=LOWER) for text in model["cover_equations"]]
    determinant = sp.sympify(model["jacobian_determinant"], locals=LOWER)
    wall = companion(determinant)
    jacobian = sp.Matrix(equations).jacobian(VARIABLES)
    adjugate = jacobian.adjugate()
    candidates = []
    for column in range(4):
        vector = adjugate[:, column]
        fold = sp.factor(sum(vector[row] * sp.diff(wall, VARIABLES[row]) for row in range(4)))
        minor = sp.factor(adjugate[column, column])
        if fold != 0 and minor != 0:
            candidates.append((len(str(fold)) + len(str(minor)), column, minor, fold))
    if not candidates:
        raise RuntimeError(f"no symbolic fold column for {model['name']}")
    _, column, minor, fold = min(candidates)
    return {
        "model": model["name"],
        "adjugate_column": column,
        "rank_three_minor": str(minor),
        "kernel_transversality": str(fold),
        "rank_three_minor_length": len(str(minor)),
        "kernel_transversality_length": len(str(fold)),
        "interpretation": "nonzero ambient polynomials; exact nonvanishing on the selected algebraic sample is a separate gate",
    }


def main() -> None:
    models = json.loads(SOURCE.read_text())["models"]
    results = [audit(model) for model in models]
    TARGET.write_text(json.dumps({"schema": "marici.eight_site_companion_symbolic_fold.v1", "models": results}, indent=2) + "\n")
    print(json.dumps({item["model"]: {"column": item["adjugate_column"], "minor_length": item["rank_three_minor_length"], "fold_length": item["kernel_transversality_length"]} for item in results}))


if __name__ == "__main__":
    main()
