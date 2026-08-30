"""Scout the exact Schur bound for Nima's level-44 prime-two kernel."""

import math


LENGTH = math.log(2.0)
D44 = 2.633783493671972324594303424623756044375


def kernel(t: float) -> float:
    return math.exp(t / 2.0) - sum(
        math.exp(-(2 * n + 0.5) * t) for n in range(1, 44)
    )


def primitive(t: float) -> float:
    return 2.0 * (math.exp(t / 2.0) - 1.0) - sum(
        (1.0 - math.exp(-(2 * n + 0.5) * t)) / (2 * n + 0.5)
        for n in range(1, 44)
    )


lo, hi = 0.0, LENGTH
for _ in range(100):
    mid = (lo + hi) / 2.0
    if kernel(mid) < 0.0:
        lo = mid
    else:
        hi = mid
T_STAR = (lo + hi) / 2.0
I_STAR = primitive(T_STAR)


def absolute_primitive(t: float) -> float:
    if t <= T_STAR:
        return -primitive(t)
    return primitive(t) - 2.0 * I_STAR


def row_absolute_integral(x: float) -> float:
    return absolute_primitive(x) + absolute_primitive(LENGTH - x)


grid = [LENGTH * i / 100_000 for i in range(100_001)]
values = [row_absolute_integral(x) for x in grid]
index = max(range(len(values)), key=values.__getitem__)

print(f"length={LENGTH:.17g}")
print(f"t_star={T_STAR:.17g}")
print(f"maximizer_grid={grid[index]:.17g}")
print(f"schur_sup_grid={values[index]:.17g}")
print(f"d44={D44:.17g}")
print(f"schur_reserve_grid={D44-values[index]:.17g}")
print(f"endpoint={row_absolute_integral(0.0):.17g}")
print(f"center={row_absolute_integral(LENGTH/2.0):.17g}")

# Trace/HS scout for the robust second-eigenvalue gate.  If B is proved
# positive, lambda_1 >= the constant Rayleigh quotient and therefore
# lambda_2^2 <= ||B||_HS^2-lambda_1^2.
count = 1_000_000
step = LENGTH / count
k_at_length = kernel(LENGTH)
integral_b = 0.0
integral_b_squared = 0.0
for i in range(count):
    t = (i + 0.5) * step
    b = k_at_length - kernel(t)
    weight = LENGTH - t
    integral_b += weight * b
    integral_b_squared += weight * b * b
integral_b *= step
integral_b_squared *= step
constant_rayleigh = 2.0 * integral_b / LENGTH
hs_squared = 2.0 * integral_b_squared
lambda2_from_hs = math.sqrt(max(0.0, hs_squared - constant_rayleigh**2))
print(f"B_trace={LENGTH*(k_at_length-kernel(0.0)):.17g}")
print(f"B_constant_rayleigh={constant_rayleigh:.17g}")
print(f"B_hs_squared={hs_squared:.17g}")
print(f"lambda2_hs_bound={lambda2_from_hs:.17g}")
print(f"lambda2_hs_reserve={D44-lambda2_from_hs:.17g}")

# Odd reflection sector on [0,L/2].  Its positive folded kernel is
# B(|x-y|)-B(x+y), and its row integral has an exact primitive.
half = LENGTH / 2.0


def primitive_b(s: float) -> float:
    return s * k_at_length - primitive(s)


def odd_row_integral(x: float) -> float:
    return (
        primitive_b(x)
        + primitive_b(half - x)
        - primitive_b(x + half)
        + primitive_b(x)
    )


odd_grid = [half * i / 100_000 for i in range(100_001)]
odd_rows = [odd_row_integral(x) for x in odd_grid]
odd_index = max(range(len(odd_rows)), key=odd_rows.__getitem__)
print(f"odd_schur_maximizer_grid={odd_grid[odd_index]:.17g}")
print(f"odd_schur_bound_grid={odd_rows[odd_index]:.17g}")
print(f"odd_schur_reserve_grid={D44-odd_rows[odd_index]:.17g}")
