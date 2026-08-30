"""Dense all-angle falsifier for the exact one-loop QED Bell minimum."""

import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_exact_qed_bell_onset import bell


mp.mp.dps = 35

if __name__ == "__main__":
    onset = mp.mpf("0.42015760875460728129837661981582642")
    energies = (mp.mpf("0.4"), onset, mp.mpf("0.43"))
    count = 1024
    summaries = []
    for y in energies:
        values = []
        for i in range(1, count + 1):
            x = mp.mpf(i) / (2 * count)
            values.append(bell(y, x))
        drops = [values[i] - values[i + 1] for i in range(count - 1)]
        assert min(drops) > 0
        h = mp.mpf(1) / (2 * count)
        transverse_curvature = 2 * (values[-2] - values[-1]) / h**2
        assert transverse_curvature > 0
        summaries.append(
            {
                "y": str(y),
                "points_on_half_interval": count,
                "smallest_adjacent_drop": str(min(drops)),
                "largest_adjacent_drop": str(max(drops)),
                "transverse_value": str(values[-1]),
                "one_sided_transverse_curvature_estimate": str(transverse_curvature),
                "strictly_decreasing_toward_transverse": True,
            }
        )
    payload = {
        "schema": "marici.exact-qed-global-angular-audit.v1",
        "summaries": summaries,
        "symmetry": "x maps to 1-x, so the half-interval census covers the full physical angular interval",
        "verdict": "No secondary angular minimum or stationary reversal appears on 3072 exact-amplitude samples around the onset; the transverse point remains the unique sampled global minimum.",
        "scope": "High-density falsifier, not an interval-arithmetic continuum proof.",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
    out = Path(__file__).parent / "results" / "exact-qed-global-angular-audit.json"
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"samples": 3 * count, "summaries": summaries}))
