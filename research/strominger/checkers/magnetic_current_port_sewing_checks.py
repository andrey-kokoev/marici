"""Exact bounded span audit for the inter-component current defect."""
import json
import math
import os
from fractions import Fraction


def rising(value, count):
    return math.prod(value + offset for offset in range(count))


def source_coefficients(g, a):
    return [math.comb(g, j) * (-1) ** (g - j) *
            rising(a, g - j) * rising(4 - a, j)
            for j in range(g + 1)]


def path_coefficients(g, a, m):
    c = source_coefficients(g, a)
    return ([m * c[0]] +
            [(m + j) * c[j] + (m + j - 1 - g) * c[j - 1]
             for j in range(1, g + 1)] +
            [m * c[g]])


def canonical_column(g, a, m):
    delta = 1 - g - (a + m)
    shift = -a - g if delta > 0 else -a - g + abs(delta)
    sign = 1 if delta > 0 else -1
    return {shift + j: sign * value
            for j, value in enumerate(path_coefficients(g, a, m)) if value}


def component(g, k, q):
    center = 1 - g
    return [canonical_column(g, a, m)
            for a in range(0, 2 * k + 1, 2)
            for m in (center - q - a, center + q - a)]


def current_defect(g, a, q):
    c = source_coefficients(g, a)
    current = [c[0]] + [c[j] + c[j - 1] for j in range(1, g + 1)] + [c[g]]
    output = {}
    for shift, sign in ((-a - g, -2), (-a - g + q + 2, 2)):
        for j, value in enumerate(current):
            output[shift + j] = output.get(shift + j, 0) + sign * value
    return {row: value for row, value in output.items() if value}


def rank(matrix):
    work = [[Fraction(value) for value in row] for row in matrix]
    nrows = len(work)
    ncols = len(work[0]) if nrows else 0
    pivot_row = 0
    for column in range(ncols):
        pivot = next((row for row in range(pivot_row, nrows)
                      if work[row][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for row in range(pivot_row + 1, nrows):
            if work[row][column]:
                scale = work[row][column]
                work[row] = [work[row][j] - scale * work[pivot_row][j]
                             for j in range(ncols)]
        pivot_row += 1
        if pivot_row == nrows:
            break
    return pivot_row


def belongs_to_span(columns, vector):
    rows = sorted(set(vector) | {row for column in columns for row in column})
    matrix = [[column.get(row, 0) for column in columns] for row in rows]
    augmented = [line + [vector.get(row, 0)]
                 for line, row in zip(matrix, rows)]
    return rank(matrix) == rank(augmented)


checks = []


def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


same_cutoff = []
for g in range(2, 9):
    for k in range(2, 7):
        for q in range(1, 9):
            target = component(g, k, q + 2)
            for a in range(0, 2 * k + 1, 2):
                same_cutoff.append(
                    (g, k, q, a,
                     belongs_to_span(target, current_defect(g, a, q))))

record("SPAN.same_cutoff", "no tested defect belongs to the same-cutoff target image",
       all(not item[-1] for item in same_cutoff),
       f"cases={len(same_cutoff)}; first={same_cutoff[0]}")

expanded = []
for g in range(2, 9):
    for q in range(1, 9):
        for a in range(0, 9, 2):
            flags = [
                belongs_to_span(component(g, cutoff, q + 2),
                                current_defect(g, a, q))
                for cutoff in range(max(2, a // 2), 13)
            ]
            expanded.append((g, q, a, flags))

record("SPAN.expanded", "no tested defect enters the image under cutoff expansion",
       all(not any(item[-1]) for item in expanded),
       f"cases={len(expanded)}; cutoff<=12")
record("BOUNDARY.not_upper", "the bounded failures persist after adding deeper columns",
       all(len(item[-1]) >= 9 and not any(item[-1]) for item in expanded if item[2] <= 4),
       "a<=4 receives at least nine independent cutoff extensions")

smallest = next(item for item in same_cutoff if not item[-1])
record("FALSIFIER.smallest", "the smallest audited target already rejects internal sewing",
       smallest[:4] == (2, 2, 1, 0),
       smallest)

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_current_port_sewing_checks.py",
    "author": "marici.Strominger",
    "scope": {
        "strength": "bounded exact rational span census",
        "same_cutoff": "2<=g<=8, 2<=k<=6, 1<=q<=8",
        "expanded_cutoff": "2<=g<=8, 1<=q<=8, even 0<=a<=8, K<=12",
    },
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": (
        "The universal inter-component current defect is not generated by "
        "ordinary target columns anywhere in the bounded census, and remains "
        "outside after independent cutoff expansion. This is evidence for a "
        "genuine current port, pending an unbounded left-cokernel theorem."
    ),
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_current_port_sewing.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
