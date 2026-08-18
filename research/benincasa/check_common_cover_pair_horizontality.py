"""Compare the pair-symbol weight with the horizontal map on the common cover."""

from fractions import Fraction

# Exponent vector in (ell1, ell2, ell3, ell4).
r = (-1, 1, 1, -1)  # Delta_minus / Delta_plus.
horizontal_weight = tuple(Fraction(exponent, 2) for exponent in r)
symbol_weight = tuple(Fraction(exponent, 1) for exponent in r)
mismatch = tuple(symbol - horizontal for symbol, horizontal in zip(symbol_weight, horizontal_weight))

assert horizontal_weight == (Fraction(-1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(-1, 2))
assert symbol_weight == (-1, 1, 1, -1)
assert mismatch == horizontal_weight
assert any(exponent.denominator == 2 for exponent in horizontal_weight)

print(f"R_EXPONENTS={r}")
print(f"HORIZONTAL_MAP_EXPONENTS={horizontal_weight}")
print("HORIZONTAL_MAP=rho_where_rho^2=R")
print(f"WEIGHTED_SYMBOL_MAP_EXPONENTS={symbol_weight}")
print("WEIGHTED_SYMBOL_MAP=R=rho^2")
print(f"HORIZONTALITY_MISMATCH_EXPONENTS={mismatch}")
print("RATIONAL_BASE_HORIZONTAL_MAP=false")
print("COMMON_COVER_HORIZONTAL_MAP_DECK_CHARACTER=odd")
print("WEIGHTED_SYMBOL_MAP_DECK_CHARACTER=even")
