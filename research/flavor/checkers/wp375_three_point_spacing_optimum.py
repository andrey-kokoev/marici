"""WP375: exact finite D-optimal spacing on the equal mass-width benchmark."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    step = sp.symbols("d", positive=True)
    determinant_magnitude = (
        step**3 * (3 * step**3 + 11 * step**2 + 12 * step + 6)
        / ((step**2 + 2 * step + 2)**2 * (2 * step**2 + 2 * step + 1)**2)
    )
    derivative_numerator = sp.factor(
        sp.together(sp.diff(determinant_magnitude, step)).as_numer_denom()[0]
    )
    stationarity_polynomial = (
        12 * step**7 + 66 * step**6 + 108 * step**5 + 33 * step**4
        - 126 * step**3 - 200 * step**2 - 132 * step - 36
    )
    coefficients = sp.Poly(stationarity_polynomial, step).all_coeffs()
    signs = [sp.sign(coefficient) for coefficient in coefficients]
    sign_changes = sum(1 for left, right in zip(signs, signs[1:]) if left != right)
    numerical_roots = sp.nroots(stationarity_polynomial, maxsteps=200)
    positive_real_roots = [
        float(sp.re(root)) for root in numerical_roots
        if abs(float(sp.im(root))) < 1e-12 and float(sp.re(root)) > 0
    ]

    checks = {
        "derivative_numerator_has_declared_factorization": sp.expand(
            derivative_numerator + step**2 * stationarity_polynomial
        ) == 0,
        "stationarity_polynomial_has_one_descartes_sign_change": sign_changes == 1,
        "lower_bracket_is_negative": stationarity_polynomial.subs(step, 1) == -275,
        "upper_bracket_is_positive": stationarity_polynomial.subs(step, sp.Rational(3, 2)) == sp.Rational(3339, 4),
        "collapsed_spacing_limit_zero": sp.limit(determinant_magnitude, step, 0, dir="+") == 0,
        "large_spacing_limit_zero": sp.limit(determinant_magnitude, step, sp.oo) == 0,
        "determinant_is_positive_at_unit_spacing": determinant_magnitude.subs(step, 1) > 0,
        "numerical_locator_has_one_positive_real_root": len(positive_real_roots) == 1,
        "numerical_locator_lies_in_exact_bracket": 1 < positive_real_roots[0] < 1.5,
        "deliberate_monotonic_improvement_claim_fails": sp.limit(determinant_magnitude, step, sp.oo) < determinant_magnitude.subs(step, 1),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    result = {
        "work_package": "WP375",
        "admitted_state_domain": "WP374 three-point equally spaced scan at the frozen dimensionless benchmark L=Omega=1 with setting-independent covariance and cost",
        "faithful_quotient_coordinate": "the local six-parameter threshold packet from WP374; determinant magnitude is a robustness measure, not a new quotient",
        "source_authorized_probe_family": "predeclared equally spaced three-setting scans compared by exact reduced Jacobian determinant",
        "contextual_partition": "all d>0 remain rank-faithful, but information volume vanishes at both spacing boundaries and has one interior maximum",
        "classification": "conditional D-optimal instrument design on a frozen benchmark; neither source selector nor universal scan prescription",
        "determinant_magnitude": str(determinant_magnitude),
        "derivative_numerator": str(derivative_numerator),
        "stationarity_polynomial": str(stationarity_polynomial),
        "exact_root_bracket": ["1", "3/2"],
        "positive_root_locator": positive_real_roots[0],
        "determinant_at_locator": float(determinant_magnitude.subs(step, positive_real_roots[0])),
        "smallest_exact_falsifier": "lim_{d->infinity} D(d)=0, so increasing scan separation indefinitely does not improve conditioning",
        "remaining_physical_instrument_gate": "recompute the design with measured width ratio, count-rate covariance, control cost, and background model frozen independently of flavor outcomes",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp375_three_point_spacing_optimum.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
