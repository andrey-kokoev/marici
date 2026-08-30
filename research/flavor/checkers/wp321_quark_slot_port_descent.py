"""WP321: exact descent audit for six proposed quark-labelled binary ports."""

import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def sector_weights(word):
    return sum(word[:3]), sum(word[3:])


def exchange_orbit_label(weights):
    return tuple(sorted(weights))


def binary_address(word):
    return sum(bit << index for index, bit in enumerate(word))


def main():
    words = list(itertools.product((0, 1), repeat=6))
    sector_orbits = sorted({sector_weights(word) for word in words})
    exchange_orbits = sorted({exchange_orbit_label(sector_weights(word)) for word in words})
    hostile_left = (1, 0, 0, 0, 0, 0)
    hostile_right = (0, 1, 0, 0, 0, 0)
    checks = {
        "literal_quark_slot_words_number_64": len(words) == 64,
        "independent_generation_permutations_leave_16_orbits": len(sector_orbits) == 16,
        "sector_exchange_leaves_10_orbits": len(exchange_orbits) == 10,
        "sector_weight_is_complete_orbit_label": sector_orbits == list(itertools.product(range(4), repeat=2)),
        "hostile_words_share_generation_quotient": sector_weights(hostile_left) == sector_weights(hostile_right),
        "hostile_words_have_different_binary_addresses": binary_address(hostile_left) != binary_address(hostile_right),
        "address_map_fails_permutation_descent": binary_address(hostile_left) != binary_address(hostile_right),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP321",
        "admitted_state_domain": "six binary slots provisionally named as three up-sector and three down-sector generation ports",
        "declared_groupoids": ["literal labelled slots", "S3_up x S3_down generation permutations", "generation permutations plus up/down exchange"],
        "literal_count": len(words),
        "generation_quotient_count": len(sector_orbits),
        "generation_plus_exchange_quotient_count": len(exchange_orbits),
        "generation_quotient_labels": [list(label) for label in sector_orbits],
        "source_authorized_probe_family": "without generation reference ports, only the two sector Hamming weights descend under the permutation subgroup",
        "contextual_partition": "64 labelled words collapse to 16 sector-weight classes, then to 10 unordered sector-weight classes under exchange",
        "hostile_pair": {
            "left": "100|000",
            "right": "010|000",
            "common_quotient_label": list(sector_weights(hostile_left)),
            "binary_addresses": [binary_address(hostile_left), binary_address(hostile_right)],
        },
        "classification": "quark names do not provide six source ports; a binary-address or literal-cardinality map fails descent under generation permutations and is presentation data",
        "smallest_exact_falsifier": "100|000 and 010|000 are related by an up-generation permutation but receive different binary addresses",
        "remaining_physical_instrument_gate": "derive generation-resolving source projectors before the Yukawa readout and show that they transform covariantly under the full weak-basis group; mass ordering derived from the Yukawas is downstream and circular",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp321_quark_slot_port_descent.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
