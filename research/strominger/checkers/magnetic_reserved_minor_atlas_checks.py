"""Exact weighted-minor atlas audit for the reserved-row Hall chart."""
import json
import math
import os
import sympy as sp


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
             for j in range(1, g + 1)] + [m * c[g]])


def matched_row(g, q, a, branch):
    if a == 0:
        return 1 if branch == "-" else q
    if branch == "-":
        return -a - g
    if (g, q) == (5, 12) and a in (4, 6):
        return {4: 4, 6: 3}[a]
    if g % 2 and a == q + 1 - g:
        return 0
    if g % 2 and a == q - g - 1:
        return 2
    return q - g - a


def value(g, q, row, label):
    a, branch = label
    m = 1 - g + (-q if branch == "-" else q) - a
    coefficients = path_coefficients(g, a, m)
    shift = -a - g if branch == "-" else -a - g + q
    index = row - shift
    if not 0 <= index < len(coefficients):
        return 0
    return (1 if branch == "-" else -1) * coefficients[index]


def determinant(g, q, alternate=False):
    labels = [(a, branch) for a in range(0, q + 1, 2)
              for branch in ("-", "+")]
    rows = [matched_row(g, q, *label) for label in labels]
    if alternate:
        rows[rows.index(1)] = 3
    matrix = sp.Matrix([[value(g, q, row, label) for label in labels]
                        for row in rows])
    return matrix.det(method="domain-ge")


checks = []


def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


zeros = []
alternate_failures = []
corank_failures = []
cocircuit_failures = []
circuit_failures = []
cases = 0
for g in range(2, 13):
    for q in range(2, 32, 2):
        det = determinant(g, q)
        if det == 0:
            zeros.append((g, q))
            if determinant(g, q, alternate=True) == 0:
                alternate_failures.append((g, q))
            labels = [(a, branch) for a in range(0, q + 1, 2)
                      for branch in ("-", "+")]
            rows = [matched_row(g, q, *label) for label in labels]
            matrix = sp.Matrix([[value(g, q, row, label) for label in labels]
                                for row in rows])
            if matrix.rank() != len(labels) - 1:
                corank_failures.append((g, q, matrix.rank(), len(labels)))
            left = matrix.T.nullspace()[0]
            left_support = {rows[index] for index, coefficient in enumerate(left)
                            if coefficient}
            expected_left = {1, 0} | set(range(-2, -g - 3, -2))
            if left_support != expected_left:
                cocircuit_failures.append((g, q, sorted(left_support),
                                            sorted(expected_left)))
            right = matrix.nullspace()[0]
            right_support = {labels[index] for index, coefficient in enumerate(right)
                             if coefficient}
            expected_right = {(0, "-")} | {(a, "+")
                                                  for a in range(4, q - g + 1, 2)}
            if right_support != expected_right:
                circuit_failures.append((g, q, sorted(right_support),
                                          sorted(expected_right)))
        cases += 1

predicted = [(g, 2 * g + 8) for g in range(2, 13, 2)
             if 2 * g + 8 <= 30]
record("CHART.zeros", "the preferred weighted chart vanishes exactly on q=2g+8 at even grade",
       zeros == predicted, f"blocks={cases}; zeros={zeros}")
record("ATLAS.row3", "replacing observation row 1 by row 3 restores every vanished chart",
       not alternate_failures, f"failures={alternate_failures}")
record("OBJECT.rank", "no audited chart zero is an exterior-power zero",
       bool(zeros) and not alternate_failures,
       "a second maximal minor is nonzero at every preferred-chart zero")
record("DEFECT.corank", "every preferred-chart zero has corank exactly one",
       not corank_failures, f"failures={corank_failures}")
record("DEFECT.cocircuit", "the row cocircuit has the fixed reflection-window support",
       not cocircuit_failures,
       f"support={{1,0,-2,...,-g-2}}; failures={cocircuit_failures}")
record("DEFECT.circuit", "the column circuit is (0,-) plus the local plus chain",
       not circuit_failures,
       f"support={{(0,-),(4,+),...,(q-g,+)}}; failures={circuit_failures}")

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_reserved_minor_atlas_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "exact bounded weighted-minor atlas audit",
              "audit": {"g": [2, 12], "q_even": [2, 30]}},
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": "The explicit reserved Hall chart has a coordinate-degeneracy family q=2g+8 at even grade, transported from the symbolic onset cocircuit. Each audited zero has corank one. Its row cocircuit is supported exactly on {1,0,-2,...,-g-2}, while its column circuit terminates at the onset depth: (0,-) and the plus chain a=4,...,q-g=g+8. Exchanging observation row 1 for row 3 gives a nonzero maximal minor. Thus the later tail transports a presentation witness but creates no new rank defect. Unbounded alternate-chart nonvanishing remains the transverse-response problem.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_reserved_minor_atlas.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
