"""WP344: exact shared-latent obstruction to marginal domain factorization."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    center, displacement = sp.symbols("pbar d", real=True, positive=True)
    p_minus = center - displacement
    p_plus = center + displacement
    first = sp.simplify((p_minus + p_plus) / 2)
    second = sp.simplify((p_minus**2 + p_plus**2) / 2)
    third = sp.simplify((p_minus**3 + p_plus**3) / 2)
    connected_second = sp.simplify(second - first**2)
    product_second = sp.simplify(first**2)
    product_third = sp.simplify(first**3)
    displacement_squared_inverse = sp.simplify(second - first**2)
    checks = {
        "marginal_first_moment_equals_center": first == center,
        "shared_latent_second_moment_contains_variance": second == center**2 + displacement**2,
        "connected_pair_coincidence_is_d_squared": connected_second == displacement**2,
        "third_moment_contains_latent_correction": sp.simplify(third - center**3 - 3 * center * displacement**2) == 0,
        "product_model_has_same_first_moment": first == center,
        "product_model_differs_at_second_order": sp.simplify(second - product_second) == displacement**2,
        "product_model_differs_at_third_order": sp.simplify(third - product_third) == 3 * center * displacement**2,
        "zero_displacement_recovers_factorization_through_third": second.subs(displacement, 0) == center**2 and third.subs(displacement, 0) == center**3,
        "second_order_identifies_latent_variance_not_sign": displacement_squared_inverse == displacement**2,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP344",
        "admitted_state_domain": "six domains conditionally iid given one shared binary mediator selecting probabilities pbar-d and pbar+d with equal weights, restricted by 0<d<min(pbar,1-pbar)",
        "faithful_quotient_coordinate": "the marginal coincidence hierarchy after the shared mediator is unobserved",
        "source_operation": "draw one common mediator branch, then prepare all domains independently conditional on that branch",
        "conditional_probabilities": [str(p_minus), str(p_plus)],
        "marginal_first_moment": str(first),
        "marginal_second_moment": str(second),
        "connected_second_moment": str(connected_second),
        "marginal_third_moment": str(third),
        "contextual_partition": "first order merges the shared-latent mixture with the product law at pbar; second order detects d^2 but still identifies opposite mediator displacements",
        "classification": "a source-generated common-cause obstruction to WP343 factorization; conditional independence does not imply marginal independence after forgetting the mediator",
        "smallest_exact_falsifier": "the latent mixture and product law have identical first moment pbar but second moments pbar^2+d^2 and pbar^2",
        "remaining_physical_instrument_gate": "measure a calibrated connected pair coincidence or directly resolve the mediator branch; then test whether the mediator is shared across the same domains and freeze-out history",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp344_shared_latent_mediator.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
