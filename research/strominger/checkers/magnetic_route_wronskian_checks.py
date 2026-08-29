"""Exact route-Wronskian classification of the rational magnetic crossings."""
from fractions import Fraction
from pathlib import Path
import json
import math

class Dual:
    def __init__(self, value, derivative=0):
        self.value = Fraction(value)
        self.derivative = Fraction(derivative)

    def _dual(self, other):
        return other if isinstance(other, Dual) else Dual(other)

    def __add__(self, other):
        other = self._dual(other)
        return Dual(self.value+other.value, self.derivative+other.derivative)

    __radd__ = __add__

    def __neg__(self):
        return Dual(-self.value, -self.derivative)

    def __sub__(self, other):
        return self + (-self._dual(other))

    def __rsub__(self, other):
        return self._dual(other) - self

    def __mul__(self, other):
        other = self._dual(other)
        return Dual(
            self.value*other.value,
            self.derivative*other.value+self.value*other.derivative,
        )

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self._dual(other)
        return Dual(
            self.value/other.value,
            (self.derivative*other.value-self.value*other.derivative)
            / (other.value*other.value),
        )

    def __rtruediv__(self, other):
        return self._dual(other) / self

def rf(value, count):
    result = Dual(1) if isinstance(value, Dual) else Fraction(1)
    for offset in range(count):
        result *= value+offset
    return result

def route_duals(grade, excess):
    g = Fraction(grade)
    d = Dual(excess, 1)
    left = -(2*d*g+2*d-g*g-11*g-4)*rf(d-1, grade-1)
    right = (g*(d-4)*(d-3)*(g-2)*(g-1)*(g+3)
             * rf(d+1, grade-3)/2)
    c_left = (g*(g+3)*(d*g-2*d-5*g+4)
              * math.factorial(grade+3)*rf(d+1, grade-1)/6)
    c_right = math.factorial(grade+3)*rf(d-1, grade+1)/3
    return c_left*left, c_right*right

def obstruction(g, d):
    return ((g*g+g-6)*d*d
            + (-g**3-12*g*g-5*g+30)*d
            + (5*g**3+39*g*g+12*g-40))

def obstruction_derivative(g, d):
    return (2*(g*g+g-6)*d
            + (-g**3-12*g*g-5*g+30))

checks = []

def record(cid, statement, condition, detail):
    checks.append({
        "id": cid,
        "statement": statement,
        "status": "pass" if condition else "FAIL",
        "detail": str(detail),
    })

roots = (Fraction(17, 3), Fraction(37, 3))
records = []
for root in roots:
    A, B = route_duals(6, root)
    scalar = A+B
    difference = A-B
    wronskian = A.value*B.derivative-B.value*A.derivative
    records.append({
        "d": root,
        "A": A.value,
        "B": B.value,
        "A_prime": A.derivative,
        "B_prime": B.derivative,
        "scalar": scalar.value,
        "scalar_prime": scalar.derivative,
        "difference": difference.value,
        "wronskian": wronskian,
        "P_prime": obstruction_derivative(6, root),
    })

record("ROOT.exact", "both grade-six points are exact roots of the residual obstruction",
       all(obstruction(6, item["d"]) == 0 for item in records), roots)
record("ROUTE.live", "both routes remain nonzero at both scalar-dark points",
       all(item["A"] and item["B"] for item in records),
       [(item["A"], item["B"]) for item in records])
record("ROUTE.antidiagonal", "the scalar-dark packet is nonzero anti-diagonal interference",
       all(item["scalar"] == 0 and item["B"] == -item["A"] for item in records),
       [(item["A"], item["B"]) for item in records])
record("CROSS.simple", "the scalar augmentation crosses transversely at both roots",
       all(item["scalar_prime"] != 0 for item in records),
       [item["scalar_prime"] for item in records])
record("CROSS.opposite", "the two rational fibers have opposite scalar crossing orientation",
       records[0]["scalar_prime"]*records[1]["scalar_prime"] < 0,
       [item["scalar_prime"] for item in records])
record("WRONSKIAN.nonzero", "the route Wronskian is nonzero at both crossings",
       all(item["wronskian"] != 0 for item in records),
       [item["wronskian"] for item in records])
record("WRONSKIAN.identity",
       "on the anti-diagonal, the Wronskian equals A times the scalar derivative",
       all(item["wronskian"] == item["A"]*item["scalar_prime"]
           for item in records),
       "A*B'-B*A'=A*(A'+B') when B=-A")
record("CHARACTER.visible", "the complementary difference character is nonzero at each crossing",
       all(item["difference"] != 0 for item in records),
       [item["difference"] for item in records])
record("LOSS.separate", "the integral grade-two exception has zero routes rather than a Wronskian crossing",
       all(route.value == 0 for route in route_duals(2, Fraction(5))),
       "A=B=0 at (g,d)=(2,5)")
record("P.orientation", "the residual polynomial also has simple oppositely oriented roots",
       [item["P_prime"] for item in records] == [Fraction(-240), Fraction(240)],
       [item["P_prime"] for item in records])

failed = [item for item in checks if item["status"] != "pass"]
payload = {
    "schema": "marici.strominger.magnetic_route_wronskian.v1",
    "status": "passed" if not failed else "failed",
    "gate_count": len(checks),
    "passed_gate_count": len(checks)-len(failed),
    "records": [
        {key: str(value) for key, value in item.items()}
        for item in records
    ],
    "checks": checks,
    "verdict": (
        "The two grade-six rational scalar zeros are simple nonzero-interference "
        "crossings with nonvanishing route Wronskian and opposite orientations. "
        "The complementary difference character detects both. This is an invariant "
        "of the analytically continued local route packet, not yet a source-authorized "
        "fractional magnetic state or full-kernel claim."
    ),
}
out = Path(__file__).resolve().parents[1] / "results" / "magnetic_route_wronskian.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(1 if failed else 0)
