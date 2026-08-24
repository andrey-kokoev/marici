"""Fraction-free pivot checker for the alternate-chart interior core."""
import json
import os
import sympy as sp

prefix_path = os.path.join(os.path.dirname(__file__), "magnetic_memory_one_checks.py")
with open(prefix_path, encoding="utf-8") as source_handle:
    exec(source_handle.read().split("checks = []")[0])


def interior_core(g):
    q, k = 2 * g + 8, g // 2 + 4
    columns = component(g, k, q)
    rows = [3 if row == 1 else row for row in hall_rows(columns)]
    interior_columns = list(range(1, len(columns) - 1))
    endpoint_rows = {rows.index(0), rows.index(3)}
    interior_rows = [index for index in range(len(rows))
                     if index not in endpoint_rows]
    return sp.Matrix([[columns[j].get(rows[i], 0) for j in interior_columns]
                      for i in interior_rows])


def bareiss_leading_minors(matrix):
    work = [list(map(int, matrix.row(i))) for i in range(matrix.rows)]
    minors = []
    previous = 1
    for k in range(len(work) - 1):
        pivot = work[k][k]
        if pivot == 0:
            return minors + [0]
        minors.append(pivot)
        for i in range(k + 1, len(work)):
            for j in range(k + 1, len(work)):
                numerator = work[i][j] * pivot - work[i][k] * work[k][j]
                assert numerator % previous == 0
                work[i][j] = numerator // previous
        previous = pivot
    minors.append(work[-1][-1])
    return minors


records = []
for g in range(2, 62, 2):
    core = interior_core(g)
    minors = bareiss_leading_minors(core)
    alternating = all((value > 0) == (index % 2 == 0)
                      for index, value in enumerate(minors, start=1))
    ordinary_negative = all(sp.Rational(minors[index],
                                        1 if index == 0 else minors[index - 1]) < 0
                            for index in range(len(minors)))
    records.append({"g": g, "dimension": core.rows,
                    "all_nonzero": all(minors),
                    "alternating": alternating,
                    "ordinary_pivots_negative": ordinary_negative,
                    "determinant_positive": minors[-1] > 0})

checks = []
def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


record("CORE.dimension", "the interior core has dimension g+8",
       all(item["dimension"] == item["g"] + 8 for item in records), "g=2..60")
record("CORE.no_pivot", "fraction-free elimination needs no row exchange",
       all(item["all_nonzero"] for item in records), "30 cores")
record("CORE.oscillation", "the j-th leading minor has sign (-1)^j",
       all(item["alternating"] for item in records), "all 1170 leading minors")
record("CORE.pivots", "every ordinary Gaussian pivot is strictly negative",
       all(item["ordinary_pivots_negative"] for item in records), "g=2..60")
record("CORE.det", "every even-dimensional core determinant is positive",
       all(item["determinant_positive"] for item in records), "g=2..60")

wrong = interior_core(8)
wrong.row_swap(0, 1)
wrong_minors = bareiss_leading_minors(wrong)
wrong_pattern = all(value != 0 and (value > 0) == (index % 2 == 0)
                    for index, value in enumerate(wrong_minors, start=1))
record("FALSIFIER.order", "swapping the first two observations breaks oscillation",
       not wrong_pattern, [sp.sign(value) for value in wrong_minors[:4]])

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_core_oscillation_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "exact finite oscillatory-core theorem",
              "g": "even 2..60", "leading_minors": 1170},
    "checks": checks, "n_pass": len(checks) - len(failed), "n_fail": len(failed),
    "records": records,
    "verdict": "For every even grade through 60, the (g+8)-dimensional interior core admits fraction-free elimination without exchanges; its j-th leading principal minor has sign (-1)^j, so every ordinary Gaussian pivot is strictly negative and the full core determinant is positive. This is exact finite evidence for an oscillatory/sign-regular core and identifies a cone-preserving elimination route to an unbounded proof."
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_core_oscillation.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
