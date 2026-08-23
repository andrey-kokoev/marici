"""Hostile Pick-matrix split into endpoint-theta and theta-theta blocks."""

import cmath
import itertools
import json
import math
from pathlib import Path


CENTER = 0.25


def phi(radius, max_label=8):
    exp2 = math.exp(2 * radius)
    terms = []
    for label in range(1, max_label + 1):
        coefficient = math.pi * label * label
        decay = math.exp(-coefficient * exp2)
        terms.append(
            (4 * coefficient * coefficient * math.exp(4.5 * radius)
             - 6 * coefficient * math.exp(2.5 * radius))
            * decay
        )
    return math.fsum(terms)


def completed_pair(w, steps, cutoff=4.0):
    """Return half-line C(w) and dC/dw from the completed theta source."""
    z = cmath.sqrt(w)
    width = cutoff / steps
    values = []
    derivatives = []
    for index in range(steps + 1):
        u = index * width
        source = phi(u)
        coefficient = 1 if index in (0, steps) else (4 if index % 2 else 2)
        values.append(coefficient * source * cmath.cosh(z * u))
        if abs(z) > 1e-14:
            derivative_kernel = u * cmath.sinh(z * u) / (2 * z)
        else:
            derivative_kernel = 0.5 * u * u
        derivatives.append(coefficient * source * derivative_kernel)
    factor = width / 3
    return math.fsum(value.real for value in values) * factor + 1j * math.fsum(
        value.imag for value in values
    ) * factor, math.fsum(value.real for value in derivatives) * factor + 1j * math.fsum(
        value.imag for value in derivatives
    ) * factor


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
    return total.real


real_grid = [-30.0, -3.0, -0.3, 0.3, 3.0, 30.0]
heights = [0.1, 1.0]
points = [complex(x, height) for height in heights for x in real_grid]
resolutions = [4000, 8000]
data = {
    steps: {point: completed_pair(point, steps) for point in points}
    for steps in resolutions
}


def matrices(chosen, steps):
    endpoint = []
    remainder = []
    full = []
    for z in chosen:
        endpoint_row = []
        remainder_row = []
        full_row = []
        cz, cpz = data[steps][z]
        uz = cz - CENTER
        az = (z - CENTER) * cpz
        for w in chosen:
            cw, cpw = data[steps][w]
            uw = cw - CENTER
            aw = (w - CENTER) * cpw
            denominator = z - w.conjugate()
            endpoint_entry = CENTER * (az - aw.conjugate()) / denominator
            remainder_entry = (az * uw.conjugate() - uz * aw.conjugate()) / denominator
            endpoint_row.append(endpoint_entry)
            remainder_row.append(remainder_entry)
            full_row.append(endpoint_entry + remainder_entry)
        endpoint.append(endpoint_row)
        remainder.append(remainder_row)
        full.append(full_row)
    return endpoint, remainder, full


rows = []
for order in (1, 2, 3):
    summary = {
        "order": order,
        "matrix_count": 0,
        "first_robust_endpoint_negative": None,
        "first_robust_remainder_negative": None,
        "first_robust_full_negative": None,
        "smallest_endpoint_determinant": None,
        "smallest_remainder_determinant": None,
        "smallest_full_determinant": None,
    }
    for chosen in itertools.combinations(points, order):
        low = matrices(chosen, resolutions[0])
        high = matrices(chosen, resolutions[1])
        for index, name in enumerate(("endpoint", "remainder", "full")):
            low_det = determinant(low[index])
            high_det = determinant(high[index])
            discrepancy = abs(high_det - low_det)
            record = {
                "points": [[point.real, point.imag] for point in chosen],
                "determinant_steps_4000": low_det,
                "determinant_steps_8000": high_det,
                "resolution_discrepancy": discrepancy,
            }
            smallest_key = f"smallest_{name}_determinant"
            if summary[smallest_key] is None or high_det < summary[smallest_key]["determinant_steps_8000"]:
                summary[smallest_key] = record
            negative_key = f"first_robust_{name}_negative"
            if high_det < -10 * max(discrepancy, 1e-12) and summary[negative_key] is None:
                summary[negative_key] = record
        summary["matrix_count"] += 1
    rows.append(summary)

result = {
    "identity": "denominator-free Pick matrix = endpoint-theta + theta-theta",
    "real_grid": real_grid,
    "heights": heights,
    "simpson_resolutions": resolutions,
    "folded_radius_cutoff": 4.0,
    "max_theta_label": 8,
    "orders": rows,
    "endpoint_block_passes_all_samples": all(row["first_robust_endpoint_negative"] is None for row in rows),
    "full_block_passes_all_samples": all(row["first_robust_full_negative"] is None for row in rows),
    "interval_certified": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-endpoint-remainder-pick-split.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for row in rows:
        print(row)
    print(f"endpoint_block_passes_all_samples={result['endpoint_block_passes_all_samples']}")
    print(f"full_block_passes_all_samples={result['full_block_passes_all_samples']}")
