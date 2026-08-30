"""Convert the weakest certified midpoint gap into average curvature."""
import json
from decimal import Decimal, localcontext
from pathlib import Path


ROOT = Path(__file__).parents[1]
payload = json.loads((ROOT / "results" / "reduced-source-central-interval-chords.json").read_text())

with localcontext() as context:
    context.prec = 90
    lo, hi = map(Decimal, payload["minimum_gap_interval"])
    a, _, b = map(Decimal, payload["minimum_chord"])
    width = b - a
    # Weighted average of H'' under the unit-mass triangular Peano kernel.
    average_curvature = (-Decimal(8) * hi / width**2, -Decimal(8) * lo / width**2)

assert average_curvature[1] < 0

result = {
    "identity": "weighted_average(H'') = -8*midpoint_gap/(b-a)^2",
    "chord": payload["minimum_chord"],
    "gap_interval": payload["minimum_gap_interval"],
    "triangular_weighted_average_H_double_prime_interval": [str(x) for x in average_curvature],
    "strictly_negative_average_curvature": True,
    "continuum_upgrade_sufficient_condition": "oscillation of H'' about its weighted average is less than the absolute upper endpoint",
    "interval_certified": True,
    "rh_proved": False,
}

if __name__ == "__main__":
    output = ROOT / "results" / "central-chord-average-curvature.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
