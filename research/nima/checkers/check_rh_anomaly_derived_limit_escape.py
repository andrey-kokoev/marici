import json
from pathlib import Path


def normalized_potentials(increments):
    values = [0]
    for increment in increments:
        values.append(values[-1] + increment)
    return values


bounded_increments = [1, -1] * 16
bounded = normalized_potentials(bounded_increments)
assert max(abs(value) for value in bounded) == 1

escape_increments = [1] * 32
escape = normalized_potentials(escape_increments)
assert all(escape[i + 1] - escape[i] == 1 for i in range(len(escape) - 1))
assert max(abs(value) for value in escape) == 32

opposite_escape = normalized_potentials([-1] * 32)
assert all(left + right == 0 for left, right in zip(escape, opposite_escape))
assert max(abs(value) for value in opposite_escape) == 32

# A global additive gauge shift cannot remove growth once the base frame is
# fixed; all differences from the base are invariant.
for shift in (-17, 0, 23):
    shifted = [value + shift for value in escape]
    assert [value - shifted[0] for value in shifted] == escape

# Exact finite solutions can still fail a declared bonding rule.
coarse = normalized_potentials([1, 1])
fine = normalized_potentials([1, 0, 1, 0])
wrong_restriction = [fine[0], fine[1], fine[2]]
assert wrong_restriction != coarse

result = {
    "schema": "marici.rh.anomaly-derived-limit-escape.v1",
    "bounded_fixture_supremum": max(abs(value) for value in bounded),
    "escape_fixture_supremum": max(abs(value) for value in escape),
    "every_escape_prefix_exact": True,
    "base_fixed_gauge_removes_escape": False,
    "typed_opposite_escapes_have_zero_scalar_sum": True,
    "incompatible_bonding_detected": True,
    "verdict": "finite coboundaries require a compatible bounded cutoff-natural contraction",
}

out = Path(__file__).parents[1] / "results" / "rh-anomaly-derived-limit-escape.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
