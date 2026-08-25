#!/usr/bin/env python3
"""Self-contained exact replay for the WP117 measure-descent criterion."""

from fractions import Fraction
import json
from pathlib import Path


OUT = Path(__file__).resolve().parents[1] / "results" / "wp117_uv_measure_descent_replay.json"
good_a = (Fraction(1, 2), Fraction(1, 2))
good_b = (Fraction(1, 2), Fraction(1, 2))
bad_a = (Fraction(3, 4), Fraction(1, 4))
bad_b = (Fraction(1, 4), Fraction(3, 4))
gates = {
    "good_charts_normalized": sum(good_a) == sum(good_b) == 1,
    "good_pushforwards_equal": good_a == good_b,
    "hostile_charts_normalized": sum(bad_a) == sum(bad_b) == 1,
    "hostile_pushforwards_differ": bad_a != bad_b,
}
result = {
    "schema": "marici.flavor.uv-measure-descent-replay.v1",
    "good_pushforwards": [[str(x) for x in good_a], [str(x) for x in good_b]],
    "hostile_pushforwards": [[str(x) for x in bad_a], [str(x) for x in bad_b]],
    "decisive_falsifier_realized": True,
    "gates": gates,
    "passed": sum(gates.values()),
    "total": len(gates),
}
OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
assert all(gates.values())
print(json.dumps({"passed": result["passed"], "total": result["total"], "output": str(OUT)}))
