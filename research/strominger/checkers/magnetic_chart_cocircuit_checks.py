"""Exact cocircuit checker for the even primary-chart boundary."""
from functools import reduce
import json
import math
import os
import sympy as sp

prefix_path = os.path.join(os.path.dirname(__file__), "magnetic_memory_one_checks.py")
with open(prefix_path, encoding="utf-8") as source_handle:
    exec(source_handle.read().split("checks = []")[0])


def primitive(vector):
    denominator = sp.ilcm(*[value.q for value in vector])
    integers = [int(value * denominator) for value in vector]
    divisor = reduce(math.gcd, (abs(value) for value in integers if value), 0)
    integers = [value // divisor for value in integers]
    first = next(value for value in integers if value)
    return [-value for value in integers] if first < 0 else integers


records = []
for g in range(2, 16, 2):
    q = 2 * g + 8
    k = g // 2 + 4
    columns = component(g, k, q)
    rows = hall_rows(columns)
    primary = sp.Matrix([[item.get(row, 0) for item in columns] for row in rows])
    left = primitive(list(primary.T.nullspace()[0]))
    alternate_rows = [3 if row == 1 else row for row in rows]
    alternate = sp.Matrix([[item.get(row, 0) for item in columns]
                           for row in alternate_rows])
    active = [(row, value) for row, value in zip(rows, left) if value]
    predicted = [(1, (2 * g + 7) // math.gcd(2 * g + 7, 3 * g + 7)),
                 (0, -(3 * g + 7) // math.gcd(2 * g + 7, 3 * g + 7))]
    row_relation = (2 * g + 7) * primary[rows.index(1), :] - \
        (3 * g + 7) * primary[rows.index(0), :]
    wrong_relation = (2 * g + 8) * primary[rows.index(1), :] - \
        (3 * g + 7) * primary[rows.index(0), :]
    records.append({"g": g, "q": q, "k": k, "rows": rows,
                    "left_cocircuit": left, "active": active,
                    "predicted_active": predicted,
                    "source_relation_zero": row_relation == sp.zeros(1, primary.cols),
                    "wrong_relation_nonzero": wrong_relation != sp.zeros(1, primary.cols),
                    "left_nullity": len(primary.T.nullspace()),
                    "alternate_nonzero": alternate.det() != 0})
    print(f"g={g} active={active}", flush=True)

checks = []
def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


record("COCIRCUIT.unique", "each preferred chart has a unique primitive left cocircuit",
       all(item["left_nullity"] == 1 for item in records),
       [(item["g"], item["left_nullity"]) for item in records])
record("COCIRCUIT.repair", "row exchange 1->3 kills the chart cocircuit",
       all(item["alternate_nonzero"] for item in records), "confirmed=7")
record("COCIRCUIT.formula",
       "the primitive cocircuit is the reduction of (2g+7)e1-(3g+7)e0",
       all(item["active"] == item["predicted_active"] for item in records),
       [(item["g"], item["active"]) for item in records])
record("COCIRCUIT.source",
       "the unnormalized two-row relation annihilates every source column",
       all(item["source_relation_zero"] for item in records), "confirmed=7")
record("FALSIFIER.shift",
       "shifting the first coefficient by one leaves a nonzero residual",
       all(item["wrong_relation_nonzero"] for item in records), "confirmed=7")

failed = [check for check in checks if check["status"] != "pass"]
output = {"schema": "marici.checker_results.v1",
          "checker": "magnetic_chart_cocircuit_checks.py",
          "author": "marici.Strominger",
          "scope": {"strength": "exact finite cocircuit formula",
                    "g": [2, 4, 6, 8, 10, 12, 14],
                    "locus": "q=2g+8, k=g/2+4"},
          "records": records, "checks": checks,
          "n_pass": len(checks) - len(failed), "n_fail": len(failed),
          "verdict": "At every tested even chart onset the preferred square matrix has the unique primitive left cocircuit obtained from (2g+7)e_1-(3g+7)e_0. The relation holds columnwise, so primary determinant failure is a literal dependence of target rows 1 and 0, not determinant-term cancellation. Replacing row 1 by row 3 restores a nonzero maximal minor."}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_chart_cocircuit.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
