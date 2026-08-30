"""Exact strict transform of the q_G12 residue surface at physical X1-soft."""

from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    x, p, kappa, a, b, xi = sp.symbols("x p kappa a b xi")
    y = p + x * kappa / 2
    z = p - x * kappa / 2
    e = x + y + z
    x2, y2, z2, e2 = x**2, y**2, z**2, e**2
    h = x2 + y2 - z2

    f = x2 * a**4 - h * a**2 * b**2 + y2 * b**4
    g_a = h * (x2 + e2) - 2 * x2 * (y2 + e2)
    g_b = h * (y2 + e2) - 2 * y2 * (x2 + e2)
    h0 = z2 * ((e2 - y2) * (e2 - x2) + e2 * z2)
    k0 = sp.expand(f + g_a * a**2 + g_b * b**2 + h0)

    b_soft = e + x * xi
    pulled = sp.factor(sp.expand(k0.subs(b, b_soft)))
    exceptional = sp.factor(sp.cancel(pulled / x**2).subs(x, 0))
    remainder = sp.factor(sp.expand(pulled - x**2 * exceptional))

    # The residue-surface measure is da^db/sqrt(K0).  At fixed external
    # energies db=x dxi, hence the normal Jacobian cancels sqrt(x^2).
    measure_ratio_squared = sp.factor(
        sp.cancel(x**2 / pulled) * exceptional
    )
    measure_limit = sp.simplify(measure_ratio_squared.subs(x, 0))

    # Entry 2361's raw quotient pivots are represented by 1,a,a^2,a^3.
    # Their pullbacks remain distinct polynomial numerators on the strict
    # transform before any physical integration functional is chosen.
    quotient = [sp.Integer(1), a, a**2, a**3]
    coefficient_matrix = sp.Matrix([
        [sp.expand(poly).coeff(a, degree) for poly in quotient]
        for degree in range(4)
    ])

    # Exceptional branch support, typed as a quadratic in A=a^2.
    A = sp.symbols("A")
    exceptional_A = sp.Poly(sp.expand(exceptional.subs(a**2, A)), A)
    branch_discriminant = sp.factor(sp.discriminant(exceptional_A.as_expr(), A))
    expected_discriminant = 64 * p**4 * (1 - kappa**2) * (1 - xi**2)

    q_g1 = x * (xi + 1)
    q_g2 = a - p + x * (kappa / 2 - 1)
    q_g3 = a + 3 * p + x * (1 + xi - kappa / 2)
    q_g23 = 2 * p + x * xi
    q_g31 = a - p - x * kappa / 2
    source_numerator = sp.expand(q_g23 + q_g31)
    normalized_source = sp.factor(sp.cancel(
        x * source_numerator / (q_g1 * q_g2 * q_g3 * q_g23 * q_g31)
    ).subs(x, 0))
    expected_source = (a + p) / (
        2 * p * (xi + 1) * (a - p) ** 2 * (a + 3 * p)
    )

    checks = {
        "soft_order_at_least_two": sp.expand(pulled.subs(x, 0)) == 0
        and sp.expand(sp.diff(pulled, x).subs(x, 0)) == 0,
        "exceptional_kernel_nonzero": exceptional != 0,
        "measure_jacobian_cancels_soft_square_root": measure_limit == 1,
        "four_quotient_numerators_remain_independent": coefficient_matrix.det() != 0,
        "exceptional_branch_discriminant_has_only_existing_endpoints": sp.expand(
            branch_discriminant - expected_discriminant
        ) == 0,
        "marked_collision_is_kappa_plus_endpoint": sp.expand(
            (q_g2 - q_g31) / x - (kappa - 1)
        ) == 0,
        "normalized_source_form_exact": sp.factor(
            normalized_source - expected_source
        ) == 0,
    }
    if not all(checks.values()):
        raise AssertionError({
            "failed": {name: value for name, value in checks.items() if not value},
            "order0": str(sp.factor(pulled.subs(x, 0))),
            "order1": str(sp.factor(sp.diff(pulled, x).subs(x, 0))),
            "pulled": str(pulled),
        })

    print(json.dumps({
        "schema": "marici.benincasa.x1-soft-physical-strict-transform.v1",
        "source_kernel": "q_G12-residue Cayley-Menger K0",
        "weighted_chart": "b=E+X1*xi",
        "soft_order": 2,
        "exceptional_kernel": str(exceptional),
        "pulled_kernel_factorization": str(pulled),
        "higher_normal_remainder_over_x3": str(sp.factor(sp.cancel(remainder / x**3))),
        "measure_transform": (
            "da^db/sqrt(K0) = da^(x dxi)/sqrt(x^2*K_exc+...) "
            "and has unit leading ratio on the chosen positive sheet"
        ),
        "quotient_numerator_basis": ["1", "a", "a^2", "a^3"],
        "quotient_pullback_polynomial_rank": int(coefficient_matrix.rank()),
        "exceptional_branch_discriminant_in_a_squared": str(branch_discriminant),
        "exceptional_branch_support": ["kappa=1", "kappa=-1", "xi=1", "xi=-1"],
        "strict_transform_walls": {
            "q_g1_over_x": "xi+1",
            "q_g2": str(q_g2),
            "q_g3": str(q_g3),
            "q_g23": str(q_g23),
            "q_g31": str(q_g31),
            "q_g2_minus_q_g31_over_x": "kappa-1",
        },
        "source_x_valuation_after_measure_cancellation": -1,
        "normalized_exceptional_source_rational_factor": str(normalized_source),
        "checks": checks,
        "status": "finite_exceptional_bulk_period_exists_and_retains_four_raw_quotient_numerators",
        "scope": (
            "algebraic strict transform and numerator independence only; "
            "no claim that the four resulting periods are independent or physically nonzero"
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
