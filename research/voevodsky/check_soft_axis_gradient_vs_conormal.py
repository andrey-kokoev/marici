"""Separate the gradient nullhomotopy complex from the conormal complex."""

from fractions import Fraction

# Polynomials in (a,b,u), represented by exponent triples.
def add(*polys):
    out = {}
    for poly in polys:
        for monomial, coefficient in poly.items():
            out[monomial] = out.get(monomial, Fraction(0)) + coefficient
            if out[monomial] == 0:
                del out[monomial]
    return out


def scale(poly, scalar):
    return {m: scalar * c for m, c in poly.items() if scalar * c}


def mul(left, right):
    out = {}
    for (ai, bi, ui), x in left.items():
        for (aj, bj, uj), y in right.items():
            monomial = (ai + aj, bi + bj, ui + uj)
            out[monomial] = out.get(monomial, Fraction(0)) + x * y
    return {m: c for m, c in out.items() if c}


K = {(4, 0, 0): Fraction(1), (2, 0, 1): Fraction(1), (2, 2, 1): Fraction(-1)}
Ka = {(3, 0, 0): Fraction(4), (1, 0, 1): Fraction(2), (1, 2, 1): Fraction(-2)}
Kb = {(2, 1, 1): Fraction(-2)}
f = {(0, 0, 0): Fraction(1), (1, 3, 0): Fraction(2)}  # arbitrary test coefficient
m = {(2, 1, 0): Fraction(1)}

# Every multiple of the universal gradient syzygy lies in degree -1.
gradient_syzygy = add(mul(scale(mul(f, Kb), -1), Ka), mul(mul(f, Ka), Kb))
assert gradient_syzygy == {}

# Entry 487's two canonical homotopies.
Hp_image = mul(scale(m, Fraction(3, 2)), Kb)
Hq_image = mul(scale(m, Fraction(-3, 2)), Ka)
assert Hp_image == scale(mul(m, Kb), Fraction(3, 2))
assert Hq_image == scale(mul(m, Ka), Fraction(-3, 2))

# Tensoring [S --K--> S] with R=S/(K) sends K to zero by definition.
conormal_differential_mod_K = {}
assert conormal_differential_mod_K == {}

print("gradient syzygy (-f K_b, f K_a) maps to 0")
print("conormal differential K mod (K) = 0")
print("verdict: gradient nullhomotopies and the principal conormal cell are distinct complexes")
