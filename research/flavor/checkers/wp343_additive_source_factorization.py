"""WP343: exact iid factorization theorem for a strictly additive domain source."""

import itertools
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    size = 6
    weight_zero, weight_one = sp.symbols("w0 w1", real=True, positive=True)
    words = list(itertools.product((0, 1), repeat=size))
    partition = sp.expand(sum(weight_zero ** (size - sum(word)) * weight_one ** sum(word) for word in words))
    expected_partition = sp.expand((weight_zero + weight_one) ** size)
    probability_one = sp.simplify(weight_one / (weight_zero + weight_one))
    law = {
        word: sp.simplify(weight_zero ** (size - sum(word)) * weight_one ** sum(word) / partition)
        for word in words
    }
    subset_moments = {}
    for order in range(size + 1):
        subset = tuple(range(order))
        subset_moments[order] = sp.simplify(
            sum(probability * sp.prod(word[index] for index in subset) for word, probability in law.items())
        )
    odd_probability = sp.simplify(sum(probability for word, probability in law.items() if sum(word) % 2 == 1))
    odd_closed_form = sp.simplify((1 - (1 - 2 * probability_one) ** size) / 2)
    fair_law = {word: sp.simplify(probability.subs({weight_zero: 1, weight_one: 1})) for word, probability in law.items()}
    checks = {
        "partition_function_factorizes": sp.simplify(partition - expected_partition) == 0,
        "law_is_normalized": sp.simplify(sum(law.values())) == 1,
        "all_subset_moments_are_iid_powers": all(sp.simplify(subset_moments[order] - probability_one**order) == 0 for order in range(size + 1)),
        "odd_parity_probability_has_product_form": sp.simplify(odd_probability - odd_closed_form) == 0,
        "fair_source_has_full_support": all(probability == sp.Rational(1, 64) for probability in fair_law.values()),
        "fair_source_is_not_odd_parity_law": fair_law[(0, 0, 0, 0, 0, 0)] != 0,
        "strict_positive_weights_exclude_zero_support_words": all(probability.is_positive for probability in law.values()),
        "first_moment_recovers_weight_ratio": sp.simplify(probability_one / (1 - probability_one) - weight_one / weight_zero) == 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP343",
        "admitted_state_domain": "six binary domains with a strictly additive identical one-site source action, positive local weights w0,w1, and no shared latent field or global constraint",
        "faithful_quotient_coordinate": "the iid Bernoulli probability p=w1/(w0+w1)",
        "source_operation": "normalized product Gibbs preparation with weight proportional to product_i w_(x_i)",
        "partition_function": str(sp.factor(partition)),
        "single_site_probability": str(probability_one),
        "subset_moments": {str(order): str(value) for order, value in subset_moments.items()},
        "odd_parity_probability": str(sp.factor(odd_probability)),
        "contextual_partition": "within the strict additive grammar the first moment has singleton p-fibers and all higher moments are forced powers; parity-constrained laws are outside the source domain",
        "classification": "a conditional source theorem authorizing first-order sufficiency, not a numerical selector of p and not stable under unmodelled latent-variable marginalization",
        "smallest_exact_falsifier": "any observed connected coincidence u_j-p^j different from zero falsifies the strict additive no-latent source grammar",
        "remaining_physical_instrument_gate": "derive the additive action and absence of shared mediators or constraints from flavor dynamics, then test at least one calibrated connected coincidence rather than assuming factorization from notation",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp343_additive_source_factorization.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
