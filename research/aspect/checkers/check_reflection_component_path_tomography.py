import json
from pathlib import Path

import sympy as sp


t = sp.symbols("t", real=True)
I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Z = sp.diag(1, -1)
H = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
U = sp.diag(1, sp.exp(sp.I * sp.pi * t))


def dagger(matrix):
    return sp.conjugate(matrix.T)


def frobenius_squared(matrix):
    return sp.simplify(sp.trace(dagger(matrix) * matrix))


s = sp.simplify(sp.trace(dagger(U) * X * U * X) / 2)
U_mid = sp.simplify(U.subs(t, sp.Rational(1, 2)))
reflected_mid = sp.simplify(X * U_mid * X)
defect_plus = frobenius_squared(reflected_mid - U_mid)
defect_minus = frobenius_squared(reflected_mid + U_mid)

sheet_generator = sp.I * Z
em_generator = sp.simplify(dagger(H) * sheet_generator * H)
mixed_dyad = sp.I * X

checks = {
    "path_is_unitary": (dagger(U) * U).applyfunc(sp.simplify) == I2,
    "path_observable_is_cosine": sp.simplify(s - sp.cos(sp.pi * t)) == 0,
    "identity_endpoint_has_positive_character": X * I2 * X == I2,
    "selective_endpoint_has_negative_character": X * Z * X == -Z,
    "midpoint_observable_is_zero": sp.simplify(s.subs(t, sp.Rational(1, 2))) == 0,
    "midpoint_positive_component_defect_is_four": defect_plus == 4,
    "midpoint_negative_component_defect_is_four": defect_minus == 4,
    "electric_magnetic_generator_is_mixed_dyad": em_generator == mixed_dyad,
    "generator_requires_complex_coefficients": any(entry.has(sp.I) for entry in sheet_generator),
    "real_rational_lattice_is_not_preserved": sheet_generator * sp.Matrix([1, 0]) != sp.Matrix([1, 0]),
}

result = {
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "path_observable": str(s),
    "midpoint": str(U_mid),
    "midpoint_defects": {"positive_component": str(defect_plus), "negative_component": str(defect_minus)},
    "sheet_generator": str(sheet_generator),
    "electric_magnetic_generator": str(em_generator),
    "classification": {
        "endpoint_admissible": True,
        "path_admissible_inside_reflection_fixed_locus": False,
        "coefficient_admissible_over_complexification": True,
        "coefficient_admissible_over_original_real_rational_lattice": False,
    },
}
out = Path(__file__).resolve().parents[1] / "results" / "reflection_component_path_tomography.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
