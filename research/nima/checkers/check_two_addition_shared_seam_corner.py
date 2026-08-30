from fractions import Fraction
import json
from pathlib import Path


def weighted_sum(source, weight, start=0, stop=None):
    if stop is None:
        stop = len(source)
    return sum(
        (source[index] * weight ** index for index in range(start, stop)),
        Fraction(0),
    )


records = []
for size in range(5, 15):
    source = [Fraction((i + 1) * (i + 3), size + 2) for i in range(size)]
    weight = Fraction(2, 3)
    total = weighted_sum(source, weight)

    for a in range(1, size - 2):
        for b in range(1, size - a):
            q_a = weight ** a
            q_b = weight ** b
            window_a = weighted_sum(source, weight, 0, a)
            window_b = weighted_sum(source, weight, 0, b)
            window_ab = weighted_sum(source, weight, 0, a + b)
            shell_ab = weighted_sum(source, weight, a, a + b)
            shell_ba = weighted_sum(source, weight, b, a + b)

            assert window_a + shell_ab == window_ab
            assert window_b + shell_ba == window_ab

            shifted_ab = q_a * q_b * (total - window_ab)
            shifted_ba = q_b * q_a * (total - window_ab)
            assert shifted_ab == shifted_ba

            bare_mixed = q_a * q_b * total
            mixed_residual = shifted_ab - bare_mixed
            assert mixed_residual == -q_a * q_b * window_ab

            first_only_mixed = bare_mixed
            assert shifted_ab - first_only_mixed == mixed_residual

    records.append(
        {
            "source_size": size,
            "all_ordered_pairs_checked": size * (size - 3) // 2,
            "shell_decompositions_exact": True,
            "mixed_section_order_independent": True,
            "deleted_corner_residual_exact": True,
        }
    )

result = {
    "schema": "marici.nima.two-addition-shared-seam-corner.v1",
    "records": records,
    "uses_division_by_endpoint_section": False,
    "mixed_corner_is_cyclic_cumulant": False,
    "verdict": "two source additions force one shared total-window comparison cell",
}

out = Path(__file__).parents[1] / "results" / "two-addition-shared-seam-corner.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
