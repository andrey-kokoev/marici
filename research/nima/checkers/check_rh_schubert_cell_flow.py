import json
from fractions import Fraction
from pathlib import Path


def unsafe_state(z):
    return (1 - z, z)


def unsafe_r(z):
    x, y = unsafe_state(z)
    return Fraction(y, x)


def safe_state(z):
    return (1, z)


samples = [Fraction(-2), Fraction(-1), Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)]
riccati_rows = []
for z in samples:
    r = unsafe_r(z)
    derivative = Fraction(1, (1 - z) ** 2)
    rhs = (1 + r) ** 2
    assert derivative == rhs
    riccati_rows.append({"z": str(z), "r": str(r), "r_prime": str(derivative)})

assert unsafe_state(Fraction(1)) == (0, 1)
assert all(safe_state(z)[0] == 1 for z in samples + [Fraction(1), Fraction(10)])

result = {
    "unsafe_generator": [[-1, -1], [1, 1]],
    "unsafe_hidden_to_observed_block_beta": -1,
    "unsafe_state_formula": "(1-z,z)",
    "unsafe_projective_formula": "z/(1-z)",
    "unsafe_chart_exit": "z=1",
    "unsafe_riccati_samples": riccati_rows,
    "safe_generator": [[0, 0], [1, 0]],
    "safe_hidden_to_observed_block_beta": 0,
    "safe_state_formula": "(1,z)",
    "safe_fixed_overlap": 1,
    "verdict": "zero exclusion is invariance of the fixed-observer Schubert big cell",
}

output = Path(__file__).parents[1] / "results" / "rh-schubert-cell-flow.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))

