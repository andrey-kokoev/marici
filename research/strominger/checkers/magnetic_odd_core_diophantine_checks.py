"""Dependency-free exact Diophantine certificate for the odd collision core."""
from fractions import Fraction
import json
import math
import os


def coefficients(g):
    return (
        g * g + g - 6,
        -g**3 - 12 * g**2 - 5 * g + 30,
        5 * g**3 + 39 * g**2 + 12 * g - 40,
    )


def obstruction(g, d):
    a, b, c = coefficients(g)
    return a * d * d + b * d + c


def discriminant(g):
    a, b, c = coefficients(g)
    return b * b - 4 * a * c


def square_floor(g):
    return g**3 + 2 * g**2 - 13 * g + 14


checks = []


def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


record("GRADE.two", "at g=2 the obstruction is -36(d-5)",
       all(obstruction(2, d) == -36 * (d - 5) for d in range(-2, 10)),
       "degree-one identity certified at more than two points")
record("QUAD.leading", "the quadratic coefficient is (g+3)(g-2)",
       all(coefficients(g)[0] == (g + 3) * (g - 2) for g in range(-4, 5)),
       "degree-two identity certified at more than three points")

# Each side below is a polynomial of degree at most six. Seven exact values
# certify the displayed polynomial identity by interpolation uniqueness.
lower_identity = all(
    discriminant(g) - square_floor(g)**2 == 128 * (g * g + 4 * g - 2)
    for g in range(7)
)
record("SQUARE.lower", "Delta-S^2=128(g^2+4g-2)",
       lower_identity, "seven-point exact polynomial identity")

upper_identity = all(
    (square_floor(x + 67) + 1)**2 - discriminant(x + 67)
    == 2 * x**3 + 278 * x**2 + 9780 * x + 9129
    for x in range(4)
)
record("SQUARE.upper", "(S+1)^2-Delta has a positive shifted cubic",
       upper_identity, "four-point exact cubic identity at g=67+x")

small_squares = []
for grade in range(3, 67):
    value = discriminant(grade)
    root = math.isqrt(value)
    if root * root == value:
        small_squares.append((grade, value, root))
record("SQUARE.small", "the only square Delta for 3<=g<=66 is at g=6",
       small_squares == [(6, 57600, 240)], small_squares)

a6, b6, _ = coefficients(6)
roots6 = sorted((Fraction(-b6 - 240, 2 * a6),
                 Fraction(-b6 + 240, 2 * a6)))
record("SQUARE.g6", "the g=6 roots are nonintegral",
       roots6 == [Fraction(17, 3), Fraction(37, 3)], roots6)

record("THEOREM.integer",
       "P(g,d)=0 for integral g>=2,d implies (g,d)=(2,5)",
       lower_identity and upper_identity
       and small_squares == [(6, 57600, 240)]
       and all(root.denominator != 1 for root in roots6),
       "g=2 is linear; 3..66 exact; g>=67 lies between consecutive squares")
record("THEOREM.odd", "the unique admissible odd solution is (2,5)",
       obstruction(2, 5) == 0 and 5 % 2 == 1 and 5 >= 3,
       "equivalently (g,q)=(2,7)")

failed = [item for item in checks if item["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_odd_core_diophantine_checks.py",
    "author": "marici.Strominger",
    "scope": {
        "strength": "dependency-free exact Diophantine theorem",
        "domain": "integers g>=2 and d",
        "method": "polynomial identities, discriminant trapping, finite exact interval",
    },
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": (
        "The odd-core obstruction has the unique integral zero (g,d)=(2,5). "
        "At g=6 its algebraic interference roots are 17/3 and 37/3, so scalar "
        "extension creates zeros that the integral constructor lattice excludes."
    ),
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_odd_core_diophantine.json"),
          "w", encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
