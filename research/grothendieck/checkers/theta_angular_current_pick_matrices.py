"""Hostile finite Pick-matrix scan for H(w)=reduced_F(w)/4."""

import itertools
import json
from pathlib import Path

from reduced_source_pick_hostile_scan import reduced_F


def current(w, depth):
    return reduced_F(w, depth) / 4


def pick_entry(z, w, depth):
    return (current(z, depth) - current(w, depth).conjugate()) / (z - w.conjugate())


def determinant(matrix):
    order = len(matrix)
    total = 0j
    for permutation in itertools.permutations(range(order)):
        inversions = sum(
            permutation[left] > permutation[right]
            for left in range(order)
            for right in range(left + 1, order)
        )
        term = 1 + 0j
        for row in range(order):
            term *= matrix[row][permutation[row]]
        total += (-1 if inversions % 2 else 1) * term
    return total


real_grid = [-100.0, -30.0, -10.0, -3.0, -1.0, -0.3, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0]
heights = [0.03, 0.1, 0.3, 1.0]
point_sets = [[complex(x, height) for x in real_grid] for height in heights]

rows = []
for order in (1, 2, 3):
    smallest = None
    robust_negative = None
    count = 0
    maximum_depth_discrepancy = 0.0
    for points in point_sets:
        for chosen in itertools.combinations(points, order):
            matrix40 = [[pick_entry(z, w, 40) for w in chosen] for z in chosen]
            matrix36 = [[pick_entry(z, w, 36) for w in chosen] for z in chosen]
            value40 = determinant(matrix40).real
            value36 = determinant(matrix36).real
            discrepancy = abs(value40 - value36)
            maximum_depth_discrepancy = max(maximum_depth_discrepancy, discrepancy)
            count += 1
            record = {
                "points": [[z.real, z.imag] for z in chosen],
                "determinant_depth_40": value40,
                "determinant_depth_36": value36,
                "depth_discrepancy": discrepancy,
            }
            if smallest is None or value40 < smallest["determinant_depth_40"]:
                smallest = record
            if value40 < -10 * max(discrepancy, 1e-12) and robust_negative is None:
                robust_negative = record
    rows.append(
        {
            "order": order,
            "matrix_count": count,
            "smallest_determinant": smallest,
            "maximum_depth_36_40_discrepancy": maximum_depth_discrepancy,
            "first_robust_negative": robust_negative,
            "all_sampled_determinants_nonnegative_with_depth_guard": robust_negative is None,
        }
    )

result = {
    "identity": "H(w)=reduced_F(w)/4=(w-1/4)C'(w)/C(w)",
    "real_grid": real_grid,
    "heights": heights,
    "orders": rows,
    "all_sampled_pick_matrices_pass": all(
        row["all_sampled_determinants_nonnegative_with_depth_guard"] for row in rows
    ),
    "zero_locations_used": False,
    "interval_certified": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-angular-current-pick-matrices.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for row in rows:
        print(row)
    print(f"all_sampled_pick_matrices_pass={result['all_sampled_pick_matrices_pass']}")
