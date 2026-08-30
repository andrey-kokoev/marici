"""WP376: exact unique scan-spacing optimum for every positive width ratio."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    spacing, ratio = sp.symbols("h r", positive=True)
    positive_polynomial = (
        3 + 12 * spacing + 6 * ratio**2 + 15 * spacing**2
        + 12 * ratio**2 * spacing + 6 * spacing**3
        + 3 * ratio**4 + 7 * ratio**2 * spacing**2
    )
    determinant_magnitude = (
        8 * ratio * spacing**3 * positive_polynomial
        / (
            (1 + ratio**2)**2
            * ((1 + spacing)**2 + ratio**2)**2
            * ((1 + 2 * spacing)**2 + ratio**2)**2
        )
    )
    stationarity_polynomial = (
        48 * spacing**7
        + (84 * ratio**2 + 180) * spacing**6
        + (216 * ratio**2 + 216) * spacing**5
        + (25 * ratio**4 + 98 * ratio**2 + 9) * spacing**4
        - (54 * ratio**4 + 252 * ratio**2 + 198) * spacing**3
        - (20 * ratio**6 + 220 * ratio**4 + 380 * ratio**2 + 180) * spacing**2
        - (66 * ratio**6 + 198 * ratio**4 + 198 * ratio**2 + 66) * spacing
        - (9 * ratio**8 + 36 * ratio**6 + 54 * ratio**4 + 36 * ratio**2 + 9)
    )
    derivative_numerator = sp.factor(
        sp.together(sp.diff(determinant_magnitude, spacing)).as_numer_denom()[0]
    )
    coefficients = sp.Poly(stationarity_polynomial, spacing).all_coeffs()
    coefficient_signs = [sp.sign(coefficient) for coefficient in coefficients]
    sign_changes = sum(
        1 for left, right in zip(coefficient_signs, coefficient_signs[1:])
        if left != right
    )

    wp375_polynomial = (
        12 * spacing**7 + 66 * spacing**6 + 108 * spacing**5
        + 33 * spacing**4 - 126 * spacing**3 - 200 * spacing**2
        - 132 * spacing - 36
    )
    sample_ratios = [sp.Rational(1, 2), sp.Integer(1), sp.Integer(2)]
    root_locators = {}
    for sample_ratio in sample_ratios:
        roots = sp.nroots(stationarity_polynomial.subs(ratio, sample_ratio), maxsteps=200)
        positive_roots = [
            float(sp.re(root)) for root in roots
            if abs(float(sp.im(root))) < 1e-12 and float(sp.re(root)) > 0
        ]
        root_locators[str(sample_ratio)] = positive_roots

    checks = {
        "derivative_has_declared_stationarity_factor": sp.simplify(
            derivative_numerator + 8 * ratio * spacing**2 * stationarity_polynomial
        ) == 0,
        "four_leading_coefficients_are_positive": all(coefficient.is_positive for coefficient in coefficients[:4]),
        "four_trailing_coefficients_are_negative": all(coefficient.is_negative for coefficient in coefficients[4:]),
        "descartes_sign_change_count_is_one": sign_changes == 1,
        "stationarity_polynomial_is_negative_at_zero": stationarity_polynomial.subs(spacing, 0).is_negative,
        "stationarity_polynomial_has_positive_leading_coefficient": coefficients[0].is_positive,
        "collapsed_spacing_limit_zero": sp.limit(determinant_magnitude, spacing, 0, dir="+") == 0,
        "large_spacing_limit_zero": sp.limit(determinant_magnitude, spacing, sp.oo) == 0,
        "ratio_one_recovers_wp375_polynomial": sp.expand(
            stationarity_polynomial.subs(ratio, 1) - 4 * wp375_polynomial
        ) == 0,
        "sample_locators_each_have_one_positive_root": all(
            len(roots) == 1 for roots in root_locators.values()
        ),
        "sample_optimum_moves_with_width_ratio": (
            root_locators["1/2"][0] < root_locators["1"][0] < root_locators["2"][0]
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    result = {
        "work_package": "WP376",
        "admitted_state_domain": "positive dimensionless width ratio r=Omega/L and spacing h=d/L under WP375's constant-covariance and equal-cost design assumptions",
        "faithful_quotient_coordinate": "the WP374 local threshold packet; h is an instrument-design coordinate calibrated by source ratio r",
        "source_authorized_probe_family": "three equally spaced scans whose spacing is chosen from independently measured pole mass and width",
        "contextual_partition": "for each r>0 all h>0 remain rank-faithful, with exactly one determinant-maximizing h_star(r)",
        "classification": "source-calibrated unique D-optimal spacing law under frozen design assumptions; not a flavor selector",
        "determinant_magnitude": str(determinant_magnitude),
        "stationarity_polynomial": str(stationarity_polynomial),
        "coefficient_signs": [str(sign) for sign in coefficient_signs],
        "root_locators": root_locators,
        "scaling_law": "d_star=L*h_star(Omega/L)",
        "smallest_exact_falsifier": "more than one positive root of Q_r for any r>0; excluded here by the single coefficient sign change plus endpoint signs",
        "remaining_physical_instrument_gate": "freeze measured r, covariance, scan cost, and background support before applying the root law; recompute if those inputs change",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp376_width_ratio_scan_optimum.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
