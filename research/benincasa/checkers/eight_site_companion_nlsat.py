"""Exact QF_NRA gate for generic real-Euclidean C8 companion walls."""

import json
import os
from pathlib import Path

import sympy as sp
import z3


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results" / "eight-site-base-reduced-companion-models.json"
TARGET = ROOT / "results" / "eight-site-companion-nlsat.json"
NAMES = ("a", "b", "c", "d", "z", "k", "l")
SQUARE_NAMES = ("A", "B", "C", "D", "Z", "k", "l")
SP = dict(zip(NAMES, sp.symbols(" ".join(NAMES))))
SQ_SP = dict(zip(SQUARE_NAMES, sp.symbols(" ".join(SQUARE_NAMES))))
Z3 = {name: z3.Real(name) for name in SQUARE_NAMES}


def companion(det: sp.Expr) -> sp.Expr:
    supports = [(len(sp.Add.make_args(factor)), factor) for factor, _ in sp.factor_list(det)[1]]
    largest = max(size for size, _ in supports)
    candidates = [factor for size, factor in supports if size == largest]
    if len(candidates) != 1 or largest < 4:
        raise RuntimeError(f"non-unique companion: {supports}")
    return candidates[0]


def convert(value: sp.Expr):
    if value.is_Integer:
        return z3.IntVal(int(value))
    if value.is_Rational:
        return z3.RealVal(f"{value.p}/{value.q}")
    if value.is_Symbol:
        return Z3[str(value)]
    if value.is_Add:
        return sum((convert(arg) for arg in value.args), z3.IntVal(0))
    if value.is_Mul:
        result = z3.IntVal(1)
        for arg in value.args:
            result *= convert(arg)
        return result
    if value.is_Pow and value.exp.is_Integer and int(value.exp) >= 0:
        return convert(value.base) ** int(value.exp)
    raise TypeError(f"unsupported expression: {value}")


def square_reduce(value: sp.Expr) -> sp.Expr:
    result = sp.Integer(0)
    for powers, coefficient in sp.Poly(value, *(SP[name] for name in NAMES)).terms():
        if any(power % 2 for power in powers[:5]):
            raise RuntimeError(f"non-even edge exponent in {value}")
        term = coefficient
        for name, power in zip(SQUARE_NAMES[:5], powers[:5]):
            term *= SQ_SP[name] ** (power // 2)
        term *= SQ_SP["k"] ** powers[5] * SQ_SP["l"] ** powers[6]
        result += term
    return sp.expand(result)


def eliminate_positive_linear(equations: list[sp.Expr], variable_name: str):
    variable = SQ_SP[variable_name]
    containing = [index for index, equation in enumerate(equations) if equation.has(variable)]
    if len(containing) != 1:
        raise RuntimeError(f"{variable_name} occurs in {len(containing)} equations")
    index = containing[0]
    equation = equations[index]
    coefficient = sp.diff(equation, variable)
    constant = equation.subs(variable, 0)
    if coefficient.has(variable) or sp.degree(equation, variable) != 1:
        raise RuntimeError(f"{variable_name} is not linear")
    reduced = equations[:index] + equations[index + 1 :]
    # The eliminated solution is -constant/coefficient. Its positivity is
    # equivalent to (-constant)*coefficient > 0 and also forces coefficient != 0.
    return reduced, sp.expand(-constant * coefficient)


def solve(model: dict) -> dict:
    equations = [square_reduce(sp.sympify(text, locals=SP)) for text in model["cover_equations"]]
    wall = square_reduce(companion(sp.sympify(model["jacobian_determinant"], locals=SP)))
    eliminated = []
    positivity = []
    boundary_face = os.environ.get("MARICI_BOUNDARY_FACE", "0") == "1"
    boundary_constraints = []
    if boundary_face:
        if model["name"].startswith("family_A_"):
            substitutions = {SQ_SP["B"]: 0, SQ_SP["l"]: 2 * SQ_SP["k"]}
            boundary_constraints.append(Z3["l"] == 2 * Z3["k"])
        elif model["name"] == "family_B_surviving_edge_4_free_odd":
            substitutions = {SQ_SP["B"]: 0, SQ_SP["l"]: -1}
            boundary_constraints.append(Z3["l"] == -1)
        else:
            raise RuntimeError("no frozen boundary face for this model")
        equations = [sp.expand(value.subs(substitutions)) for value in equations]
        wall = sp.expand(wall.subs(substitutions))
        eliminated.extend(str(name) for name in substitutions if str(name) in ("A", "B", "C", "D", "Z"))
    if model["name"].startswith("family_A_"):
        for variable_name in ("C", "D"):
            equations, condition = eliminate_positive_linear(equations, variable_name)
            eliminated.append(variable_name)
            positivity.append(condition)
    elif model["name"] == "family_B_surviving_edge_4_free_odd":
        equations, condition = eliminate_positive_linear(equations, "D")
        eliminated.append("D")
        positivity.append(condition)
    s = z3.Real("sqrt2")
    k, l = Z3["k"], Z3["l"]
    solver = z3.SolverFor("QF_NRA")
    solver.set(timeout=int(os.environ.get("MARICI_NLSAT_TIMEOUT_MS", "60000")))
    solver.add(s > 0, s * s == 2)
    solver.add(*(Z3[name] > 0 for name in ("A", "B", "C", "D", "Z") if name not in eliminated))
    solver.add(*(convert(eq) == 0 for eq in equations), convert(wall) == 0)
    solver.add(*(convert(condition) > 0 for condition in positivity))
    solver.add(*boundary_constraints)
    eigenvalues = [
        6 + 2 * k + l,
        2 + 3 * s / 2 - s * k - l,
        1 + l,
        2 - 3 * s / 2 + s * k - l,
        l - 2 * k,
    ]
    strict_routing = os.environ.get("MARICI_STRICT_ROUTING", "0") == "1"
    solver.add(*(value > 0 if strict_routing else value >= 0 for value in eigenvalues))
    verdict = solver.check()
    result = {"model": model["name"], "verdict": str(verdict), "companion_factor": str(wall), "eliminated_positive_variables": eliminated, "strict_positive_routing": strict_routing, "boundary_face": boundary_face}
    if verdict == z3.sat:
        assignment = solver.model()
        result["model_values"] = {name: str(assignment.eval(Z3[name], model_completion=True)) for name in SQUARE_NAMES}
        result["sqrt2"] = str(assignment.eval(s, model_completion=True))
    elif verdict == z3.unknown:
        result["reason_unknown"] = solver.reason_unknown()
    return result


def main() -> None:
    packet = json.loads(SOURCE.read_text())
    requested = os.environ.get("MARICI_MODEL_INDEX")
    models = packet["models"] if requested is None else [packet["models"][int(requested)]]
    results = []
    for model in models:
        result = solve(model)
        results.append(result)
        print(json.dumps(result), flush=True)
    output = {"schema": "marici.eight_site_companion_nlsat.v1", "models": results}
    target = TARGET if requested is None else TARGET.with_name(f"{TARGET.stem}-model-{requested}.json")
    target.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({item["model"]: item["verdict"] for item in results}), flush=True)


if __name__ == "__main__":
    main()
