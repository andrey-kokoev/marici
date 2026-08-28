from fractions import Fraction
import json
from pathlib import Path


def chunk(vector, width):
    return [vector[start : start + width] for start in range(0, len(vector), width)]


def flatten(chunks):
    return [value for block in chunks for value in block]


def norm_squared(vector):
    return sum(value * value for value in vector)


def overlap_length(left_start, left_end, right_start, right_end):
    return max(0, min(left_end, right_end) - max(left_start, right_start))


records = []
dimension = 60
source = [Fraction((i + 1) * ((-1) ** i), 61) for i in range(dimension)]
widths = [2, 3, 4, 5, 6, 10, 12, 15]

for left_width in widths:
    for right_width in widths:
        left_chart = chunk(source, left_width)
        right_chart = chunk(source, right_width)
        resegmented = chunk(flatten(left_chart), right_width)
        assert resegmented == right_chart
        assert norm_squared(flatten(resegmented)) == norm_squared(source)

        for third_width in widths:
            via_right = chunk(flatten(resegmented), third_width)
            direct = chunk(flatten(left_chart), third_width)
            assert via_right == direct

        overlap_entries = 0
        for j in range(len(left_chart)):
            left_start = j * left_width
            left_end = min((j + 1) * left_width, dimension)
            for k in range(len(right_chart)):
                right_start = k * right_width
                right_end = min((k + 1) * right_width, dimension)
                overlap = overlap_length(
                    left_start, left_end, right_start, right_end
                )
                if overlap:
                    overlap_entries += 1
                    assert left_start < right_end and right_start < left_end

        common_length = min(left_width, right_width)
        common = [Fraction(1, common_length) for _ in range(common_length)] + [
            Fraction(0) for _ in range(dimension - common_length)
        ]
        left_common = flatten(chunk(common, left_width))
        right_common = flatten(chunk(common, right_width))
        assert left_common == right_common == common
        assert norm_squared(left_common) == norm_squared(right_common)

        records.append(
            {
                "left_width": left_width,
                "right_width": right_width,
                "resegmentation_exact": True,
                "all_third_chart_compositions_exact": True,
                "overlap_entries": overlap_entries,
                "common_state_full_norm": True,
            }
        )

result = {
    "schema": "marici.nima.prime-seam-resegmentation.v1",
    "records": records,
    "resegmentation_operator_norm": 1,
    "prime_charts_orthogonal": False,
    "verdict": "prime seam charts are unitary resegmentations of one boundary history",
}

out = Path(__file__).parents[1] / "results" / "prime-seam-resegmentation.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
