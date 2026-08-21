"""Exact tail bound needed for eta derivatives through order six."""
import json
import math
from fractions import Fraction
from pathlib import Path

N, M, J = 10_000, 15, 6

def qcoeff(m):
    q = [Fraction(1)]
    for k in range(1, m+1):
        new = q + [Fraction(0)]
        for r, value in enumerate(q): new[r+1] += value/k
        q = new
    return q

def polynomial(m, j, y):
    q = qcoeff(m)
    return sum(Fraction(math.comb(j,r))*(-1)**r*math.factorial(r)*q[r]*y**(j-r)
               for r in range(j+1))

signs = [[polynomial(m,j,Fraction(9)) for j in range(J+1)] for m in (M,M+1)]
assert all(x > 0 for row in signs for x in row)
bounds = [Fraction(math.factorial(M))*polynomial(M,j,Fraction(10))
          /(Fraction(2)**M * Fraction(N)**(M+1)) for j in range(J+1)]
assert max(bounds) < Fraction(2, 10**52)
result = {
    "tail_start": N,
    "euler_transforms": M,
    "maximum_eta_derivative_order": J,
    "sign_polynomials_positive_exactly": True,
    "remainder_bounds": [f"{float(x):.7e}" for x in bounds],
    "all_remainders_below_2e-52": True,
}
if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "eta-order-six-euler-tail-bound.json"
    output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    for key,value in result.items(): print(f"{key}={value}")
