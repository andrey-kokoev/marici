"""Exact spectral residues and conditional quark-width sum rules for WP509."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]
wp508 = json.loads(
    (root / "results" / "wp508_canonical_heavy_gauge_poles.json").read_text(
        encoding="utf-8"
    )
)

z = sp.symbols("z")
g_f, g_p, g_e, mu, s, a, b = sp.symbols(
    "g_F g_P g_E mu s a b", positive=True
)
symbols = {
    "z": z,
    "g_F": g_f,
    "g_P": g_p,
    "g_E": g_e,
    "mu": mu,
    "s": s,
    "a": a,
    "b": b,
}
q = 3 * g_f**2 * mu**2


def expression(value):
    return sp.sympify(value, locals=symbols)


packets = []
factor_checks = []
leading_checks = []
quintet_rank_checks = []
quintet_normalization_checks = []
cubic_rank_checks = []
numeric_positive_checks = []

substitution = {
    g_f: sp.Rational(2, 3),
    g_p: sp.Rational(3, 5),
    g_e: sp.Rational(4, 7),
    mu: sp.Rational(5, 4),
    s: sp.Rational(7, 6),
    a: sp.Rational(9, 8),
    b: sp.Rational(11, 10),
}

for component in wp508["heavy_gauge_poles"]["components"]:
    if component["size"] != 4:
        continue
    cubic = sp.Poly(expression(component["cubic_characteristic_polynomial"]), z)
    resolvent = component["flavor_current_resolvent"]
    denominator = sp.Poly(expression(resolvent["denominator"]), z)
    numerator = sp.Matrix(
        [[expression(value) for value in row] for row in resolvent["numerator_matrix"]]
    )

    factor_checks.append(
        sp.Poly(denominator.as_expr() - (z - q) * cubic.as_expr(), z).is_zero
    )
    leading = numerator.applyfunc(lambda value: sp.Poly(value, z).coeff_monomial(z**3))
    leading_checks.append(leading == g_f**2 * sp.eye(2))

    c_at_q = sp.factor(cubic.as_expr().subs(z, q))
    quintet_residue = numerator.applyfunc(
        lambda value: sp.factor(value.subs(z, q) / c_at_q)
    )
    quintet_rank_checks.append(sp.factor(quintet_residue.det()) == 0)
    quintet_normalization_checks.append(
        (quintet_residue * quintet_residue - g_f**2 * quintet_residue).applyfunc(
            sp.factor
        )
        == sp.zeros(2)
    )

    determinant_remainder = sp.rem(
        sp.Poly(sp.factor(numerator.det()), z), cubic
    ).as_expr()
    cubic_rank_checks.append(sp.factor(determinant_remainder) == 0)

    cubic_numeric = sp.Poly(cubic.as_expr().subs(substitution), z)
    numerator_numeric = numerator.subs(substitution)
    q_numeric = q.subs(substitution)
    roots = sp.nroots(cubic_numeric.as_expr(), n=30, maxsteps=200)
    sector_positive = len(roots) == 3
    numeric_residues = []
    for pole in roots:
        pole_complex = complex(pole)
        sector_positive = sector_positive and abs(pole_complex.imag) < 1e-20
        pole_real = sp.re(pole)
        derivative = sp.diff(cubic_numeric.as_expr(), z).subs(z, pole_real)
        residue = numerator_numeric.subs(z, pole_real) / (
            (pole_real - q_numeric) * derivative
        )
        residue_eval = residue.evalf(24)
        trace_value = float(sp.re(sp.trace(residue_eval)))
        determinant_value = abs(complex(residue_eval.det()))
        sector_positive = (
            sector_positive
            and trace_value > 0
            and determinant_value < 1e-18
            and float(sp.re(residue_eval[0, 0])) >= -1e-18
            and float(sp.re(residue_eval[1, 1])) >= -1e-18
        )
        numeric_residues.append(
            {
                "pole_squared": str(sp.N(pole_real, 16)),
                "trace_residue": str(sp.N(sp.trace(residue_eval), 16)),
                "determinant_residue": str(sp.N(residue_eval.det(), 8)),
            }
        )
    numeric_positive_checks.append(bool(sector_positive))

    packets.append(
        {
            "generators": component["generators"],
            "cubic": str(cubic.as_expr()),
            "simple_spectrum_domain": "C_r has three distinct positive roots and C_r(Q) is nonzero",
            "quintet_residue_matrix": [
                [str(value) for value in row] for row in quintet_residue.tolist()
            ],
            "cubic_root_residue": "R_r(rho)=N_r(rho)/((rho-Q) C_r'(rho))",
            "cubic_residue_sum_matrix": [
                [str(value) for value in row]
                for row in (g_f**2 * sp.eye(2) - quintet_residue).tolist()
            ],
            "total_residue_sum": "R_Q+sum_{C_r(rho)=0}R_r(rho)=g_F^2 I_2",
            "six_quark_fractional_width": "Gamma_q(rho)/M_rho=tr(R_r(rho))/(4 pi)",
            "six_quark_width_sum": "Gamma_q(Q)/M_Q+sum_rho Gamma_q(rho)/M_rho=g_F^2/(2 pi)",
            "positive_witness": numeric_residues,
        }
    )

checks = {
    "wp508_dependency_passed": bool(wp508["passed"]),
    "three_mixed_sectors_are_present": len(packets) == 3,
    "each_denominator_is_quintet_times_cubic": all(factor_checks),
    "large_z_current_normalization_is_gf_squared_identity": all(leading_checks),
    "each_embedded_quintet_residue_has_rank_one": all(quintet_rank_checks),
    "each_embedded_quintet_residue_is_a_scaled_projector": all(
        quintet_normalization_checks
    ),
    "each_cubic_root_residue_has_rank_at_most_one": all(cubic_rank_checks),
    "generic_positive_witness_has_three_positive_rank_one_cubic_residues": all(
        numeric_positive_checks
    ),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP509",
    "domain": "WP508 positive source domain restricted to simple positive heavy poles; six effectively massless quarks for the conditional partial-width statement",
    "source_frozen_spectral_packet": packets,
    "classification": "The source action freezes exact pole-residue functionals and six-quark partial-width sum rules conditionally on its parameters. It does not select their numerical values or establish total widths.",
    "selector": False,
    "rigidifier": bool(len(packets) == 3 and all(cubic_rank_checks)),
    "instrument": None,
    "smallest_exact_falsifier": "At C_r(Q)=0 or discriminant(C_r)=0, the simple-pole residue formula fails and must be replaced by a degenerate spectral projector; opening any nonquark channel falsifies identification of the quark partial width with the total width.",
    "remaining_gate": "Select the dimensionless source coefficients, derive all physical scalar and messenger thresholds in the same vacuum, and attach a calibrated flavor-current pole instrument before assigning numerical residues or total widths.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp509_spectral_residue_width_sum_rules.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
