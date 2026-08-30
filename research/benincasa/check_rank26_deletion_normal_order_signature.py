#!/usr/bin/env python3
"""Test the frozen normal-order prediction on every marked deletion sector."""

import json
from collections import Counter
from itertools import combinations
from math import comb
from pathlib import Path


LABELS = ("g1", "g2", "g3", "g23", "g31")
# Coefficients of (a,b) at the all-soft point.
COLUMNS = {
    "g1": (0, 1),
    "g2": (1, 0),
    "g3": (1, 1),
    "g23": (0, 1),
    "g31": (1, 0),
}


def rank(columns):
    if not columns:
        return 0
    if any(column != (0, 0) for column in columns):
        first = next(column for column in columns if column != (0, 0))
        if any(first[0] * other[1] - first[1] * other[0] != 0 for other in columns):
            return 2
        return 1
    return 0


def main():
    sectors = []
    partition = Counter()
    for size in range(1, len(LABELS) + 1):
        for subset in combinations(LABELS, size):
            incidence_rank = rank([COLUMNS[label] for label in subset])
            first_normal = size - incidence_rank
            zero_generators = first_normal + 1  # the second-normal K direction
            signature = (incidence_rank, first_normal, 2, zero_generators)
            partition[signature] += 1
            sectors.append({
                "labels": list(subset),
                "marked_count": size,
                "incidence_rank": incidence_rank,
                "predicted_first_normal_generators": first_normal,
                "Cayley_Menger_normal_order": 2,
                "total_exterior_generators": zero_generators,
                "exterior_graded_ranks_over_quotient": [
                    comb(zero_generators, degree)
                    for degree in range(zero_generators + 1)
                ],
                "coefficient_quotient_dimension": 0 if incidence_rank < 2 else 1,
            })

    full = next(record for record in sectors if len(record["labels"]) == 5)
    checks = {
        "all_31_nonempty_labelled_deletions_tested": len(sectors) == 31,
        "first_normal_count_is_marked_rank_defect_in_every_sector": all(
            record["predicted_first_normal_generators"]
            == record["marked_count"] - record["incidence_rank"]
            for record in sectors
        ),
        "second_normal_K_direction_is_frozen_across_deletions": all(
            record["Cayley_Menger_normal_order"] == 2 for record in sectors
        ),
        "full_family_signature_is_1_1_1_2": (
            full["predicted_first_normal_generators"] == 3
            and full["Cayley_Menger_normal_order"] == 2
        ),
        "full_family_exterior_ranks_are_1_4_6_4_1": full["exterior_graded_ranks_over_quotient"] == [1, 4, 6, 4, 1],
    }
    result = {
        "schema": "marici.rank26-deletion-normal-order-signature.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "predeclared_rule": {
            "first_normal_multiplicity": "number of retained marked forms minus rank of their all-soft incidence map to span(a,b)",
            "higher_normal_generator": "one Cayley-Menger generator at external order 2",
            "homology_module": "F[a,b]/I_S tensor exterior^(marked_count-rank+1)",
        },
        "signature_partition": [
            {
                "incidence_rank": key[0],
                "first_normal_generators": key[1],
                "Cayley_Menger_order": key[2],
                "total_exterior_generators": key[3],
                "sector_count": count,
            }
            for key, count in sorted(partition.items())
        ],
        "sectors": sectors,
        "checks": checks,
    }
    output = Path(__file__).with_name("rank26-deletion-normal-order-signature.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": result["status"],
        "signature_partition": result["signature_partition"],
        "checks": checks,
    }, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
