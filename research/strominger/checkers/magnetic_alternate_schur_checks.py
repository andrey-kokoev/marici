"""Exact fixed-width Schur reduction of the even alternate chart."""
import json
import os
import sympy as sp

prefix_path = os.path.join(os.path.dirname(__file__), "magnetic_memory_one_checks.py")
with open(prefix_path, encoding="utf-8") as source_handle:
    exec(source_handle.read().split("checks = []")[0])


def permutation_sign(order):
    inversions = sum(order[i] > order[j] for i in range(len(order))
                     for j in range(i + 1, len(order)))
    return -1 if inversions % 2 else 1


records = []
for g in range(2, 32, 2):
    q, k = 2 * g + 8, g // 2 + 4
    columns = component(g, k, q)
    rows = [3 if row == 1 else row for row in hall_rows(columns)]
    endpoint_columns = [0, len(columns) - 1]
    interior_columns = [index for index in range(len(columns))
                        if index not in endpoint_columns]
    endpoint_rows = [rows.index(0), rows.index(3)]
    interior_rows = [index for index in range(len(rows))
                     if index not in endpoint_rows]
    A = sp.Matrix([[columns[j].get(rows[i], 0) for j in interior_columns]
                   for i in interior_rows])
    B = sp.Matrix([[columns[j].get(rows[i], 0) for j in endpoint_columns]
                   for i in interior_rows])
    C = sp.Matrix([[columns[j].get(rows[i], 0) for j in interior_columns]
                   for i in endpoint_rows])
    E = sp.Matrix([[columns[j].get(rows[i], 0) for j in endpoint_columns]
                   for i in endpoint_rows])
    core_det = A.det()
    schur = sp.simplify(E - C * A.inv() * B)
    row_sign = permutation_sign(interior_rows + endpoint_rows)
    column_sign = permutation_sign(interior_columns + endpoint_columns)
    records.append({
        "g": g, "core_nonzero": core_det != 0,
        "s11": int(schur[0, 0]), "s12": int(schur[0, 1]),
        "s21": int(schur[1, 0]), "s22": str(schur[1, 1]),
        "s22_nonzero": schur[1, 1] != 0,
        "s11_formula": schur[0, 0] == -(2 * g + 7) * sp.rf(4, g),
        "s12_formula": schur[0, 1] == -sp.rf(g + 8, g),
        "factorization":
            sp.det(sp.Matrix([[columns[j].get(rows[i], 0)
                               for j in range(len(columns))]
                              for i in range(len(rows))])) ==
            row_sign * column_sign * core_det * schur.det()})

checks = []
def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


record("SCHUR.core", "the interior core is invertible at every tested even grade",
       all(item["core_nonzero"] for item in records), "g=2..30")
record("SCHUR.triangular", "the endpoint Schur block has zero lower-left entry",
       all(item["s21"] == 0 for item in records), "g=2..30")
record("SCHUR.first", "S11=-(2g+7)*(4 rising g)",
       all(item["s11_formula"] for item in records), "g=2..30")
record("SCHUR.second", "S12=-(g+8 rising g)",
       all(item["s12_formula"] for item in records), "g=2..30")
record("SCHUR.transverse", "the remaining transverse response tau_g is nonzero",
       all(item["s22_nonzero"] for item in records),
       [(item["g"], item["s22"]) for item in records[:6]] + ["..."])
record("SCHUR.factor", "the full alternate determinant equals det(A)*det(S)",
       all(item["factorization"] for item in records), "g=2..30")

# A false zero transverse response would force the already computed alternate
# determinant to vanish; retain one exact nonzero witness as a deliberate gate.
record("FALSIFIER.tau", "tau_2 is the nonzero rational 320/3",
       records[0]["s22"] == "320/3", records[0]["s22"])

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_alternate_schur_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "exact finite fixed-width alternate-chart reduction",
              "g": "even 2..30", "locus": "q=2g+8,k=g/2+4"},
    "checks": checks, "n_pass": len(checks) - len(failed), "n_fail": len(failed),
    "records": records,
    "verdict": "At every even grade through 30, eliminating the interior rows and columns reduces the row-3 alternate chart to an upper-triangular 2x2 Schur block. Its first row is exactly (-(2g+7)(4 rising g), -(g+8 rising g)); the lower-left entry vanishes and the remaining transverse response tau_g is nonzero. Thus unbounded alternate-chart nonvanishing reduces to invertibility of the interior core and tau_g nonvanishing."
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_alternate_schur.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
