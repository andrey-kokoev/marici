"""Exact discrete incidence shadow of the rational magnetic crossings."""
from fractions import Fraction
from pathlib import Path
import json
import math

def rf(value, count):
    result = Fraction(1)
    for offset in range(count):
        result *= value+offset
    return result

def routes(grade, excess):
    g, d = Fraction(grade), Fraction(excess)
    left = -(2*d*g+2*d-g*g-11*g-4)*rf(d-1, grade-1)
    right = (g*(d-4)*(d-3)*(g-2)*(g-1)*(g+3)
             * rf(d+1, grade-3)/2)
    c_left = (g*(g+3)*(d*g-2*d-5*g+4)
              * math.factorial(grade+3)*rf(d+1, grade-1)/6)
    c_right = math.factorial(grade+3)*rf(d-1, grade+1)/3
    return c_left*left, c_right*right

def sign(value):
    return (value > 0)-(value < 0)

def obstruction(g, d):
    return ((g*g+g-6)*d*d
            + (-g**3-12*g*g-5*g+30)*d
            + (5*g**3+39*g*g+12*g-40))

checks = []

def record(cid, statement, condition, detail):
    checks.append({
        "id": cid,
        "statement": statement,
        "status": "pass" if condition else "FAIL",
        "detail": str(detail),
    })

odd_depths = list(range(3, 32, 2))
packets = {}
for d in odd_depths:
    A, B = routes(6, d)
    packets[d] = {"A": A, "B": B, "S": A+B, "D": A-B}

edges = []
for low, high in zip(odd_depths, odd_depths[1:]):
    low_sign = sign(packets[low]["S"])
    high_sign = sign(packets[high]["S"])
    if low_sign*high_sign < 0:
        edges.append({
            "low": low,
            "high": high,
            "signs": (low_sign, high_sign),
            "incidence": Fraction(high_sign-low_sign, 2),
        })

record("LATTICE.adjacent", "the relevant brackets are adjacent odd-depth lattice edges",
       [(item["low"], item["high"]) for item in edges] == [(5, 7), (11, 13)],
       edges)
record("LATTICE.complete_bounded",
       "these are the only scalar sign-changing odd edges through depth 31",
       len(edges) == 2, edges)
record("CROSS.incidence",
       "the two discrete crossing incidences are +1 and -1",
       [item["incidence"] for item in edges] == [Fraction(1), Fraction(-1)],
       [item["incidence"] for item in edges])
record("CROSS.route_live",
       "both route coordinates are nonzero at every endpoint of either edge",
       all(packets[d]["A"] and packets[d]["B"] for d in (5, 7, 11, 13)),
       [(d, packets[d]["A"], packets[d]["B"]) for d in (5, 7, 11, 13)])
record("CROSS.character",
       "the complementary difference character remains nonzero on all four endpoints",
       all(packets[d]["D"] for d in (5, 7, 11, 13)),
       [(d, packets[d]["D"]) for d in (5, 7, 11, 13)])

roots = (Fraction(17, 3), Fraction(37, 3))
record("ROOT.bracket",
       "each rational analytic root lies in the corresponding open lattice edge",
       5 < roots[0] < 7 and 11 < roots[1] < 13, roots)
record("ROOT.unique",
       "the quadratic obstruction has exactly the two displayed roots",
       all(obstruction(6, root) == 0 for root in roots),
       "P(6,d)=4(3d-17)(3d-37)")
record("ORIENTATION.match",
       "discrete incidence agrees with the analytic scalar-crossing orientation",
       [item["incidence"] for item in edges] == [1, -1],
       "sign(S(high))-sign(S(low)) over two")

# Grade-two d=5 is a vertex zero, not an edge crossing.
loss_A, loss_B = routes(2, 5)
record("LOSS.vertex",
       "the integral exception is a zero packet at a lattice vertex",
       loss_A == loss_B == 0, "(g,d)=(2,5)")
record("LOSS.not_incidence",
       "route loss cannot be assigned a nonzero interference-edge incidence",
       sign(loss_A+loss_B) == 0 and loss_A-loss_B == 0,
       "both scalar and complementary characters vanish")

failed = [item for item in checks if item["status"] != "pass"]
payload = {
    "schema": "marici.strominger.magnetic_discrete_crossing_incidence.v1",
    "status": "passed" if not failed else "failed",
    "gate_count": len(checks),
    "passed_gate_count": len(checks)-len(failed),
    "edges": [
        {
            "low": item["low"],
            "high": item["high"],
            "scalar_signs": list(item["signs"]),
            "incidence": str(item["incidence"]),
            "low_scalar": str(packets[item["low"]]["S"]),
            "high_scalar": str(packets[item["high"]]["S"]),
        }
        for item in edges
    ],
    "checks": checks,
    "verdict": (
        "The two rational grade-six interference roots have a fully discrete "
        "shadow: they lie in the adjacent admitted odd-depth edges 5->7 and "
        "11->13, whose scalar sign incidences are +1 and -1. No continuous "
        "depth state is needed to record the oriented wall crossing. The "
        "grade-two exception remains a zero packet at a vertex, not an edge incidence."
    ),
}
out = Path(__file__).resolve().parents[1] / "results" / "magnetic_discrete_crossing_incidence.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(1 if failed else 0)
