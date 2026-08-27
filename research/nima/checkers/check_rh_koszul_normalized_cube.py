import json
from pathlib import Path


def koszul_sign(left_degree, right_degree):
    return -1 if (left_degree * right_degree) % 2 else 1


raw_residual = -1
typing_cases = []
for left_degree, right_degree in ((1, 1), (1, 0), (0, 1), (0, 0)):
    expected = koszul_sign(left_degree, right_degree)
    normalized = raw_residual * expected
    coherent = normalized == 1
    typing_cases.append({
        "left_degree": left_degree,
        "right_degree": right_degree,
        "expected_koszul_sign": expected,
        "raw_residual": raw_residual,
        "normalized_residual": normalized,
        "coherent": coherent,
    })

assert typing_cases[0]["coherent"] is True
assert all(case["coherent"] is False for case in typing_cases[1:])

# Reciprocal orientation is tracked separately and cannot be silently reused
# as the Koszul factor.
reciprocal_orientation_sign = -1
koszul_odd_odd_sign = -1
combined_declared_sign = reciprocal_orientation_sign * koszul_odd_odd_sign
assert combined_declared_sign == 1

result = {
    "typing_cases": typing_cases,
    "reciprocal_orientation_sign": reciprocal_orientation_sign,
    "odd_odd_koszul_sign": koszul_odd_odd_sign,
    "combined_declared_sign": combined_declared_sign,
    "sign_sources_must_remain_distinct": True,
    "verdict": "cube coherence is decided only after source-derived Koszul and reciprocal normalization",
}

output = Path(__file__).parents[1] / "results" / "rh-koszul-normalized-cube.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))

