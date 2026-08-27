from fractions import Fraction
import json
import math
from pathlib import Path


cutoffs = [1, 2, 4, 8, 16, 32, 64]


def partial_sums(increments):
    total = Fraction(0)
    values = []
    for increment in increments:
        total += increment
        values.append(total)
    return values


summable_increments = [Fraction(-1, 2**n) for n in range(1, max(cutoffs) + 1)]
summable_logs = partial_sums(summable_increments)
assert all(value > -1 for value in summable_logs)
assert summable_logs[-1] == -1 + Fraction(1, 2**max(cutoffs))

collapsing_increments = [Fraction(-1, n) for n in range(1, max(cutoffs) + 1)]
collapsing_logs = partial_sums(collapsing_increments)
reciprocal_logs = [-value for value in collapsing_logs]
assert all(left + right == 0 for left, right in zip(collapsing_logs, reciprocal_logs))

rows = []
for cutoff in cutoffs:
    index = cutoff - 1
    plus_log = collapsing_logs[index]
    minus_log = reciprocal_logs[index]
    rows.append(
        {
            "cutoff": cutoff,
            "collapsing_log_scale": str(plus_log),
            "reciprocal_log_scale": str(minus_log),
            "paired_log_scale": str(plus_log + minus_log),
        }
    )

assert collapsing_logs[-1] < collapsing_logs[31] < collapsing_logs[15]
assert math.exp(float(collapsing_logs[-1])) < math.exp(float(collapsing_logs[31]))

result = {
    "schema": "marici.rh.rotor-connection-scale.v1",
    "summable_connection_lower_log_bound": "-1",
    "summable_connection_scale_above_exp_minus_one": True,
    "harmonic_connection_log_scale_decreases_without_bound": True,
    "reciprocal_paired_log_scale": "0",
    "reciprocal_pair_hides_sector_collapse": True,
    "verdict": "nonvanishing requires a source-derived compact-uniform lower bound on real connection integrals",
}

out = Path(__file__).parents[1] / "results" / "rh-rotor-connection-scale.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
