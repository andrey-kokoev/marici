from fractions import Fraction
import json
from pathlib import Path


def edge(n):
    return Fraction(n, n + 1)


def composite(start, end):
    value = Fraction(1)
    for n in range(start, end):
        value *= edge(n)
    return value


for x in range(1, 8):
    for y in range(x, 9):
        for z in range(y, 10):
            assert composite(x, z) == composite(y, z) * composite(x, y)

samples = {str(n): str(composite(1, n)) for n in (2, 4, 8, 16, 32, 64)}
assert composite(1, 64) == Fraction(1, 64)

result = {
    "schema": "marici.rh-determinant-unit-completion.v1",
    "edge_unit": "u_(n,n+1)=n/(n+1)",
    "every_finite_edge_is_invertible": True,
    "cocycle_holds": True,
    "base_to_cutoff_units": samples,
    "completion_limit": "0",
    "invertibility_survives_completion": False,
    "required_gate": "locally_uniform_control_of_units_and_reciprocals",
}

out = Path(__file__).parents[1] / "results" / "rh-determinant-unit-completion.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
