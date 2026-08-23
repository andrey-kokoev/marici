"""Zero-free reconnaissance of the theta logarithmic-derivative cone split."""
import json
from pathlib import Path

from reduced_source_pick_hostile_scan import reduced_F


coordinates = (0.02, 0.05, 0.1, 0.2, 0.35, 0.49, 0.51, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0)


def evaluate(a, b, depth):
    z = complex(a, b)
    t = z * z
    F = reduced_F(t, depth)
    M = 2 * z * F / (4 * t - 1)
    radius_squared = a * a + b * b
    alpha = 2 * a - a / (2 * radius_squared)
    beta = 2 * b + b / (2 * radius_squared)
    margin = beta * M.real + alpha * M.imag
    return M, alpha, beta, margin


rows = []
maximum_depth_discrepancy = 0.0
for a in coordinates:
    for b in coordinates:
        M, alpha, beta, margin = evaluate(a, b, 50)
        M40, _, _, margin40 = evaluate(a, b, 40)
        maximum_depth_discrepancy = max(
            maximum_depth_discrepancy,
            abs(M - M40),
            abs(margin - margin40),
        )
        radius_squared = a * a + b * b
        cone_slack = None
        if radius_squared < 0.25:
            cone_ceiling = (b / a) * (1 + 4 * radius_squared) / (1 - 4 * radius_squared)
            cone_slack = cone_ceiling - M.imag / M.real
        rows.append(
            {
                "a": a,
                "b": b,
                "radius_squared": radius_squared,
                "M_real": M.real,
                "M_imag": M.imag,
                "alpha": alpha,
                "beta": beta,
                "pick_margin": margin,
                "inner_cone_slack": cone_slack,
            }
        )

minimum_real = min(rows, key=lambda row: row["M_real"])
minimum_imag = min(rows, key=lambda row: row["M_imag"])
minimum_margin = min(rows, key=lambda row: row["pick_margin"])
inner_rows = [row for row in rows if row["inner_cone_slack"] is not None]
minimum_cone_slack = min(inner_rows, key=lambda row: row["inner_cone_slack"])

assert minimum_real["M_real"] > 0
assert minimum_imag["M_imag"] > 0
assert minimum_margin["pick_margin"] > 0
assert minimum_cone_slack["inner_cone_slack"] > 0

result = {
    "grid_size": len(rows),
    "coordinate_grid": list(coordinates),
    "minimum_M_real": minimum_real,
    "minimum_M_imag": minimum_imag,
    "minimum_pick_margin": minimum_margin,
    "minimum_inner_cone_slack": minimum_cone_slack,
    "maximum_depth_40_50_discrepancy": maximum_depth_discrepancy,
    "no_sampled_first_quadrant_violation": True,
    "no_sampled_inner_cone_violation": True,
    "no_sampled_pick_violation": True,
    "interval_certified": False,
    "zero_locations_used": False,
    "rh_proved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-log-derivative-cone-scan.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
