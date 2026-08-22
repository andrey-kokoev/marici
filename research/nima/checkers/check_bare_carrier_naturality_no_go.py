import itertools
import json
from pathlib import Path


P = 5
OUT = Path(__file__).resolve().parents[1] / "results" / "bare_carrier_naturality_no_go.json"


def normalize(v):
    x, y = (v[0] % P, v[1] % P)
    pivot = x if x else y
    inv = pow(pivot, -1, P)
    return ((x * inv) % P, (y * inv) % P)


lines = sorted({normalize(v) for v in itertools.product(range(P), repeat=2) if v != (0, 0)})
gl2 = [
    ((a, b), (c, d))
    for a, b, c, d in itertools.product(range(P), repeat=4)
    if (a * d - b * c) % P
]


def act(g, line):
    x, y = line
    return normalize(((g[0][0] * x + g[0][1] * y) % P, (g[1][0] * x + g[1][1] * y) % P))


globally_invariant_lines = [line for line in lines if all(act(g, line) == line for g in gl2)]

result = {
    "checker": "bare_carrier_naturality_no_go",
    "field": f"F_{P}",
    "carrier_dimension": 2,
    "automorphism_group_order": len(gl2),
    "candidate_nonzero_proper_subspaces": len(lines),
    "globally_invariant_nonzero_proper_subspaces": globally_invariant_lines,
    "only_universal_invariant_subspaces": ["0", "V"],
    "bare_carrier_nontrivial_natural_filtration_possible": bool(globally_invariant_lines),
    "no_go_pass": not globally_invariant_lines,
}

assert len(lines) == P + 1
assert len(gl2) == (P * P - 1) * (P * P - P)
assert result["no_go_pass"]
OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
