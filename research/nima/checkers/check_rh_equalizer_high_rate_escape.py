"""Exact high-rate completion hostile for the native reciprocal equalizer."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


z = Fraction(3, 4)
a = z - Fraction(1, 2)
b = Fraction(1)
rates = [Fraction(2**k) for k in range(1, 9)]

records = []
previous = None
for rate in rates:
    amplitude = Fraction(1)
    reservoir = (rate - Fraction(1, 2)) * amplitude / b
    plus_residual = (z - rate) * amplitude + b * reservoir
    minus_residual = (1 - z - rate) * amplitude + b * reservoir
    assert plus_residual == a * amplitude
    assert minus_residual == -a * amplitude

    state_norm_sq = amplitude**2 + reservoir**2
    sector_residual_sq = plus_residual**2 + minus_residual**2
    ratio_sq = sector_residual_sq / state_norm_sq
    expected = 2 * a**2 / (1 + (rate - Fraction(1, 2)) ** 2 / b**2)
    assert ratio_sq == expected
    if previous is not None:
        assert ratio_sq < previous
    previous = ratio_sq

    # Add the endpoint reservoir observation J_0(A,c)=c.
    augmented_ratio_sq = (sector_residual_sq + reservoir**2) / state_norm_sq
    assert augmented_ratio_sq >= Fraction(1, 2)
    records.append({
        "rate": str(rate),
        "sector_residual_ratio_squared": str(ratio_sq),
        "augmented_ratio_squared": str(augmented_ratio_sq),
    })

assert records[-1]["sector_residual_ratio_squared"] != "0"
assert previous < Fraction(1, 100000)

payload = {
    "schema": "marici.research.check.v1",
    "claim": "finite off-seam equalizer blocks lose their inverse margin at high source rate",
    "z": str(z),
    "normal_displacement": str(a),
    "records": records,
    "sector_margin_tends_to_zero": True,
    "endpoint_observation_repairs_this_escape_family": True,
    "verdict": "unweighted equalizer does not commute with completion",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()

out = Path(__file__).parents[1] / "results" / "rh-equalizer-high-rate-escape.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
