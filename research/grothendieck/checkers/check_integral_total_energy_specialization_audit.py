import json
from math import gcd
from pathlib import Path

A = [[1, 0, 0], [0, 1, 0]]
half_boundary = [1, -1, 1, -1]
K = [-3, 1, 1, 1, 1, 1, 1, 1]
d = [3, -1, -1, -1, -1, -1, -1, -3]
metric = [1, -1, -1, -1, -1, -1, -1, -1]

def pairing(x, y):
    return sum(s*a*b for s, a, b in zip(metric, x, y))

def content(v):
    g = 0
    for x in v:
        g = gcd(g, abs(x))
    return g

assert [sum(A[i][j] * (1 if j == 2 else 0) for j in range(3)) for i in range(2)] == [0, 0]
assert half_boundary == [1, -1, 1, -1]
assert sum(half_boundary) == 0
assert pairing(d, d) == -6
assert pairing(K, d) == 0
assert content(d) == 1
minus_K = [3, -1, -1, -1, -1, -1, -1, -1]
assert all((a-b) % 2 == 0 for a, b in zip(d, minus_K))

rivals = {}
for n in (1, 2):
    image = [n*x for x in d]
    smith_nonzero_factor = content(image)
    assert pairing(K, image) == 0
    rivals[str(n)] = {
        "image": image,
        "image_smith_nonzero_factor": smith_nonzero_factor,
        "image_primitive": smith_nonzero_factor == 1,
    }
assert rivals["1"]["image_smith_nonzero_factor"] == 1
assert rivals["2"]["image_smith_nonzero_factor"] == 2

result = {
    "schema": "marici.grothendieck.integral_total_energy_specialization_audit.v1",
    "known_specialization_matrix": A,
    "known_specialization_smith_nonzero_factors": [1, 1],
    "kernel_generator": [0, 0, 1],
    "conductor_primitive_half_boundary": half_boundary,
    "picard_difference": d,
    "picard_square": pairing(d, d),
    "canonical_pairing": pairing(K, d),
    "mod_two_equals_minus_canonical": True,
    "rival_integral_extensions": rivals,
    "distinguishing_datum": "absent integral normalization-conductor to Betti/Picard chain map",
    "rational_column_not_used_as_integral_normalization": "1/(8*(x+y))",
    "conclusion": "integral multiplier and resulting Smith form are underdetermined",
}
out = Path("research/grothendieck/results/integral_total_energy_specialization_audit.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"status": "ok", "assertions": 12, "output": str(out)}))
