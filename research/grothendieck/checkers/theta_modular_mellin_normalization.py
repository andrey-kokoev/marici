"""Audit the modular Mellin normalization at w=2 (z=3/2)."""
import json
import math
from pathlib import Path

from theta_one_copy_orbit_factorization import one_copy


z = 1.5
resolutions = [5000, 10000, 20000]
values = []
for steps in resolutions:
    bilateral = math.fsum(one_copy(label, z, 0.0, steps)[0].real for label in range(1, 8))
    values.append(bilateral)

completed_xi_at_two = math.pi / 6
result = {
    "z": z,
    "w": z + 0.5,
    "bilateral_transform_values": values,
    "completed_xi_w2_pi_over_6": completed_xi_at_two,
    "ratios_to_completed_xi": [value / completed_xi_at_two for value in values],
    "half_line_B_values": [value / 2 for value in values],
    "mellin_identity": "integral_R exp(z*u) Phi(|u|) du = xi(1/2+z)",
    "interval_certified": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-modular-mellin-normalization.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
