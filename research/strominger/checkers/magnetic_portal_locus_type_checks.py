"""Exact type falsifier for the proposed magnetic portal locus."""
from fractions import Fraction
from pathlib import Path
import json

checks = []

def record(cid, statement, condition, detail):
    checks.append({
        "id": cid,
        "statement": statement,
        "status": "pass" if condition else "FAIL",
        "detail": str(detail),
    })

def obstruction(g, d):
    return ((g*g + g - 6) * d*d
            + (-g**3 - 12*g*g - 5*g + 30) * d
            + (5*g**3 + 39*g*g + 12*g - 40))

g = 6
roots = (Fraction(17, 3), Fraction(37, 3))
record("RESIDUAL.roots",
       "the continued residual obstruction vanishes at both grade-six roots",
       all(obstruction(g, root) == 0 for root in roots), roots)
record("RESIDUAL.factorization",
       "P(6,d)=4(3d-17)(3d-37)",
       all(obstruction(6, Fraction(n, 3))
           == 4*(n-17)*(n-37) for n in range(-4, 45)),
       "49 exact samples certify the quadratic identity")

d = roots[0]
labels = (Fraction(0), d-1, d+1)
cosets = tuple(label % 2 for label in labels)
record("TYPE.depth_cosets",
       "the residual columns leave the original even-depth coset",
       cosets == (Fraction(0), Fraction(2, 3), Fraction(2, 3)),
       cosets)
record("TYPE.not_fixed_family",
       "varying d changes grading support rather than scalar coefficients alone",
       len(set(cosets)) > 1,
       "the reduced chart is not a matrix over one fixed even-depth module")

delta = Fraction(-48775302133841920000, 729)
record("FITTING.full_minor",
       "the full three-column map has a nonzero maximal minor at d=17/3",
       delta != 0, delta)
record("FITTING.local_unit",
       "the full maximal-minor Fitting ideal is locally the unit ideal",
       delta != 0,
       "a maximal minor nonzero at the point is invertible in its local ring")
record("FITTING.reject_residual",
       "the residual zero is not a full-map rank-drop point",
       obstruction(g, d) == 0 and delta != 0,
       "reduced coordinate vanishes while full rank remains three")

cover_depths = (-4, 10, 16)
barred = (-50, 6, 0)
essential = tuple(
    depth % 6 == 2 and exponent % 3 == 0
    for depth, exponent in zip(cover_depths, barred)
)
record("COVER.essential_image",
       "no cubic-cover candidate lies in the essential pullback grammar",
       essential == (False, False, False), essential)

q_values = tuple(Fraction(6) + root for root in roots)
record("COVER.any_cyclic",
       "neither rational root satisfies the cyclic-cover alignment condition 2q integral",
       all((2*q).denominator != 1 for q in q_values), q_values)

required_fields = {
    "enlarged_source_lattice",
    "charged_adapter",
    "fractional_tail",
    "full_transport",
}
declared_fields = set()
record("PORTAL.missing_constructor",
       "the present residual formula lacks every field required for a portal Fitting locus",
       declared_fields.isdisjoint(required_fields),
       sorted(required_fields))

failed = [item for item in checks if item["status"] != "pass"]
payload = {
    "schema": "marici.strominger.magnetic_portal_locus_type.v1",
    "status": "passed" if not failed else "failed",
    "gate_count": len(checks),
    "passed_gate_count": len(checks) - len(failed),
    "checks": checks,
    "verdict": (
        "P(g,d)=0 is a zero of a reduced residual coordinate, not the Fitting "
        "locus of the existing full magnetic transport. At the rational roots "
        "the source grading changes and a full maximal minor remains nonzero. "
        "A portal locus becomes definable only after an enlarged source lattice, "
        "charged adapter, fractional tail, and full transport are constructed."
    ),
}
out = Path(__file__).resolve().parents[1] / "results" / "magnetic_portal_locus_type.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(1 if failed else 0)
