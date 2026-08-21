"""Exact D3 control for the paired radiative memory/charge readout."""

import json
from itertools import product
from pathlib import Path


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def mv(a, v):
    return [sum(a[i][j] * v[j] for j in range(2)) for i in range(2)]


def tr(a):
    return [[a[j][i] for j in range(2)] for i in range(2)]


def pair(f, v, g):
    return sum(f[i] * g[i][j] * v[j] for i in range(2) for j in range(2))


I = [[1, 0], [0, 1]]
r = [[0, -1], [1, -1]]
s = [[1, 0], [1, -1]]
G = [[2, -1], [-1, 2]]  # polar form of 2(a^2-ab+b^2)

group = []
cur = I
for _ in range(3):
    group.append(cur)
    group.append(mm(s, cur))
    cur = mm(r, cur)
assert len({tuple(sum(x, [])) for x in group}) == 6

metric_checks = pairing_checks = fixed_detector_failures = 0
for h in group:
    assert mm(mm(tr(h), G), h) == G
    metric_checks += 1
    for f in product(range(-3, 4), repeat=2):
        for v in product(range(-3, 4), repeat=2):
            assert pair(mv(h, f), mv(h, v), G) == pair(f, v, G)
            pairing_checks += 1
            if pair(f, mv(h, v), G) != pair(f, v, G):
                fixed_detector_failures += 1

assert fixed_detector_failures > 0
result = {
    "schema": "marici.radiative_memory.paired_readout.v1",
    "source_entry": 1056,
    "invariant_metric": G,
    "metric_checks": metric_checks,
    "simultaneous_pairing_checks": pairing_checks,
    "fixed_detector_failure_count": fixed_detector_failures,
    "passed": True,
    "verdict": "memory and detector must be transported together",
}
out = Path(__file__).with_name("results") / "radiative-memory-paired-readout.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))
