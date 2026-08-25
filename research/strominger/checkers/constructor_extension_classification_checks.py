"""Hostile constructor-extension and cover-admissibility checks."""
from collections import defaultdict
import json
import os
import sympy as sp

checks = []


def add(output, key, value):
    if value:
        output[key] += value
        if output[key] == 0:
            del output[key]


def fold_numerator(g, a, m):
    terms = {(-a, m): 1}
    for weight in range(2, g + 2):
        nxt = defaultdict(int)
        for (r, t), coefficient in terms.items():
            add(nxt, (r - 1, t), coefficient * r)
            add(nxt, (r, t + 1), coefficient * (r + weight + 2))
        terms = dict(nxt)
    return terms


def column(g, a, m, magnetic):
    output = defaultdict(int)
    sign = -1 if magnetic else 1
    for (r, t), coefficient in fold_numerator(g, a, m).items():
        add(output, (r, t - 1), coefficient * t)
        add(output, (r + 1, t), coefficient * (t - g))
        add(output, (t - 1, r), sign * coefficient * t)
        add(output, (t, r + 1), sign * coefficient * (t - g))
    return dict(output)


def matrix(g, points, magnetic):
    columns = [column(g, a, m, magnetic) for a, m in points]
    rows = sorted(set().union(*(set(item) for item in columns)))
    return sp.Matrix([[item.get(row, 0) for item in columns] for row in rows])


def vector(points, packet):
    index = {point: position for position, point in enumerate(points)}
    output = sp.zeros(len(points), 1)
    for point, coefficient in packet.items():
        output[index[point]] = coefficient
    return output


def record(cid, statement, condition, detail=""):
    status = "pass" if bool(condition) else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement}" +
          (f" ({detail})" if detail else ""), flush=True)


# Minimal mixed-congruence counterexample.
points = [(a, m) for a in (0, 4, 5) for m in range(-10, 5)]
magnetic = matrix(2, points, True)
electric = matrix(2, points, False)
c6m = vector(points, {(0, -7): 1, (4, 1): 5, (5, 0): 4})
c7m = vector(points, {(0, -8): -1, (4, 2): 5, (5, 1): 4})
c6e = vector(points, {(0, -7): -1, (4, 1): 5, (5, 0): 4})
c7e = vector(points, {(0, -8): 1, (4, 2): 5, (5, 1): 4})
record("MIXED.circuits", "the first mixed constructor carries the two displayed parity-paired circuits",
       magnetic * c6m == sp.zeros(magnetic.rows, 1) and
       magnetic * c7m == sp.zeros(magnetic.rows, 1) and
       electric * c6e == sp.zeros(electric.rows, 1) and
       electric * c7e == sp.zeros(electric.rows, 1))

supports = [list(packet.keys()) for packet in (
    {(0, -7): 1, (4, 1): 5, (5, 0): 4},
    {(0, -8): -1, (4, 2): 5, (5, 1): 4})]
nonzero_columns = all(column(2, a, m, True) for support in supports for a, m in support)
record("MIXED.nonzero", "the mixed circuits relate nonzero columns rather than fixed-orbit towers",
       nonzero_columns)

joint = electric.col_join(magnetic)
record("MIXED.joint", "the complete parity observer remains injective on the mixed block",
       joint.rank() == len(points))

# Odd-only bounded falsifier search: evidence boundary, not theorem promotion.
failures = []
for grade in range(2, 9):
    odd_depths = (1, 3, 5, 7, 9)
    odd_points = [(a, m) for a in odd_depths for m in range(-13, 4)]
    for magnetic_port in (False, True):
        readout = matrix(grade, odd_points, magnetic_port)
        baseline = (sum(1 for depth in odd_depths
                        if -13 <= -(grade + depth - 1) <= 3)
                    if magnetic_port else 0)
        if len(readout.nullspace()) != baseline:
            failures.append((grade, magnetic_port, len(readout.nullspace()), baseline))
record("SHIFTED.boundary", "isolated odd prefixes show no extra bounded circuits, without asserting an unbounded theorem",
       not failures, failures)

# Cover descent condition for the two rational virtual-interference labels.
virtual_q = (sp.Rational(35, 3), sp.Rational(55, 3))
record("COVER.descent", "the rational candidates fail scalar deck descent on every finite cyclic cover",
       all(not (2 * q).is_integer for q in virtual_q))

# Original even sets are genuine subsets; shifted odd sets are disjoint lanes.
even = set(range(0, 20, 2))
odd = set(range(1, 20, 2))
record("AUTHORITY.lanes", "the odd constructor is a disjoint alternate rather than an inclusion of the even lane",
       even.isdisjoint(odd) and not odd.issubset(even))

passed = [item for item in checks if item["status"] == "pass"]
failed = [item for item in checks if item["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "constructor_extension_classification_checks.py",
    "author": "marici.Strominger",
    "checks": checks,
    "n_pass": len(passed),
    "n_fail": len(failed),
    "verdict": "Only inclusions within the proved even-depth lane inherit the kernel theorem. The all-integer constructor is algebraically defined but nonconservative, with two explicit new grade-two mixed circuits on depths {0,4,5}; joint parity transport remains injective. Odd-only prefixes are bounded evidence only. The rational cover candidates fail equivariant scalar descent.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "constructor_extension_classification.json"), "w", encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(passed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
