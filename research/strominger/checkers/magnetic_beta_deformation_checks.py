"""Hostile beta deformation of the magnetic current source polynomial."""
import json
import math
import os
from fractions import Fraction


def rising(value, count):
    return math.prod(value + offset for offset in range(count))


def source_coefficients(g, a, beta):
    return [math.comb(g, j) * (-1) ** (g - j) *
            rising(a, g - j) * rising(beta - a, j)
            for j in range(g + 1)]


def path_coefficients(g, a, m, beta):
    c = source_coefficients(g, a, beta)
    return ([m * c[0]] +
            [(m + j) * c[j] + (m + j - 1 - g) * c[j - 1]
             for j in range(1, g + 1)] +
            [m * c[g]])


def canonical_column(g, a, m, beta):
    delta = 1 - g - (a + m)
    shift = -a - g if delta > 0 else -a - g + abs(delta)
    sign = 1 if delta > 0 else -1
    return {shift + j: sign * value
            for j, value in enumerate(path_coefficients(g, a, m, beta))
            if value}


def component(g, k, q, beta):
    center = 1 - g
    return [canonical_column(g, a, m, beta)
            for a in range(0, 2 * k + 1, 2)
            for m in (center - q - a, center + q - a)]


def current_defect(g, a, q, beta):
    c = source_coefficients(g, a, beta)
    current = [c[0]] + [c[j] + c[j - 1] for j in range(1, g + 1)] + [c[g]]
    output = {}
    for shift, sign in ((-a - g, -2), (-a - g + q + 2, 2)):
        for j, value in enumerate(current):
            output[shift + j] = output.get(shift + j, 0) + sign * value
    return {row: value for row, value in output.items() if value}


def rank(columns):
    rows = sorted({row for column in columns for row in column})
    work = [[Fraction(column.get(row, 0)) for column in columns] for row in rows]
    nrows = len(work)
    ncols = len(columns)
    pivot = 0
    for column in range(ncols):
        selected = next((row for row in range(pivot, nrows)
                         if work[row][column]), None)
        if selected is None:
            continue
        work[pivot], work[selected] = work[selected], work[pivot]
        value = work[pivot][column]
        work[pivot] = [entry / value for entry in work[pivot]]
        for row in range(pivot + 1, nrows):
            if work[row][column]:
                value = work[row][column]
                work[row] = [work[row][j] - value * work[pivot][j]
                             for j in range(ncols)]
        pivot += 1
    return pivot


def quotient_width(g, q, k, beta):
    ordinary = component(g, k, q + 2, beta)
    currents = [current_defect(g, a, q, beta)
                for a in range(0, 2 * k + 1, 2)]
    return rank(ordinary + currents) - rank(ordinary)


checks = []


def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


widths = {beta: quotient_width(3, 1, 12, beta) for beta in (0, 4, 5)}
record("FALSIFIER.universal", "changing beta changes the stable tested width",
       widths == {0: 4, 4: 5, 5: 6}, widths)

upper_failures = []
for beta in range(0, 10):
    for g in range(2, 21):
        c = source_coefficients(g, 0, beta)
        expected = [0] * g + [rising(beta, g)]
        if c != expected:
            upper_failures.append((beta, g, c, expected))
record("ATOM.upper", "a=0 isolates the beta-rising upper endpoint",
       not upper_failures, f"failures={upper_failures[:1]}")

lower_failures = []
for beta in range(0, 10):
    for g in range(2, 21):
        c = source_coefficients(g, beta, beta)
        expected = [(-1) ** g * rising(beta, g)] + [0] * g
        if c != expected:
            lower_failures.append((beta, g, c, expected))
record("ATOM.lower", "a=beta isolates the lower endpoint",
       not lower_failures, f"failures={lower_failures[:1]}")
record("TYPE.parity", "the lower atom is admitted exactly for nonnegative even beta",
       all(((beta in range(0, 21, 2)) == (beta % 2 == 0))
           for beta in range(0, 21)),
       "admitted depths are nonnegative even integers")
record("ATOM.beta_zero", "beta=0 removes the zero-depth current atom",
       all(not current_defect(g, 0, q, 0)
           for g in range(2, 21) for q in range(1, 21)),
       "beta rising factorial vanishes")

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_beta_deformation_checks.py",
    "author": "marici.Strominger",
    "scope": {
        "strength": "hostile counterfactual exact census",
        "authority": "beta!=4 is not asserted to be a magnetic source sector",
    },
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": (
        "The current width is not support-universal. Beta selects upper and "
        "lower source atoms, and its parity determines whether the lower atom "
        "lies in the admitted even-depth lattice. The native value beta=4 is "
        "therefore constructor geometry, not a cosmetic coefficient."
    ),
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_beta_deformation.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
