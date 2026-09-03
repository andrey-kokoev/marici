"""Enumerate finite prime-power coefficient masses for support windows."""

import json
import math
from pathlib import Path


def von_mangoldt(limit):
    values = [0.0] * (limit + 1)
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, limit + 1):
        if not sieve[p]:
            continue
        power = p
        while power <= limit:
            values[power] = math.log(p)
            if power > limit // p:
                break
            power *= p
        if p * p <= limit:
            sieve[p * p : limit + 1 : p] = b"\x00" * (((limit - p * p) // p) + 1)
    return values


rows = []
for L in (1, 2, 3, 4, 5):
    limit = int(math.floor(math.exp(2 * L)))
    mangoldt = von_mangoldt(limit)
    mass = sum(mangoldt[n] / math.sqrt(n) for n in range(2, limit + 1))
    bound = 4 * L * math.exp(L)
    rows.append(
        {
            "L": L,
            "prime_power_cutoff": limit,
            "coefficient_mass": mass,
            "elementary_bound_kappa_one": bound,
            "ratio_to_bound": mass / bound,
            "bound_passes": mass <= bound,
        }
    )

result = {
    "schema": "marici.grothendieck.fixed-support-prime-translation-norm-scout.v1",
    "rows": rows,
    "all_bounds_pass": all(row["bound_passes"] for row in rows),
    "claim_boundary": "Floating enumeration checks samples; the bound itself follows from Lambda(n)<=log n and the elementary reciprocal-square-root sum.",
}
assert result["all_bounds_pass"]
output = Path(__file__).parents[1] / "results" / "fixed-support-prime-translation-norm-scout.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
