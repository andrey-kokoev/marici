"""Two-chart determinant atlas checker for the first q=12 chart failure."""
import json
import os
import sympy as sp

prefix_path = os.path.join(os.path.dirname(__file__), "magnetic_memory_one_checks.py")
with open(prefix_path, encoding="utf-8") as source_handle:
    exec(source_handle.read().split("checks = []")[0])


def chart_data(k):
    columns = component(2, k, 12)
    primary_rows = hall_rows(columns)
    primary = sp.Matrix([[item.get(row, 0) for item in columns]
                         for row in primary_rows])
    all_rows = sorted(set().union(*(item.keys() for item in columns)))
    full = sp.Matrix([[item.get(row, 0) for item in columns] for row in all_rows])
    pivot_indices = full.T.rref()[1]
    alternate_rows = [all_rows[index] for index in pivot_indices]
    alternate = sp.Matrix([[item.get(row, 0) for item in columns]
                           for row in alternate_rows])
    return primary_rows, primary, alternate_rows, alternate, full


checks = []
def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


data = [chart_data(k) for k in range(0, 21)]
record("ATLAS.coincide", "primary and alternate charts coincide through cutoff four",
       all(set(data[k][0]) == set(data[k][2]) for k in range(0, 5)),
       "0<=k<=4")

exchanges = [(k, sorted(set(primary_rows) - set(alternate_rows)),
              sorted(set(alternate_rows) - set(primary_rows)))
             for k, (primary_rows, _, alternate_rows, _, _) in
             enumerate(data[5:], start=5)]
record("ATLAS.exchange", "one persistent row exchange gives the alternate chart",
       all(drop == [1] and add == [3] for _, drop, add in exchanges),
       str(exchanges[:4]))

record("ATLAS.nested", "the alternate row sets remain nested after the transition",
       all(set(data[k - 1][2]) <= set(data[k][2]) for k in range(1, 21)),
       "0<=k<=20")
record("ATLAS.cover", "the alternate chart is nonzero wherever the primary chart vanishes",
       all(data[k][3].det() != 0 for k in range(5, 21)) and
       all(data[k][1].det() == 0 for k in range(5, 21)),
       f"alternate_D5={data[5][3].det()}")
record("ATLAS.rank", "every q=12 component remains full column rank",
       all(full.rank() == full.cols for _, _, _, _, full in data),
       "0<=k<=20")

def q12_character(k):
    a = 2 * k
    return int(12 * 2 * 5 * sp.rf(a, 2) * sp.rf(a, 1) * (a + 13))


ratio_failures = []
for k in range(8, 21):
    ratio = sp.Rational(data[k][3].det(), data[k - 1][3].det())
    if abs(ratio) != q12_character(k):
        ratio_failures.append((k, ratio, q12_character(k)))
record("ATLAS.transfer", "the replacement chart resumes the q=12 parity character",
       not ratio_failures, f"8<=k<=20; failures={ratio_failures}")

# The transition step itself is nonmultiplicative in the old scalar chart.
transition_ratio = sp.Rational(data[5][3].det(), data[4][3].det())
record("ATLAS.transition", "the chart transition has a finite nonzero rational coordinate",
       transition_ratio == sp.Rational(-809600, 3), str(transition_ratio))

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_q12_atlas_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "finite-range two-chart transfer theorem",
              "g": 2, "q": 12, "k": [0, 20]},
    "checks": checks, "n_pass": len(checks) - len(failed), "n_fail": len(failed),
    "verdict": "At (g,q,k)=(2,12,5), replace target row 1 by row 3. This single row exchange gives a nested alternate maximal-minor chart that stays nonzero through k=20 while the primary chart remains zero. The full component is injective throughout. From k=8 onward, alternate determinant ratios recover the q=12 parity character up to fixed orientation sign; the finite chart transition coordinate is -809600/3. This demonstrates a two-chart determinant atlas, not a kernel exception."
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_q12_atlas.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
