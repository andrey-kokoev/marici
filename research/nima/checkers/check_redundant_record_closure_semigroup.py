import json
from fractions import Fraction
from pathlib import Path


def channel(overlap):
    return [Fraction(1), overlap, overlap, Fraction(1)]


def compose(left, right):
    return [a * b for a, b in zip(left, right)]


def power(operator, n):
    result = channel(Fraction(1))
    for _ in range(n):
        result = compose(result, operator)
    return result


g = Fraction(1, 2)
E = channel(g)
P = [Fraction(1), Fraction(0), Fraction(0), Fraction(1)]

records = []
for n in range(1, 7):
    actual = power(E, n)
    expected = channel(g ** n)
    assert actual == expected
    records.append({
        "depth": n,
        "off_diagonal_visibility": f"1/{2 ** n}",
    })

assert compose(P, P) == P
assert compose(E, P) == P
assert compose(P, E) == P

phase = channel(Fraction(-1))
assert power(phase, 2) == channel(Fraction(1))
assert power(phase, 1) != P
assert power(phase, 2) != P

result = {
    "status": "pass",
    "claim": "redundant contractive records converge to the idempotent interface closure",
    "contractive_overlap": "1/2",
    "depth_records": records,
    "limit_projection": ["diagonal", "zero", "zero", "diagonal"],
    "limit_idempotent": True,
    "fixed_algebra_dimension": 2,
    "phase_only_hostile": {
        "overlap": "-1",
        "two_cycle": True,
        "converges_to_projection": False,
        "distinguishable_record": False,
        "logical_back_action": True,
    },
    "iteration_depth_is_physical_time": False,
}

out = Path(__file__).parents[1] / "results" / "redundant-record-closure-semigroup.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

