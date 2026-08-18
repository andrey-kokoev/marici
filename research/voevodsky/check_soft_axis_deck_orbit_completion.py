"""Verify deck conjugacy of the two first-order soft exact lattices."""

from fractions import Fraction as Q


# Sparse polynomials in (u,a,b), truncated by u^2=0.
def add(*terms):
    out = {}
    for term in terms:
        for monomial, coefficient in term.items():
            out[monomial] = out.get(monomial, Q(0)) + coefficient
    return {m: c for m, c in out.items() if c and m[0] < 2}


def scale(poly, scalar):
    return {m: scalar * c for m, c in poly.items() if scalar * c}


def multiply_two(left, right):
    out = {}
    for (u1, a1, b1), x in left.items():
        for (u2, a2, b2), y in right.items():
            if u1 + u2 < 2:
                m = (u1 + u2, a1 + a2, b1 + b2)
                out[m] = out.get(m, Q(0)) + x * y
    return {m: c for m, c in out.items() if c}


def mul(*polynomials):
    out = one if "one" in globals() else {(0, 0, 0): Q(1)}
    for polynomial in polynomials:
        out = multiply_two(out, polynomial)
    return out


def power(poly, exponent):
    out = {(0, 0, 0): Q(1)}
    for _ in range(exponent):
        out = mul(out, poly)
    return out


def derivative(poly, coordinate):
    out = {}
    for degrees, coefficient in poly.items():
        degree = degrees[coordinate]
        if degree:
            target = list(degrees)
            target[coordinate] -= 1
            out[tuple(target)] = coefficient * degree
    return out


def rho(poly):
    return {m: (-1) ** m[1] * c for m, c in poly.items()}


one = {(0, 0, 0): Q(1)}
u = {(1, 0, 0): Q(1)}
a = {(0, 1, 0): Q(1)}
b = {(0, 0, 1): Q(1)}
L1 = add(b, one, scale(u, -1))
L2_minus = add(a, scale(u, Q(-1, 2)))
L2_plus = add(a, scale(u, Q(1, 2)))
K = add(power(a, 4), mul(u, power(a, 2)), scale(mul(u, power(a, 2), power(b, 2)), -1))

assert rho(K) == K
assert rho(L1) == L1
assert rho(L2_minus) == scale(L2_plus, -1)
assert L2_minus != L2_plus


def exact(sector, f, is_q, conjugate=False):
    sa, sb = sector
    ea, eb = 2 - sa, 2 - sb
    l2 = L2_plus if conjugate else L2_minus
    base = mul(power(L1, ea), power(l2, eb))
    if not is_q:
        result = scale(mul(derivative(f, 2), base, K), -1)
        if sa:
            result = add(result, scale(mul(f, power(L1, ea - 1), power(l2, eb), K), sa))
        return add(result, scale(mul(f, base, derivative(K, 2)), Q(3, 2)))
    result = mul(derivative(f, 1), base, K)
    if sb:
        result = add(result, scale(mul(f, power(L1, ea), power(l2, eb - 1), K), -sb))
    return add(result, scale(mul(f, base, derivative(K, 1)), Q(-3, 2)))


for sector in ((1, 1), (1, 0), (0, 1), (0, 0)):
    eb = 2 - sector[1]
    for i in range(4):
        for j in range(3):
            f = mul(power(a, i), power(b, j))
            reflected_f = rho(f)
            p_left = rho(exact(sector, f, False))
            p_right = scale(exact(sector, reflected_f, False, True), (-1) ** eb)
            q_left = rho(exact(sector, f, True))
            q_right = scale(exact(sector, reflected_f, True, True), (-1) ** (eb + 1))
            assert p_left == p_right
            assert q_left == q_right

print("rho(L2_minus) = -L2_plus")
print("one-sided lattice deck invariant: false modulo u^2")
print("minus/plus orbit-completed exact operators: conjugate in all four sectors")
print("p transport sign: (-1)^eb; q transport sign: (-1)^(eb+1)")
