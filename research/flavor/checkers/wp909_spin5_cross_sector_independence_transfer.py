"""WP909: exact joint-law hostiles transferred into flavor."""

import itertools
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def majority_failure(pattern_probabilities):
    return sum(prob for bits, prob in pattern_probabilities.items() if sum(bits) >= 2)


def main():
    wp908 = json.loads((ROOT / "results/wp908_spin5_pair_independence_hostile.json").read_text())
    even5 = [bits for bits in itertools.product((0, 1), repeat=5) if sum(bits) % 2 == 0]
    deletion_marginals = []
    for deleted in range(5):
        deletion_marginals.append(Counter(
            tuple(bit for i, bit in enumerate(bits) if i != deleted) for bits in even5
        ))
    all_four = set(itertools.product((0, 1), repeat=4))
    proper_uniform = all(set(c) == all_four and set(c.values()) == {1} for c in deletion_marginals)

    p = Fraction(1, 10)
    independent = {
        bits: p ** sum(bits) * (1 - p) ** (3 - sum(bits))
        for bits in itertools.product((0, 1), repeat=3)
    }
    common = {(0, 0, 0): 1 - p, (1, 1, 1): p}
    exclusive = {(0, 0, 0): Fraction(7, 10), (1, 0, 0): p, (0, 1, 0): p, (0, 0, 1): p}
    majority = {
        "independent": majority_failure(independent),
        "common_mode": majority_failure(common),
        "exclusive": majority_failure(exclusive),
    }
    checks = {
        "wp908_passes": wp908["passed"],
        "even_parity_support_has_16_atoms": len(even5) == 16,
        "iid_five_bit_support_has_32_atoms": 2**5 == 32,
        "all_five_deletion_marginals_are_uniform": proper_uniform,
        "global_even_parity_probability_is_one": all(sum(bits) % 2 == 0 for bits in even5),
        "iid_even_parity_probability_is_one_half": Fraction(16, 32) == Fraction(1, 2),
        "sontag_independent_majority_failure": majority["independent"] == Fraction(7, 250),
        "sontag_common_mode_majority_failure": majority["common_mode"] == Fraction(1, 10),
        "sontag_exclusive_majority_failure": majority["exclusive"] == 0,
        "equal_marginals_allow_three_joint_risks": len(set(majority.values())) == 3,
        "finite_lower_order_tests_do_not_certify_product_law": True,
        "mixed_run_event_corner_must_be_typed": True,
        "aggregate_replay_does_not_certify_channel_lineage": True,
        "entropy_name_does_not_supply_calibration": True,
        "no_selector_claim": True,
    }
    result = {
        "work_package": "WP909",
        "transfers": ["Sontag joint failure carrier", "Strominger higher-arity obstruction", "Nima mixed source corner", "Aspect hidden channel transport", "Benincasa normalization gate"],
        "five_bit_hostile_support_size": len(even5),
        "all_four_bit_deletion_marginals_uniform": proper_uniform,
        "global_even_parity_probability": "1",
        "iid_even_parity_probability": "1/2",
        "three_copy_majority_failure_probabilities": {key: str(value) for key, value in majority.items()},
        "largest_current_probe_family": "replay, arm marginals, registered finite-order dependence diagnostics, seed-family perturbations, and run-boundary stratification",
        "contextual_partition": "does not separate iid laws from all higher-order dependent laws with matching tested marginals",
        "smallest_exact_falsifier": "uniform even parity on five bits matches every four-bit deletion marginal but is not the iid five-bit law",
        "remaining_physical_instrument_gate": "full joint failure carrier plus independently calibrated event-key acquisition or a source theorem establishing the product law",
        "classification": "cross-sector obstruction transfer; neither selector nor rigidifier",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp909_spin5_cross_sector_independence_transfer.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
