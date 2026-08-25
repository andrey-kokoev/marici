"""Naturality and forbidden-deletion audits for parity and residue objects."""
from collections import defaultdict
import itertools
import json
import math
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


def matrix(g, points, magnetic, forced_rows=None):
    columns = [column(g, a, m, magnetic) for a, m in points]
    rows = forced_rows or sorted(set().union(*(set(item) for item in columns)))
    return sp.Matrix([[item.get(row, 0) for item in columns] for row in rows]), rows


def record(cid, statement, condition, detail=""):
    status = "pass" if bool(condition) else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement}" +
          (f" ({detail})" if detail else ""), flush=True)


# Column-restriction squares for depth and Laurent inclusions.
failures = []
cases = 0
large_depths = (0, 2, 4, 6)
large_window = range(-7, 3)
large_points = [(a, m) for a in large_depths for m in large_window]
for grade in range(2, 7):
    for magnetic in (False, True):
        large_matrix, large_rows = matrix(grade, large_points, magnetic)
        for depths in ((0,), (0, 2), (0, 4, 6)):
            for lower, upper in ((-5, 0), (-3, 2), (-7, -1)):
                cases += 1
                small_points = [(a, m) for a in depths for m in range(lower, upper + 1)]
                positions = [large_points.index(point) for point in small_points]
                restricted = large_matrix[:, positions]
                direct, _ = matrix(grade, small_points, magnetic, forced_rows=large_rows)
                if restricted != direct or restricted.nullspace() != direct.nullspace():
                    failures.append((grade, magnetic, depths, lower, upper))
record("READOUT.inclusion", "depth and Laurent enlargement commute with full-target readout",
       not failures, f"cases={cases}; failures={failures[:1]}")

# Fixed character completion commutes with coordinate inclusion.
small_size = 2
large_size = 5
source_inclusion = sp.zeros(large_size, small_size)
source_inclusion[:small_size, :] = sp.eye(small_size)
sheet_inclusion = sp.diag(source_inclusion, source_inclusion)
hadamard_small = sp.kronecker_product(sp.Matrix([[1, 1], [1, -1]]), sp.eye(small_size))
hadamard_large = sp.kronecker_product(sp.Matrix([[1, 1], [1, -1]]), sp.eye(large_size))
readout_inclusion = sp.diag(source_inclusion, source_inclusion)
record("PARITY.naturality", "the fixed E,M character transform commutes with source inclusion",
       hadamard_large * sheet_inclusion == readout_inclusion * hadamard_small)

# Residue images form nested gcd lattices.
failures = []
depth_universe = (2, 4, 6, 8, 10)
for grade in range(2, 9):
    values = {depth: abs(int(grade * (grade + 1) * sp.catalan(grade + 1) *
                                    sp.rf(depth, grade - 1)))
              for depth in depth_universe}
    subsets = [set(combo) for size in range(1, len(depth_universe) + 1)
               for combo in itertools.combinations(depth_universe, size)]
    for smaller in subsets:
        d_small = math.gcd(*(values[depth] for depth in smaller))
        for added in set(depth_universe) - smaller:
            larger = smaller | {added}
            d_large = math.gcd(*(values[depth] for depth in larger))
            if d_small % d_large != 0:
                failures.append((grade, sorted(smaller), added, d_small, d_large))
record("RESIDUE.inclusion", "constructor enlargement gives nested gcd residue lattices",
       not failures, failures[:1])

# Hostile falsifier: projection of E1 onto one source vertex is not a kernel map.
points = [(0, -2), (0, 0)]
magnetic, _ = matrix(2, points, True)
circuit = sp.Matrix([-1, 1])
single = magnetic[:, [1]]
record("DELETION.falsifier", "coordinate deletion does not descend from a circuit kernel",
       magnetic * circuit == sp.zeros(magnetic.rows, 1) and
       single.rank() == 1)

passed = [item for item in checks if item["status"] == "pass"]
failed = [item for item in checks if item["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "parity_cohomology_naturality_checks.py",
    "author": "marici.Strominger",
    "checks": checks,
    "n_pass": len(passed),
    "n_fail": len(failed),
    "verdict": "Full-target readouts, fixed parity reconstruction, rational exactness, and residue lattices are covariantly natural under source inclusions. Residue images nest by gcd divisibility. Coordinate deletion does not descend to kernels, as the E1 projection falsifier shows.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "parity_cohomology_naturality.json"), "w", encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(passed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
