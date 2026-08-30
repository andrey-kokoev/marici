"""Exact factorization of the reachable-boundary initial variation."""

import sympy as sp


a, b = sp.symbols("a b", nonnegative=True)
p = 2 * a / (1 + a**2)
q = 2 * b / (1 + b**2)
t = (a - b) / (1 - a * b)
r = t * (a + b) / (1 + a * b)

slope_sum = p + q
slope_product = p * q
n_t = (
    4 * t**3
    + 2 * t * slope_product
    - 2 * t * (2 + slope_product) * r**2
    - slope_sum * r * (1 - r**2)
)
n_r = (
    -t * slope_sum
    + 2 * (1 - 2 * t**2 - t**2 * slope_product) * r
    + 3 * t * slope_sum * r**2
)

# G=2 dF/dL along T'=(1-T^2)/2, R'=p(1-R^2)/2.
g = sp.factor((1 - t**2) * n_t + p * (1 - r**2) * n_r)
numerator, denominator = sp.fraction(sp.cancel(g))
factorization = sp.factor(numerator)

print(f"initial_G_numerator_factor={factorization}")
print(f"initial_G_denominator_factor={sp.factor(denominator)}")
print(f"initial_variation_positive_domain=0<=b<a<1")

z0 = sp.cancel(r / t)
x0 = sp.cancel(t * t)
d0 = sp.factor(
    p - z0 + x0 * (-2 * p**2 * z0 + 3 * p * z0**2 - 2 * p + z0)
)
print(f"initial_D_factor={d0}")

# For p<1, R approaches one like exp(-pL), more slowly than T approaches
# one like exp(-L).  The leading large-L orientation is therefore obtained
# by setting T=1 and expanding R=1-epsilon.
epsilon = sp.symbols("epsilon", positive=True)
tt, rr = sp.symbols("T R")
nt = (
    4 * tt**3 + 2 * tt * p * q
    - 2 * tt * (2 + p * q) * rr**2
    - (p + q) * rr * (1 - rr**2)
)
nr = (
    -tt * (p + q)
    + 2 * (1 - 2 * tt**2 - tt**2 * p * q) * rr
    + 3 * tt * (p + q) * rr**2
)
gg = (1 - tt**2) * nt + p * (1 - rr**2) * nr
tail = sp.Poly(sp.expand(gg.subs({tt: 1, rr: 1 - epsilon})), epsilon)
valuation = min(power[0] for power, coefficient in tail.terms() if coefficient != 0)
leading = sp.factor(tail.coeff_monomial(epsilon**valuation))
print(f"large_holding_R_defect_valuation={valuation}")
print(f"large_holding_leading_factor={leading}")
