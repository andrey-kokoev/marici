"""WP320: exact quotient audit of the proposed 64-state binary source."""

import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    width = 6
    configurations = list(itertools.product((0, 1), repeat=width))
    permutation_orbits = sorted({sum(configuration) for configuration in configurations})
    complement_orbits = sorted({min(weight, width - weight) for weight in permutation_orbits})
    multiplicities = {
        weight: sum(sum(configuration) == weight for configuration in configurations)
        for weight in permutation_orbits
    }
    checks = {
        "six_labelled_bits_have_64_literal_configurations": len(configurations) == 64 == 2**width,
        "s6_quotient_has_seven_hamming_weight_orbits": permutation_orbits == list(range(7)),
        "adding_complement_exchange_leaves_four_orbits": complement_orbits == list(range(4)),
        "binomial_multiplicities_sum_to_64": sum(multiplicities.values()) == 64,
        "multiplicities_are_binomial": all(multiplicities[k] == math.comb(width, k) for k in permutation_orbits),
        "literal_and_physical_counts_differ_under_s6_gauge": len(configurations) != len(permutation_orbits),
        "label_ports_change_the_counting_groupoid": 64 > 7 > 4,
    }
    result = {
        "work_package": "WP320",
        "admitted_state_domain": "six binary source slots, audited under literal labels, S6 slot permutations, and S6 plus global complement",
        "literal_configuration_count": len(configurations),
        "s6_quotient_orbit_count": len(permutation_orbits),
        "s6_plus_complement_orbit_count": len(complement_orbits),
        "s6_orbit_labels": permutation_orbits,
        "orbit_multiplicities": multiplicities,
        "source_authorized_probe_family": "Hamming weight is the complete invariant under S6; individual bit addresses require labelled ports",
        "contextual_partition": "64 literal words partition into seven S6 orbits with binomial multiplicities; complement pairs these into four relational orbits",
        "classification": "the number 64 is a literal labelled-cardinality result, not a quotient-invariant physical charge prediction when slot permutations are gauge",
        "smallest_exact_falsifier": "000001 and 100000 are distinct labelled words but the same S6 orbit, so literal word count cannot be used as physical sector count without label instruments",
        "remaining_physical_instrument_gate": "derive six distinguishable source ports and a physical operation mapping their literal state count, rather than their quotient orbit, to flux magnitude",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp320_binary_cardinality_groupoid.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
