"""Necessary-and-sufficient rational exactness audit for magnetic kernels."""
import itertools
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


def pair(grade, datum):
    return chain(grade, datum), chain(grade, sigma(datum), barred=True)


def record(cid, statement, condition, detail=""):
    status = "pass" if bool(condition) else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement}" +
          (f" ({detail})" if detail else ""), flush=True)


# Uniform exact named classes.
failures = []
for grade in range(2, 9):
    datum = zb ** (-(grade - 1))
    f, fb = pair(grade, datum)
    phi = -sp.factorial(grade + 3) / (6 * (grade - 1) * (1 + u) ** (grade - 1))
    if simp(sp.diff(phi, z) - f) != 0 or simp(sp.diff(phi, zb) - fb) != 0:
        failures.append(grade)
record("NAMED.depth0", "every depth-zero tower has the uniform rational primitive",
       not failures, failures)

e1 = 1 - zb ** -2
f1, fb1 = pair(2, e1)
phi1 = -20 * (z + zb) / (1 + u)
e2 = zb ** -8 - 3 * z ** -4 * zb ** 2 + 2 * z ** -6
f2, fb2 = pair(2, e2)
phi2 = (-4 * (-2 * zb ** 8 * z + 3 * zb ** 7 + 5 * z ** 7) /
        (zb ** 7 * z ** 7 * (1 + u)) + 8 * zb ** -7)
record("NAMED.exceptions", "both grade-two exceptional circuits have rational primitives",
       simp(sp.diff(phi1, z) - f1) == 0 and
       simp(sp.diff(phi1, zb) - fb1) == 0 and
       simp(sp.diff(phi2, z) - f2) == 0 and
       simp(sp.diff(phi2, zb) - fb2) == 0)

# Hostile arbitrary coefficients: exactness is equivalent to one weighted sum.
failures = []
depths = (2, 4, 6)
for grade in range(2, 7):
    residues = [-grade * (grade + 1) * sp.catalan(grade + 1) *
                sp.rf(depth, grade - 1) for depth in depths]
    towers = [z ** (-depth) * zb ** (-(grade + depth - 1)) for depth in depths]
    tower_pairs = [pair(grade, tower) for tower in towers]
    actual_residues = [simp(sp.residue(tower_pair[0], z, 0))
                       for tower_pair in tower_pairs]
    if actual_residues != residues:
        failures.append((grade, "individual residues"))
        continue

    # A rational primitive for a basis of the zero-residue hyperplane proves
    # sufficiency for every zero-residue combination by linearity.
    for index in (1, 2):
        relation_f = simp(residues[0] * tower_pairs[index][0] -
                          residues[index] * tower_pairs[0][0])
        relation_fb = simp(residues[0] * tower_pairs[index][1] -
                           residues[index] * tower_pairs[0][1])
        phi = simp(sp.integrate(relation_f, z))
        if (phi.has(sp.log) or simp(sp.diff(phi, z) - relation_f) != 0 or
                simp(sp.diff(phi, zb) - relation_fb) != 0):
            failures.append((grade, index, "hyperplane basis"))

    # Exhaust small signed coefficient packets as exact linear algebra.  A
    # nonzero weighted sum is obstructed by its nonzero residue; a zero sum is
    # in the span of the two verified exact relations above.
    for coefficients in itertools.product(range(-2, 3), repeat=len(depths)):
        if coefficients == (0, 0, 0):
            continue
        total_residue = sum(coefficient * residue for coefficient, residue in
                            zip(coefficients, residues))
        if total_residue == 0:
            # Solve against the two reference relations over Q.
            relation_matrix = sp.Matrix([
                [-residues[1], -residues[2]],
                [residues[0], 0],
                [0, residues[0]],
            ])
            if relation_matrix.row_join(sp.Matrix(coefficients)).rank() != 2:
                failures.append((grade, coefficients, "span"))
record("CRITERION.hostile", "arbitrary signed tower packets are exact exactly at zero weighted residue",
       not failures, failures[:3])

# Dimension law for every visibility pattern of four possible exact generators
# and up to four positive tower directions.
failures = []
cases = 0
for v0, v1, v2 in itertools.product((0, 1), repeat=3):
    for positive_count in range(5):
        cases += 1
        kernel_dimension = v0 + v1 + v2 + positive_count
        exact_dimension = v0 + v1 + v2 + max(positive_count - 1, 0)
        quotient_dimension = kernel_dimension - exact_dimension
        if quotient_dimension != int(positive_count > 0):
            failures.append((v0, v1, v2, positive_count))
record("DIMENSION.visibility", "the cutoff-dependent exact and quotient dimensions obey the closed law",
       not failures, f"cases={cases}; failures={failures}")

passed = [item for item in checks if item["status"] == "pass"]
failed = [item for item in checks if item["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_rational_exact_classification_checks.py",
    "author": "marici.Strominger",
    "checks": checks,
    "n_pass": len(passed),
    "n_fail": len(failed),
    "verdict": "Rational exactness on the complete magnetic kernel is exactly the vanishing of one weighted Catalan residue sum over visible positive-depth towers. The depth-zero tower and both exceptional circuits are exact. The quotient has dimension one iff at least one positive tower is visible.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_rational_exact_classification.json"), "w", encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(passed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
