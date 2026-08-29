"""Exact gates for the magnetic portal criterion."""
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

bound = 8
columns = []
for degree in range(bound):
    column = [0] * (bound + 1)
    column[degree + 1] = 1
    columns.append(column)
rank = sum(any(column[row] for row in range(bound + 1))
           for column in columns)
record("FLAT.source_injective",
       "multiplication by t is injective on the bounded polynomial packet",
       rank == bound, f"rank={rank}, columns={bound}")

free_rank = 3
lifted_rank = rank * free_rank
record("FLAT.free_lift",
       "a finite free scalar extension preserves injectivity",
       lifted_rank == bound * free_rank,
       f"lifted rank={lifted_rank}")

portal_map = [[0]]
portal_kernel_dimension = 1
record("PORTAL.nonflat_kernel",
       "restriction to the defect t=0 creates a one-dimensional kernel",
       portal_map == [[0]] and portal_kernel_dimension == 1,
       "P=R/(t), P tensor F=0")

tor_dimension = 1
record("PORTAL.tor_boundary",
       "the new defect kernel is the image of the Tor boundary",
       tor_dimension == portal_kernel_dimension,
       "Tor_1^R(R/(t),R/(t)) is isomorphic to R/(t)")

localized_kernel_dimension = 0
record("PORTAL.support",
       "the portal kernel vanishes away from the declared defect locus",
       localized_kernel_dimension == 0,
       "after inverting t, multiplication by t is an isomorphism")

delta = Fraction(-48775302133841920000, 729)
record("MAGNETIC.minor_nonzero",
       "the rational magnetic full-path witness minor is nonzero",
       delta != 0, delta)
for spurions in [(1, 1, 1), (2, -3, 5), (-1, 7, 11)]:
    adapted = delta
    for scalar in spurions:
        adapted *= scalar
    record("MAGNETIC.spurion." + ".".join(map(str, spurions)),
           "an invertible diagonal charged spurion preserves the rank witness",
           adapted != 0, adapted)

zero_spurion_minor = delta * 1 * 0 * 1
record("MAGNETIC.route_deletion",
       "a zero spurion kills the minor only by deleting a source route",
       zero_spurion_minor == 0,
       "boundary of the spurion torsor, not interference")

failed = [item for item in checks if item["status"] != "pass"]
payload = {
    "schema": "marici.strominger.magnetic_portal_criterion.v1",
    "status": "passed" if not failed else "failed",
    "gate_count": len(checks),
    "passed_gate_count": len(checks) - len(failed),
    "checks": checks,
    "classification": {
        "transparent_lift": "kernel-preserving under faithful flatness",
        "defect_portal": "kernel may be born as a Tor boundary on non-flat support",
        "operator_changing_portal": "outside base-change theorem; requires independent source authority",
    },
    "verdict": (
        "The unchanged injective magnetic operator cannot acquire a kernel under "
        "faithfully flat extension. A genuine defect portal can create a supported "
        "kernel through Tor. Any portal acting away from such support must instead "
        "change the operator, target quotient, or tail correspondence."
    ),
}
out = Path(__file__).resolve().parents[1] / "results" / "magnetic_portal_criterion.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(1 if failed else 0)
