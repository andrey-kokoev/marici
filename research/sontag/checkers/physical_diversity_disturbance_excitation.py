import json
from pathlib import Path


def apply(matrix, disturbance):
    return tuple(
        sum(a * b for a, b in zip(row, disturbance)) % 2
        for row in matrix
    )


def rank_f2(matrix):
    rows = [list(row) for row in matrix]
    rank = 0
    for column in range(len(rows[0])):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for i in range(len(rows)):
            if i != rank and rows[i][column]:
                rows[i] = [a ^ b for a, b in zip(rows[i], rows[rank])]
        rank += 1
    return rank


common = ((1, 0), (1, 0))
diverse = ((1, 0), (1, 1))
zero = (0, 0)
d1 = (1, 0)
d2 = (0, 1)

checks = {
    "shared_baseline": apply(common, zero) == apply(diverse, zero) == zero,
    "rank_one_common_coupling": rank_f2(common) == 1,
    "rank_two_diverse_coupling": rank_f2(diverse) == 2,
    "one_excitation_is_aliased": apply(common, d1) == apply(diverse, d1) == (1, 1),
    "second_excitation_breaks_alias": apply(common, d2) != apply(diverse, d2),
    "two_excitations_recover_common_columns": tuple(zip(apply(common, d1), apply(common, d2))) == common,
    "two_excitations_recover_diverse_columns": tuple(zip(apply(diverse, d1), apply(diverse, d2))) == diverse,
    "rank_two_still_contains_common_mode": apply(diverse, d1) == (1, 1),
}

result = {
    "model": "binary linear copy errors e = B d over F2",
    "matrices": {"common": common, "diverse": diverse},
    "responses": {
        "d1": {"common": apply(common, d1), "diverse": apply(diverse, d1)},
        "d2": {"common": apply(common, d2), "diverse": apply(diverse, d2)},
    },
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
}

assert all(checks.values()), result
output = Path(__file__).parents[1] / "results" / "physical_diversity_disturbance_excitation.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
