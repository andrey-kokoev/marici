"""Compare signed higher-label transforms directly to the first mode."""
import json
import math
from pathlib import Path

from theta_cross_label_orbit_compensation import orbit_block


a = 1.0
b_values = [8.0, 11.0, 16.0, 24.0, 32.0]
samples = []
for b in b_values:
    band_count = math.ceil(3.0 * b / math.pi)
    kwargs = {
        "a": a,
        "b": b,
        "band_count": band_count,
        "d_steps_per_band": 80,
        "s_steps": 1200,
    }
    diagonal_11 = orbit_block(labels=[(1, 1)], **kwargs)
    exchange_12 = orbit_block(labels=[(1, 2), (2, 1)], **kwargs)
    diagonal_22 = orbit_block(labels=[(2, 2)], **kwargs)
    samples.append({
        "b": b,
        "band_count": band_count,
        "diagonal_11": diagonal_11,
        "exchange_12_21": exchange_12,
        "diagonal_22": diagonal_22,
        "exchange_to_first_ratio": exchange_12 / diagonal_11,
        "second_diagonal_to_first_ratio": diagonal_22 / diagonal_11,
        "two_mode_sum": diagonal_11 + exchange_12 + diagonal_22,
    })

result = {
    "a": a,
    "integration_domain": "0 <= d <= ceil(3*b/pi)*pi/b; |S| <= 8",
    "samples": samples,
    "interval_certified": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-phase-aware-orbit-ratio-scan.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for sample in samples:
        print(
            f"b={sample['b']:.1f} I11={sample['diagonal_11']:.16e} "
            f"I12={sample['exchange_12_21']:.16e} "
            f"ratio12={sample['exchange_to_first_ratio']:.10e} "
            f"ratio22={sample['second_diagonal_to_first_ratio']:.10e}"
        )
