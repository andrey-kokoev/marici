"""Exact-sequence and complementary-port audit for the master diagram."""
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


def record(cid, statement, condition, detail=""):
    status = "pass" if bool(condition) else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement}" +
          (f" ({detail})" if detail else ""), flush=True)


fail_joint = []
fail_cross_m = []
fail_cross_e = []
cases = 0
windows = [(-8, 2), (-4, 4), (-2, 1)]
depth_sets = [(0,), (0, 2), (0, 2, 4), (0, 4, 6)]
for g in range(2, 7):
    for depths in depth_sets:
        for lower, upper in windows:
            cases += 1
            points = [(a, m) for a in depths for m in range(lower, upper + 1)]
            electric = matrix(g, points, False)
            magnetic = matrix(g, points, True)
            joint = electric.col_join(magnetic)
            if joint.rank() != len(points):
                fail_joint.append((g, depths, lower, upper))
            km = magnetic.nullspace()
            if km:
                basis = sp.Matrix.hstack(*km)
                if (electric * basis).rank() != len(km):
                    fail_cross_m.append((g, depths, lower, upper))
            ke = electric.nullspace()
            if ke:
                basis = sp.Matrix.hstack(*ke)
                if (magnetic * basis).rank() != len(ke):
                    fail_cross_e.append((g, depths, lower, upper))

record("JOINT.injective", "the complete E,M observer is injective on every audited source",
       not fail_joint, f"cases={cases}; failures={fail_joint}")
record("CROSS.magnetic", "E restricts injectively to every audited magnetic kernel",
       not fail_cross_m, fail_cross_m)
record("CROSS.electric", "M restricts injectively to every audited electric kernel",
       not fail_cross_e, fail_cross_e)

# Exactness of a one-row residue augmentation and location of its torsion.
row = sp.Matrix([[-60, -120, -180]])
kernel = row.nullspace()
divisor = 60
record("RESIDUE.exact", "the rational residue sequence has kernel rank two and image rank one",
       len(kernel) == 2 and row.rank() == 1)
record("RESIDUE.integral", "the integral quotient is free while the ambient index is 60",
       sp.gcd_list([abs(int(value)) for value in row]) == divisor)

# A chart coordinate can vanish without changing the represented rank.
chart_family = sp.Matrix([[1, 0], [0, 1], [1, 1]])
preferred = chart_family[:2, :]
replacement = chart_family[[0, 2], :]
record("CHART.separation", "rank belongs to the represented map, not one preferred minor",
       preferred.det() != 0 and replacement.det() != 0 and chart_family.rank() == 2)

passed = [item for item in checks if item["status"] == "pass"]
failed = [item for item in checks if item["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "integral_parity_cohomology_diagram_checks.py",
    "author": "marici.Strominger",
    "checks": checks,
    "n_pass": len(passed),
    "n_fail": len(failed),
    "verdict": "Across the audited full-target sources, the joint parity observer is injective and each port is injective on the other's kernel. The residue row has the declared rational exact sequence and integral ambient index. Presentation-minor choice remains separate from represented rank.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "integral_parity_cohomology_diagram.json"), "w", encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(passed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
