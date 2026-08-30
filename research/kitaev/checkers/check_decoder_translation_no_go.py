import hashlib
import itertools
import json
from pathlib import Path


H = list(itertools.product(range(2), repeat=2))


def add(left, right):
    return tuple((a + b) % 2 for a, b in zip(left, right))


fixed_by_all = [point for point in H if all(add(point, shift) == point for shift in H)]
assert fixed_by_all == []

nonzero = [shift for shift in H if shift != (0, 0)]
fixed_by_nonzero = {
    shift: [point for point in H if add(point, shift) == point] for shift in nonzero
}
assert all(points == [] for points in fixed_by_nonzero.values())

# The uniform distribution is invariant, but it does not select a point.
uniform_weight = {point: "1/4" for point in H}
for shift in H:
    translated = {add(point, shift): weight for point, weight in uniform_weight.items()}
    assert translated == uniform_weight

reference = (0, 0)
coordinates_from_reference = {str(point): add(point, reference) for point in H}
assert len(set(coordinates_from_reference.values())) == 4

payload = {
    "status": "pass",
    "theorem": "no_deterministic_decoder_is_canonical_under_logical_translations",
    "logical_group": "F2^2",
    "torsor_size": len(H),
    "global_fixed_points": len(fixed_by_all),
    "fixed_points_by_nonzero_translation": {
        str(key): len(value) for key, value in fixed_by_nonzero.items()
    },
    "uniform_randomized_rule_translation_invariant": True,
    "uniform_randomized_rule_selects_origin": False,
    "pointed_reference_selects_origin": True,
    "reference_breaks_translation_symmetry": True,
    "physical_decoder_constructed": False,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "decoder-translation-no-go.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
