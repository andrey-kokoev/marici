"""Exact audit of the Fourier-graded Gaussian dilation module."""

import json
from pathlib import Path

import sympy as sp


y = sp.symbols("y", real=True)
pi = sp.pi
gaussian = sp.exp(-pi * y**2)


def fourier_tower_polynomials(max_degree):
    transforms = [gaussian]
    for _ in range(max_degree):
        transforms.append(sp.simplify(-sp.diff(transforms[-1], y, 2) / (4 * pi)))
    polynomials = [sp.expand(item / gaussian).subs(y**2, sp.symbols("t") / pi) for item in transforms]
    return [sp.expand(item) for item in polynomials]


def coefficient_matrix(polynomials):
    t = sp.symbols("t")
    size = len(polynomials)
    matrix = sp.zeros(size)
    for column, polynomial in enumerate(polynomials):
        poly = sp.Poly(polynomial, t)
        for row in range(column + 1):
            matrix[row, column] = poly.coeff_monomial(t**row)
    return matrix


def dilation_rect(columns):
    matrix = sp.zeros(columns + 1, columns)
    for k in range(columns):
        matrix[k, k] = 2 * k + sp.Rational(1, 2)
        matrix[k + 1, k] = -2
    return matrix


polynomials = fourier_tower_polynomials(7)
checks = {}
for size in range(1, 7):
    Cn = coefficient_matrix(polynomials[:size])
    Cnext = coefficient_matrix(polynomials[: size + 1])
    A = dilation_rect(size)
    checks[f"size_{size}_involution"] = Cn**2 == sp.eye(size)
    checks[f"size_{size}_anticommutation"] = Cnext * A + A * Cn == sp.zeros(size + 1, size)

C3 = coefficient_matrix(polynomials[:3])
physical = sp.Matrix([0, -6, 4])
checks["physical_vector_fourier_even"] = C3 * physical == physical
checks["physical_vector_vacuum_null"] = physical[0] == 0

a, b = sp.symbols("a b")
candidate = sp.Matrix([0, a, b])
condition = sp.expand(C3 * candidate - candidate)
solution = sp.linsolve(list(condition), (a, b))
checks["degree_two_even_vacuum_null_line"] = solution == sp.linsolve([2 * a + 3 * b], (a, b))

result = {
    "schema": "marici.grothendieck.theta_graded_fourier_dilation_module.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "first_fourier_polynomials": [str(item) for item in polynomials[:3]],
    "relations": ["C^2=1", "CA+AC=0"],
    "physical_vector": "4g2-6g1",
}

output = Path(__file__).parents[1] / "results" / "theta_graded_fourier_dilation_module.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

