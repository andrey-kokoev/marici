"""Audits for the symbolic radialization and logarithmic normal-form proof."""
import json
import os
import sympy as sp

z, zb, u = sp.symbols("z zb u")
k, weight = sp.symbols("k weight", integer=True)
H = sp.Function("H")
checks = []


def simp(value):
    return sp.cancel(sp.together(sp.expand(value)))


def record(cid, statement, condition, detail=""):
    status = "pass" if bool(condition) else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement}" +
          (f" ({detail})" if detail else ""), flush=True)


# One covariant step, with u substituted only after differentiating.
Hu = H(z * zb)
left = sp.diff(zb ** k * Hu, z) + 2 * weight * zb * zb ** k * Hu / (1 + z * zb)
right = zb ** (k + 1) * (
    sp.Subs(sp.Derivative(H(u), u), u, z * zb) +
    2 * weight * H(z * zb) / (1 + z * zb))
record("RADIAL.step", "one covariant factor obeys the radialization identity",
       sp.simplify(left - right) == 0)


def one_variable_fold(grade, depth):
    value = u ** (-depth)
    for current_weight in range(2, grade + 2):
        value = simp(sp.diff(value, u) + 2 * current_weight * value / (1 + u))
    return value


# The radial form is closed and has only the declared divisor poles.
failures = []
for grade in range(2, 8):
    for depth in (0, 2, 4, 6):
        value = one_variable_fold(grade, depth)
        f = zb * value.subs(u, z * zb)
        fb = z * value.subs(u, z * zb)
        if simp(sp.diff(f, zb) - sp.diff(fb, z)) != 0:
            failures.append((grade, depth, "closed"))
        if depth > 0:
            expected = -grade * (grade + 1) * sp.catalan(grade + 1) * sp.rf(depth, grade - 1)
            residues = [simp(sp.residue(value, u, pole)) for pole in (0, -1)]
            if residues != [expected, -expected]:
                failures.append((grade, depth, residues, expected))
record("RADIAL.grid", "radial tower forms are closed and have the Catalan residue pair",
       not failures, failures)

# Hermite reduction after subtracting the universal logarithmic carrier.
failures = []
eta = 1 / u - 1 / (1 + u)
for grade in range(2, 7):
    for depth in (2, 4, 6):
        value = one_variable_fold(grade, depth)
        residue = -grade * (grade + 1) * sp.catalan(grade + 1) * sp.rf(depth, grade - 1)
        reduced = simp(value - residue * eta)
        primitive = simp(sp.integrate(reduced, u))
        if primitive.has(sp.log) or simp(sp.diff(primitive, u) - reduced) != 0:
            failures.append((grade, depth))
record("HERMITE.normal", "subtracting residue*eta leaves a rational derivative",
       not failures, failures)

# Uniform depth-zero primitive.
failures = []
for grade in range(2, 9):
    value = one_variable_fold(grade, 0)
    primitive = -sp.factorial(grade + 3) / (6 * (grade - 1) * (1 + u) ** (grade - 1))
    if simp(sp.diff(primitive, u) - value) != 0:
        failures.append(grade)
record("DEPTH0.primitive", "the depth-zero radial primitive has the uniform factorial coefficient",
       not failures, failures)

passed = [item for item in checks if item["status"] == "pass"]
failed = [item for item in checks if item["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_tower_logarithmic_normal_form_checks.py",
    "author": "marici.Strominger",
    "checks": checks,
    "n_pass": len(passed),
    "n_fail": len(failed),
    "verdict": "The covariant chain radializes tower data to a one-variable rational form. The audited forms are closed, carry the exact Catalan residue pair, reduce modulo one universal logarithmic carrier to rational derivatives, and have the stated uniform depth-zero primitive.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_tower_logarithmic_normal_form.json"), "w", encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(passed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
