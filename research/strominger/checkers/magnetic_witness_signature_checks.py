"""Typed witness-signature checker for presentation and transport failures."""
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


def full_matrix(columns):
    rows = sorted(set().union(*(item.keys() for item in columns)))
    return rows, sp.Matrix([[item.get(row, 0) for item in columns] for row in rows])


checks = []
def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


# Presentation boundary: the selected square observation map P*M is singular,
# but its apparent right-kernel vector is not a kernel vector of the full map M.
presentation_records = []
for g in range(2, 16, 2):
    q, k = 2 * g + 8, g // 2 + 4
    columns = component(g, k, q)
    all_rows, full = full_matrix(columns)
    rows = hall_rows(columns)
    chart = sp.Matrix([[item.get(row, 0) for item in columns] for row in rows])
    chart_kernel = chart.nullspace()
    apparent = chart_kernel[0]
    alternate_rows = [3 if row == 1 else row for row in rows]
    alternate = sp.Matrix([[item.get(row, 0) for item in columns]
                           for row in alternate_rows])
    presentation_records.append({
        "g": g, "q": q, "k": k,
        "chart_left_nullity": len(chart.T.nullspace()),
        "chart_right_nullity": len(chart_kernel),
        "full_right_nullity": len(full.nullspace()),
        "apparent_kernel_full_residual_nonzero":
            full * apparent != sp.zeros(full.rows, 1),
        "alternate_right_nullity": len(alternate.nullspace())})

record("TYPE.presentation",
       "a chart kernel at the even divisor is not a kernel of the represented map",
       all(item["chart_right_nullity"] == 1 and
           item["full_right_nullity"] == 0 and
           item["apparent_kernel_full_residual_nonzero"]
           for item in presentation_records),
       [(item["g"], item["chart_right_nullity"], item["full_right_nullity"])
        for item in presentation_records])
record("TYPE.cocircuit",
       "the presentation witness is a unique observation cocircuit",
       all(item["chart_left_nullity"] == 1 for item in presentation_records),
       "confirmed=7")
record("TYPE.transition",
       "the adjacent observation chart removes both artificial null directions",
       all(item["alternate_right_nullity"] == 0 for item in presentation_records),
       "row exchange 1->3")

# Transport boundary: the primitive right circuit is killed by the full map,
# so no choice of target observations can restore faithfulness.
q7_columns = component(2, 3, 7)
q7_rows, q7_full = full_matrix(q7_columns)
q7_kernel = primitive(list(q7_full.nullspace()[0]))
expected_q7 = [1, 0, 0, 0, 0, -3, 0, 2]
record("TYPE.transport",
       "the q=7 witness is a primitive circuit of the full represented map",
       q7_kernel == expected_q7 and
       q7_full * sp.Matrix(expected_q7) == sp.zeros(q7_full.rows, 1),
       f"active={[value for value in expected_q7 if value]}")
record("TYPE.irreparable",
       "full-map rank loss cannot be repaired by changing target observations",
       q7_full.rank() == q7_full.cols - 1,
       f"rank={q7_full.rank()}; columns={q7_full.cols}")

# The q=1 initialization residue supplies the second full-map circuit type.
q1_columns = component(2, 0, 1)
_, q1_full = full_matrix(q1_columns)
q1_kernel = primitive(list(q1_full.nullspace()[0]))
record("TYPE.initial",
       "the q=1 initialization witness is also a primitive full-map circuit",
       q1_kernel in ([1, -1], [-1, 1]) and
       q1_full * sp.Matrix(q1_kernel) == sp.zeros(q1_full.rows, 1),
       q1_kernel)

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_witness_signature_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "exact typed-witness separation",
              "presentation_family": "even g=2..14, q=2g+8, k=g/2+4",
              "transport_fibers": [[2, 1, 0], [2, 7, 3]]},
    "checks": checks, "n_pass": len(checks) - len(failed), "n_fail": len(failed),
    "presentation_records": presentation_records,
    "transport_witnesses": {"q1": q1_kernel, "q7": expected_q7},
    "verdict": "The witness signature is typed by the map on which a null vector lives. At every tested even chart boundary, the selected observation map P*M has left and right nullity one, but the apparent right null vector has nonzero residual under the full M and disappears after the row transition. At q=1 and q=7, the primitive right circuits are annihilated by the full map, so no target-chart change can repair them."
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_witness_signature.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
