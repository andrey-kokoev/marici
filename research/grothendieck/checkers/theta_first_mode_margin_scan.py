"""Coarse parameter scan for the coupled first-mode positivity gate."""
import json
import math
from pathlib import Path

from theta_cross_label_orbit_compensation import diagonal_signed_and_absolute


rho = 2.1760611574854079e-3
source_threshold = 2 * rho + rho * rho
a_values = [0.05, 0.1, 0.25, 0.5, 1.0, 2.0, 4.0]
b_values = [4.0, 6.0, 8.0, 11.0, 16.0, 24.0]
samples = []
for a in a_values:
    for b in b_values:
        band_count = math.ceil(3.0 * b / math.pi)
        signed, absolute = diagonal_signed_and_absolute(
            a, b, band_count=band_count, d_steps_per_band=40, s_steps=600
        )
        ratio = signed / absolute
        samples.append({
            "a": a,
            "b": b,
            "band_count": band_count,
            "signed_first_mode": signed,
            "absolute_first_mode": absolute,
            "normalized_margin": ratio,
            "exceeds_source_threshold": ratio > source_threshold,
        })

weakest = min(samples, key=lambda item: item["normalized_margin"])
result = {
    "source_rho_diagnostic": rho,
    "source_threshold_2rho_plus_rho_squared": source_threshold,
    "integration_domain": "0 <= d <= ceil(3*b/pi)*pi/b; |S| <= 8",
    "samples": samples,
    "weakest_sample": weakest,
    "all_samples_exceed_threshold": all(item["exceeds_source_threshold"] for item in samples),
    "interval_certified": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-first-mode-margin-scan.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for sample in samples:
        print(
            f"a={sample['a']:.2f} b={sample['b']:.1f} "
            f"ratio={sample['normalized_margin']:.10e} "
            f"passes={sample['exceeds_source_threshold']}"
        )
    print(f"source_threshold={source_threshold:.10e}")
    print(f"weakest_sample={weakest}")
