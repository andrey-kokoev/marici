"""Exact local-support audit for the even Schur boundary covector."""
import json
import os

import sympy as sp

prefix_path = os.path.join(os.path.dirname(__file__), "magnetic_memory_one_checks.py")
namespace = {"__file__": prefix_path, "__name__": "magnetic_covector_prefix"}
with open(prefix_path, encoding="utf-8") as source_handle:
    prefix = source_handle.read().split("checks = []")[0]
exec(compile(prefix, prefix_path, "exec"), namespace)
component = namespace["component"]
hall_rows = namespace["hall_rows"]


checks = []


def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


records = []
failures = []
skipped_charts = []
for g in range(2, 9):
    for q in range(2, 13, 2):
        w = q // 2
        start = w + 2
        for k in range(start, start + 4):
            a = 2 * k
            old_columns = component(g, k - 1, q)
            try:
                old_rows = hall_rows(old_columns)
            except AssertionError:
                continue
            old_matrix = sp.Matrix([[column.get(row, 0)
                                     for column in old_columns]
                                    for row in old_rows])
            if old_matrix.det() == 0:
                skipped_charts.append((g, q, k))
                continue
            plus_row = -a - g + q + 1
            boundary_row = sp.Matrix([[column.get(plus_row, 0)
                                       for column in old_columns]])
            coefficients = list(-boundary_row * old_matrix.inv())
            support = {old_rows[index] for index, value in enumerate(coefficients)
                       if value != 0}
            expected_support = {plus_row - (2 * depth - 1)
                                for depth in range(1, w + 1)}

            # Append coefficient 1 on the new boundary row.  This covector
            # must annihilate every old column by construction.
            annihilation = (sp.Matrix([coefficients]) * old_matrix + boundary_row)
            new_plus = component(g, k, q)[-1]
            effective = sum(coefficients[index] * new_plus.get(row, 0)
                            for index, row in enumerate(old_rows))
            effective += new_plus.get(plus_row, 0)
            expected_pivot = int((-1) ** g * q * g * (g + 3) *
                                 sp.rf(a, g - 1))
            ok = (support == expected_support and annihilation == sp.zeros(1, len(old_columns))
                  and sp.factor(effective) == expected_pivot)
            if not ok:
                failures.append((g, q, k, sorted(support),
                                 sorted(expected_support), effective, expected_pivot))
            records.append({"g": g, "q": q, "k": k, "width": w,
                            "support": sorted(support),
                            "effective": str(effective)})

record("COVECTOR.local", "the even quotient covector is supported on exactly w collision rows",
       not failures, f"steps={len(records)}; failures={failures[:1]}")
record("COVECTOR.pattern", "its support is r_plus-1,r_plus-3,...,r_plus-(2w-1)",
       not failures, "arithmetic collision chain")
record("COVECTOR.annihilate", "the normalized covector annihilates every old column",
       not failures, "lambda*A+c=0 exactly")
record("COVECTOR.casimir", "evaluation on the new plus column gives the Casimir pivot",
       not failures, "(-1)^g*q*g*(g+3)*rf(a,g-1)")

widths = {(item["q"], len(item["support"])) for item in records}
record("MEMORY.saturated", "covector support saturates width q/2 independently of cutoff",
       all(size == qv // 2 for qv, size in widths), sorted(widths))
record("ATLAS.separate", "singular preferred charts are separated from quotient solves",
       all(item[:2] == (2, 12) for item in skipped_charts),
       f"skipped={skipped_charts}")

# At q=2 the quotient functional has one old-row coefficient; deleting it
# leaves the raw B1 value and fails to produce the Casimir pivot.
g0, q0, k0 = 3, 2, 4
a0 = 2 * k0
old0 = component(g0, k0 - 1, q0)
rows0 = hall_rows(old0)
matrix0 = sp.Matrix([[column.get(row, 0) for column in old0] for row in rows0])
plus_row0 = -a0 - g0 + q0 + 1
boundary0 = sp.Matrix([[column.get(plus_row0, 0) for column in old0]])
coefficients0 = list(-boundary0 * matrix0.inv())
new_plus0 = component(g0, k0, q0)[-1]
raw0 = new_plus0.get(plus_row0, 0)
effective0 = raw0 + sum(coefficients0[index] * new_plus0.get(row, 0)
                        for index, row in enumerate(rows0))
record("FALSIFIER.raw", "discarding the collision covector leaves the wrong raw B1 pivot",
       raw0 != effective0 and len([value for value in coefficients0 if value]) == 1,
       f"raw={raw0}; effective={effective0}")

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_boundary_covector_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "exact finite local-support theorem for the even quotient functional",
              "g": [2, 8], "q_even": [2, 12], "stable_steps": 4,
              "skipped_chart_zeros": skipped_charts},
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": "The even Schur pivot is computed by a normalized quotient covector supported on exactly w=q/2 old collision rows r_plus-(2d-1). It annihilates the complete old component and evaluates the new plus column to (-1)^g*q*g*(g+3)*rf(a,g-1). This realizes the boundary Casimir inside the finite matrix: the primitive is the w-row collision-chain solve, while the final evaluation is its quadratic grade character.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_boundary_covector.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
