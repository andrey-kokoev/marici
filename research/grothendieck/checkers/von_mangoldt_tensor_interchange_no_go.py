"""Exact support audit for the first coprime arithmetic rectangle."""

import math


p, q = 2, 3
w_p = math.log(p) / math.sqrt(p)
w_q = math.log(q) / math.sqrt(q)
w_pq = 0.0  # Lambda(6)=0 because 6 is not a prime power.

assert w_p > 0 and w_q > 0
assert w_p * w_q > 0
assert w_pq == 0
assert w_pq != w_p * w_q

result = {
    "first_coprime_pair": [p, q],
    "Lambda(p)_nonzero": True,
    "Lambda(q)_nonzero": True,
    "Lambda(pq)": "0",
    "product_edge_nonzero": True,
    "arithmetic_tensor_interchange_falsified": True,
    "completed_gamma_endpoint_defect_still_to_test": True,
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "von-mangoldt-tensor-interchange-no-go.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")

