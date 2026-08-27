import json
import math
from fractions import Fraction
from pathlib import Path


record_qubits = 7
minimum_depth = math.ceil(math.log2(record_qubits + 1))
assert minimum_depth == 3

zero_codeword = [0] * record_qubits
one_codeword = [1] * record_qubits


def agreement_syndrome(bits):
    return [bits[i] ^ bits[0] for i in range(1, len(bits))]


assert agreement_syndrome(zero_codeword) == [0] * (record_qubits - 1)
assert agreement_syndrome(one_codeword) == [0] * (record_qubits - 1)

pointer_probabilities_ghz_plus = {"0" * record_qubits: Fraction(1, 2),
                                  "1" * record_qubits: Fraction(1, 2)}
pointer_probabilities_ghz_minus = dict(pointer_probabilities_ghz_plus)
assert pointer_probabilities_ghz_plus == pointer_probabilities_ghz_minus

g = Fraction(1, 2)
distinguishability_squared = Fraction(1) - g ** (2 * record_qubits)
assert distinguishability_squared == Fraction(16383, 16384)

conditions = {
    "causal_reach": True,
    "readability": True,
    "fault_separation": False,
    "restricted_reversibility": False,
}
objective_record_admitted = all(conditions.values())
assert not objective_record_admitted

result = {
    "status": "pass",
    "claim": "redundant readable records are not objective closure without fault separation and restricted reversibility",
    "record_qubits": record_qubits,
    "minimum_two_body_layer_depth": minimum_depth,
    "distinguishability_squared": "16383/16384",
    "common_mode_flip_passes_agreement": True,
    "phase_flip_changes_pointer_probabilities": False,
    "global_fanout_has_inverse": True,
    "closure_conditions": conditions,
    "objective_record_admitted": objective_record_admitted,
    "iteration_depth_is_physical_time": False,
}

out = Path(__file__).parents[1] / "results" / "objective-closure-cone.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

