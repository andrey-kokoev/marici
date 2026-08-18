"""Compute the generic soft Bockstein in the specialized 3-gradient Koszul complex."""

from fractions import Fraction as Q

# Work over Q(c)[a]/(a^4), with c=1-b^2 treated as a nonzero scalar.
# A polynomial is its four coefficients in 1,a,a^2,a^3.
def mon(degree, coefficient=Q(1)):
    out = [Q(0)] * 4
    if degree < 4:
        out[degree] = coefficient
    return out


def add(x, y):
    return [a + b for a, b in zip(x, y)]


def scale(x, q):
    return [q * a for a in x]


def multiply(x, y):
    out = [Q(0)] * 4
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            if i + j < 4:
                out[i + j] += a * b
    return out


zero = mon(4)
g_a, g_b, g_u = mon(3, Q(4)), zero, mon(2)  # absorb generic c into e_u

# Divide a^3*(a/4,0,u/2) by u, using a^4=-u*a^2*c before u=0.
bockstein = (mon(2, Q(-1, 4)), zero, mon(3, Q(1, 2)))

def d1(vector):
    return add(add(multiply(vector[0], g_a), multiply(vector[1], g_b)), multiply(vector[2], g_u))


assert d1(bockstein) == zero

# d2((1/4)e_a wedge e_u)=(-a^2/4,0,a^3).
boundary = (mon(2, Q(-1, 4)), zero, mon(3))
normal_form = tuple(add(x, scale(y, -1)) for x, y in zip(bockstein, boundary))
assert normal_form == (zero, zero, mon(3, Q(-1, 2)))

# A boundary with vanishing e_a component needs its e_a-e_u coefficient to
# annihilate a^2, hence to lie in (a^2); its e_u component 4*a^3*h is then 0.
# Therefore a^3 e_u is not a boundary.
assert multiply(mon(2), g_u) == zero
assert multiply(mon(2), g_a) == zero

print("Bockstein = (-a^2/4, 0, a^3/2)")
print("mod Koszul boundaries = -(a^3/2) e_u")
print("a^3 e_u is nonzero in H1")
print("verdict: derived u-specialization restores exactly the lost conormal socle")
