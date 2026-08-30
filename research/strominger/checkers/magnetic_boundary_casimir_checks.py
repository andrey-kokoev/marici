"""Boundary generating-operator derivation of the stable Schur pivots."""
import json
import os

import sympy as sp

t, a, q, h = sp.symbols("t a q h")


def theta(expression):
    return sp.expand(t * sp.diff(expression, t))


def truncated_left(order):
    return sum((-1) ** g * sp.rf(a, g) * t ** g / sp.factorial(g)
               for g in range(order + 1))


def coefficient_character(expression, g):
    return sp.factor(sp.expand(expression).coeff(t, g) * sp.factorial(g))


checks = []


def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


order = 32
left = truncated_left(order)

# Minus and odd-plus pivots are first-order boundary characters.
minus_series = -(theta(left) + (a + q - 1) * left)
odd_plus_series = theta(left) + (a - q - 1) * left

minus_failures = []
odd_failures = []
for g in range(0, order + 1):
    minus_expected = (-1) ** (g + 1) * (a + g + q - 1) * sp.rf(a, g)
    odd_expected = (-1) ** g * (a + g - q - 1) * sp.rf(a, g)
    if sp.simplify(coefficient_character(minus_series, g) - minus_expected) != 0:
        minus_failures.append(g)
    if sp.simplify(coefficient_character(odd_plus_series, g) - odd_expected) != 0:
        odd_failures.append(g)
record("BOUNDARY.minus", "the minus pivot is -(Theta+a+q-1) on the left endpoint",
       not minus_failures, "formal grades g=0..32")
record("BOUNDARY.odd", "the odd plus pivot is (Theta+a-q-1) on the left endpoint",
       not odd_failures, "formal grades g=0..32")

# The primitive shifts rf(a,g) to rf(a,g-1).  Its sign is chosen to match the
# semantic even pivot orientation.
primitive = -sum((-1) ** (g - 1) * sp.rf(a, g - 1) * t ** g /
                 sp.factorial(g) for g in range(1, order + 1))
primitive_closed_derivative = sp.simplify(sp.diff(primitive, t) + left)
record("BOUNDARY.primitive", "the boundary primitive satisfies J'=-L to audited order",
       all(sp.expand(primitive_closed_derivative).coeff(t, degree) == 0
           for degree in range(order)), "J=-integral L")

casimir_primitive = q * theta(theta(primitive) + (h - 1) * primitive)
even_failures = []
for g in range(1, order + 1):
    expected = (-1) ** g * q * g * (g + h - 1) * sp.rf(a, g - 1)
    if sp.simplify(coefficient_character(casimir_primitive, g) - expected) != 0:
        even_failures.append(g)
record("BOUNDARY.even", "the even pivot is q*Theta*(Theta+h-1) on the primitive",
       not even_failures, "formal grades g=1..32")

# Theta diagonalizes on the exponential-grade basis.
grade_eigen_failures = []
for g in range(0, 51):
    basis = t ** g / sp.factorial(g)
    acted = theta(theta(basis) + (h - 1) * basis)
    if sp.simplify(acted - g * (g + h - 1) * basis) != 0:
        grade_eigen_failures.append(g)
record("CASIMIR.eigen", "Theta(Theta+h-1) has eigenvalue g(g+h-1)",
       not grade_eigen_failures, "grades g=0..50")

grade_symbol = sp.symbols("grade_symbol")
record("CASIMIR.baseline", "the rigid offset h=4 gives the eigenvalue g(g+3)",
       sp.expand((grade_symbol * (grade_symbol + h - 1)).subs(h, 4) -
                 grade_symbol * (grade_symbol + 3)) == 0, "h=4")

# First-order grade calculus cannot reproduce the quadratic even eigenvalue.
alpha, beta, grade = sp.symbols("alpha beta grade")
linear_solution = sp.solve(sp.Poly(alpha * grade + beta -
                                   grade * (grade + h - 1), grade).all_coeffs(),
                           [alpha, beta], dict=True)
record("FALSIFIER.first_order", "no first-order polynomial in Theta gives the even character",
       not linear_solution, "quadratic Casimir is minimal")

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_boundary_casimir_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "formal boundary-operator derivation of all semantic pivot formulas",
              "grade_audit": [0, 50]},
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": "All stable semantic pivots are coefficient characters of the left-endpoint EGF L=(1+t)^(-a). Minus and odd-plus pivots are first-order affine functions of Theta=t*d/dt. The even renormalized pivot is q*Theta*(Theta+h-1) applied to the boundary primitive J=-integral L, producing (-1)^g*q*g*(g+h-1)*rf(a,g-1). Thus g(g+3) at h=4 is the exact quadratic grade-Casimir eigenvalue read by the even collision lane.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_boundary_casimir.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
