"""WP267: exact renormalization-relative curvature audit for a one-loop selector."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    y, x = sp.symbols("y x", positive=True)
    amplitude, slope, mass2, mu2 = sp.symbols("amplitude slope mass2 mu2", positive=True)
    subtraction = sp.symbols("subtraction", real=True)

    loop_function = amplitude * y**2 * (sp.log(y / mu2) - subtraction)
    mass_function = mass2 + slope * x
    loop_potential = loop_function.subs(y, mass_function)
    curvature = sp.simplify(sp.diff(loop_potential, x, 2).subs(x, 0))

    log_ratio = sp.symbols("log_ratio", real=True)
    curvature_expected = amplitude * slope**2 * (2 * sp.log(mass2 / mu2) - 2 * subtraction + 3)
    curvature_residual = sp.expand_log(curvature - curvature_expected, force=True).simplify()
    curvature_log_form = amplitude * slope**2 * (2 * log_ratio - 2 * subtraction + 3)
    conventional_subtraction = sp.Rational(3, 2)
    curvature_conventional = sp.simplify(curvature_log_form.subs(subtraction, conventional_subtraction))

    positive_packet = sp.simplify(curvature_conventional.subs(log_ratio, 1))
    zero_packet = sp.simplify(curvature_conventional.subs(log_ratio, 0))
    negative_packet = sp.simplify(curvature_conventional.subs(log_ratio, -1))

    # A local counterterm c2*x^2 contributes curvature 2*c2 and is required to
    # make the total matching condition scale-independent.
    counterterm = sp.symbols("counterterm", real=True)
    total_curvature = sp.simplify(curvature_log_form + 2 * counterterm)
    counterterm_for_target = sp.solve(sp.Eq(total_curvature, sp.symbols("target_curvature")), counterterm)[0]

    checks = {
        "one_loop_curvature_formula_exact": curvature_residual == 0,
        "conventional_packet_positive_at_log_plus_one": positive_packet == 2 * amplitude * slope**2,
        "conventional_packet_zero_at_matching_log_zero": zero_packet == 0,
        "conventional_packet_negative_at_log_minus_one": negative_packet == -2 * amplitude * slope**2,
        "loop_curvature_sign_not_scale_invariant": positive_packet > 0 and negative_packet < 0,
        "counterterm_enters_total_curvature_independently": sp.diff(total_curvature, counterterm) == 2,
        "target_curvature_fixes_counterterm_boundary": counterterm_for_target.has(sp.symbols("target_curvature")),
        "deliberate_loop_only_positive_selector_claim_fails": zero_packet == 0 and negative_packet < 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP267",
        "theorem_domain": "one-loop real effective-potential contribution A*m(x)^4*(log(m(x)^2/mu^2)-c) with m(x)^2=M^2+k*x",
        "loop_curvature_exact": str(curvature_log_form),
        "subtraction_packet": "c=3/2",
        "hostile_log_packets": [
            {"log_M2_over_mu2": "1", "curvature": str(positive_packet)},
            {"log_M2_over_mu2": "0", "curvature": str(zero_packet)},
            {"log_M2_over_mu2": "-1", "curvature": str(negative_packet)},
        ],
        "total_curvature_with_counterterm": str(total_curvature),
        "counterterm_matching_relation": str(counterterm_for_target),
        "classification": "a loop determinant can contribute positive curvature in a chosen matching presentation, but loop-only sign and magnitude are renormalization-relative and do not define a source-authorized numerical selector",
        "smallest_exact_falsifier": "with c=3/2 the same loop grammar gives curvature +2*A*k^2, 0, or -2*A*k^2 at log(M^2/mu^2)=1, 0, or -1",
        "remaining_authority_gate": "derive the renormalized x^2 coefficient and its boundary condition from a complete UV matching packet, including field content, statistics, thresholds, scheme transport, and counterterms before flavor readout",
        "scope_limit": "does not deny that a complete UV theory can predict a renormalized coefficient; it denies authority to the isolated loop term or a scale choice",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp267_one_loop_curvature_authority.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
