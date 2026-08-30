"""Symbolic collision cores in the low-grade initialization wedge q>g."""
import json
import math
import os
import sympy as sp

g, d = sp.symbols("g d", integer=True, positive=True)


def source(a, j):
    # Remove the columnwise common parity sign (-1)^g; it is restored where
    # an odd number of plus columns occurs.
    return sp.binomial(g, j) * (-1)**j * sp.rf(a, g - j) * sp.rf(4 - a, j)


def path(a, m, j):
    if j == 0:
        return m * source(a, 0)
    return sp.factor((m + j) * source(a, j) +
                     (m + j - 1 - g) * source(a, j - 1))


F = sp.rf(4, g)
m_minus = 1 - 2 * g - d

# Even excess: rows (1,0), columns (0,-),(d,+), with endpoint plus m=1.
even_core = sp.Matrix([
    [m_minus * F, -path(d, 1, 1)],
    [(1 - g - d) * F, -path(d, 1, 0)],
])
even_reduced = sp.factor(sp.combsimp(even_core.det()))
even_expected = sp.factor(-g * (d - g - 8) * F * sp.rf(d, g))

# Odd excess: rows (1,2,0), columns (0,-),(d-1,+),(d+1,+).
odd_core = sp.Matrix([
    [m_minus * F, -path(d - 1, 2, 0), -path(d + 1, 0, 2)],
    [0, -path(d - 1, 2, 1), -path(d + 1, 0, 3)],
    [(1 - g - d) * F, 0, -path(d + 1, 0, 1)],
])
odd_reduced = sp.factor(sp.combsimp(odd_core.det()))
P = sp.factor(
    d**2 * g**2 + d**2 * g - 6 * d**2 - d * g**3 -
    12 * d * g**2 - 5 * d * g + 30 * d +
    5 * g**3 + 39 * g**2 + 12 * g - 40)
odd_expected = sp.factor(
    -g * (g + 3) * P * sp.factorial(g + 3) *
    sp.factorial(d + g - 3) * sp.factorial(d + g - 1) /
    (6 * sp.factorial(d) * sp.factorial(d - 2)))

# Adjacent low-grade stratum d=1.  The apparent odd core overlaps at depth
# zero, so it is a separate 2x2 endpoint block: rows (1,0), columns
# (0,-),(2,+).  All remaining columns peel from their outer endpoints.
d1_core = sp.Matrix([
    [-2 * g * F, -path(2, 0, 2)],
    [-g * F, -path(2, 0, 1)],
])
d1_reduced = sp.factor(sp.combsimp(d1_core.det()))
d1_expected = sp.factor(
    -g * (g + 3) * (2 * g - 1) * sp.factorial(g) *
    sp.factorial(g + 3) / 3)

checks = []


def record(cid, statement, condition, detail):
    status = "pass" if bool(condition) else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


record("CORE.even", "the even-excess residual core is the displayed 2x2 block",
       sp.factor(sp.combsimp(even_reduced - even_expected)) == 0, even_expected)
record("CORE.even_zero", "its only positive-domain zero is the chart divisor d=g+8",
       sp.solve(sp.Eq(even_expected / (F * sp.rf(d, g)), 0), d) == [g + 8],
       "repaired by the symbolic row-3 transverse theorem")
record("CORE.odd", "the odd-excess residual core has obstruction polynomial P(g,d)",
       sp.factor(odd_reduced - odd_expected) == 0, P)
record("CORE.exception", "the known grade-two exception is exactly P(2,d)=-36(d-5)",
       sp.expand(P.subs(g, 2) + 36 * (d - 5)) == 0,
       "d=5 gives (g,q)=(2,7)")
record("CORE.d1", "the overlapping d=1 endpoint core has a closed nonzero determinant",
       sp.factor(d1_reduced - d1_expected) == 0, d1_expected)
record("CORE.d1_nonzero", "the d=1 core is nonsingular for every integer g>=2",
       all(d1_expected.subs(g, grade) != 0 for grade in range(2, 501)),
       "displayed factors are positive apart from the overall sign")

prefix_path = os.path.join(os.path.dirname(__file__), "magnetic_memory_one_checks.py")
namespace = {"__file__": prefix_path, "__name__": "magnetic_low_core_prefix"}
with open(prefix_path, encoding="utf-8") as source_handle:
    prefix = source_handle.read().split("checks = []")[0]
exec(compile(prefix, prefix_path, "exec"), namespace)
component = namespace["component"]

matrix_failures = []
zeroes = []
for grade in range(2, 31):
    for excess in range(2, 32):
        q = grade + excess
        columns = component(grade, (q + q % 2) // 2, q)
        if excess % 2 == 0:
            chosen_columns = [columns[0], columns[excess + 1]]
            rows = [1, 0]
            matrix = sp.Matrix([[column.get(row, 0) for column in chosen_columns]
                                for row in rows])
            predicted = (-1)**grade * even_expected.subs({g: grade, d: excess})
        elif excess >= 3:
            chosen_columns = [columns[0], columns[excess], columns[excess + 2]]
            rows = [1, 2, 0]
            matrix = sp.Matrix([[column.get(row, 0) for column in chosen_columns]
                                for row in rows])
            predicted = odd_expected.subs({g: grade, d: excess})
        else:
            continue
        actual = sp.factor(matrix.det())
        if actual != predicted:
            matrix_failures.append((grade, q, actual, predicted))
        if actual == 0:
            zeroes.append((grade, q, excess))

record("CORE.generated", "the symbolic cores equal all generated local matrices",
       not matrix_failures, f"failures={matrix_failures[:1]}")
predicted_zeroes = ([(grade, 2 * grade + 8, grade + 8)
                     for grade in range(2, 24, 2)] + [(2, 7, 5)])
record("CORE.zeros", "the bounded core zeros are the even chart divisor and (2,7)",
       sorted(zeroes) == sorted(predicted_zeroes), f"zeros={zeroes}")

d1_failures = []
for grade in range(2, 31):
    columns = component(grade, (grade + 2) // 2, grade + 1)
    matrix = sp.Matrix([[columns[index].get(row, 0) for index in (0, 3)]
                        for row in (1, 0)])
    actual = sp.factor(matrix.det())
    predicted = (-1) ** grade * d1_expected.subs(g, grade)
    if actual != predicted:
        d1_failures.append((grade, actual, predicted))
record("CORE.d1_generated", "the symbolic d=1 core equals every generated endpoint block",
       not d1_failures, f"2<=g<=30; failures={d1_failures[:1]}")

def obstruction(grade, excess):
    return (excess**2 * grade**2 + excess**2 * grade - 6 * excess**2 -
            excess * grade**3 - 12 * excess * grade**2 -
            5 * excess * grade + 30 * excess + 5 * grade**3 +
            39 * grade**2 + 12 * grade - 40)


odd_integer_zeroes = [(grade, excess) for grade in range(2, 501)
                      for excess in range(3, 1002, 2)
                      if obstruction(grade, excess) == 0]
record("ODD.audit", "the odd obstruction has only (g,d)=(2,5) in the large audit",
       odd_integer_zeroes == [(2, 5)],
       "2<=g<=500; odd 3<=d<=1001")

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_low_grade_core_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "symbolic local collision minors with bounded embedding audit",
              "domain": "q>g>=2", "audit": "g<=500, odd d<=1001"},
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": "With d=q-g, the adjacent stratum d=1 has a nonsingular 2x2 endpoint core, the even strata have a 2x2 collision coordinate proportional to d-g-8, and odd d>=3 has a 3x3 coordinate controlled by P(g,d). The even zero is the repaired chart divisor, while P(2,d) gives the genuine (2,7) exception. The aligned plus-chain and boundary-compatibility packets supply the global reduction that raw forced leaf peeling alone could not provide.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_low_grade_core.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
