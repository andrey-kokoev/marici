import json
from pathlib import Path


states = (0, 1, 2, 3)

# Both operations are idempotent. They stabilize state 0 toward different
# source representatives.
closure_a = {0: 1, 1: 1, 2: 2, 3: 3}
closure_b = {0: 2, 1: 1, 2: 2, 3: 3}


def compose(first: dict[int, int], second: dict[int, int]) -> dict[int, int]:
    return {x: second[first[x]] for x in states}


def kernel_pairs(function: dict[int, int]) -> list[tuple[int, int]]:
    return [
        (x, y)
        for x in states
        for y in states
        if x <= y and function[x] == function[y]
    ]


def is_idempotent(function: dict[int, int]) -> bool:
    return compose(function, function) == function


ab = compose(closure_a, closure_b)
ba = compose(closure_b, closure_a)

# The scalar readout deliberately identifies stabilized representatives 1 and
# 2 while retaining state 3.
readout = {0: "x", 1: "x", 2: "x", 3: "y"}
readout_ab = {x: readout[ab[x]] for x in states}
readout_ba = {x: readout[ba[x]] for x in states}

kernel_ab = kernel_pairs(ab)
kernel_ba = kernel_pairs(ba)

assert is_idempotent(closure_a)
assert is_idempotent(closure_b)
assert ab != ba
assert readout_ab == readout_ba
assert kernel_ab != kernel_ba
assert (0, 1) in kernel_ab and (0, 1) not in kernel_ba
assert (0, 2) in kernel_ba and (0, 2) not in kernel_ab

result = {
    "schema": "marici.nima.provenance-bearing-closures.v1",
    "status": "pass",
    "closure_a_idempotent": True,
    "closure_b_idempotent": True,
    "composite_ab": ab,
    "composite_ba": ba,
    "scalar_readouts_equal": readout_ab == readout_ba,
    "kernel_ab": kernel_ab,
    "kernel_ba": kernel_ba,
    "kernel_pairs_differ": kernel_ab != kernel_ba,
    "interchange_authorized": False,
}

output = Path(__file__).parents[1] / "results" / "provenance-bearing-closures.json"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
