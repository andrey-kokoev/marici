"""High-precision reconnaissance for the continuum oscillation budget."""
import json
from decimal import Decimal, localcontext
from functools import lru_cache
from pathlib import Path

from reduced_source_central_analytic_slope import analytic_slope


with localcontext() as context:
    context.prec = 90
    D = Decimal
    endpoints = []
    for power in range(8, 2, -1):
        endpoints.extend((D(f"1e-{power}"), D(f"3e-{power}")))
    endpoints.append(D("1e-2"))

    @lru_cache(maxsize=None)
    def H(text):
        return 1 / analytic_slope(D(text), 132).sqrt()

    rows = []
    for a, b in zip(endpoints, endpoints[1:]):
        x = (a + b) / 2
        h = min(x / 20, (b - a) / 20)
        values = {j: H(str(x + j * h)) for j in (-2, -1, 0, 1, 2)}
        h2 = (-values[2] + 16 * values[1] - 30 * values[0] + 16 * values[-1] - values[-2]) / (12 * h * h)
        h3 = (values[2] - 2 * values[1] + 2 * values[-1] - values[-2]) / (2 * h**3)
        oscillation = abs(h3) * (b - a)
        rows.append((a, b, h2, h3, oscillation))

    largest_oscillation = max(rows, key=lambda row: row[4])
    least_negative_h2 = max(rows, key=lambda row: row[2])
    shortest = rows[0]

result = {
    "cell_count": len(rows),
    "shortest_cell": [str(shortest[0]), str(shortest[1])],
    "shortest_cell_H_double_prime_estimate": str(shortest[2]),
    "shortest_cell_H_triple_prime_estimate": str(shortest[3]),
    "shortest_cell_oscillation_budget": str(shortest[4]),
    "largest_estimated_oscillation_budget": str(largest_oscillation[4]),
    "largest_oscillation_cell": [str(largest_oscillation[0]), str(largest_oscillation[1])],
    "least_negative_sampled_H_double_prime": str(least_negative_h2[2]),
    "least_negative_H_double_prime_cell": [str(least_negative_h2[0]), str(least_negative_h2[1])],
    "all_sampled_H_double_prime_negative": all(row[2] < 0 for row in rows),
    "finite_difference_reconnaissance_only": True,
    "interval_certified": False,
    "rh_proved": False,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "central-H-third-derivative-reconnaissance.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
