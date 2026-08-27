import itertools
import json
from fractions import Fraction as F
from pathlib import Path


patterns = tuple(itertools.product((0, 1), repeat=3))
p = F(1, 10)


def independent_probability(pattern):
    errors = sum(pattern)
    return p**errors * (1 - p) ** (3 - errors)


independent = {pattern: independent_probability(pattern) for pattern in patterns}
common_mode = {pattern: F(0) for pattern in patterns}
common_mode[(0, 0, 0)] = F(9, 10)
common_mode[(1, 1, 1)] = F(1, 10)
exclusive = {pattern: F(0) for pattern in patterns}
exclusive[(0, 0, 0)] = F(7, 10)
exclusive[(1, 0, 0)] = F(1, 10)
exclusive[(0, 1, 0)] = F(1, 10)
exclusive[(0, 0, 1)] = F(1, 10)


def marginal(distribution, index):
    return sum(
        probability
        for pattern, probability in distribution.items()
        if pattern[index]
    )


def majority_error(distribution):
    return sum(
        probability
        for pattern, probability in distribution.items()
        if sum(pattern) >= 2
    )


def pair_error(distribution, left, right):
    return sum(
        probability
        for pattern, probability in distribution.items()
        if pattern[left] and pattern[right]
    )


def all_agree(distribution):
    return distribution[(0, 0, 0)] + distribution[(1, 1, 1)]


models = {
    "independent": independent,
    "common_mode": common_mode,
    "exclusive": exclusive,
}
marginals = {
    name: tuple(marginal(distribution, index) for index in range(3))
    for name, distribution in models.items()
}
majority_errors = {
    name: majority_error(distribution) for name, distribution in models.items()
}
pair_errors = {
    name: pair_error(distribution, 0, 1) for name, distribution in models.items()
}
agreement = {
    name: all_agree(distribution) for name, distribution in models.items()
}

checks = {
    "all_distributions_normalize": all(
        sum(distribution.values(), F(0)) == 1 for distribution in models.values()
    ),
    "all_copy_marginals_equal_one_tenth": all(
        values == (p, p, p) for values in marginals.values()
    ),
    "independent_majority_error_is_seven_over_250": majority_errors[
        "independent"
    ]
    == F(7, 250),
    "common_mode_majority_error_is_one_tenth": majority_errors["common_mode"]
    == F(1, 10),
    "exclusive_majority_error_is_zero": majority_errors["exclusive"] == 0,
    "equal_marginals_do_not_determine_majority_reliability": len(
        set(majority_errors.values())
    )
    == 3,
    "pair_coincidences_distinguish_the_models": pair_errors
    == {"independent": F(1, 100), "common_mode": F(1, 10), "exclusive": F(0)},
    "common_mode_has_perfect_inter_copy_agreement": agreement["common_mode"]
    == 1,
    "perfect_agreement_does_not_imply_correct_majority": agreement["common_mode"]
    == 1
    and majority_errors["common_mode"] > 0,
}

result = {
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "marginal_error_rates": {
        name: [str(value) for value in values] for name, values in marginals.items()
    },
    "majority_error_rates": {
        name: str(value) for name, value in majority_errors.items()
    },
    "pair_error_rates": {name: str(value) for name, value in pair_errors.items()},
    "all_copy_agreement_rates": {
        name: str(value) for name, value in agreement.items()
    },
    "classification": {
        "broadcastability": "fanout of a commutative record label",
        "redundancy": "decoder performance under the full joint disturbance law",
        "missing_state": "common-cause and cross-copy error correlation",
    },
}

output = Path(__file__).parents[1] / "results" / "broadcast_joint_failure_carrier.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

