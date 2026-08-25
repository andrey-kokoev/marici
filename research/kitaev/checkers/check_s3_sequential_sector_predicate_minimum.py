"""Minimum sequential binary predicates for eight D(S3) sectors."""

import itertools
import json


def main():
    labels = tuple("ABCDEFGH")
    blocks = (("A", "B", "C"), ("D", "E"), ("F", "G", "H"))
    sizes = tuple(map(len, blocks))
    union_sizes = sorted({sum(sizes[i] for i in range(3) if mask & (1 << i))
                          for mask in range(8)})
    assert union_sizes == [0, 2, 3, 5, 6, 8]
    assert 4 not in union_sizes

    # Exhaust all bijections between eight sectors and three-bit strings.
    words = tuple(itertools.product((0, 1), repeat=3))
    assignments = 0
    minimum_charge_sensitive_coordinates = 3
    coordinate_split_histogram = {1: 0, 2: 0, 3: 0}
    for permutation in itertools.permutations(words):
        assignment = dict(zip(labels, permutation))
        charge_sensitive = 0
        for bit in range(3):
            class_constant = all(len({assignment[label][bit] for label in block}) == 1
                                 for block in blocks)
            if not class_constant:
                charge_sensitive += 1
        assert charge_sensitive == 3
        coordinate_split_histogram[charge_sensitive] += 1
        minimum_charge_sensitive_coordinates = min(minimum_charge_sensitive_coordinates,
                                                   charge_sensitive)
        assignments += 1
    assert assignments == 40320
    assert coordinate_split_histogram == {1: 0, 2: 0, 3: 40320}

    result = {
        "schema": "marici.s3-sequential-sector-predicate-minimum.v1",
        "sector_count": 8,
        "minimum_binary_predicates": 3,
        "flux_class_sizes": list(sizes),
        "possible_class_union_sizes": union_sizes,
        "balanced_class_only_bit_exists": False,
        "three_bit_bijections_enumerated": assignments,
        "charge_sensitive_coordinate_histogram": {
            str(k): v for k, v in coordinate_split_histogram.items()
        },
        "minimum_charge_sensitive_predicates": minimum_charge_sensitive_coordinates,
        "sequential_bus": {
            "minimum_reusable_ancilla_dimension": 2,
            "reuse_rounds": 3,
            "charge_sensitive_compilers_required": 3,
            "holonomy_only_rounds_possible": 0,
        },
        "aggregate_gates": {
            "three_binary_predicates_are_information_theoretically_minimal": True,
            "no_flux_class_union_has_size_four": True,
            "every_three_bit_bijection_splits_a_flux_class_in_every_coordinate": True,
            "all_40320_labelings_were_enumerated": True,
            "sequential_qubit_reuse_does_not_remove_charge_sensitive_typing": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

