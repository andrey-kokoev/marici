"""Exact Bernstein certificate for G(d=1/2)<0 on the small-slope triangle."""

from math import comb
import sympy as sp


p, c, r, t = sp.symbols("p c r T")
q = c * p
d = sp.Rational(1, 2)
t_value = 1 - p**2 * d
slope_sum, product = p + q, p*q
n_t = (
    4*t**3 + 2*t*product - 2*t*(2+product)*r**2
    - slope_sum*r*(1-r**2)
)
n_r = (
    -t*slope_sum + 2*(1-2*t**2-t**2*product)*r
    + 3*t*slope_sum*r**2
)
g = sp.expand((1-t**2)*n_t + p*(1-r**2)*n_r)

# The compact numerator is 8p*(G/p^2)=8G/p.  Its sign equals G for p>0.
compact = sp.cancel(8*g.subs(t, t_value)/p)
assert sp.fraction(compact)[1] == 1

u, s = sp.symbols("u s", nonnegative=True)
cube = sp.Poly(
    sp.expand((-compact).subs({p: u/10, r: 2*(u/10)+(1-2*(u/10))*s})),
    u, s, c,
)
degrees = tuple(cube.degree(variable) for variable in (u,s,c))
power = {monomial: coefficient for monomial, coefficient in cube.terms()}


def bernstein(index):
    total = sp.Rational(0)
    for monomial, coefficient in power.items():
        if all(monomial[axis] <= index[axis] for axis in range(3)):
            weight = sp.Rational(1)
            for axis in range(3):
                weight *= sp.Rational(
                    comb(index[axis], monomial[axis]),
                    comb(degrees[axis], monomial[axis]),
                )
            total += coefficient * weight
    return sp.factor(total)


coefficients = {
    (i,j,k): bernstein((i,j,k))
    for i in range(degrees[0]+1)
    for j in range(degrees[1]+1)
    for k in range(degrees[2]+1)
}
nonpositive = {index:value for index,value in coefficients.items() if value <= 0}
negative = {index:value for index,value in coefficients.items() if value < 0}
zero = {index:value for index,value in coefficients.items() if value == 0}
minimum_index, minimum = min(coefficients.items(), key=lambda item: item[1])
strict_witnesses = {
    k: coefficients[(degrees[0], 0, k)] for k in range(degrees[2]+1)
}
strict_physical_interior = (
    not negative and all(value > 0 for value in strict_witnesses.values())
)

print(f"cube_power_degrees={degrees}")
print(f"bernstein_coefficient_count={len(coefficients)}")
print(f"bernstein_nonpositive_count={len(nonpositive)}")
print(f"bernstein_negative={negative}")
print(f"bernstein_zero_indices={tuple(zero)}")
print(f"bernstein_minimum_index={minimum_index}")
print(f"bernstein_minimum={minimum}")
print(f"strict_witness_coefficients_i_max_j_0={strict_witnesses}")
print(f"closed_cube_nonnegative_certified={not negative}")
print(f"physical_domain_strictly_positive_certified={strict_physical_interior}")
print(f"small_slope_d_half_barrier_certified={strict_physical_interior}")

# Stronger post-barrier slab: d=h/2 for 0<=h<=1.
h = sp.symbols("h", nonnegative=True)
t_slab = 1 - p**2 * h/2
g_slab = sp.expand(g.subs(t, t_slab))
compact_slab = sp.cancel(8*g_slab/p)
assert sp.fraction(compact_slab)[1] == 1
cube4 = sp.Poly(
    sp.expand((-compact_slab).subs({
        p: u/10,
        r: 2*(u/10)+(1-2*(u/10))*s,
    })),
    u, s, c, h,
)
variables4 = (u,s,c,h)
degrees4 = tuple(cube4.degree(variable) for variable in variables4)
power4 = {monomial:coefficient for monomial,coefficient in cube4.terms()}


def bernstein4(index):
    total = sp.Rational(0)
    for monomial, coefficient in power4.items():
        if all(monomial[axis] <= index[axis] for axis in range(4)):
            weight = sp.Rational(1)
            for axis in range(4):
                weight *= sp.Rational(
                    comb(index[axis],monomial[axis]),
                    comb(degrees4[axis],monomial[axis]),
                )
            total += coefficient*weight
    return sp.factor(total)


coefficients4 = {
    (i,j,k,m):bernstein4((i,j,k,m))
    for i in range(degrees4[0]+1)
    for j in range(degrees4[1]+1)
    for k in range(degrees4[2]+1)
    for m in range(degrees4[3]+1)
}
negative4 = {index:value for index,value in coefficients4.items() if value<0}
strict4 = {
    (k,m):coefficients4[(degrees4[0],0,k,m)]
    for k in range(degrees4[2]+1)
    for m in range(degrees4[3]+1)
}
print(f"slab_cube_degrees={degrees4}")
print(f"slab_bernstein_coefficient_count={len(coefficients4)}")
print(f"slab_bernstein_negative_count={len(negative4)}")
print(f"slab_strict_witness_min={min(strict4.values())}")
print(f"post_barrier_slab_G_strictly_negative_certified={not negative4 and min(strict4.values())>0}")
