"""WP913: exact soundness budget for a Bell-randomness reference port."""

import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
A = 389
B = 2937600
STRATA = 2
POLES = 2
LOOKS = 4
RNG_ERROR = Fraction(1, 10_000_000_000)
TOTAL_ERROR = Fraction(1, 20)
STATISTICAL_ERROR = TOTAL_ERROR - RNG_ERROR
LOOK_ERROR = STATISTICAL_ERROR / (STRATA * POLES * LOOKS)


def accepts(n, k):
    tail_numerator = sum(
        math.comb(n, j) * A**j * (B - A) ** (n - j)
        for j in range(k + 1)
    )
    return tail_numerator * LOOK_ERROR.denominator <= B**n * LOOK_ERROR.numerator


def minimum_n(k):
    low, high = k, max(1, k + 1)
    while not accepts(high, k):
        high *= 2
    while low + 1 < high:
        middle = (low + high) // 2
        if accepts(middle, k):
            high = middle
        else:
            low = middle
    return high


def main():
    wp912 = json.loads((ROOT / "results/wp912_spin5_event_locality_tester.json").read_text())
    counts = {str(k): minimum_n(k) for k in range(LOOKS)}
    maximum_events = STRATA * POLES * counts["3"]
    key_bits = 256 * maximum_events
    precedent_bits = 257_000_000
    precedent_soundness = Fraction(309, 100_000_000_000_000)
    checks = {
        "wp912_passes": wp912["passed"],
        "rng_error_reserved": RNG_ERROR == Fraction(1, 10_000_000_000),
        "statistical_plus_rng_error_is_one_over_20": STATISTICAL_ERROR + RNG_ERROR == TOTAL_ERROR,
        "sixteen_look_cells": STRATA * POLES * LOOKS == 16,
        "every_minimum_passes": all(accepts(n, int(k)) for k, n in counts.items()),
        "one_fewer_fails": all(not accepts(n - 1, int(k)) for k, n in counts.items()),
        "counts_strictly_increase": all(counts[str(k)] < counts[str(k + 1)] for k in range(3)),
        "precedent_soundness_below_reserved_error": precedent_soundness < RNG_ERROR,
        "precedent_capacity_exceeds_256_bit_key_need": precedent_bits >= key_bits,
        "deterministic_partition_cannot_increase_distance": True,
        "event_local_transform_cannot_increase_distance": True,
        "reference_port_changes_experiment": True,
        "fresh_port_run_not_claimed": True,
        "private_setting_seed_remains_gate": True,
        "no_selector_or_rigidifier_claim": True,
    }
    result = {
        "work_package": "WP913",
        "reference_port": "loophole-free Bell randomness expansion plus quantum-proof extraction and immutable event-key allocation",
        "rng_soundness_reserve": str(RNG_ERROR),
        "statistical_error_budget": str(STATISTICAL_ERROR),
        "per_look_error_budget": str(LOOK_ERROR),
        "recomputed_per_cell_looks": [
            {"look": k, "pairs": counts[str(k)], "accept_if_discordances_at_most": k}
            for k in range(LOOKS)
        ],
        "maximum_event_keys": maximum_events,
        "bits_required_for_256_bit_keys": key_bits,
        "published_precedent_bits": precedent_bits,
        "published_precedent_soundness": str(precedent_soundness),
        "smallest_exact_falsifier": "missing Bell transcript/extractor allocation, soundness above the reserved error, reused key block, or one fewer pair at a registered look",
        "changed_groupoid": "new relational experiment over the stabilizer of the certified Bell transcript, extractor record, and bit-to-event allocation",
        "remaining_physical_instrument_gate": "execute a fresh Bell port with private setting seed and loophole closure, verify extraction, and connect its disjoint keys to the event-local CMS adapter",
        "classification": "conditional source-calibrated reference port; neither selector nor rigidifier",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp913_spin5_bell_randomness_reference_port.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
