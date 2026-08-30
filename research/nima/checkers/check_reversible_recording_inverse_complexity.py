from fractions import Fraction
import json
from pathlib import Path


def compose(left, right):
    return tuple(left[right[i]] for i in range(len(left)))


def inverse(permutation):
    out = [0] * len(permutation)
    for i, image in enumerate(permutation):
        out[image] = i
    return tuple(out)


identity = tuple(range(4))

# Two-bit gates as exact basis permutations.
x0 = (2, 3, 0, 1)
cnot_01 = (0, 1, 3, 2)
assert compose(x0, x0) == identity
assert compose(cnot_01, cnot_01) == identity
assert compose(x0, cnot_01) != compose(cnot_01, x0)

# Recording applies X0 first and CNOT second.
recording = compose(cnot_01, x0)
correct_inverse = compose(inverse(x0), inverse(cnot_01))
wrong_same_order_replay = compose(cnot_01, x0)
assert compose(correct_inverse, recording) == identity
assert compose(wrong_same_order_replay, recording) != identity

# General finite words have inverse words of exactly equal length.
gates = (x0, cnot_01, x0, cnot_01, cnot_01, x0)
word = identity
for gate in gates:
    word = compose(gate, word)
inverse_word = identity
for gate in reversed(gates):
    inverse_word = compose(inverse(gate), inverse_word)
assert compose(inverse_word, word) == identity
assert len(gates) == len(tuple(reversed(gates)))

# Exact worst-case telescoping precision fixture.
length = 40
target_error = Fraction(1, 100)
per_gate_error = target_error / length
assert length * per_gate_error == target_error

result = {
    "schema": "marici.reversible-recording-inverse-complexity.v1",
    "recording_gate_count": len(gates),
    "inverse_gate_count": len(gates),
    "exact_inverse_passes": True,
    "same_order_replay_fails_for_noncommuting_gates": True,
    "ordered_history_required": True,
    "precision_fixture": {
        "length": length,
        "target_error": "1/100",
        "sufficient_per_gate_error": "1/4000",
    },
    "claim_boundary": "reversible circuit length alone supplies no computational arrow",
    "status": "pass",
}

output = Path(__file__).resolve().parents[1] / "results" / "reversible-recording-inverse-complexity.json"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
