"""Alternating-cycle falsifier for global magnetic triangularity."""
import json
import os

import sympy as sp

prefix_path = os.path.join(os.path.dirname(__file__), "magnetic_memory_one_checks.py")
namespace = {"__file__": prefix_path, "__name__": "magnetic_cycle_prefix"}
with open(prefix_path, encoding="utf-8") as source_handle:
    prefix = source_handle.read().split("checks = []")[0]
exec(compile(prefix, prefix_path, "exec"), namespace)
component = namespace["component"]
hall_rows = namespace["hall_rows"]


def matching_terms(columns, rows, cap=3):
    options = [[i for i, row in enumerate(rows) if columns[j].get(row, 0)]
               for j in range(len(columns))]
    order = sorted(range(len(columns)), key=lambda j: len(options[j]))
    output = []

    def extend(step, used, matching):
        if len(output) >= cap:
            return
        if step == len(order):
            output.append(dict(matching))
            return
        column = order[step]
        for row_index in options[column]:
            if row_index not in used:
                matching[column] = row_index
                extend(step + 1, used | {row_index}, matching)
                matching.pop(column, None)

    extend(0, set(), {})
    return output


checks = []


def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


# q=1 is the scalar/interval case: every tested preferred Hall minor has one
# determinant term.  Higher q develops alternating cycles immediately.
q1_failures = []
for g in range(3, 13):
    for k in range(2, 10):
        columns = component(g, k, 1)
        rows = hall_rows(columns)
        if len(matching_terms(columns, rows, cap=2)) != 1:
            q1_failures.append((g, k))
record("Q1.unique", "the q=1 preferred Hall chart has a unique determinant term",
       not q1_failures, "3<=g<=12; 2<=k<=9")

first_cycles = {}
for q in range(2, 9):
    k = q // 2 + 2
    for g in range(2, 9):
        columns = component(g, k, q)
        try:
            rows = hall_rows(columns)
        except AssertionError:
            continue
        terms = matching_terms(columns, rows)
        if len(terms) > 1:
            first_cycles[q] = (g, k, len(columns), len(terms))
            break
record("QGT1.cycles", "every q=2..8 has an alternating cycle at its first stable step",
       set(first_cycles) == set(range(2, 9)), first_cycles)

# The smallest stable obstruction is a literal supported K_2,2.
columns = component(2, 3, 2)
cycle_rows = [-4, -3]
cycle_columns = [2, 5]
cycle = sp.Matrix([[columns[j].get(row, 0) for j in cycle_columns]
                   for row in cycle_rows])
record("FALSIFIER.smallest", "the (g,q,k)=(2,2,3) stable block contains a nonzero K_2,2",
       all(cycle) and cycle == sp.Matrix([[-30, 60], [-10, 100]]), cycle.tolist())
record("FALSIFIER.cancel", "the first cycle has two nonzero determinant terms with partial cancellation",
       cycle[0, 0] * cycle[1, 1] == -3000 and
       cycle[0, 1] * cycle[1, 0] == -600 and cycle.det() == -2400,
       "-3000-(-600)=-2400")

# Multiple determinant terms do not imply rank loss.
rank_failures = []
for q, (g, k, _, _) in first_cycles.items():
    columns = component(g, k, q)
    rows = hall_rows(columns)
    matrix = sp.Matrix([[column.get(row, 0) for column in columns] for row in rows])
    if matrix.det() == 0:
        rank_failures.append((g, q, k))
record("RANK.separate", "the first stable alternating cycles remain full rank",
       not rank_failures, "q=2..8")

# Odd q begins with an oriented cycle whose two Leibniz contributions reinforce.
columns = component(2, 3, 3)
odd_cycle = sp.Matrix([[columns[j].get(row, 0) for j in [0, 3]]
                       for row in [1, 0]])
record("ORIENTATION.parity", "the first q=3 cycle reinforces rather than partially cancels",
       odd_cycle == sp.Matrix([[-80, -20], [-40, 20]]) and
       odd_cycle.det() == -2400, odd_cycle.tolist())

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_stable_cycle_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "exact bounded falsification of global triangularity",
              "q": [1, 8], "g": [2, 12], "k": [2, 9]},
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": "The interval filtration globalizes only to a banded quotient filtration. The q=1 preferred chart has a unique determinant term in the tested range, but every q>=2 tested develops an alternating cycle at the first stable step. The smallest is the full-rank K_2,2 at (2,2,3). Thus Hall support gives local pivots, while cycle orientation is genuinely required for higher q.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_stable_cycles.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
