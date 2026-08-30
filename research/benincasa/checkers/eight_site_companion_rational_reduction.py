"""Generic rational reduction of the two hard C8 companion feasibility queries."""

import json
import os
from pathlib import Path

import sympy as sp
import z3

from eight_site_companion_nlsat import (
    SP as LOWER,
    SQ_SP,
    companion,
    eliminate_positive_linear,
    square_reduce,
)


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results" / "eight-site-base-reduced-companion-models.json"
TARGET = ROOT / "results" / "eight-site-companion-rational-reduction.json"


def zconvert(value: sp.Expr, variables: dict[str, z3.ArithRef]):
    if value.is_Integer:
        return z3.IntVal(int(value))
    if value.is_Rational:
        return z3.RealVal(f"{value.p}/{value.q}")
    if value.is_Symbol:
        return variables[str(value)]
    if value.is_Add:
        return sum((zconvert(arg, variables) for arg in value.args), z3.IntVal(0))
    if value.is_Mul:
        result = z3.IntVal(1)
        for arg in value.args:
            result *= zconvert(arg, variables)
        return result
    if value.is_Pow and value.exp.is_Integer and int(value.exp) >= 0:
        return zconvert(value.base, variables) ** int(value.exp)
    raise TypeError(value)


def rational_parts(value: sp.Expr):
    numerator, denominator = sp.fraction(sp.cancel(value))
    return sp.expand(numerator), sp.expand(denominator)


def reduce_model(model: dict, kind: str):
    equations = [square_reduce(sp.sympify(text, locals=LOWER)) for text in model["cover_equations"]]
    wall = square_reduce(companion(sp.sympify(model["jacobian_determinant"], locals=LOWER)))
    positivity = []
    if kind == "A":
        for name in ("C", "D"):
            equations, condition = eliminate_positive_linear(equations, name)
            positivity.append(condition)
        solved = sp.solve([equations[1], wall], [SQ_SP["A"], SQ_SP["Z"]], dict=True, simplify=False)[0]
        remaining = equations[0].subs(solved)
        positivity.extend([SQ_SP["B"], solved[SQ_SP["A"]], solved[SQ_SP["Z"]]])
    else:
        equations, condition = eliminate_positive_linear(equations, "D")
        positivity.append(condition)
        solved = sp.solve(
            [equations[1], equations[2], wall],
            [SQ_SP["A"], SQ_SP["C"], SQ_SP["Z"]],
            dict=True,
            simplify=False,
        )[0]
        remaining = equations[0].subs(solved)
        positivity.extend([SQ_SP["B"], solved[SQ_SP["A"]], solved[SQ_SP["C"]], solved[SQ_SP["Z"]]])
    positivity = [value.subs(solved) for value in positivity]
    return remaining, positivity, solved


def decide(model: dict, kind: str):
    remaining, positivity, solved = reduce_model(model, kind)
    names = ("B", "k", "l", "sqrt2")
    variables = {name: z3.Real(name) for name in names}
    B, k, l, s = (variables[name] for name in names)
    solver = z3.SolverFor("QF_NRA")
    solver.set(timeout=int(os.environ.get("MARICI_NLSAT_TIMEOUT_MS", "120000")))
    solver.add(s > 0, s * s == 2)
    numerator, denominator = rational_parts(remaining)
    solver.add(zconvert(numerator, variables) == 0, zconvert(denominator, variables) != 0)
    for condition in positivity:
        numerator, denominator = rational_parts(condition)
        solver.add(zconvert(numerator * denominator, variables) > 0)
    solver.add(6 + 2 * k + l >= 0)
    solver.add(2 + 3 * s / 2 - s * k - l >= 0)
    solver.add(1 + l >= 0)
    solver.add(2 - 3 * s / 2 + s * k - l >= 0)
    solver.add(l - 2 * k >= 0)
    verdict = solver.check()
    remaining_numerator = rational_parts(remaining)[0]
    polynomial_in_B = sp.Poly(remaining_numerator, SQ_SP["B"])
    discriminant = sp.factor(sp.discriminant(polynomial_in_B.as_expr(), SQ_SP["B"]))
    result = {
        "model": model["name"],
        "verdict": str(verdict),
        "remaining_numerator": str(remaining_numerator),
        "degree_in_B": polynomial_in_B.degree(),
        "B_discriminant": str(discriminant),
        "B_discriminant_factorization": str(sp.factor_list(discriminant)),
        "solutions": {str(key): str(value) for key, value in solved.items()},
    }
    if verdict == z3.unknown:
        result["reason_unknown"] = solver.reason_unknown()
    elif verdict == z3.sat:
        assignment = solver.model()
        result["model_values"] = {name: str(assignment.eval(value, model_completion=True)) for name, value in variables.items()}
    return result


def main() -> None:
    models = json.loads(SOURCE.read_text())["models"]
    results = [decide(models[0], "A"), decide(models[3], "B4")]
    TARGET.write_text(json.dumps({"schema": "marici.eight_site_companion_rational_reduction.v1", "models": results}, indent=2) + "\n")
    print(json.dumps({item["model"]: item["verdict"] for item in results}))


if __name__ == "__main__":
    main()
