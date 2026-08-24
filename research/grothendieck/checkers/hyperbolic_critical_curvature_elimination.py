"""Eliminate q from G=0 and factor the exact critical curvature DG."""

import sympy as sp


t, r, p, q = sp.symbols("T R p q", positive=True)
s = p + q
product = p * q
b = 1 - 2 * t**2 - t**2 * product
n_t = (
    4 * t**3 + 2 * t * product
    - 2 * t * (2 + product) * r**2
    - s * r * (1 - r**2)
)
n_r = -t * s + 2 * b * r + 3 * t * s * r**2
n_tt = 12 * t**2 + 2 * product - 2 * (2 + product) * r**2
n_tr = -4 * t * (2 + product) * r - s * (1 - 3 * r**2)
n_rr = 2 * b + 6 * t * s * r
vt = 1 - t**2
vr = p * (1 - r**2)
g = sp.expand(vt * n_t + vr * n_r)
dg = sp.expand(
    -2 * t * vt * n_t
    - 2 * p**2 * r * (1 - r**2) * n_r
    + vt**2 * n_tt
    + 2 * p * vt * (1 - r**2) * n_tr
    + p**2 * (1 - r**2) ** 2 * n_rr
)

g_poly = sp.Poly(g, q)
assert g_poly.degree() == 1
gq = g_poly.coeff_monomial(q)
g0 = g_poly.coeff_monomial(1)
q_critical = sp.cancel(-g0 / gq)
critical_dg = sp.cancel(dg.subs(q, q_critical))
numerator, denominator = sp.fraction(critical_dg)

print(f"G_q_factor={sp.factor(gq)}")
print(f"G_0_factor={sp.factor(g0)}")
print(f"q_at_critical={sp.factor(q_critical)}")
print(f"DG_critical_numerator_factor={sp.factor(numerator)}")
print(f"DG_critical_denominator_factor={sp.factor(denominator)}")
print(
    "DG_critical_degrees="
    f"{(sp.degree(numerator,t),sp.degree(numerator,r),sp.degree(numerator,p))}"
)

z = sp.symbols("z", positive=True)
z_numerator = sp.factor(numerator.subs(r, t * z))
z_denominator = sp.factor(denominator.subs(r, t * z))
print(f"DG_critical_ratio_numerator_factor={z_numerator}")
print(f"DG_critical_ratio_denominator_factor={z_denominator}")
print(
    "DG_critical_ratio_degrees="
    f"{(sp.degree(z_numerator,t),sp.degree(z_numerator,z),sp.degree(z_numerator,p))}"
)

x = sp.symbols("x", nonnegative=True)
d_ratio = sp.factor(-z_denominator / t).subs(t**2, x)
print(f"D_affine_in_T2={sp.factor(d_ratio)}")
print(f"D_at_T2_0={sp.factor(d_ratio.subs(x,0))}")
print(f"D_at_T2_1={sp.factor(d_ratio.subs(x,1))}")

# Small-slope/unbounded-holding chart: q=c p, R=p y, T=1 at leading order.
c, y, epsilon = sp.symbols("c y epsilon", nonnegative=True)
small_g = sp.Poly(
    sp.expand(g.subs({q: c * epsilon, p: epsilon, r: epsilon * y, t: 1})),
    epsilon,
)
small_dg = sp.Poly(
    sp.expand(dg.subs({q: c * epsilon, p: epsilon, r: epsilon * y, t: 1})),
    epsilon,
)
g_valuation = min(power[0] for power, coefficient in small_g.terms() if coefficient)
dg_valuation = min(power[0] for power, coefficient in small_dg.terms() if coefficient)
print(f"small_slope_G_valuation={g_valuation}")
print(f"small_slope_G_leading={sp.factor(small_g.coeff_monomial(epsilon**g_valuation))}")
print(f"small_slope_DG_valuation={dg_valuation}")
print(f"small_slope_DG_leading={sp.factor(small_dg.coeff_monomial(epsilon**dg_valuation))}")

v = sp.symbols("v", nonnegative=True)
t_faithful = 1 - epsilon**2 * v / 2
faithful_g = sp.Poly(
    sp.series(
        g.subs({q: c * epsilon, p: epsilon, r: epsilon * y, t: t_faithful}),
        epsilon, 0, 6,
    ).removeO().expand(),
    epsilon,
)
faithful_dg = sp.Poly(
    sp.series(
        dg.subs({q: c * epsilon, p: epsilon, r: epsilon * y, t: t_faithful}),
        epsilon, 0, 6,
    ).removeO().expand(),
    epsilon,
)
fgv = min(power[0] for power, coefficient in faithful_g.terms() if coefficient)
fdv = min(power[0] for power, coefficient in faithful_dg.terms() if coefficient)
print(f"faithful_small_slope_G_valuation={fgv}")
print(f"faithful_small_slope_G_leading={sp.factor(faithful_g.coeff_monomial(epsilon**fgv))}")
print(f"faithful_small_slope_DG_valuation={fdv}")
print(f"faithful_small_slope_DG_leading={sp.factor(faithful_dg.coeff_monomial(epsilon**fdv))}")

# Exact faithful chart, reduced modulo T^2=1-p^2 v rather than Taylorizing T.
exact_substitutions = {q: c * epsilon, p: epsilon, r: epsilon * y}
relation = sp.Poly(t**2 - (1 - epsilon**2 * v), t,
                   domain=sp.QQ.frac_field(epsilon, c, y, v))
g_reduced = sp.rem(
    sp.Poly(sp.expand(g.subs(exact_substitutions)), t,
            domain=sp.QQ.frac_field(epsilon, c, y, v)),
    relation,
).as_expr()
dg_reduced = sp.rem(
    sp.Poly(sp.expand(dg.subs(exact_substitutions)), t,
            domain=sp.QQ.frac_field(epsilon, c, y, v)),
    relation,
).as_expr()
g_normalized = sp.factor(g_reduced / epsilon**2)
dg_normalized = sp.factor(dg_reduced / epsilon**2)
print(f"exact_faithful_G_over_p2={g_normalized}")
print(f"exact_faithful_DG_over_p2={dg_normalized}")
print(
    "exact_faithful_G_degrees="
    f"{tuple(sp.degree(g_normalized, variable) for variable in (epsilon,c,y,v,t))}"
)
print(
    "exact_faithful_DG_degrees="
    f"{tuple(sp.degree(dg_normalized, variable) for variable in (epsilon,c,y,v,t))}"
)

v_field = sp.QQ.frac_field(epsilon, c, y, t)
_, dg_mod_g = sp.div(
    sp.Poly(dg_normalized, v, domain=v_field),
    sp.Poly(g_normalized, v, domain=v_field),
)
critical_remainder = sp.cancel(dg_mod_g.as_expr())
cr_num, cr_den = sp.fraction(critical_remainder)
print(f"faithful_DG_mod_G_v_degree={sp.degree(cr_num,v)}")
print(
    "faithful_DG_mod_G_numerator_degrees="
    f"{tuple(sp.degree(cr_num, variable) for variable in (epsilon,c,y,v,t))}"
)
print(f"faithful_DG_mod_G_denominator_factor={sp.factor(cr_den)}")
print(f"faithful_DG_mod_G_numerator_factor={sp.factor(cr_num)}")

cr_reduced = sp.rem(
    sp.Poly(cr_num, t, domain=sp.QQ.frac_field(epsilon, c, y, v)),
    relation,
).as_expr()
print(
    "faithful_DG_mod_G_relation_reduced_degrees="
    f"{tuple(sp.degree(cr_reduced, variable) for variable in (epsilon,c,y,v,t))}"
)
print(f"faithful_DG_mod_G_relation_reduced_factor={sp.factor(cr_reduced)}")

d = sp.symbols("d", nonnegative=True)
polynomial_substitutions = {
    q: c * epsilon,
    p: epsilon,
    r: epsilon * y,
    t: 1 - epsilon**2 * d,
}
g_poly_tail = sp.factor(sp.expand(g.subs(polynomial_substitutions)) / epsilon**2)
dg_poly_tail = sp.factor(sp.expand(dg.subs(polynomial_substitutions)) / epsilon**2)
print(
    "polynomial_tail_G_degrees="
    f"{tuple(sp.degree(g_poly_tail,var) for var in (epsilon,c,y,d))}"
)
print(
    "polynomial_tail_DG_degrees="
    f"{tuple(sp.degree(dg_poly_tail,var) for var in (epsilon,c,y,d))}"
)
print(f"polynomial_tail_G_at_p0={sp.factor(g_poly_tail.subs(epsilon,0))}")
print(f"polynomial_tail_DG_at_p0={sp.factor(dg_poly_tail.subs(epsilon,0))}")
d_field = sp.QQ.frac_field(epsilon, c, y)
_, tail_remainder = sp.div(
    sp.Poly(dg_poly_tail, d, domain=d_field),
    sp.Poly(g_poly_tail, d, domain=d_field),
)
tail_rem = sp.cancel(tail_remainder.as_expr())
tail_num, tail_den = sp.fraction(tail_rem)
print(f"polynomial_tail_DG_mod_G_d_degree={sp.degree(tail_num,d)}")
print(
    "polynomial_tail_DG_mod_G_numerator_degrees="
    f"{tuple(sp.degree(tail_num,var) for var in (epsilon,c,y,d))}"
)
print(f"polynomial_tail_DG_mod_G_denominator_factor={sp.factor(tail_den)}")
print(f"polynomial_tail_DG_mod_G_p0={sp.factor(tail_rem.subs(epsilon,0))}")

c_poly = sp.Poly(g_poly_tail, c, domain=sp.QQ.frac_field(epsilon,y,d))
assert c_poly.degree() == 1
c1 = c_poly.coeff_monomial(c)
c0 = c_poly.coeff_monomial(1)
c_critical = sp.cancel(-c0/c1)
k_at_c = sp.cancel(dg_poly_tail.subs(c,c_critical))
kc_num,kc_den = sp.fraction(k_at_c)
print(f"polynomial_tail_c_critical_numerator_factor={sp.factor(-c0)}")
print(f"polynomial_tail_c_critical_denominator_factor={sp.factor(c1)}")
print(
    "polynomial_tail_DG_at_c_numerator_degrees="
    f"{tuple(sp.degree(kc_num,var) for var in (epsilon,y,d))}"
)
print(f"polynomial_tail_DG_at_c_denominator_factor={sp.factor(kc_den)}")
print(f"polynomial_tail_DG_at_c_p0={sp.factor(k_at_c.subs(epsilon,0))}")

barrier = sp.factor(g_poly_tail.subs(d, sp.Rational(1, 2)))
print(f"polynomial_tail_G_at_d_half_factor={barrier}")
barrier_poly = sp.Poly(barrier, y, c, epsilon)
barrier_signs = {
    "positive": sum(1 for _, coefficient in barrier_poly.terms() if coefficient > 0),
    "negative": sum(1 for _, coefficient in barrier_poly.terms() if coefficient < 0),
}
print(f"polynomial_tail_G_at_d_half_coefficient_signs={barrier_signs}")

r_compact = sp.symbols("r", nonnegative=True)
barrier_compact = sp.cancel(barrier.subs(y, r_compact / epsilon))
bc_num, bc_den = sp.fraction(barrier_compact)
print(f"polynomial_tail_barrier_compact_denominator={sp.factor(bc_den)}")
print(
    "polynomial_tail_barrier_compact_degrees="
    f"{tuple(sp.degree(bc_num,var) for var in (epsilon,c,r_compact))}"
)
print(f"polynomial_tail_barrier_compact_factor={sp.factor(bc_num)}")
print(f"polynomial_tail_barrier_R1={sp.factor(bc_num.subs(r_compact,1))}")
barrier_r_factor = sp.factor(bc_num / (1-r_compact)) if sp.rem(
    sp.Poly(bc_num,r_compact), sp.Poly(1-r_compact,r_compact)
).is_zero else None
print(f"polynomial_tail_barrier_div_one_minus_R={barrier_r_factor}")
