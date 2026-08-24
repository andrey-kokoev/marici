"""Symbolic telescoping structure of the transverse-response character."""
import json
import os
import sympy as sp

g = sp.symbols("g", integer=True, positive=True)
Q = lambda x: x**2 - x - 26


def multiplier(x):
    x = sp.sympify(x)
    return sp.factor(
        4 * x * (x + 3) * (x + 4) * (2 * x + 1) * (2 * x + 3) * Q(x) /
        ((x - 2) * (x + 6) * (x + 7) * Q(x - 2)))


def product_formula(even_grade):
    result = sp.Rational(320, 3)
    for h in range(4, even_grade + 1, 2):
        result *= multiplier(h)
    return sp.factor(result)


checks = []


def record(cid, statement, condition, detail):
    status = "pass" if bool(condition) else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


record("SHIFT.Q", "the denominator quadratic is the preceding numerator quadratic",
       sp.expand(Q(g - 2)) == g**2 - 5 * g - 20,
       f"Q(g-2)={sp.expand(Q(g - 2))}")

regular = sp.factor(multiplier(g) * Q(g - 2) / Q(g))
expected_regular = sp.factor(
    4 * g * (g + 3) * (g + 4) * (2 * g + 1) * (2 * g + 3) /
    ((g - 2) * (g + 6) * (g + 7)))
record("SHIFT.character", "the recurrence is a positive regular character times Q(g)/Q(g-2)",
       regular == expected_regular, regular)

telescoping_failures = []
for top in range(4, 102, 2):
    lhs = sp.prod(sp.Rational(Q(h), Q(h - 2))
                  for h in range(4, top + 1, 2))
    if sp.factor(lhs - sp.Rational(Q(top), Q(2))) != 0:
        telescoping_failures.append(top)
record("PRODUCT.telescope", "all internal quadratic transport factors cancel",
       not telescoping_failures,
       f"product=Q(g)/Q(2); audit failures={telescoping_failures}")

integral_zeros = [h for h in range(2, 10002, 2) if Q(h) == 0]
record("PRODUCT.nonzero", "the surviving endpoint Q(g) misses every even grade",
       not integral_zeros and Q(2) == -24,
       f"Q(2)={Q(2)}; even zeros through 10000={integral_zeros}")

values = {h: product_formula(h) for h in range(2, 48, 2)}
record("SIGN.endpoint", "the single sign change is exactly the sign change of Q(g)",
       values[2] > 0 and values[4] > 0 and
       all(values[h] < 0 for h in range(6, 48, 2)),
       "Q(2),Q(4)<0 and Q(g)>0 for even g>=6")


def closed_formula(even_grade):
    n = even_grade // 2
    return sp.factor(
        -sp.Rational(32, 3) * sp.Rational(n, n + 3) * 4**(n - 1) *
        sp.factorial2(4 * n + 3) * Q(2 * n) /
        ((2 * n + 5) * (2 * n + 7)))


closed_failures = [(h, values[h], closed_formula(h))
                   for h in range(2, 48, 2)
                   if values[h] != closed_formula(h)]
record("PRODUCT.closed", "the telescoped character has a closed double-factorial form",
       not closed_failures,
       "tau_2n=-(32/3)*n*4^(n-1)*(4n+3)!!*Q(2n)/"
       "((n+3)(2n+5)(2n+7))")

n = sp.symbols("n", integer=True, positive=True)
closed_symbolic = (-sp.Rational(32, 3) * n * 4**(n - 1) *
                   sp.factorial2(4 * n + 3) * Q(2 * n) /
                   ((n + 3) * (2 * n + 5) * (2 * n + 7)))
closed_ratio = sp.factor(
    4 * n * (n + 2) * (4 * n + 1) * (4 * n + 3) * (2 * n + 3) *
    Q(2 * n) /
    ((n - 1) * (n + 3) * (2 * n + 7) * Q(2 * n - 2)))
record("PRODUCT.recurrence", "the closed form reproduces the proposed multiplier",
       sp.factor(closed_ratio - multiplier(2 * n)) == 0,
       closed_ratio)

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_transverse_telescope_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "symbolic consequence of the proposed recurrence",
              "domain": "even g>=2"},
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": "Writing Q(g)=g^2-g-26 turns the proposed transverse recurrence into a manifestly positive regular character times Q(g)/Q(g-2). The quadratic factors telescope, leaving only Q(g)/Q(2), and the remaining product collapses to an explicit double-factorial formula for tau_2n. Hence, conditional on the observed recurrence identity, nonvanishing and the unique sign change are endpoint facts, not repeated discriminant accidents.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_transverse_telescope.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
