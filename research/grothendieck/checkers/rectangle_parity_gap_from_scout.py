"""Infer effective squared-spectral gaps from positive rectangle determinants."""

import json
import math
from pathlib import Path

ROOT = Path(__file__).parents[1]
source = ROOT / "results" / "gaussian-translation-weil-rectangle-scout.json"
rows = json.loads(source.read_text(encoding="utf-8"))["rows"]

estimates = []
for left, right in zip(rows, rows[1:]):
    t0, t1 = float(left["t"]), float(right["t"])
    record = {"t_left": t0, "t_right": t1}
    for key in ("D_plus", "D_minus"):
        d0, d1 = float(left[key]), float(right[key])
        record[f"effective_gap_from_{key}"] = math.log(d0 / d1) / (t1 - t0)
    estimates.append(record)

late = estimates[-3:]
plus = [row["effective_gap_from_D_plus"] for row in late]
minus = [row["effective_gap_from_D_minus"] for row in late]
result = {
    "schema": "marici.grothendieck.rectangle-parity-gap-scout.v1",
    "estimates": estimates,
    "late_plus_range": [min(plus), max(plus)],
    "late_minus_range": [min(minus), max(minus)],
    "late_channel_max_difference": max(abs(a - b) for a, b in zip(plus, minus)),
    "claim_boundary": "Derived from non-certified determinant samples; discovery evidence only.",
}
output = ROOT / "results" / "rectangle-parity-gap-scout.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
