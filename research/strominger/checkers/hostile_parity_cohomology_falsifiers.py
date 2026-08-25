"""Executable hostile boundary tests for the parity-cohomology theorem."""
from collections import defaultdict
import json
import math
import os
import sympy as sp

z, zb, u = sp.symbols("z zb u")
G0 = -2 * zb / (1 + z * zb)
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


def column(g, a, m, magnetic=True):
    output = defaultdict(int)
    sign = -1 if magnetic else 1
    for (r, t), coefficient in fold_numerator(g, a, m).items():
        add(output, (r, t - 1), coefficient * t)
        add(output, (r + 1, t), coefficient * (t - g))
        add(output, (t - 1, r), sign * coefficient * t)
        add(output, (t, r + 1), sign * coefficient * (t - g))
    return dict(output)


def matrix(g, points, magnetic=True, rows=None):
    columns = [column(g, a, m, magnetic) for a, m in points]
    rows = rows or sorted(set().union(*(set(item) for item in columns)))
    return sp.Matrix([[item.get(row, 0) for item in columns] for row in rows])


def simp(value):
    return sp.cancel(sp.together(sp.expand(value)))


def sigma(value):
    return value.subs([(z, zb), (zb, z)], simultaneous=True)


def chain(grade, datum, barred=False):
    gamma = sigma(G0) if barred else G0
    variable = zb if barred else z
    value = datum
    for weight in range(2, grade + 2):
        value = simp(sp.diff(value, variable) - weight * gamma * value)
    return value


def pair(grade, datum):
    return chain(grade, datum), chain(grade, sigma(datum), barred=True)


def record(cid, statement, condition, detail=""):
    status = "pass" if bool(condition) else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement}" +
          (f" ({detail})" if detail else ""), flush=True)


# F1: a bounded target box creates a spurious source kernel.
points = [(0, -4), (0, -3)]
full = matrix(2, points, True)
box_rows = [(-1, 1), (1, -1)]
truncated = matrix(2, points, True, rows=box_rows)
record("F1.target", "target truncation lowers rank and creates a spurious class",
       full.rank() == 2 and truncated == sp.Matrix([[0, 60], [0, -60]]) and
       truncated.rank() == 1)

# F2: cross-depth residue cancellation is rational-exact.
datum = 2 * z ** -2 * zb ** -3 - z ** -4 * zb ** -5
f, fb = pair(2, datum)
phi = simp(sp.integrate(f, z))
record("F2.depthwise", "two individually nonexact towers can combine rational-exactly",
       simp(sp.residue(f, z, 0)) == 0 and not phi.has(sp.log) and
       simp(sp.diff(phi, z) - f) == 0 and simp(sp.diff(phi, zb) - fb) == 0)

# F3: primitive pairwise circuits span index five, not the saturated kernel.
row = sp.Matrix([[10, 21, 36]])
pairwise = sp.Matrix([[21, 18], [-10, 0], [0, -5]])
missing = sp.Matrix([-12, 4, 1])
minors = [abs(int(pairwise[list(rows), :].det()))
          for rows in ((0, 1), (0, 2), (1, 2))]
record("F3.saturation", "pairwise primitive circuits can miss a primitive kernel vector",
       row * pairwise == sp.zeros(1, 2) and row * missing == sp.zeros(1, 1) and
       math.gcd(*minors) == 5)

# F4: rational rank is stable while the integral gcd changes.
record("F4.arithmetic", "adding a depth refines the Smith index without changing rational rank",
       math.gcd(3360, 7056) == 336 and
       sp.Matrix([[3360]]).rank() == sp.Matrix([[3360, 7056]]).rank() == 1)

# F5: deleting one E1 vertex destroys the circuit.
e1_matrix = matrix(2, [(0, -2), (0, 0)], True)
record("F5.deletion", "source projection does not descend to the magnetic kernel",
       e1_matrix * sp.Matrix([-1, 1]) == sp.zeros(e1_matrix.rows, 1) and
       e1_matrix[:, [1]].rank() == 1)

# F6: objectwise full-rank gauges need not commute with inclusion.
small_h = sp.Matrix([[1, 1], [1, -1]])
large_h = sp.kronecker_product(small_h, sp.eye(2))
sheet_inclusion = sp.Matrix([[1, 0], [0, 0], [0, 1], [0, 0]])
readout_inclusion = sheet_inclusion
gauged_large = sp.diag(2, 1, 1, 1) * large_h
record("F6.gauge", "full-rank cutoff-dependent port gauges can break the reconstruction square",
       small_h.det() != 0 and gauged_large.det() != 0 and
       gauged_large * sheet_inclusion != readout_inclusion * small_h)

# F7: mixed integer-depth circuit beyond the even theorem.
mixed_points = [(a, m) for a in (0, 4, 5) for m in range(-10, 5)]
mixed = matrix(2, mixed_points, True)
index = {point: position for position, point in enumerate(mixed_points)}
circuit = sp.zeros(len(mixed_points), 1)
for point, coefficient in {(0, -7): 1, (4, 1): 5, (5, 0): 4}.items():
    circuit[index[point]] = coefficient
record("F7.constructor", "all-integer depth mixing creates a new single-port circuit",
       mixed * circuit == sp.zeros(mixed.rows, 1))

# F8: the radial denominator has no divisor beyond u=0,-1, and infinity has
# zero residue; subtracting eta leaves a rational derivative.
failures = []
eta = 1 / u - 1 / (1 + u)
for grade in range(2, 7):
    for depth in (2, 4, 6):
        value = u ** -depth
        for weight in range(2, grade + 2):
            value = simp(sp.diff(value, u) + 2 * weight * value / (1 + u))
        denominator = sp.factor(sp.denom(value))
        allowed = simp(denominator / (u ** (depth + grade) * (1 + u) ** grade))
        residue = simp(sp.residue(value, u, 0))
        infinity = -simp(sp.residue(value.subs(u, 1 / z) / z ** 2, z, 0))
        primitive = simp(sp.integrate(simp(value - residue * eta), u))
        if allowed != 1 or infinity != 0 or primitive.has(sp.log) or \
                simp(sp.diff(primitive, u) - (value - residue * eta)) != 0:
            failures.append((grade, depth, denominator, infinity))
record("F8.divisors", "no hidden logarithmic divisor survives radial Hermite reduction",
       not failures, failures)

passed = [item for item in checks if item["status"] == "pass"]
failed = [item for item in checks if item["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "hostile_parity_cohomology_falsifiers.py",
    "author": "marici.Strominger",
    "checks": checks,
    "n_pass": len(passed),
    "n_fail": len(failed),
    "verdict": "Eight hostile boundaries are reproduced exactly: target truncation, false depthwise cohomology, nonsaturated pairwise bases, independent arithmetic stabilization, forbidden source deletion, nonnatural port gauges, nonconservative integer-depth mixing, and hidden-divisor absence.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "hostile_parity_cohomology_falsifiers.json"), "w", encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(passed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
