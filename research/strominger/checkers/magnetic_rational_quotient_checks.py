"""Rational-exact quotient of the classified magnetic kernel."""
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


# Positive-depth towers: exact residue character on a broad independent grid.
failures = []
for grade in range(2, 9):
    catalan = sp.catalan(grade + 1)
    for depth in range(2, 14, 2):
        datum = z ** (-depth) * zb ** (-(grade + depth - 1))
        f, _ = pair(grade, datum)
        residues = [simp(sp.residue(f, z, pole))
                    for pole in (0, -1 / zb)]
        expected = -grade * (grade + 1) * catalan * sp.rf(depth, grade - 1)
        if residues != [expected, -expected]:
            failures.append((grade, depth, residues, expected))
record("TOWER.residue", "positive-depth towers have the Catalan residue character",
       not failures, failures)

# Symbolic equality between the adjoint product and the Catalan factor.
g, a = sp.symbols("g a", integer=True, positive=True)
adjoint_product = sp.factorial(2 * g + 2) / sp.factorial(g + 2)
coefficient = sp.factorial(g + a - 2) / (
    sp.factorial(a - 1) * sp.factorial(g - 1))
catalan_explicit = sp.factorial(2 * g + 2) / (
    sp.factorial(g + 1) * sp.factorial(g + 2))
catalan_form = g * (g + 1) * catalan_explicit * sp.rf(a, g - 1)
record("TOWER.factor", "the residue adjoint product factors into the Catalan character",
       sp.combsimp(adjoint_product * coefficient - catalan_form) == 0)

# Ordinary rational cohomology forgets depth labels.  Every combination whose
# common residue coordinate cancels must become rational-exact.
failures = []
for grade in range(2, 7):
    reference = 2
    c_ref = grade * (grade + 1) * sp.catalan(grade + 1) * sp.rf(reference, grade - 1)
    d_ref = z ** (-reference) * zb ** (-(grade + reference - 1))
    for depth in (4, 6):
        c_depth = grade * (grade + 1) * sp.catalan(grade + 1) * sp.rf(depth, grade - 1)
        datum = c_ref * z ** (-depth) * zb ** (-(grade + depth - 1)) - c_depth * d_ref
        f, fb = pair(grade, datum)
        if simp(sp.residue(f, z, 0)) != 0 or simp(sp.residue(f, z, -1 / zb)) != 0:
            failures.append((grade, depth, "residue"))
            continue
        phi = simp(sp.integrate(f, z))
        if simp(sp.diff(phi, z) - f) != 0 or simp(sp.diff(phi, zb) - fb) != 0:
            failures.append((grade, depth, "primitive"))
record("TOWER.cancellation", "cross-depth zero-residue combinations are rational-exact",
       not failures, failures)

# Divisor-level normal form: all positive towers are multiples of one common
# logarithmic class eta=dlog(u/(1+u)), modulo rational exact forms.
eta_z = simp(1 / z - zb / (1 + u))
eta_zb = simp(1 / zb - z / (1 + u))
failures = []
for grade in range(2, 6):
    for depth in (2, 4, 6):
        datum = z ** (-depth) * zb ** (-(grade + depth - 1))
        f, fb = pair(grade, datum)
        residue = -grade * (grade + 1) * sp.catalan(grade + 1) * sp.rf(depth, grade - 1)
        reduced_f = simp(f - residue * eta_z)
        reduced_fb = simp(fb - residue * eta_zb)
        phi = simp(sp.integrate(reduced_f, z))
        if (simp(sp.diff(phi, z) - reduced_f) != 0 or
                simp(sp.diff(phi, zb) - reduced_fb) != 0):
            failures.append((grade, depth))
record("TOWER.normal_form", "every audited tower is residue*eta modulo a rational exact form",
       not failures, failures)

# The two exceptional magnetic circuits are rational-exact.
e1 = 1 - zb ** -2
f1, fb1 = pair(2, e1)
phi1 = -20 * (z + zb) / (1 + u)
record("EXACT.e1", "the two-term exceptional circuit is rational-exact",
       simp(sp.diff(phi1, z) - f1) == 0 and
       simp(sp.diff(phi1, zb) - fb1) == 0)

e2 = zb ** -8 - 3 * z ** -4 * zb ** 2 + 2 * z ** -6
f2, fb2 = pair(2, e2)
phi2 = (-4 * (-2 * zb ** 8 * z + 3 * zb ** 7 + 5 * z ** 7) /
        (zb ** 7 * z ** 7 * (1 + u)) + 8 * zb ** -7)
record("EXACT.e2", "the three-term exceptional circuit is rational-exact",
       simp(sp.diff(phi2, z) - f2) == 0 and
       simp(sp.diff(phi2, zb) - fb2) == 0, sp.factor(phi2))

# The depth-zero tower potentials have one uniform coefficient.
failures = []
for grade in range(2, 9):
    datum = zb ** (-(grade - 1))
    f, fb = pair(grade, datum)
    coefficient = sp.factorial(grade + 3) / (6 * (grade - 1))
    phi = -coefficient / (1 + u) ** (grade - 1)
    if simp(sp.diff(phi, z) - f) != 0 or simp(sp.diff(phi, zb) - fb) != 0:
        failures.append((grade, coefficient))
record("EXACT.depth0", "every audited depth-zero tower has the uniform rational primitive",
       not failures, failures)

passed = [item for item in checks if item["status"] == "pass"]
failed = [item for item in checks if item["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_rational_quotient_checks.py",
    "author": "marici.Strominger",
    "checks": checks,
    "n_pass": len(passed),
    "n_fail": len(failed),
    "verdict": "Both grade-two exceptional circuits and every depth-zero tower are rational-exact. Every positive-depth tower has nonzero opposite residues with magnitude g(g+1)Catalan(g+1) rising(a,g-1), but all occupy the same unlabelled residue line. Cross-depth combinations with zero total residue are rational-exact. Hence the ordinary rational de Rham quotient has dimension one when any positive depth is visible, and zero otherwise.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_rational_quotient.json"), "w", encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(passed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
