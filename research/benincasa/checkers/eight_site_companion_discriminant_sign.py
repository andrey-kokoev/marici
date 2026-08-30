"""Exact PSD-polygon sign audit for the final C8 quadratic discriminants."""

import json
from pathlib import Path

import sympy as sp
import z3

from eight_site_companion_rational_reduction import SOURCE, rational_parts, reduce_model, zconvert
from eight_site_companion_nlsat import SP as LOWER, SQ_SP, companion, square_reduce


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "results" / "eight-site-companion-discriminant-sign.json"


def query(discriminant: sp.Expr, relation: str) -> str:
    variables = {name: z3.Real(name) for name in ("k", "l", "sqrt2")}
    k, l, s = (variables[name] for name in ("k", "l", "sqrt2"))
    solver = z3.SolverFor("QF_NRA")
    solver.set(timeout=60_000)
    solver.add(s > 0, s * s == 2)
    solver.add(6 + 2 * k + l >= 0)
    solver.add(2 + 3 * s / 2 - s * k - l >= 0)
    solver.add(1 + l >= 0)
    solver.add(2 - 3 * s / 2 + s * k - l >= 0)
    solver.add(l - 2 * k >= 0)
    value = zconvert(discriminant, variables)
    solver.add(value > 0 if relation == "positive" else value == 0)
    return str(solver.check())


def audit(model: dict, kind: str) -> dict:
    remaining, _, solved = reduce_model(model, kind)
    numerator = rational_parts(remaining)[0]
    discriminant = sp.factor(sp.discriminant(numerator, SQ_SP["B"]))
    denominator = rational_parts(next(iter(solved.values())))[1]
    return {
        "model": model["name"],
        "positive_on_psd_exists": query(discriminant, "positive"),
        "zero_on_psd_exists": query(discriminant, "zero"),
        "discriminant_factorization": str(sp.factor_list(discriminant)),
        "linear_solve_denominator": str(sp.factor(denominator)),
        "exceptional_denominator_verdict": exceptional_denominator(model, denominator),
    }


def exceptional_denominator(model: dict, denominator: sp.Expr) -> str:
    names = ("A", "B", "C", "D", "Z", "k", "l", "sqrt2")
    variables = {name: z3.Real(name) for name in names}
    A, B, C, D, Z, k, l, s = (variables[name] for name in names)
    equations = [square_reduce(sp.sympify(text, locals=LOWER)) for text in model["cover_equations"]]
    wall = square_reduce(companion(sp.sympify(model["jacobian_determinant"], locals=LOWER)))
    solver = z3.SolverFor("QF_NRA")
    solver.set(timeout=120_000)
    solver.add(s > 0, s * s == 2)
    solver.add(A > 0, B > 0, C > 0, D > 0, Z > 0)
    solver.add(*(zconvert(equation, variables) == 0 for equation in equations))
    solver.add(zconvert(wall, variables) == 0, zconvert(denominator, variables) == 0)
    if model["name"] == "family_B_surviving_edge_4_free_odd":
        reduced_equations = list(equations)
        containing_d = [index for index, equation in enumerate(reduced_equations) if equation.has(SQ_SP["D"])]
        if len(containing_d) != 1:
            raise RuntimeError("unexpected B4 D incidence")
        reduced_equations.pop(containing_d[0])
        linear_equations = [reduced_equations[1], reduced_equations[2], wall]
        matrix, right = sp.linear_eq_to_matrix(linear_equations, [SQ_SP["A"], SQ_SP["C"], SQ_SP["Z"]])
        for column in range(3):
            replaced = matrix.copy()
            replaced[:, column] = right
            solver.add(zconvert(sp.expand(replaced.det()), variables) == 0)
    solver.add(6 + 2 * k + l >= 0)
    solver.add(2 + 3 * s / 2 - s * k - l >= 0)
    solver.add(1 + l >= 0)
    solver.add(2 - 3 * s / 2 + s * k - l >= 0)
    solver.add(l - 2 * k >= 0)
    verdict = solver.check()
    return str(verdict) if verdict != z3.unknown else f"unknown:{solver.reason_unknown()}"


def main() -> None:
    models = json.loads(Path(SOURCE).read_text())["models"]
    results = [audit(models[0], "A"), audit(models[3], "B4")]
    TARGET.write_text(json.dumps({"schema": "marici.eight_site_companion_discriminant_sign.v1", "models": results}, indent=2) + "\n")
    print(json.dumps(results))


if __name__ == "__main__":
    main()
