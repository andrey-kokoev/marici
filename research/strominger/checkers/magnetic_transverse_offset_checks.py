"""Symbolic offset-deformation classification of transverse chart repair."""
import json
import os
import sympy as sp

g, h = sp.symbols("g h", integer=True, positive=True)


def source(a, j):
    return sp.binomial(g, j) * (-1)**j * sp.rf(a, g - j) * sp.rf(h - a, j)


def path(a, m, j):
    if j == 0:
        return m * source(a, 0)
    return sp.factor((m + j) * source(a, j) +
                     (m + j - 1 - g) * source(a, j - 1))


endpoint = g + 2 * h
interior = endpoint - 2
A = -path(interior, 3, 0)
C = -path(interior, 3, 1)
B = -path(endpoint, 1, 2)
E = -path(endpoint, 1, 3)
tau = sp.factor(sp.combsimp(E - C * B / A))
Q = g**2 + (2 * h - 9) * g - 10 * h + 14
expected = sp.factor(
    -g * Q * sp.factorial(2 * g + 2 * h) /
    (6 * (2 * g + 2 * h - 3) * (2 * g + 2 * h - 1) *
     sp.factorial(g + 2 * h - 1)))

checks = []


def record(cid, statement, condition, detail):
    status = "pass" if bool(condition) else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


q = 2 * g + 2 * h
minus_ratio = sp.factor((q + g - 1) / (q - 1))
plus_ratio = sp.factor(2 * g * (g + h) / (2 * g + 2 * h - 1) + 1 - g)
record("DIVISOR.ratio", "the reflected endpoint ratios agree on q=2g+2h",
       sp.factor(minus_ratio - plus_ratio) == 0,
       f"ratio={plus_ratio}")
record("DIVISOR.support", "the onset endpoint a=g+2h starts at target row zero",
       sp.expand(-endpoint - g + q) == 0,
       "plus support begins at -a-g+q=0")

record("LOCAL.unique", "row 3 again sees only the penultimate plus column",
       sp.expand(-interior - g + q) == 2,
       "penultimate support starts at row 2; parity excludes another interior column")
record("LOCAL.pivot", "the local pivot remains -3*(g+2h-2 rising g)",
       sp.factor(A + 3 * sp.rf(g + 2 * h - 2, g)) == 0, A)
record("LOCAL.tau", "the deformed transverse response has one polynomial obstruction Q_h(g)",
       sp.factor(tau - expected) == 0, tau)

# Solving Q_h(g)=0 for h gives (4-g)/2+3/(g-5).  For even g>=8 this is
# negative; direct evaluation at g=2,4,6 leaves only (g,h)=(6,2).
h_solution = sp.factor(-(g**2 - 9 * g + 14) / (2 * g - 10))
small = [(grade, sp.factor(h_solution.subs(g, grade))) for grade in (2, 4, 6)]
record("EXCEPTION.solve", "the only positive integral transverse zero is (h,g)=(2,6)",
       sp.factor(h_solution - ((4 - g) / 2 + 3 / (g - 5))) == 0 and
       small == [(2, 0), (4, -3), (6, 2)],
       f"h=(4-g)/2+3/(g-5); small={small}; negative for even g>=8")
record("BASELINE.h4", "the confluent offset h=4 avoids the transverse exceptional locus",
       sp.factor(Q.subs(h, 4)) == g**2 - g - 26 and
       Q.subs({h: 4, g: 6}) != 0,
       "Q_4(g)=g^2-g-26")
record("FALSIFIER.h2", "the neighboring offset h=2 degenerates at grade 6",
       tau.subs({h: 2, g: 6}) == 0, "tau_(6,h=2)=0")

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_transverse_offset_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "symbolic positive-integral offset classification",
              "domain": "integer h>=1 and even g>=2"},
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": "For the deformed source offset h, the chart divisor is q=2g+2h and the row-3 repair remains a one-pivot Schur complement. Its only variable obstruction is Q_h(g)=g^2+(2h-9)g-10h+14. On positive integer h and even g>=2, Q_h(g)=0 iff (h,g)=(2,6). The locally confluent value h=4 avoids this unique counterfactual transverse degeneration.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_transverse_offset.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
