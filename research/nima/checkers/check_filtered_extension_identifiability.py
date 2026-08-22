import itertools
import json
from pathlib import Path


P = 5
OUT = Path(__file__).resolve().parents[1] / "results" / "filtered_extension_identifiability.json"


def normalize(v):
    x, y = (v[0] % P, v[1] % P)
    if x:
        inv = pow(x, -1, P)
    else:
        inv = pow(y, -1, P)
    return ((x * inv) % P, (y * inv) % P)


lines = sorted({normalize(v) for v in itertools.product(range(P), repeat=2) if v != (0, 0)})

# T and the total record are both identities. Every line is T-invariant, and
# simultaneous change of basis preserves both pieces of total-object data.
T = ((1, 0), (0, 1))
record = ((1, 0), (0, 1))

gl2 = []
for a, b, c, d in itertools.product(range(P), repeat=4):
    if (a * d - b * c) % P:
        gl2.append(((a, b), (c, d)))

orbit = {
    normalize(((g[0][0] * 1 + g[0][1] * 0) % P, (g[1][0] * 1 + g[1][1] * 0) % P))
    for g in gl2
}

result = {
    "checker": "filtered_extension_identifiability",
    "field": f"F_{P}",
    "total_transport": T,
    "total_record": record,
    "nonzero_proper_invariant_lines": lines,
    "invariant_line_count": len(lines),
    "expected_projective_line_count": P + 1,
    "gl2_order": len(gl2),
    "gl2_orbit_of_one_line": sorted(orbit),
    "orbit_is_all_filtrations": orbit == set(lines),
    "degenerate_filtrations_always_exist": ["0 subset E", "E subset E"],
    "filtration_identifiable_from_total_data": len(lines) == 1,
    "existential_extension_explanation_falsified": len(lines) > 1 and orbit == set(lines),
}

assert len(lines) == P + 1
assert len(gl2) == (P * P - 1) * (P * P - P)
assert result["existential_extension_explanation_falsified"]
OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
