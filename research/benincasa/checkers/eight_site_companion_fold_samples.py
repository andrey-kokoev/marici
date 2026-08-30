"""Complex discovery samples for local C8 companion fold geometry."""

import json
from pathlib import Path

import numpy as np
import sympy as sp

from eight_site_companion_nlsat import SP as LOWER, SQ_SP, companion, square_reduce


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results" / "eight-site-base-reduced-companion-models.json"
TARGET = ROOT / "results" / "eight-site-companion-fold-samples.json"
AMP = [LOWER[name] for name in ("a", "b", "c", "d")]


def eliminate(equations, variable):
    containing = [index for index, equation in enumerate(equations) if equation.has(variable)]
    if len(containing) != 1:
        raise RuntimeError(f"unexpected incidence for {variable}")
    index = containing[0]
    equation = equations[index]
    solution = sp.solve(equation, variable, dict=False)[0]
    return equations[:index] + equations[index + 1 :], solution


def sample(model: dict, kind: str, k_value: sp.Rational, l_value: sp.Rational) -> dict:
    amplitude_equations = [sp.sympify(text, locals=LOWER) for text in model["cover_equations"]]
    equations = [square_reduce(value) for value in amplitude_equations]
    wall = square_reduce(companion(sp.sympify(model["jacobian_determinant"], locals=LOWER)))
    recovered = {}
    if kind == "A":
        equations, recovered[SQ_SP["C"]] = eliminate(equations, SQ_SP["C"])
        equations, recovered[SQ_SP["D"]] = eliminate(equations, SQ_SP["D"])
        solved = sp.solve([equations[1], wall], [SQ_SP["A"], SQ_SP["Z"]], dict=True, simplify=False)[0]
        remaining = equations[0].subs(solved)
    elif kind == "B4":
        equations, recovered[SQ_SP["D"]] = eliminate(equations, SQ_SP["D"])
        solved = sp.solve(
            [equations[1], equations[2], wall],
            [SQ_SP["A"], SQ_SP["C"], SQ_SP["Z"]],
            dict=True,
            simplify=False,
        )[0]
        remaining = equations[0].subs(solved)
    else:
        equations, recovered[SQ_SP["D"]] = eliminate(equations, SQ_SP["D"])
        equations, recovered[SQ_SP["Z"]] = eliminate(equations, SQ_SP["Z"])
        edge_variables = [SQ_SP["A"], SQ_SP["B"], SQ_SP["C"]]
        linear = [equation for equation in equations if sp.Poly(equation, *edge_variables).total_degree() == 1]
        nonlinear = [equation for equation in equations if sp.Poly(equation, *edge_variables).total_degree() != 1]
        if len(linear) != 1 or len(nonlinear) != 1:
            raise RuntimeError(f"unexpected {kind} degree split")
        solved = sp.solve([linear[0], wall], [SQ_SP["A"], SQ_SP["C"]], dict=True, simplify=False)[0]
        remaining = nonlinear[0].subs(solved)
    substitutions = {SQ_SP["k"]: k_value, SQ_SP["l"]: l_value}
    polynomial = sp.Poly(sp.together(remaining.subs(substitutions)).as_numer_denom()[0], SQ_SP["B"])
    roots = [complex(root) for root in sp.nroots(polynomial)]
    B_value = roots[0]
    values = {SQ_SP["B"]: B_value, **substitutions}
    for variable, expression in solved.items():
        values[variable] = complex(sp.N(expression.subs(values), 30))
    for variable, expression in recovered.items():
        values[variable] = complex(sp.N(expression.subs(values), 30))
    amplitudes = [np.sqrt(values[SQ_SP[name]]) for name in ("A", "B", "C", "D")]
    z_value = np.sqrt(values[SQ_SP["Z"]])
    numeric_subs = {
        LOWER["a"]: amplitudes[0], LOWER["b"]: amplitudes[1], LOWER["c"]: amplitudes[2], LOWER["d"]: amplitudes[3],
        LOWER["z"]: z_value, LOWER["k"]: float(k_value), LOWER["l"]: float(l_value),
    }
    jacobian_expr = sp.Matrix(amplitude_equations).jacobian(AMP)
    jacobian = np.asarray(jacobian_expr.evalf(30, subs=numeric_subs)).astype(complex)
    left_svd, singular, right_h = np.linalg.svd(jacobian)
    right_kernel = right_h.conj().T[:, -1]
    left_kernel = left_svd[:, -1].conj()
    second = np.zeros(4, dtype=complex)
    for index, equation in enumerate(amplitude_equations):
        hessian = np.asarray(sp.hessian(equation, AMP).evalf(30, subs=numeric_subs)).astype(complex)
        second[index] = right_kernel @ hessian @ right_kernel
    fold_scalar = left_kernel @ second
    residuals = np.asarray([complex(sp.N(eq.subs(numeric_subs), 30)) for eq in amplitude_equations])
    return {
        "model": model["name"],
        "k": str(k_value),
        "l": str(l_value),
        "edge_squares": {str(key): [value.real, value.imag] for key, value in values.items() if str(key) in ("A", "B", "C", "D", "Z")},
        "cover_residual_max": float(np.max(np.abs(residuals))),
        "jacobian_singular_values": singular.tolist(),
        "fold_scalar": [float(fold_scalar.real), float(fold_scalar.imag)],
        "fold_scalar_abs": float(abs(fold_scalar)),
        "status": "discovery_sample_not_exact_certificate",
    }


def main() -> None:
    models = json.loads(SOURCE.read_text())["models"]
    results = [
        sample(models[0], "A", sp.Rational(1, 5), sp.Rational(1, 7)),
        sample(models[1], "B8", sp.Rational(1, 5), sp.Rational(1, 7)),
        sample(models[2], "B6", sp.Rational(1, 5), sp.Rational(1, 7)),
        sample(models[3], "B4", sp.Rational(1, 5), sp.Rational(1, 7)),
    ]
    TARGET.write_text(json.dumps({"schema": "marici.eight_site_companion_fold_samples.discovery.v1", "models": results}, indent=2) + "\n")
    print(json.dumps({item["model"]: {"residual": item["cover_residual_max"], "fold_abs": item["fold_scalar_abs"]} for item in results}))


if __name__ == "__main__":
    main()
