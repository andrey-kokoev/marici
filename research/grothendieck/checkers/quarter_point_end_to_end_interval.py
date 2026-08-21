"""End-to-end interval certificate for the first quarter-point localizers."""
import json
import math
from decimal import Decimal
from fractions import Fraction
from pathlib import Path

from eta_jet_decimal_interval import intervals, down, up, add, neg, sub

binary_add = add
def add(*xs):
    total = (Decimal(0), Decimal(0))
    for x in xs: total = binary_add(total, x)
    return total

def mul(x, y):
    products_lo = [down.multiply(a, b) for a in x for b in y]
    products_hi = [up.multiply(a, b) for a in x for b in y]
    return min(products_lo), max(products_hi)

def scale(q, x):
    qi = decimal_interval(q, q)
    return mul(qi, x)

def reciprocal_positive(x):
    assert x[0] > 0
    return down.divide(Decimal(1), x[1]), up.divide(Decimal(1), x[0])

def divide_positive(x, y): return mul(x, reciprocal_positive(y))
def power(x, n):
    out = (Decimal(1), Decimal(1))
    for _ in range(n): out = mul(out, x)
    return out

def decimal_interval(qlo, qhi):
    return (down.divide(Decimal(qlo.numerator), Decimal(qlo.denominator)),
            up.divide(Decimal(qhi.numerator), Decimal(qhi.denominator)))

def atan_rational_interval(q, terms):
    total = Fraction(0)
    for k in range(terms): total += (-1)**k * q**(2*k+1) / (2*k+1)
    next_total = total + (-1)**terms * q**(2*terms+1) / (2*terms+1)
    return min(total, next_total), max(total, next_total)

# Exact-rational alternating enclosures for pi and Apery's constant.
a5 = atan_rational_interval(Fraction(1, 5), 60)
a239 = atan_rational_interval(Fraction(1, 239), 20)
pi_q = (16*a5[0] - 4*a239[1], 16*a5[1] - 4*a239[0])
pi = decimal_interval(*pi_q)

z3_sum = Fraction(0)
terms = 40
for n in range(1, terms + 1):
    z3_sum += Fraction((-1)**(n-1), n**3 * math.comb(2*n, n))
z3_next = z3_sum + Fraction((-1)**terms, (terms+1)**3 * math.comb(2*(terms+1), terms+1))
zeta3 = decimal_interval(Fraction(5, 2)*min(z3_sum, z3_next),
                         Fraction(5, 2)*max(z3_sum, z3_next))

L = intervals[0]
c1 = intervals[1]
c2 = scale(Fraction(1, 2), intervals[2])
c3 = scale(Fraction(1, 6), intervals[3])
c4 = scale(Fraction(1, 24), intervals[4])

g0 = divide_positive(add(c1, scale(Fraction(1, 2), power(L, 2))), L)
g1 = neg(divide_positive(add(c2, scale(Fraction(1, 2), mul(power(L, 2), g0)),
                              scale(Fraction(-1, 6), power(L, 3))), L))
g2 = scale(Fraction(2), divide_positive(
    add(c3, scale(Fraction(-1, 2), mul(power(L, 2), g1)),
        scale(Fraction(-1, 6), mul(power(L, 3), g0)),
        scale(Fraction(1, 24), power(L, 4))), L))
g3 = scale(Fraction(-6), divide_positive(
    add(c4, scale(Fraction(1, 4), mul(power(L, 2), g2)),
        scale(Fraction(1, 6), mul(power(L, 3), g1)),
        scale(Fraction(1, 24), mul(power(L, 4), g0)),
        scale(Fraction(-1, 120), power(L, 5))), L))

one = (Decimal(1), Decimal(1))
log_pi = (down.next_minus(down.ln(pi[0])), up.next_plus(up.ln(pi[1])))
log_two_sqrt_pi = add(L, scale(Fraction(1, 2), log_pi))
l0 = sub(add(one, scale(Fraction(1, 2), g0)), log_two_sqrt_pi)
l1 = add(neg(one), scale(Fraction(-2), g1), neg(power(g0, 2)),
         scale(Fraction(1, 8), power(pi, 2)))
l2 = add(one, power(g0, 3), scale(Fraction(3), mul(g0, g1)),
         scale(Fraction(3, 2), g2), scale(Fraction(-7, 8), zeta3))
l3 = add(neg(one), scale(Fraction(-2, 3), g3),
         scale(Fraction(-2), mul(g0, g2)), scale(Fraction(-2), power(g1, 2)),
         scale(Fraction(-4), mul(power(g0, 2), g1)), neg(power(g0, 4)),
         scale(Fraction(1, 96), power(pi, 4)))
A0 = l0
A1 = add(scale(Fraction(2), l0), neg(l1))
A2 = add(l2, scale(Fraction(-3), l1), scale(Fraction(6), l0))
A3 = add(neg(l3), scale(Fraction(4), l2), scale(Fraction(-10), l1), scale(Fraction(20), l0))
lower = sub(mul(A1, A3), power(A2, 2))
u00 = add(scale(Fraction(4), A0), neg(A1))
u01 = add(scale(Fraction(4), A1), neg(A2))
u11 = add(scale(Fraction(4), A2), neg(A3))
upper = sub(mul(u00, u11), power(u01, 2))
assert lower[0] > 0 and upper[0] > 0

def strings(x): return [str(x[0]), str(x[1])]
result = {
    "stieltjes_intervals": [strings(x) for x in (g0,g1,g2,g3)],
    "completed_source_intervals": [strings(x) for x in (l0,l1,l2,l3)],
    "moment_intervals": [strings(x) for x in (A0,A1,A2,A3)],
    "lower_localizer_determinant_interval": strings(lower),
    "upper_localizer_determinant_interval": strings(upper),
    "first_localizer_signs_interval_certified": True,
    "zero_locations_used": False,
    "rh_proved": False,
}
if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "quarter-point-end-to-end-interval.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items(): print(f"{key}={value}")
