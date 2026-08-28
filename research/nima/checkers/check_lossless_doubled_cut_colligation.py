from fractions import Fraction
import json
from pathlib import Path


def norm_squared(vector):
    return sum(value * value for value in vector)


def prefix_cut(vector, length):
    return vector[:length], vector[length:]


def suffix_cut(vector, length):
    return vector[-length:], vector[:-length]


def reverse_pair(pair):
    seam, remainder = pair
    return list(reversed(seam)), list(reversed(remainder))


records = []
one_sector_hostile_found = False

for n in range(5, 15):
    vector = [Fraction((i + 1) * (i + 2), n + 1) for i in range(n)]
    reversed_vector = list(reversed(vector))

    for length in range(1, n):
        positive = prefix_cut(vector, length)
        negative = suffix_cut(vector, length)

        assert norm_squared(positive[0]) + norm_squared(positive[1]) == norm_squared(vector)
        assert norm_squared(negative[0]) + norm_squared(negative[1]) == norm_squared(vector)
        assert prefix_cut(reversed_vector, length) == reverse_pair(negative)

        if prefix_cut(reversed_vector, length) != reverse_pair(positive):
            one_sector_hostile_found = True

    order_checks = 0
    for a in range(1, n - 2):
        for b in range(1, n - a):
            first_a, tail_a = prefix_cut(vector, a)
            shell_b, final_tail_ab = prefix_cut(tail_a, b)
            flattened_ab = first_a + shell_b + final_tail_ab

            first_b, tail_b = prefix_cut(vector, b)
            shell_a, final_tail_ba = prefix_cut(tail_b, a)
            flattened_ba = first_b + shell_a + final_tail_ba

            assert flattened_ab == vector
            assert flattened_ba == vector
            assert first_a + shell_b == vector[: a + b]
            assert first_b + shell_a == vector[: a + b]
            assert final_tail_ab == final_tail_ba == vector[a + b :]
            order_checks += 1

    records.append(
        {
            "dimension": n,
            "all_cut_energy_splits_exact": True,
            "reciprocal_prefix_suffix_intertwiner_exact": True,
            "two_order_recutting_checks": order_checks,
        }
    )

assert one_sector_hostile_found

result = {
    "schema": "marici.nima.lossless-doubled-cut-colligation.v1",
    "records": records,
    "one_sector_reflection_closed": False,
    "doubled_prefix_suffix_reflection_equivariant": True,
    "verdict": "the shared seam has a lossless operator lift; reciprocal dagger requires doubled sectors",
}

out = Path(__file__).parents[1] / "results" / "lossless-doubled-cut-colligation.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
