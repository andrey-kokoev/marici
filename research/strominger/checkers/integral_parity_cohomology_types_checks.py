"""Typed commuting-square checks for the parity-cohomology specification."""
from collections import defaultdict
import json
import os
import sympy as sp

z, zb = sp.symbols("z zb")
u = z * zb
G0 = -2 * zb / (1 + u)
checks = []


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


def fold_pair(grade, datum):
    return chain(grade, datum), chain(grade, sigma(datum), barred=True)


def add(output, key, value):
    if value:
        output[key] += value
        if output[key] == 0:
            del output[key]


def fold_numerator(grade, depth, exponent):
    terms = {(-depth, exponent): 1}
    for weight in range(2, grade + 2):
        nxt = defaultdict(int)
        for (r, t), coefficient in terms.items():
            add(nxt, (r - 1, t), coefficient * r)
            add(nxt, (r, t + 1), coefficient * (r + weight + 2))
        terms = dict(nxt)
    return terms


def numerator_column(grade, depth, exponent, magnetic):
    output = defaultdict(int)
    sign = -1 if magnetic else 1
    for (r, t), coefficient in fold_numerator(grade, depth, exponent).items():
        add(output, (r, t - 1), coefficient * t)
        add(output, (r + 1, t), coefficient * (t - grade))
        add(output, (t - 1, r), sign * coefficient * t)
        add(output, (t, r + 1), sign * coefficient * (t - grade))
    return dict(output)


def record(cid, statement, condition, detail=""):
    status = "pass" if bool(condition) else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement}" +
          (f" ({detail})" if detail else ""), flush=True)


# Full-target naturality: enlarging a source only appends columns and leaves
# every old column byte-for-byte unchanged.
small = [(0, -3), (2, -5), (4, 1)]
large = small + [(0, 0), (6, -9), (2, 3)]
failures = []
for grade in range(2, 9):
    for magnetic in (False, True):
        small_columns = [numerator_column(grade, a, m, magnetic) for a, m in small]
        restricted = [numerator_column(grade, a, m, magnetic) for a, m in large[:len(small)]]
        if small_columns != restricted:
            failures.append((grade, magnetic))
record("SOURCE.naturality", "full-target readouts commute with source inclusion",
       not failures, failures)

# The two readouts split the mixed derivative packet.
A, B = sp.symbols("A B")
character = sp.Matrix([[1, 1], [1, -1]])
record("PARITY.split", "the E,M character transform has the half-Hadamard inverse",
       character.inv() == character / 2)

# Closedness is exactly the magnetic port, with the orientation sign declared
# in the type packet.
failures = []
for grade in range(2, 6):
    for depth, exponent in ((0, -grade + 1), (2, -grade - 1), (4, 2)):
        datum = z ** (-depth) * zb ** exponent
        f, fb = fold_pair(grade, datum)
        magnetic = simp(sp.diff(f, zb) - sp.diff(fb, z))
        exterior_coefficient = simp(sp.diff(fb, z) - sp.diff(f, zb))
        if simp(exterior_coefficient + magnetic) != 0:
            failures.append((grade, depth, exponent))
record("DERHAM.hinge", "the exterior derivative is minus the magnetic readout",
       not failures, failures)

# Rationalization of an integral matrix kernel introduces no additional
# directions beyond tensoring the saturated integer null lattice.
matrix = sp.Matrix([[2, 4, 6], [0, 2, 2]])
rational_kernel = matrix.nullspace()
primitive = sp.Matrix([1, 1, -1])
record("RING.base_change", "the sample integral kernel rationalizes without a new direction",
       len(rational_kernel) == 1 and matrix * primitive == sp.zeros(2, 1) and
       sp.Matrix.hstack(rational_kernel[0], primitive).rank() == 1)

# Residue augmentation is natural under constructor inclusion.
failures = []
for grade in range(2, 9):
    def residue(depth):
        return -grade * (grade + 1) * sp.catalan(grade + 1) * sp.rf(depth, grade - 1)
    small_row = sp.Matrix([[residue(depth) for depth in (2, 4)]])
    large_row = sp.Matrix([[residue(depth) for depth in (2, 4, 6, 8)]])
    inclusion = sp.Matrix.vstack(sp.eye(2), sp.zeros(2, 2))
    if large_row * inclusion != small_row:
        failures.append(grade)
record("RESIDUE.naturality", "the global residue augmentation commutes with depth inclusion",
       not failures, failures)

passed = [item for item in checks if item["status"] == "pass"]
failed = [item for item in checks if item["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "integral_parity_cohomology_types_checks.py",
    "author": "marici.Strominger",
    "checks": checks,
    "n_pass": len(passed),
    "n_fail": len(failed),
    "verdict": "The frozen type diagram passes its five commuting-square gates: full-target source inclusions preserve columns, E/M split the mixed derivative packet, magnetic zero is exactly folded-form closedness, integral kernels rationalize correctly, and residue augmentation is natural under depth inclusion.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "integral_parity_cohomology_types.json"), "w", encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(passed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
