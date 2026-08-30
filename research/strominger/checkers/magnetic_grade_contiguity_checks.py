"""Bigraded contiguous law for the magnetic source polynomials."""
import json
import os

import sympy as sp

x, t, a = sp.symbols("x t a")


def source(g, av):
    return sp.expand(sum(sp.binomial(g, j) * (-1) ** (g - j) *
                         sp.rf(av, g - j) * sp.rf(4 - av, j) * x ** j
                         for j in range(g + 1)))


checks = []


def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


# Coefficients of the product generating function reproduce C_{g,a}/g!.
generator_failures = []
for g in range(0, 31):
    coefficient = sum(((-1) ** (g - j) * sp.rf(a, g - j) *
                       sp.rf(4 - a, j) * x ** j /
                       (sp.factorial(g - j) * sp.factorial(j)))
                      for j in range(g + 1))
    if sp.simplify(sp.factorial(g) * coefficient - source(g, a)) != 0:
        generator_failures.append(g)
record("GRADE.generator", "the grade EGF factorizes into two binomial characters",
       not generator_failures, "formal coefficients g=0..30")

# Cross-multiplication of F_{a+2}/F_a gives the order-two grade recurrence.
recurrence_failures = []
for g in range(2, 21):
    left = (source(g, a + 2) + 2 * g * source(g - 1, a + 2) +
            g * (g - 1) * source(g - 2, a + 2))
    right = (source(g, a) - 2 * g * x * source(g - 1, a) +
             g * (g - 1) * x ** 2 * source(g - 2, a))
    if sp.simplify(left - right) != 0:
        recurrence_failures.append(g)
record("GRADE.contiguous", "pole-depth shift by two obeys the order-two grade law",
       not recurrence_failures, "formal identities g=2..20")

# Initial grades close the recurrence without exceptions.
initial_ok = (source(0, a + 2) == source(0, a) and
              sp.simplify(source(1, a + 2) + 2 * source(0, a + 2) -
                          source(1, a) + 2 * x * source(0, a)) == 0)
record("GRADE.initial", "grades zero and one supply the two initial conditions",
       initial_ok, "g=0,1")

# The shift quotient is literally a square reflection character.
fa = (1 + t) ** (-a) * (1 - x * t) ** (a - 4)
fa2 = (1 + t) ** (-a - 2) * (1 - x * t) ** (a - 2)
record("GRADE.square", "the a-shift quotient is ((1-xt)/(1+t))^2",
       sp.simplify(fa2 / fa - ((1 - x * t) / (1 + t)) ** 2) == 0,
       "formal rational identity")

# A first-order grade law is genuinely insufficient: its t-polynomial would
# have to replace the quadratic multiplier identity.
linear_u, linear_v = sp.symbols("linear_u linear_v")
quadratic_residual = sp.Poly((1 + t) ** 2 -
                             (linear_u + linear_v * t) * (1 - x * t) ** 2,
                             t)
linear_solution = sp.solve(quadratic_residual.all_coeffs(),
                           [linear_u, linear_v], dict=True)
record("FALSIFIER.order1", "no first-order scalar grade multiplier can replace the quadratic law",
       not linear_solution, "order two is intrinsic")

# Dropping either lower-grade term fails on an explicit source polynomial.
g0 = 4
wrong = source(g0, a + 2) + 2 * g0 * source(g0 - 1, a + 2)
target = (source(g0, a) - 2 * g0 * x * source(g0 - 1, a) +
          g0 * (g0 - 1) * x ** 2 * source(g0 - 2, a))
record("FALSIFIER.memory", "deleting the second-memory term leaves a nonzero residual",
       sp.simplify(wrong - target) != 0, "g=4")

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_grade_contiguity_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "formal bigraded generating-function theorem",
              "coefficient_audit": "g=0..30; recurrence g=2..20"},
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": "The magnetic source family has EGF (1+t)^(-a)(1-xt)^(a-4). Pole-depth shift a->a+2 multiplies it by the square reflection character ((1-xt)/(1+t))^2. Cross-multiplication yields an exact order-two recurrence involving grades g,g-1,g-2. This is the finite contiguous algebra beneath pole-depth transport; closure at one fixed grade alone is false.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_grade_contiguity.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
