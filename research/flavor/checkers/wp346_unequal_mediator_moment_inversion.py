"""WP346: exact three-moment inversion for an unequal two-branch mediator."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    weight, branch_a, branch_b = sp.symbols("w a b", real=True)
    moments = [sp.Integer(1)] + [
        sp.expand(weight * branch_a**order + (1 - weight) * branch_b**order)
        for order in range(1, 5)
    ]
    parameters = (weight, branch_a, branch_b)
    response = sp.Matrix([
        [sp.diff(moments[order], parameter) for parameter in parameters]
        for order in range(1, 4)
    ])
    determinant = sp.factor(response.det())
    variance = sp.factor(moments[2] - moments[1] ** 2)
    support_sum = sp.factor((moments[3] - moments[1] * moments[2]) / variance)
    support_product = sp.factor(support_sum * moments[1] - moments[2])
    fourth_residual = sp.factor(moments[4] - support_sum * moments[3] + support_product * moments[2])
    reconstructed_weight = sp.factor((moments[1] - branch_b) / (branch_a - branch_b))
    discriminant = sp.factor(support_sum**2 - 4 * support_product)
    checks = {
        "three_moment_jacobian_has_expected_factorization": sp.simplify(determinant - weight * (1 - weight) * (branch_a - branch_b) ** 4) == 0,
        "variance_detects_nontrivial_mixture": sp.simplify(variance - weight * (1 - weight) * (branch_a - branch_b) ** 2) == 0,
        "support_sum_is_reconstructed": sp.simplify(support_sum - branch_a - branch_b) == 0,
        "support_product_is_reconstructed": sp.simplify(support_product - branch_a * branch_b) == 0,
        "support_discriminant_is_squared_gap": sp.simplify(discriminant - (branch_a - branch_b) ** 2) == 0,
        "labelled_weight_is_reconstructed_after_root_ordering": sp.simplify(reconstructed_weight - weight) == 0,
        "fourth_moment_obeys_two_point_recurrence": fourth_residual == 0,
        "branch_exchange_preserves_all_moments": all(sp.simplify(moment.subs({weight: 1 - weight, branch_a: branch_b, branch_b: branch_a}, simultaneous=True) - moment) == 0 for moment in moments),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP346",
        "admitted_state_domain": "two distinct mediator probabilities a,b with mixture weight 0<w<1, quotiented by branch exchange (w,a,b)~(1-w,b,a)",
        "faithful_quotient_coordinate": "the unordered weighted two-point probability measure",
        "candidate_probe_family": "calibrated normalized coincidence moments u1,u2,u3; u4 retained as a two-point-grammar control",
        "three_moment_jacobian_determinant": str(determinant),
        "variance": str(variance),
        "support_sum_inverse": "S=(u3-u1*u2)/(u2-u1^2)",
        "support_product_inverse": "P=S*u1-u2",
        "support_polynomial": "z^2-S*z+P",
        "weight_inverse_after_root_ordering": "w=(u1-b)/(a-b)",
        "fourth_order_identity": "u4=S*u3-P*u2",
        "contextual_partition": "the first three moments have singleton fibers on the branch-exchange quotient away from zero weight and branch collision",
        "classification": "three moments generically identify the unequal two-branch mediator quotient; fourth order tests the frozen two-point grammar and none of these probes selects its parameters",
        "smallest_exact_falsifier": "the determinant vanishes at w=0, w=1, or a=b, where an unused or collided branch becomes unidentifiable",
        "reference_rule": "choosing an ordering of the two recovered roots labels mediator branches and changes to a branch-stabilized relational experiment",
        "remaining_physical_instrument_gate": "calibrate moments through order four with contrast-conditioned errors and show that one shared two-state mediator, rather than a broader mixing law, generated the domains",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp346_unequal_mediator_moment_inversion.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
