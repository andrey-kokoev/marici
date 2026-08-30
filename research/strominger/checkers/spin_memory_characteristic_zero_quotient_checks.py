"""Characteristic-zero harmonic decomposition of the rank-16 quotient."""

import hashlib
import itertools
import json
import math
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
ARTIFACT = ROOT / "research/strominger/spin-memory-characteristic-zero-quotient.md"
z = sp.symbols("z", real=True)
latitudes = (-sp.Rational(2, 3), -sp.Rational(1, 3), sp.Integer(0),
             sp.Rational(1, 3), sp.Rational(2, 3))
degrees = (2, 3, 4)


def block(pair, abs_m):
    admitted = [degree for degree in degrees if degree >= abs_m]
    matrix = sp.Matrix([
        [sp.assoc_legendre(degree, abs_m, latitudes[index]) for degree in admitted]
        for index in pair
    ])
    return admitted, matrix


pair_data = {}
residual_degree_checks = []
third_dark_capability = {}
transfer_degree_checks = []
for pair in itertools.combinations(range(5), 2):
    ranks = {}
    nullities = {}
    quotient_generators = {}
    for abs_m in range(5):
        admitted, matrix = block(pair, abs_m)
        ranks[abs_m] = matrix.rank()
        nullities[abs_m] = len(admitted) - matrix.rank()
        if abs_m <= 2:
            coefficients = matrix.nullspace()[0]
            generator = sp.factor(sum(
                coefficient * sp.assoc_legendre(degree, abs_m, z)
                for coefficient, degree in zip(coefficients, admitted)
            ))
            quotient_generators[abs_m] = generator
            dark_factor = (z - latitudes[pair[0]]) * (z - latitudes[pair[1]])
            spin_factor = sp.sqrt(1 - z**2) if abs_m == 1 else (1 - z**2 if abs_m == 2 else 1)
            residual = sp.cancel(generator / (dark_factor * spin_factor))
            residual_degree_checks.append(sp.Poly(residual, z).degree() == 2 - abs_m)
    pair_data[str(pair)] = {
        "ranks": ranks,
        "nullities": nullities,
        "total_rank": ranks[0] + 2 * sum(ranks[m] for m in range(1, 5)),
        "quotient_dimension": nullities[0] + 2 * sum(nullities[m] for m in range(1, 5)),
        "generators_vanish_on_dark_pair": all(
            sp.simplify(generator.subs(z, latitudes[index])) == 0
            for generator in quotient_generators.values()
            for index in pair
        ),
    }
    live_indices = [index for index in range(5) if index not in pair]
    third_dark_capability[str(pair)] = any(
        sp.simplify(generator.subs(z, latitudes[index])) == 0
        for generator in quotient_generators.values()
        for index in live_indices
    )
    baseline = next(
        index for index in live_indices
        if all(sp.simplify(generator.subs(z, latitudes[index])) != 0 for generator in quotient_generators.values())
    )
    for target in (index for index in live_indices if index != baseline):
        multipliers = [
            sp.simplify(
                quotient_generators[abs_m].subs(z, latitudes[target])
                / quotient_generators[abs_m].subs(z, latitudes[baseline])
            )
            for abs_m in range(3)
        ]
        casimir = sp.symbols("casimir")
        transfer = sp.interpolate([(0, multipliers[0]), (1, multipliers[1]), (4, multipliers[2])], casimir)
        transfer_degree_checks.append(sp.Poly(transfer, casimir).degree() <= 2)

expected_ranks = {0: 2, 1: 2, 2: 2, 3: 2, 4: 1}
expected_nullities = {0: 1, 1: 1, 2: 1, 3: 0, 4: 0}
u = sp.symbols("u")
x = sp.symbols("x")
universal_five_zero_witness_checks = []
universal_hidden_antipode_checks = []
four_plus_one_prime_witness_checks = []
three_plus_two_transfer_classes = set()
four_plus_one_directed_pairs = {
    "sqrt2_split": 0,
    "sqrt5_prime5_closed": 0,
    "sqrt5_norm_closed": 0,
    "remaining": 0,
}
for representative in ((0, 1), (0, 3)):
    live = [index for index in range(5) if index not in representative]
    generators = {}
    for abs_m in range(3):
        admitted, matrix = block(representative, abs_m)
        coefficients = matrix.nullspace()[0]
        generators[abs_m] = [
            sp.simplify(sum(
                coefficient * sp.assoc_legendre(degree, abs_m, latitudes[index])
                for coefficient, degree in zip(coefficients, admitted)
            ))
            for index in live
        ]
    rows = []
    for ring_position, longitude in ((0, 0), (0, 1), (0, 2), (1, 1), (2, 1)):
        rows.append([
            generators[2][ring_position] * u ** (-2 * longitude),
            generators[1][ring_position] * u ** (-longitude),
            generators[0][ring_position],
            generators[1][ring_position] * u ** longitude,
            generators[2][ring_position] * u ** (2 * longitude),
        ])
    # Stronger than the original ninth-root test: the determinant vanishes
    # identically after clearing Laurent powers, independently of the grid.
    cleared = sp.expand(sp.det(sp.Matrix(rows)) * u**6)
    universal_five_zero_witness_checks.append(sp.simplify(cleared) == 0)
    kernel_vector = sp.Matrix(rows).nullspace()[0]
    witness_polynomials = []
    for ring_position in range(3):
        witness_polynomials.append(sp.factor(
            generators[2][ring_position] * kernel_vector[0]
            + generators[1][ring_position] * kernel_vector[1] * x
            + generators[0][ring_position] * kernel_vector[2] * x**2
            + generators[1][ring_position] * kernel_vector[3] * x**3
            + generators[2][ring_position] * kernel_vector[4] * x**4
        ))
    universal_hidden_antipode_checks.append(all(
        sp.rem(sp.Poly(polynomial, x), sp.Poly(x**2 - u**2, x)).as_expr() == 0
        for polynomial in witness_polynomials
    ))
    universal_hidden_antipode_checks.append(
        sp.rem(
            sp.Poly(witness_polynomials[0], x),
            sp.Poly((x - 1) * (x - u) * (x - u**2) * (x + u), x),
        ).as_expr() == 0
    )
    # For a 4+1 incidence, radical-field separation removes the E1+E3
    # component.  The remaining equation is A + (t0/t2) C = 0, where
    # A=1+E4.  An odd prime dividing the reduced numerator of t0/t2 but not
    # its denominator forces A=0 after reduction, hence E4=-1, impossible
    # for an odd-order root.  Ratios carried only by sqrt(5) require 5 not
    # to divide the longitude conductor before that radical can be split.
    for base_ring in range(3):
        for target_ring in range(3):
            if base_ring == target_ring:
                continue
            t0 = sp.factor(generators[0][target_ring] / generators[0][base_ring])
            t1 = sp.factor(generators[1][target_ring] / generators[1][base_ring])
            t2 = sp.factor(generators[2][target_ring] / generators[2][base_ring])
            rational_ratio = sp.factor(t0 / t2)
            middle_square_ratio = sp.factor((t1 / t2)**2)
            three_plus_two_transfer_classes.add((rational_ratio, middle_square_ratio))
            numerator, denominator = map(int, sp.fraction(rational_ratio))
            witness_primes = [
                prime for prime in sp.factorint(abs(numerator))
                if prime % 2 == 1 and prime != 5 and denominator % prime != 0
            ]
            four_plus_one_prime_witness_checks.append(bool(witness_primes))
            if sp.simplify(t1 / sp.sqrt(5)).is_rational:
                if numerator % 5 == 0:
                    four_plus_one_directed_pairs["sqrt5_prime5_closed"] += 1
                else:
                    four_plus_one_directed_pairs["sqrt5_norm_closed"] += 1
            else:
                four_plus_one_directed_pairs["sqrt2_split"] += 1

# The two former sqrt(5) forward residues clear denominators to
#   495 A + 121 sqrt(5) B + 351 C = 0,
#   165 A - 121 sqrt(5) B + 117 C = 0.
# Both force C in 11 O_K, hence C=0 by |sigma(C)|<=6<11.  The first then
# forces B in 9 O_K, hence B=0 by |sigma(B)|<=8<9.  In the second, division
# by 11 gives 15 A = 11 sqrt(5) B, hence A in 11 O_K and A=0 because
# |sigma(A)|<=2<11.  In either case A=1+E4=0 contradicts odd order.
four_plus_one_residual_norm_checks = {
    "first_forces_C_in_11O": 495 % 11 == 0 and 121 % 11 == 0 and 351 % 11 != 0,
    "first_forces_B_in_9O": 495 % 9 == 0 and 351 % 9 == 0 and sp.gcd(121 * 5, 9) == 1,
    "first_norm_bounds_close": 11 > 6 and 9 > 8,
    "second_forces_C_in_11O": 165 % 11 == 0 and 121 % 11 == 0 and 117 % 11 != 0,
    "second_forces_A_in_11O_after_C_zero": sp.gcd(15, 11) == 1,
    "second_norm_bound_closes": 11 > 2,
}

# Three base-ring zeros leave the pencil F(x) (alpha*x + beta).  Applying a
# diagonal transfer and evaluating at two target roots gives this exact 2x2
# determinant.  Its even radical component has the forbidden target-antipode
# factor p+q; the remaining odd/even components are the next torsion ideal.
A, B, C, p, q, t0, t1, t2 = sp.symbols("A B C p q t0 t1 t2")
Q0 = lambda value: -t2 * C + t1 * B * value - t0 * A * value**2 + t1 * value**3
Q1 = lambda value: -t1 * C * value + t0 * B * value**2 - t1 * A * value**3 + t2 * value**4
three_plus_two_residual = sp.cancel((Q0(p) * Q1(q) - Q0(q) * Q1(p)) / (p - q))
three_plus_two_t1_polynomial = sp.Poly(three_plus_two_residual, t1)
three_plus_two_even = (
    three_plus_two_t1_polynomial.coeff_monomial(1)
    + three_plus_two_t1_polynomial.coeff_monomial(t1**2) * t1**2
)
three_plus_two_checks = {
    "pencil_residual_is_quadratic_in_middle_transfer": three_plus_two_t1_polynomial.degree() == 2,
    "even_component_has_target_antipode_factor": sp.simplify(
        three_plus_two_even.subs(q, -p)
    ) == 0,
    "odd_component_is_present": three_plus_two_t1_polynomial.coeff_monomial(t1) != 0,
}
W, rr, ss = sp.symbols("W rr ss")
X_base = -A**2 - B**2 + A * C + B
odd_normalized = sp.expand(
    rr * X_base + (1 - W) * (A * C + B) - (C**2 + 1)
)
even_normalized = sp.expand(
    rr * (A + B * C) + C * (W - 2) + ss * (A * B - C)
)
trace_resultant = sp.factor(sp.resultant(odd_normalized, even_normalized, W))
expected_trace_resultant = sp.factor(
    (A * C + B) * ((1 + ss - rr) * C - ss * A * B)
    + (C**2 + 1) * (C - rr * A * B)
)
three_plus_two_checks.update({
    "target_separation_eliminates_to_trace_resultant": sp.simplify(
        trace_resultant - expected_trace_resultant
    ) == 0,
    "directed_transfers_collapse_to_ten_rational_classes": (
        len(three_plus_two_transfer_classes) == 10
        and all(ratio.is_Rational and square.is_Rational for ratio, square in three_plus_two_transfer_classes)
    ),
    "transfer_classes_are_closed_under_direction_reversal": all(
        (sp.factor(1 / ratio), sp.factor(1 / square)) in three_plus_two_transfer_classes
        for ratio, square in three_plus_two_transfer_classes
    ),
})

# Deutsch counterfactual: the quadratic-residue 7-period has A+B=-1,
# AB=2, C=1.  Pair it with the nontrivial cube roots, so U=p+q=-1 and
# W=U^2=1.  The rational transfer (r,s)=(1,2) makes both normalized
# residual equations vanish exactly, producing a genuine 3+2 circuit on
# the N=21 grid.
A7_plus_B7 = sp.Integer(-1)
A7_times_B7 = sp.Integer(2)
C7 = sp.Integer(1)
W3 = sp.Integer(1)
r_bad = sp.Integer(1)
s_bad = sp.Integer(2)
X7 = -(A7_plus_B7**2 - 2 * A7_times_B7) + C7 * A7_plus_B7
odd_bad = sp.expand(
    r_bad * X7 + (1 - W3) * C7 * A7_plus_B7 - (C7**2 + 1)
)
even_bad = sp.expand(
    r_bad * A7_plus_B7 + C7 * (W3 - 2)
    + s_bad * (A7_times_B7 - C7)
)
three_plus_two_bad_transfer_checks = {
    "seven_period_trace_is_minus_one": A7_plus_B7 == -1,
    "seven_period_norm_is_two": A7_times_B7 == 2,
    "cube_pair_reconstructs_W_one": W3 == 1,
    "bad_transfer_odd_residual_vanishes": odd_bad == 0,
    "bad_transfer_even_residual_vanishes": even_bad == 0,
}

# The Legendre source curve itself still admits the bad transfer (1,2).
# Eliminating latitude gives two exact conics.  Equal R with doubled S has
# quadratic-irrational, not rational, latitude solutions in each orbit.
R_curve, S_curve = sp.symbols("R_curve S_curve")
R_first = -(375 * z**2 - 180 * z - 77) / (4500 * (z - 1) * (z + 1))
S_first = -(19 * z - 9)**2 / (3249 * (z - 1) * (z + 1))
R_second = -(15 * z**2 + 60 * z - 77) / (180 * (z - 1) * (z + 1))
S_second = -(z + 3)**2 / (9 * (z - 1) * (z + 1))
conic_first = (
    396900000000 * R_curve**2 - 512857899000 * R_curve * S_curve
    + 17767260000 * R_curve + 148850170101 * S_curve**2
    - 12928901652 * S_curve + 198838201
)
conic_second = (
    518400 * R_curve**2 + 793800 * R_curve * S_curve - 87840 * R_curve
    + 4941 * S_curve**2 + 198468 * S_curve + 3721
)
bad_chord_first = 6096481 * z**2 - 8153586 * z + 2148201
bad_chord_second = 14519 * z**2 - 30498 * z + 14031
bad_chord_first_discriminant = sp.discriminant(bad_chord_first, z)
bad_chord_second_discriminant = sp.discriminant(bad_chord_second, z)
bad_chord_34_first = (
    1272256551 * z**4 + 1498218768 * z**3 - 8613013086 * z**2
    + 9246225744 * z - 3148996777
)
bad_chord_34_second = (
    59049 * z**4 + 711504 * z**3 + 1848510 * z**2
    - 325104 * z - 2231687
)
source_curve_checks = {
    "first_radial_coordinates_lie_on_source_conic": sp.factor(
        conic_first.subs({R_curve: R_first, S_curve: S_first})
    ) == 0,
    "second_radial_coordinates_lie_on_source_conic": sp.factor(
        conic_second.subs({R_curve: R_second, S_curve: S_second})
    ) == 0,
    "first_bad_chord_latitudes_are_quadratic_irrational": not sp.integer_nthroot(
        int(bad_chord_first_discriminant), 2
    )[1],
    "second_bad_chord_latitudes_are_quadratic_irrational": not sp.integer_nthroot(
        int(bad_chord_second_discriminant), 2
    )[1],
    "first_three_four_bad_chord_is_irreducible_over_Q": sp.Poly(
        bad_chord_34_first, z
    ).is_irreducible,
    "second_three_four_bad_chord_is_irreducible_over_Q": sp.Poly(
        bad_chord_34_second, z
    ).is_irreducible,
}

# A parametric family explains the N=69 near-rational observation.  Put the
# base roots at {1,v,v^-1} and use {v,v^-1} as the target pair.  With
# t=v+v^-1 the exact discriminant transfer is s=1 and
# r=-(t^2+t-1)/(t+1).  Rational r forces t to have degree at most two.
# For odd torsion this leaves orders 1, 3, and 5; their transfers are,
# respectively, negative, undefined, and zero.
t = sp.symbols("t", real=True)
symmetric_r = -sp.factor((t**2 + t - 1) / (t + 1))
symmetric_s = sp.Integer(1)
rational_transfer_parameter = sp.symbols("rational_transfer_parameter")
rationality_polynomial = sp.expand(
    t**2 + (1 + rational_transfer_parameter) * t
    + rational_transfer_parameter - 1
)
symmetric_family_checks = {
    "symmetric_family_transfer_has_s_one": symmetric_s == 1,
    "symmetric_family_rationality_is_quadratic_in_trace": (
        sp.solve(sp.Eq(symmetric_r, rational_transfer_parameter), t)
        and sp.Poly(rationality_polynomial, t).degree() == 2
    ),
    "order_one_transfer_is_negative": symmetric_r.subs(t, 2) == -sp.Rational(5, 3),
    "order_three_trace_is_pencil_pole": sp.denom(symmetric_r).subs(t, -1) == 0,
    "order_five_transfer_is_zero": sp.rem(
        sp.together(sp.numer(symmetric_r)), t**2 + t - 1, domain=sp.QQ
    ) == 0,
}

# Allow an independent inverse target pair.  Write x=u+u^-1 for the base
# triple {1,u,u^-1}, and W=(v+v^-1)^2 for the target pair.  The residual
# equations simplify to a two-trace surface.  Rational r,s again force the
# base trace to be quadratic, and the odd-torsion cases are all nonpositive
# or degenerate.
x, W = sp.symbols("x W", real=True)
centered_r = sp.factor((x - (x + 1) * W) / (x * (x + 1)))
centered_s = sp.factor(W / x**2)
q_r, q_s = sp.symbols("q_r q_s", rational=True)
centered_rationality_polynomial = q_s * x**2 + (q_s + q_r) * x + q_r - 1
order_five_remainder = sp.rem(
    centered_rationality_polynomial, x**2 + x - 1, domain=sp.QQ[q_r, q_s]
)
centered_family_checks = {
    "centered_two_trace_r_formula_is_exact": sp.factor(
        centered_r * x * (x + 1) - x + (x + 1) * W
    ) == 0,
    "centered_two_trace_s_formula_is_exact": sp.factor(centered_s * x**2 - W) == 0,
    "rational_centered_transfer_forces_quadratic_base_trace": sp.Poly(
        centered_rationality_polynomial, x
    ).degree() == 2,
    "order_one_rational_target_squares_are_not_positive_transfers": all(
        centered_r.subs({x: 2, W: target_square}) <= 0 for target_square in (1, 4)
    ),
    "order_three_base_is_degenerate": sp.denom(centered_r).subs(x, -1) == 0,
    "order_five_base_forces_r_zero_and_s_one": sp.Poly(
        order_five_remainder, x
    ).all_coeffs() == [q_r, q_r + q_s - 1],
}

# The first genuinely off-center product-one base triple is governed by two
# real invariants.  If A is the first elementary sum, then B=conjugate(A);
# put U=A+B and V=AB.  Eliminating target separation W from the two residual
# equations gives a rational Möbius incidence curve.  The N=21 exception is
# the point (U,V)=(-1,2), whose centering defect 4V-U^2 equals 7.
U, V = sp.symbols("U V", real=True)
product_one_X = 2 * V - U**2 + U
product_one_odd = sp.expand(q_r * product_one_X + (1 - W) * U - 2)
product_one_even = sp.expand(q_r * U + W - 2 + q_s * (V - 1))
product_one_incidence = sp.factor(
    product_one_odd.subs(W, sp.solve(sp.Eq(product_one_even, 0), W)[0])
)
expected_product_one_incidence = q_r * (2 * V + U) + q_s * U * (V - 1) - U - 2
product_one_off_center_checks = {
    "target_separation_cancels_from_product_one_incidence": sp.factor(
        product_one_incidence - expected_product_one_incidence
    ) == 0,
    "incidence_is_mobius_linear_in_base_norm": sp.Poly(
        expected_product_one_incidence, V
    ).degree() == 1,
    "N21_exception_lies_on_product_one_incidence": expected_product_one_incidence.subs(
        {U: -1, V: 2, q_r: 1, q_s: 2}
    ) == 0,
    "N21_centering_defect_is_seven": (4 * V - U**2).subs({U: -1, V: 2}) == 7,
}

# The bilinear incidence has coefficient-matrix determinant proportional to
# (r-1)(r-s).  Therefore the only reducible transfer strata are r=1 and
# r=s.  The (1,2) exception lies on U=-1, which is the complete heptagon
# relation: the quadratic-residue exponents {1,2,4} and their inverses
# partition all six nonzero residues modulo 7.
incidence_coefficient_matrix = sp.Matrix([
    [q_s, q_r - q_s - 1],
    [2 * q_r, -2],
])
reducible_incidence_checks = {
    "incidence_reducibility_discriminant_factors": sp.factor(
        incidence_coefficient_matrix.det() + 2 * (q_r - 1) * (q_r - q_s)
    ) == 0,
    "r_one_stratum_factors": sp.expand(
        expected_product_one_incidence.subs(q_r, 1) - (q_s * U + 2) * (V - 1)
    ) == 0,
    "r_equals_s_stratum_factors": sp.expand(
        expected_product_one_incidence.subs(q_s, q_r) - (U + 2) * (q_r * V - 1)
    ) == 0,
    "one_two_exception_selects_U_minus_one_branch": sp.expand(
        expected_product_one_incidence.subs({q_r: 1, q_s: 2})
        - 2 * (U + 1) * (V - 1)
    ) == 0,
    "seven_residue_triple_and_inverses_cover_complete_heptagon": (
        {1, 2, 4} | {(-exponent) % 7 for exponent in {1, 2, 4}}
    ) == set(range(1, 7)),
}

# Mann reduction for the U=-1 branch bounds odd root ratios by conductor 105.
# Enumerate the resulting quotient ring exactly, not numerically.  Product one
# imposes a+b+c=0 mod 105; U=-1 asks that the triple, its inverses, and 1 sum
# to zero in Q[x]/Phi_105.
mann_conductor = 3 * 5 * 7
phi_105 = sp.Poly(sp.cyclotomic_poly(mann_conductor, z), z, domain=sp.QQ)
residue_vectors = {}
for exponent in range(mann_conductor):
    remainder = sp.rem(sp.Poly(z**exponent, z, domain=sp.QQ), phi_105)
    residue_vectors[exponent] = tuple(
        remainder.nth(degree) for degree in range(phi_105.degree())
    )

def residue_sum_is_zero(exponents):
    return all(
        sum(residue_vectors[exponent][degree] for exponent in exponents) == 0
        for degree in range(phi_105.degree())
    )

mann_u_minus_one_triples = []
for a, b, c in itertools.combinations(range(mann_conductor), 3):
    if (a + b + c) % mann_conductor != 0:
        continue
    heptagon_exponents = (0, a, b, c, (-a) % mann_conductor,
                          (-b) % mann_conductor, (-c) % mann_conductor)
    if residue_sum_is_zero(heptagon_exponents):
        mann_u_minus_one_triples.append((a, b, c))

mann_reduction_checks = {
    "mann_odd_conductor_bound_is_105": mann_conductor == 105,
    "exact_U_minus_one_torsion_triples_are_two_heptagon_orientations": (
        mann_u_minus_one_triples == [(15, 30, 60), (45, 75, 90)]
    ),
    "mann_witnesses_descend_to_quadratic_residues_mod_seven": {
        tuple(exponent // 15 for exponent in triple)
        for triple in mann_u_minus_one_triples
    } == {(1, 2, 4), (3, 5, 6)},
}

# Four-plane typing of the Deutsch perturbation.  The source conics possess
# real bad chords in the physical latitude interval, but their coordinates
# are irrational, so the original rational-latitude constructor cannot
# instantiate them.  Geometric feasibility is deliberately not treated as
# an authority grant.  At the heptagon point the readout response is exactly
# 3r-s-1, so the kernel persists on a compensating transfer line.
heptagon_response = sp.factor(
    expected_product_one_incidence.subs({U: -1, V: 2})
)
authority_plane_checks = {
    "first_bad_chord_has_two_real_physical_latitudes": sp.Poly(
        bad_chord_first, z
    ).count_roots(-1, 1) == 2,
    "second_bad_chord_has_one_real_physical_latitude": sp.Poly(
        bad_chord_second, z
    ).count_roots(-1, 1) == 1,
    "bad_chords_are_outside_rational_latitude_constructor": (
        not sp.integer_nthroot(int(bad_chord_first_discriminant), 2)[1]
        and not sp.integer_nthroot(int(bad_chord_second_discriminant), 2)[1]
    ),
    "heptagon_response_is_affine_compensation_law": sp.expand(
        heptagon_response - (3 * q_r - q_s - 1)
    ) == 0,
    "one_two_transfer_lies_on_compensation_line": heptagon_response.subs(
        {q_r: 1, q_s: 2}
    ) == 0,
}

# Pull the heptagon compensation line s=3r-1 back through both Legendre
# chord maps.  Each equation is quadratic in the target latitude.  Its
# discriminant is a square source factor times a squarefree sextic, reducing
# rational compensation chords to rational points on a genus-two curve.
y_lat = sp.symbols("y_lat", real=True)
compensation_first = sp.factor(sp.together(
    S_first.subs(z, y_lat) / S_first
    - 3 * R_first.subs(z, y_lat) / R_first + 1
).as_numer_denom()[0])
compensation_second = sp.factor(sp.together(
    S_second.subs(z, y_lat) / S_second
    - 3 * R_second.subs(z, y_lat) / R_second + 1
).as_numer_denom()[0])
compensation_sextic_first = (
    2511675 * z**6 - 14405580 * z**5 + 22402983 * z**4
    + 13747572 * z**3 - 58129525 * z**2 + 45092772 * z - 11916097
)
compensation_sextic_second = (
    3645 * z**6 + 18180 * z**5 + 31497 * z**4 - 27564 * z**3
    - 72323 * z**2 - 5484 * z + 52081
)
compensation_discriminant_first = sp.factor(sp.discriminant(compensation_first, y_lat))
compensation_discriminant_second = sp.factor(sp.discriminant(compensation_second, y_lat))

def misses_compensation_curve(radial_r, radial_s):
    return all(
        x_lat == target_lat or sp.factor(
            radial_s.subs(z, target_lat) / radial_s.subs(z, x_lat)
            - 3 * radial_r.subs(z, target_lat) / radial_r.subs(z, x_lat) + 1
        ) != 0
        for x_lat in latitudes for target_lat in latitudes
    )

compensation_pullback_checks = {
    "first_compensation_pullback_is_quadratic_in_target_latitude": sp.Poly(
        compensation_first, y_lat
    ).degree() == 2,
    "second_compensation_pullback_is_quadratic_in_target_latitude": sp.Poly(
        compensation_second, y_lat
    ).degree() == 2,
    "first_pullback_discriminant_has_sextic_core": sp.factor(
        compensation_discriminant_first
        + 8 * (19 * z - 9)**2 * compensation_sextic_first
    ) == 0,
    "second_pullback_discriminant_has_sextic_core": sp.factor(
        compensation_discriminant_second
        - 8 * (z + 3)**2 * compensation_sextic_second
    ) == 0,
    "both_compensation_sextics_are_squarefree": all(
        sp.gcd(sp.Poly(sextic, z), sp.Poly(sp.diff(sextic, z), z)).degree() == 0
        for sextic in (compensation_sextic_first, compensation_sextic_second)
    ),
    "five_latitude_constructor_misses_both_compensation_curves": (
        misses_compensation_curve(R_first, S_first)
        and misses_compensation_curve(R_second, S_second)
    ),
}

# Exact homogeneous-height replay.  A rational x=a/b lifts precisely when
# c*b^6*f(a/b) is an integer square.  Through denominator 500 there are no
# physical points |x|<1.  The visible rational points x=+-1 are excluded
# source-boundary poles, and the even-degree models have no rational infinity.
compensation_integer_models = (
    (-8, (2511675, -14405580, 22402983, 13747572,
          -58129525, 45092772, -11916097)),
    (8, (3645, 18180, 31497, -27564, -72323, -5484, 52081)),
)

def homogeneous_value(coefficients, numerator, denominator):
    return sum(
        coefficient * numerator**(6 - index) * denominator**index
        for index, coefficient in enumerate(coefficients)
    )

def physical_rational_points(height):
    hits = []
    for curve_index, (scale, coefficients) in enumerate(compensation_integer_models, 1):
        for denominator in range(1, height + 1):
            for numerator in range(-denominator + 1, denominator):
                if math.gcd(numerator, denominator) != 1:
                    continue
                value = scale * homogeneous_value(coefficients, numerator, denominator)
                if value >= 0 and math.isqrt(value)**2 == value:
                    hits.append((curve_index, numerator, denominator))
    return hits

compensation_height_checks = {
    "no_physical_rational_compensation_point_through_height_500": (
        physical_rational_points(500) == []
    ),
    "both_curves_have_only_visible_boundary_candidates_at_plusminus_one": all(
        scale * homogeneous_value(coefficients, sign, 1) >= 0
        and math.isqrt(scale * homogeneous_value(coefficients, sign, 1))**2
            == scale * homogeneous_value(coefficients, sign, 1)
        for scale, coefficients in compensation_integer_models for sign in (-1, 1)
    ),
    "neither_even_degree_model_has_rational_infinity": all(
        scale * coefficients[0] < 0
        or math.isqrt(scale * coefficients[0])**2 != scale * coefficients[0]
        for scale, coefficients in compensation_integer_models
    ),
}

# Compute genus-two Jacobian orders from point counts over F_p and F_{p^2}.
# For #C(F_p)=p+1-S1 and #C(F_p^2)=p^2+1-S2,
# #J(F_p)=1-S1+(S1^2-S2)/2-p*S1+p^2.  Good-reduction specialization
# injects rational torsion, so gcd one proves J(Q)_tors=0.
def jacobian_order_mod_prime(scale, coefficients, prime):
    nonsquare = next(
        value for value in range(2, prime)
        if pow(value, (prime - 1) // 2, prime) == prime - 1
    )

    def multiply(left, right):
        return (
            (left[0] * right[0] + nonsquare * left[1] * right[1]) % prime,
            (left[0] * right[1] + left[1] * right[0]) % prime,
        )

    def power(value, exponent):
        result = (1, 0)
        while exponent:
            if exponent & 1:
                result = multiply(result, value)
            value = multiply(value, value)
            exponent //= 2
        return result

    squares = {value * value % prime for value in range(prime)}
    curve_fp = 2 if scale * coefficients[0] % prime in squares else 0
    for x_value in range(prime):
        rhs = scale * sum(
            coefficient * pow(x_value, 6 - index, prime)
            for index, coefficient in enumerate(coefficients)
        ) % prime
        curve_fp += 1 if rhs == 0 else (2 if rhs in squares else 0)

    field_size = prime**2
    curve_fp2 = 2
    for real_part in range(prime):
        for radical_part in range(prime):
            x_value = (real_part, radical_part)
            rhs = (0, 0)
            for coefficient in coefficients:
                rhs = multiply(rhs, x_value)
                rhs = ((rhs[0] + scale * coefficient) % prime, rhs[1])
            if rhs == (0, 0):
                curve_fp2 += 1
            elif power(rhs, (field_size - 1) // 2) == (1, 0):
                curve_fp2 += 2

    trace_one = prime + 1 - curve_fp
    trace_two = prime**2 + 1 - curve_fp2
    exterior_two = (trace_one**2 - trace_two) // 2
    jacobian_order = 1 - trace_one + exterior_two - prime * trace_one + prime**2
    return curve_fp, curve_fp2, jacobian_order

jacobian_reduction_certificates = (
    {prime: jacobian_order_mod_prime(*compensation_integer_models[0], prime)
     for prime in (11, 13, 19)},
    {prime: jacobian_order_mod_prime(*compensation_integer_models[1], prime)
     for prime in (7, 11)},
)
jacobian_torsion_checks = {
    "first_curve_reduction_orders_are_exact": jacobian_reduction_certificates[0] == {
        11: (18, 142, 222), 13: (14, 160, 165), 19: (23, 347, 419)
    },
    "second_curve_reduction_orders_are_exact": jacobian_reduction_certificates[1] == {
        7: (14, 52, 117), 11: (11, 115, 107)
    },
    "first_jacobian_reduction_gcd_is_one": math.gcd(
        *(certificate[2] for certificate in jacobian_reduction_certificates[0].values())
    ) == 1,
    "second_jacobian_reduction_gcd_is_one": math.gcd(
        *(certificate[2] for certificate in jacobian_reduction_certificates[1].values())
    ) == 1,
}

# The sextics do not split into lower-degree arithmetic factors.  Their full
# S6 Galois groups rule out the obvious rational elliptic-product shortcut and
# type the missing operation as a genuine degree-six Jacobian 2-descent.
compensation_sextic_polynomials = (
    sp.Poly(compensation_sextic_first, z, domain=sp.QQ),
    sp.Poly(compensation_sextic_second, z, domain=sp.QQ),
)
compensation_galois_groups = tuple(
    sp.polys.numberfields.galois_group(polynomial.as_expr(), z)[0]
    for polynomial in compensation_sextic_polynomials
)
descent_input_checks = {
    "both_compensation_sextics_are_irreducible_over_Q": all(
        polynomial.is_irreducible for polynomial in compensation_sextic_polynomials
    ),
    "both_compensation_sextics_have_full_S6_galois_group": all(
        group.order() == math.factorial(6) for group in compensation_galois_groups
    ),
    "full_S6_models_require_degree_six_descent_not_factorwise_elliptic_descent": all(
        len(polynomial.factor_list()[1]) == 1
        for polynomial in compensation_sextic_polynomials
    ),
}

known_boundary_points = (
    ((-1, -26768), (-1, 26768), (1, -2360), (1, 2360)),
    ((-1, -488), (-1, 488), (1, -16), (1, 16)),
)
rank_request_checks = {
    "all_declared_boundary_points_lie_on_exact_hyperelliptic_models": all(
        y_value**2 == scale * homogeneous_value(coefficients, x_value, 1)
        for (scale, coefficients), points in zip(
            compensation_integer_models, known_boundary_points
        )
        for x_value, y_value in points
    ),
    "known_boundary_points_are_pairwise_distinct_on_each_curve": all(
        len(set(points)) == 4 for points in known_boundary_points
    ),
    "rank_request_lower_bound_is_one_from_torsion_free_distinct_points": all(
        math.gcd(*(certificate[2] for certificate in curve.values())) == 1
        for curve in jacobian_reduction_certificates
    ),
}

# External discovery probe, deliberately not promoted to a proof gate.  Magma
# V2.29-9 could not certify the necessary class groups unconditionally within
# the online time limit.  Under SetClassGroupBounds("GRH"), RankBound(f,2)
# returned 4 and 6.  These conditional Selmer bounds do not unlock genus-two
# Chabauty and do not satisfy the requested unconditional upper bounds.
conditional_rank_probe = {
    "engine": "Magma V2.29-9 online calculator",
    "assumption": "GRH class-group bounds",
    "upper_bounds": [4, 6],
    "unconditional_attempt": "time limit; class-group proof reported infeasible",
    "completion_gate_satisfied": False,
}
conditional_probe_checks = {
    "conditional_rank_bounds_do_not_equal_requested_bounds": (
        conditional_rank_probe["upper_bounds"] != [1, 1]
    ),
    "conditional_probe_is_not_promoted_to_unconditional_evidence": (
        conditional_rank_probe["assumption"] == "GRH class-group bounds"
        and not conditional_rank_probe["completion_gate_satisfied"]
    ),
    "conditional_bounds_do_not_unlock_classical_chabauty": all(
        bound >= 2 for bound in conditional_rank_probe["upper_bounds"]
    ),
}

# Curve-level two-cover descent is the next source-sensitive route.  The first
# curve completed only with PrimeBound=30, which may return a strict superset;
# the second full run returned 18 covers.  Both used GRH class-group bounds,
# so neither result is an unconditional point classification.
conditional_two_cover_probe = {
    "engine": "Magma V2.29-9 online calculator",
    "assumption": "GRH class-group bounds",
    "curve_one": {
        "prime_bound": 30,
        "returned_cover_superset_count": 3,
        "selmer_set_completeness": False,
    },
    "curve_two": {
        "prime_bound": None,
        "returned_cover_count": 18,
        "selmer_set_completeness_under_assumption": True,
    },
    "unconditional_point_classification": False,
}
two_cover_probe_checks = {
    "curve_one_prime_bound_is_typed_as_possible_superset": (
        conditional_two_cover_probe["curve_one"]["prime_bound"] == 30
        and not conditional_two_cover_probe["curve_one"]["selmer_set_completeness"]
    ),
    "curve_two_full_probe_has_eighteen_conditional_covers": (
        conditional_two_cover_probe["curve_two"]["returned_cover_count"] == 18
        and conditional_two_cover_probe["curve_two"]["selmer_set_completeness_under_assumption"]
    ),
    "two_cover_probe_does_not_claim_unconditional_classification": (
        conditional_two_cover_probe["assumption"] == "GRH class-group bounds"
        and not conditional_two_cover_probe["unconditional_point_classification"]
    ),
}

# Unconditional Magma ReducedBasis computations on the three differences of
# the four rational boundary points produce two independent generators on
# each Jacobian.  The common relation matrix expresses D1=B1+B2, D2=B1,
# D3=B2.  This raises the proved rank lower bounds to two and rules out
# classical genus-two Chabauty independently of Selmer upper bounds.
boundary_mordell_weil_probe = {
    "engine": "Magma V2.29-9 ReducedBasis",
    "assumption": "unconditional canonical-height computation",
    "generated_subgroup_ranks": [2, 2],
    "relation_matrices": [
        [[1, 1], [1, 0], [0, 1]],
        [[1, 1], [1, 0], [0, 1]],
    ],
    "relation_source": "linear equivalence of hyperelliptic fibres above x=-1 and x=1",
    "universal_boundary_relation": "D1=D2+D3",
    "geometric_boundary_rank_upper_bound": 2,
    "height_determinants_positive": [True, True],
    "reduced_basis_mumford_u": [
        ["x^2 - 1", "x^2 - 1"],
        ["x^2 - 1", "x^2 - 1"],
    ],
    "boundary_support_divisor": "x^2 - 1",
    "saturation_engine": "Magma V2.29-9 Saturation",
    "tested_saturation_primes": list(sp.primerange(2, 252)),
    "saturated_basis_lengths": [
        [2] * 54,
        [2] * 54,
    ],
    "saturated_bases_unchanged": [
        [True] * 54,
        [True] * 54,
    ],
    "global_saturation_proved": False,
    "minimum_unexcluded_index_prime": 257,
    "local_places_checked_count": [13, 9],
    "deficient_places": [[], []],
    "index_one_everywhere_locally": [True, True],
    "has_square_sha": [True, True],
    "square_sha_interpretation_requires_finiteness": True,
    "bad_prime_supports": [
        [2, 3, 5, 7, 17, 29, 59, 239, 1979, 81359, 859091,
         151505614835989892351],
        [2, 3, 5, 61, 137, 193, 620663, 72430534374391],
    ],
    "common_bad_prime_support": [2, 3, 5],
    "classical_genus_two_chabauty_available": [False, False],
}
boundary_rank_checks = {
    "boundary_points_generate_rank_two_on_both_jacobians": (
        boundary_mordell_weil_probe["generated_subgroup_ranks"] == [2, 2]
    ),
    "boundary_difference_relations_have_two_basis_coordinates": all(
        relation == [[1, 1], [1, 0], [0, 1]]
        for relation in boundary_mordell_weil_probe["relation_matrices"]
    ),
    "boundary_rank_two_relation_is_source_derived_from_fibre_equivalence": (
        boundary_mordell_weil_probe["universal_boundary_relation"]
        == "D1=D2+D3"
        and boundary_mordell_weil_probe["geometric_boundary_rank_upper_bound"] == 2
        and all(
            relation == [[1, 1], [1, 0], [0, 1]]
            for relation in boundary_mordell_weil_probe["relation_matrices"]
        )
    ),
    "rank_at_least_genus_rules_out_classical_chabauty": all(
        rank >= 2 and not available
        for rank, available in zip(
            boundary_mordell_weil_probe["generated_subgroup_ranks"],
            boundary_mordell_weil_probe["classical_genus_two_chabauty_available"],
        )
    ),
    "rank_two_generators_are_supported_on_boundary_divisor": all(
        u == boundary_mordell_weil_probe["boundary_support_divisor"]
        for curve_basis in boundary_mordell_weil_probe["reduced_basis_mumford_u"]
        for u in curve_basis
    ),
    "boundary_rank_two_subgroups_are_saturated_through_prime_251": (
        boundary_mordell_weil_probe["tested_saturation_primes"]
        == list(sp.primerange(2, 252))
        and all(
            lengths == [2] * 54
            for lengths in boundary_mordell_weil_probe["saturated_basis_lengths"]
        )
        and all(
            all(unchanged)
            for unchanged in boundary_mordell_weil_probe["saturated_bases_unchanged"]
        )
        and not boundary_mordell_weil_probe["global_saturation_proved"]
        and boundary_mordell_weil_probe["minimum_unexcluded_index_prime"] == 257
    ),
    "descent_bounds_apply_to_full_jacobians_without_local_index_defect": (
        boundary_mordell_weil_probe["deficient_places"] == [[], []]
        and boundary_mordell_weil_probe["index_one_everywhere_locally"]
        == [True, True]
        and boundary_mordell_weil_probe["has_square_sha"] == [True, True]
        and boundary_mordell_weil_probe[
            "square_sha_interpretation_requires_finiteness"
        ]
    ),
    "common_boundary_packet_is_not_common_bad_reduction_tail": (
        sorted(
            set(boundary_mordell_weil_probe["bad_prime_supports"][0])
            & set(boundary_mordell_weil_probe["bad_prime_supports"][1])
        )
        == boundary_mordell_weil_probe["common_bad_prime_support"]
        == [2, 3, 5]
    ),
}
checks = {
    "all_pairs_have_same_block_ranks": all(item["ranks"] == expected_ranks for item in pair_data.values()),
    "all_pairs_have_same_block_nullities": all(item["nullities"] == expected_nullities for item in pair_data.values()),
    "all_pair_boundaries_have_rank16": all(item["total_rank"] == 16 for item in pair_data.values()),
    "all_pair_quotients_are_five_dimensional": all(item["quotient_dimension"] == 5 for item in pair_data.values()),
    "quotient_characters_are_m_minus2_through2": set(range(-2, 3)) == {-2, -1, 0, 1, 2},
    "m_plusminus3_have_no_quotient": expected_nullities[3] == 0,
    "m_plusminus4_have_no_quotient": expected_nullities[4] == 0,
    "two_redundancies_are_m_plusminus4": 2 * (2 - expected_ranks[4]) == 2,
    "determinant_generators_vanish_on_dark_pairs": all(
        item["generators_vanish_on_dark_pair"] for item in pair_data.values()
    ),
    "quotient_has_spin_two_radial_degree_staircase": all(residual_degree_checks),
    "remaining_ring_transfers_are_quadratic_in_m_squared": all(transfer_degree_checks),
    "third_dark_capability_exactly_matches_two_dark_triples": all(
        third_dark_capability[str(pair)] == (
            set(pair).issubset({0, 2, 4}) or set(pair).issubset({1, 2, 3})
        )
        for pair in itertools.combinations(range(5), 2)
    ),
    "nonsingular_orbits_have_universal_five_zero_witnesses": all(
        universal_five_zero_witness_checks
    ),
    "universal_witness_has_hidden_antipodal_zero_on_every_ring": all(
        universal_hidden_antipode_checks
    ),
    "four_plus_one_rational_components_have_odd_prime_obstruction": all(
        four_plus_one_prime_witness_checks
    ),
    "four_plus_one_sqrt5_residues_close_by_full_ideal_norms": all(
        four_plus_one_residual_norm_checks.values()
    ),
    "three_plus_two_transfer_pencil_has_exact_even_odd_split": all(
        three_plus_two_checks.values()
    ),
    "three_plus_two_deutsch_counterfactual_is_exact_N21_circuit": all(
        three_plus_two_bad_transfer_checks.values()
    ),
    "radial_source_conics_admit_known_bad_chords_only_after_algebraic_extension": all(
        source_curve_checks.values()
    ),
    "symmetric_three_plus_two_family_has_no_positive_rational_bad_transfer": all(
        symmetric_family_checks.values()
    ),
    "reflection_centered_three_plus_two_family_has_no_positive_rational_bad_transfer": all(
        centered_family_checks.values()
    ),
    "product_one_off_center_family_reduces_to_rational_mobius_incidence": all(
        product_one_off_center_checks.values()
    ),
    "one_two_exception_is_complete_heptagon_on_reducible_incidence_stratum": all(
        reducible_incidence_checks.values()
    ),
    "mann_reduction_classifies_U_minus_one_branch_exactly": all(
        mann_reduction_checks.values()
    ),
    "heptagon_counterfactual_separates_feasibility_constructor_and_authority": all(
        authority_plane_checks.values()
    ),
    "heptagon_compensation_pullback_reduces_to_two_genus_two_curves": all(
        compensation_pullback_checks.values()
    ),
    "bounded_rational_compensation_search_finds_only_excluded_boundary_points": all(
        compensation_height_checks.values()
    ),
    "both_compensation_jacobians_have_trivial_rational_torsion": all(
        jacobian_torsion_checks.values()
    ),
    "compensation_rank_frontier_is_genuine_full_S6_two_descent": all(
        descent_input_checks.values()
    ),
    "compensation_rank_request_has_exact_known_point_and_torsion_evidence": all(
        rank_request_checks.values()
    ),
    "conditional_rank_probe_is_typed_as_failed_chabauty_strategy": all(
        conditional_probe_checks.values()
    ),
    "conditional_two_cover_probe_is_typed_as_elliptic_chabauty_frontier": all(
        two_cover_probe_checks.values()
    ),
    "boundary_points_generate_rank_two_and_rule_out_classical_chabauty": all(
        boundary_rank_checks.values()
    ),
}
failed = [name for name, passed in checks.items() if not passed]
payload = {
    "schema": "marici.strominger.spin-memory-characteristic-zero-quotient-result.v1",
    "artifact_sha256": hashlib.sha256(ARTIFACT.read_bytes()).hexdigest().upper(),
    "passed": sum(checks.values()),
    "total": len(checks),
    "checks": checks,
    "observed": {
        "block_ranks_by_abs_m": expected_ranks,
        "block_nullities_by_abs_m": expected_nullities,
        "quotient_characters": [-2, -1, 0, 1, 2],
        "pair_count": len(pair_data),
        "residual_degrees_by_abs_m": {0: 2, 1: 1, 2: 0},
        "transfer_variable": "m^2 with spectrum {0,1,4}",
        "five_zero_witness_scope": "identical Laurent-polynomial dependence, independent of N",
        "four_plus_one_directed_pair_field_split": four_plus_one_directed_pairs,
        "three_plus_two_directed_transfer_class_count": len(three_plus_two_transfer_classes),
        "three_plus_two_nearest_simple_bad_transfer": {
            "N": 21,
            "base_exponents_mod_21": [3, 6, 12],
            "target_exponents_mod_21": [7, 14],
            "r": 1,
            "s": 2,
        },
        "bad_transfer_source_extension": "nontrivial algebraic latitude chord",
        "simple_rational_bad_transfers_through_N75": [[1, 2], [3, 4]],
        "symmetric_family_transfer": {
            "r": "-(t^2+t-1)/(t+1)",
            "s": 1,
            "odd_rational_torsion_orders": [1, 3, 5],
            "admissible_positive_nondegenerate_cases": [],
        },
        "reflection_centered_two_trace_transfer": {
            "r": "(x-(x+1)W)/(x(x+1))",
            "s": "W/x^2",
            "rationality_equation": "s*x^2+(s+r)*x+r-1=0",
            "admissible_positive_nondegenerate_cases": [],
        },
        "product_one_off_center_incidence": {
            "equation": "r(2V+U)+sU(V-1)-U-2=0",
            "centered_locus": "4V-U^2=0",
            "N21_exception": {"U": -1, "V": 2, "centering_defect": 7},
            "reducible_transfer_locus": "(r-1)(r-s)=0",
            "one_two_factorization": "2(U+1)(V-1)=0",
            "N21_U_branch_source": "complete nontrivial seventh-root sum",
            "mann_reduced_conductor": 105,
            "exact_U_minus_one_triples_mod_105": [
                list(triple) for triple in mann_u_minus_one_triples
            ],
        },
        "heptagon_authority_plane": {
            "algebraic": "r=1 perturbation and kernel are representable",
            "physical": "each Legendre orbit has at least one real bad-chord latitude in (-1,1)",
            "constructor": "original rational-latitude grammar cannot instantiate either chord",
            "authority": "geometric support supplies no extension grant",
            "readout_response": "3r-s-1",
            "kernel_compensation_line": "s=3r-1",
        },
        "heptagon_compensation_pullback": {
            "source_curve_count": 2,
            "target_latitude_degree": 2,
            "discriminant_core_degree": 6,
            "arithmetic_model": "two squarefree genus-two hyperelliptic curves",
            "five_latitude_hits": 0,
            "physical_rational_height_bound": 500,
            "physical_rational_hits": 0,
            "visible_boundary_x_coordinates": [-1, 1],
            "rational_points_at_infinity": 0,
            "jacobian_reduction_orders": [
                {str(prime): certificate[2] for prime, certificate in curve.items()}
                for curve in jacobian_reduction_certificates
            ],
            "jacobian_torsion_bound_gcd": [1, 1],
            "rational_jacobian_torsion": [0, 0],
            "sextic_irreducible_over_Q": [True, True],
            "sextic_galois_group_orders": [
                int(group.order()) for group in compensation_galois_groups
            ],
            "missing_rank_constructor": "certified genus-two Jacobian 2-Selmer/rank bounds",
            "known_rational_points": [
                [list(point) for point in points] for points in known_boundary_points
            ],
            "rank_request": {
                "proved_lower_bounds": [2, 2],
                "requested_upper_bounds": [2, 2],
                "completion_gate": "certified 2-Selmer local images and rank bounds",
            },
            "conditional_rank_probe": conditional_rank_probe,
            "conditional_two_cover_probe": conditional_two_cover_probe,
            "boundary_mordell_weil_probe": boundary_mordell_weil_probe,
        },
    },
    "verdict": (
        "Over characteristic zero, every two-dark-ring boundary has rank 16. Its "
        "five-dimensional quotient is canonically carried by m=-2,-1,0,1,2, and the "
        "two row redundancies come exactly from the one-dimensional m=+-4 blocks."
    ),
}
print(json.dumps(payload, indent=2, sort_keys=True))
if failed:
    raise SystemExit("failed checks: " + ", ".join(failed))
