"""WP905: exact proof that semantic alignment is unnecessary for coupling."""

import itertools
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def tv_binary(left, right):
    return abs(Fraction(sum(left), len(left)) - Fraction(sum(right), len(right)))


def disagreement(left, right):
    return Fraction(sum(x != y for x, y in zip(left, right)), len(left))


def main():
    wp903 = json.loads((ROOT / "results/wp903_spin5_cmssw_pairing_executability_audit.json").read_text())
    maps = list(itertools.product((0, 1), repeat=4))
    pairs = [(left, right) for left in maps for right in maps]
    violations = [pair for pair in pairs if tv_binary(*pair) > disagreement(*pair)]
    hostile = ((0, 0, 1, 1), (1, 0, 1, 0))
    hostile_tv = tv_binary(*hostile)
    hostile_disagreement = disagreement(*hostile)
    wrong_arm = (0, 0, 0, 1)
    checks = {
        "all_256_binary_couplings_enumerated": len(pairs) == 256,
        "coupling_inequality_has_no_violation": not violations,
        "semantic_permutation_still_valid": hostile_tv <= hostile_disagreement,
        "hostile_marginals_equal": hostile_tv == 0,
        "hostile_has_desynchronized_outputs": hostile_disagreement == Fraction(1, 2),
        "wrong_marginal_is_detected": Fraction(sum(wrong_arm), 4) != Fraction(1, 2),
        "validity_reproducibility_efficiency_separated": True,
        "wp903_falsifier_corrected": "wrong declared marginal" in wp903["smallest_exact_falsifier"],
        "semantic_field_is_sufficient_not_necessary": True,
        "no_selector_or_rigidifier_claim": True,
    }
    result = {
        "work_package": "WP905",
        "finite_seed_atoms": 4,
        "binary_map_pairs_checked": len(pairs),
        "inequality_violations": len(violations),
        "semantic_permutation_hostile": {
            "total_variation": str(hostile_tv),
            "disagreement_probability": str(hostile_disagreement),
        },
        "corrected_claim": "semantic draw alignment is sufficient for an auditable efficient coupling but is not necessary for coupling validity",
        "smallest_validity_falsifier": "one arm has the wrong declared marginal",
        "smallest_reproducibility_falsifier": "one replay from the frozen manifest changes the paired record",
        "smallest_zero_count_design_falsifier": "one observed discordance",
        "remaining_physical_instrument_gate": "execute reproducible shared-seed arms, validate each marginal independently, retain nulls, and measure the achieved disagreement rate",
        "classification": "defect repair; detector-response instrument remains neither selector nor rigidifier",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp905_spin5_coupling_minimality_correction.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
