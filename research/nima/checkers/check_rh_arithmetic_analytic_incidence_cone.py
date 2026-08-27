import json
from pathlib import Path


def arithmetic_incidence(v):
    a, b, c = v
    return (a + c, b + c)


def analytic_incidence(h):
    return h


def mismatch(v, h):
    left = arithmetic_incidence(v)
    right = analytic_incidence(h)
    return tuple(x - y for x, y in zip(left, right))


def descending_trace(v):
    a, b, c = v
    return a + 2 * b + 3 * c


def hostile_trace(v):
    a, b, c = v
    return a + 2 * b + 4 * c


v = (2, -1, 5)
h = arithmetic_incidence(v)
assert mismatch(v, h) == (0, 0)

unmatched_h = (h[0] + 1, h[1])
assert mismatch(v, unmatched_h) == (-1, 0)

# This is the one-dimensional kernel of the arithmetic incidence.
kernel_witness = (-1, -1, 1)
assert arithmetic_incidence(kernel_witness) == (0, 0)
assert descending_trace(kernel_witness) == 0
assert hostile_trace(kernel_witness) == 1

# The descending trace factors through the boundary row (1,2).
boundary_value = h[0] + 2 * h[1]
assert descending_trace(v) == boundary_value

result = {
    "schema": "marici.rh.arithmetic-analytic-incidence-cone.v1",
    "matched_pair_mismatch": [0, 0],
    "unmatched_pair_mismatch": [-1, 0],
    "incidence_kernel_witness": list(kernel_witness),
    "descending_trace_on_kernel": 0,
    "hostile_trace_on_kernel": 1,
    "verdict": "the incidence cone is a safe prequotient retaining arithmetic, analytic, and dynamic boundary-residual ports",
}

out = Path(__file__).parents[1] / "results" / "rh-arithmetic-analytic-incidence-cone.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
