import json
import math
from pathlib import Path


def synthesize(v, cutoff):
    return (v[0], v[1] / cutoff)


def defect(v, h, cutoff):
    image = synthesize(v, cutoff)
    return (image[0] - h[0], image[1] - h[1])


def norm(vector):
    return math.sqrt(sum(value * value for value in vector))


cutoffs = [1, 2, 4, 8, 16, 32, 64]
escape = (0.0, 1.0)
rows = []

for cutoff in cutoffs:
    image = synthesize(escape, cutoff)
    assert defect(escape, image, cutoff) == (0.0, 0.0)
    analytic_norm = norm(image)
    arithmetic_norm = norm(escape)
    graph_norm = math.sqrt(arithmetic_norm**2 + analytic_norm**2)
    anomaly_trace = escape[1]
    rows.append(
        {
            "cutoff": cutoff,
            "analytic_norm": analytic_norm,
            "arithmetic_norm": arithmetic_norm,
            "graph_norm": graph_norm,
            "anomaly_trace": anomaly_trace,
        }
    )

assert all(right["analytic_norm"] < left["analytic_norm"] for left, right in zip(rows, rows[1:]))
assert all(row["arithmetic_norm"] == 1 for row in rows)
assert all(row["anomaly_trace"] == 1 for row in rows)
assert all(row["graph_norm"] >= 1 for row in rows)

unmatched = defect(escape, (0.0, 0.0), cutoffs[-1])
assert unmatched != (0.0, 0.0)

result = {
    "schema": "marici.rh.arithmetic-analytic-synthesis-graph.v1",
    "cutoffs": cutoffs,
    "final_analytic_norm": rows[-1]["analytic_norm"],
    "arithmetic_norm": 1,
    "anomaly_trace": 1,
    "graph_norm_uniform_lower_bound": 1,
    "unmatched_defect_detected": True,
    "verdict": "retain the graph of source synthesis because analytic quotienting erases arithmetic anomaly data",
}

out = Path(__file__).parents[1] / "results" / "rh-arithmetic-analytic-synthesis-graph.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
