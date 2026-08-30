import hashlib
import json
from pathlib import Path

import sympy as sp


lam, gap = sp.symbols("lambda Delta", positive=True)


def virtual_block(length):
    internal = length - 1
    block = gap * sp.eye(internal)
    for index in range(internal - 1):
        block[index, index + 1] = lam
        block[index + 1, index] = lam
    return block


leading_coefficients = {}
for length in range(2, 7):
    Q = virtual_block(length)
    amplitude = sp.simplify(lam**2 * (-Q).inv()[0, Q.rows - 1])
    coefficient = sp.simplify(sp.limit(amplitude / lam**length, lam, 0))
    expected = sp.simplify((-1) ** (length - 1) / gap ** (length - 1))
    assert coefficient == expected
    leading_coefficients[str(length)] = str(coefficient)

# Two identical length-four paths with opposite right-endpoint signs.
length = 4
Q = virtual_block(length)
Q_double = sp.diag(Q, Q)
internal = Q.rows
B = sp.zeros(2, 2 * internal)
B[0, 0] = lam
B[0, internal] = lam
B[1, internal - 1] = lam
B[1, 2 * internal - 1] = -lam
effective = sp.simplify(B * (-Q_double).inv() * B.T)
assert sp.simplify(effective[0, 1]) == 0
assert sp.simplify(effective[1, 0]) == 0
assert sp.simplify(effective[0, 0] - effective[1, 1]) == 0

payload = {
    "status": "pass",
    "theorem": "a_minimal_winding_channel_has_a_computable_fine_structure_amplitude",
    "leading_coefficients_by_path_length": leading_coefficients,
    "leading_formula": "(-1)^(L-1)/Delta^(L-1)",
    "paired_length_four_off_diagonal": "0 exactly",
    "paired_effective_operator_scalar": True,
    "distance_guarantees_nonzero_coefficient": False,
    "uniform_suppression_condition": "mu*abs(lambda) < Delta",
    "toric_source_coefficient_computed": False,
    "theta_path_formula_inferred": False,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "minimal-winding-amplitude.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
