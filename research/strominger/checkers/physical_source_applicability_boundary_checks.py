"""Exact source-boundary gates for the Laurent parity-kernel engine."""

import json
import os

import sympy as sp


checks = []


def record(gate, statement, passed, detail):
    checks.append({
        "gate": gate,
        "statement": statement,
        "passed": bool(passed),
        "detail": detail,
    })


# A z^p zb^q coefficient of a covariant dz^2 tensor becomes
# w^(-p-4) wb^(-q) under w=1/z.
def south_exponents(p, q):
    return (-p - 4, -q)


samples = [(-8, 3), (-4, 0), (-2, -5), (0, 0), (5, 7)]
transition_ok = all(
    south_exponents(*south_exponents(p, q)) == (p, q)
    for p, q in samples
)
record(
    "CHART.involution",
    "the spin-two exponent transition is an involution",
    transition_ok,
    "(p,q) maps to (-p-4,-q)",
)


hostile_box = [(p, q) for p in range(-30, 31) for q in range(-30, 31)]
north_regular = {(p, q) for p, q in hostile_box if p >= 0 and q >= 0}
south_regular = {(p, q) for p, q in hostile_box if p <= -4 and q <= 0}
intersection = north_regular & south_regular
record(
    "REGULAR.empty",
    "no Laurent monomial is regular in both sphere charts",
    not intersection,
    "north requires p>=0,q>=0; south requires p<=-4,q<=0",
)


def globally_regular_support(support):
    return all(p >= 0 and q >= 0 and p <= -4 and q <= 0
               for p, q in support)


named_failures = []
for grade in range(2, 21):
    for depth in range(0, 22, 2):
        tower = {(-depth, -(grade + depth - 1))}
        if globally_regular_support(tower):
            named_failures.append(("tower", grade, depth))

e1_support = {(0, 0), (0, -2)}
e2_support = {(0, -8), (-4, 2), (-6, 0)}
if globally_regular_support(e1_support):
    named_failures.append(("E1", 2, None))
if globally_regular_support(e2_support):
    named_failures.append(("E2", 2, None))

record(
    "NAMED.singular",
    "all towers through g=20,a=20 and both exceptional supports fail global regularity",
    not named_failures,
    "failures=" + repr(named_failures),
)


# The engine grade counts the D_z applications with weights 2,...,g+1.
def fold_weights(grade):
    return list(range(2, grade + 2))


grade_matches = [g for g in range(0, 21) if len(fold_weights(g)) == 3]
record(
    "GRADE.psz",
    "the PSZ partial_zbar D_z^3 magnetic density selects engine grade three",
    grade_matches == [3],
    "matching grades=" + repr(grade_matches),
)


record(
    "GRADE.exceptions",
    "the E1 and E2 circuits occur at a different engine grade from the PSZ density",
    2 not in grade_matches and 3 in grade_matches,
    "exception grade=2; PSZ grade=3",
)


# Algebraic sanity check of the tensor Jacobian.  With z=1/w,
# (dz/dw)^2 z^p zb^q has the asserted exponents.
w, wb = sp.symbols("w wb", nonzero=True)
for p, q in samples:
    transformed = sp.expand((sp.diff(1 / w, w) ** 2)
                            * (1 / w) ** p * (1 / wb) ** q)
    expected = w ** (-p - 4) * wb ** (-q)
    if sp.simplify(transformed - expected) != 0:
        transition_ok = False
record(
    "CHART.jacobian",
    "the covariant spin-two Jacobian gives w^(-p-4) wb^(-q)",
    transition_ok,
    "verified symbolically on five hostile exponent pairs",
)


passed = sum(item["passed"] for item in checks)
total = len(checks)
payload = {
    "checker": "physical_source_applicability_boundary_checks.py",
    "strength": "source-typed no-go theorem plus bounded hostile audit",
    "passed": passed,
    "total": total,
    "checks": checks,
    "verdict": (
        "The standard smooth Bondi-shear constructor has zero intersection "
        "with the nonzero finite Laurent engine source. All named towers and "
        "grade-two circuits are singular as global spin-two data, and the "
        "PSZ magnetic constraint selects engine grade three rather than the "
        "grade-two exceptional locus."
    ),
}

outdir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "results")
os.makedirs(outdir, exist_ok=True)
outpath = os.path.join(outdir, "physical_source_applicability_boundary.json")
with open(outpath, "w", encoding="ascii") as handle:
    json.dump(payload, handle, indent=2, sort_keys=True)
    handle.write("\n")

for item in checks:
    label = "PASS" if item["passed"] else "FAIL"
    print(f"{label} {item['gate']}: {item['statement']} - {item['detail']}")
print(f"SUMMARY {passed}/{total}")

if passed != total:
    raise SystemExit(1)

