import hashlib
import json
from fractions import Fraction
from pathlib import Path


def distance(left, right):
    z, bit = left
    w, other_bit = right
    return abs(z - w) + abs(bit - other_bit)


sequence = [(Fraction(1, n), 1) for n in (2, 4, 8, 16, 32)]
labelled_zero = (Fraction(0), 1)
unlabelled_zero = (Fraction(0), 0)

distances_to_limit = [distance(point, labelled_zero) for point in sequence]
assert distances_to_limit == [Fraction(1, n) for n in (2, 4, 8, 16, 32)]
assert labelled_zero not in ({unlabelled_zero} | set(sequence))
assert distance(labelled_zero, unlabelled_zero) == 1

delta = Fraction(1, 4)
gapped_nonzero = [(z, 1) for z in (-1, -delta, delta, 1)]
assert all(distance(point, unlabelled_zero) >= delta for point in gapped_nonzero)

# A branch decoder proportional to 1/|z| still diverges with a constant bit.
decoder_costs = [1 / abs(z) for z, bit in sequence if bit == 1]
assert decoder_costs == [2, 4, 8, 16, 32]

payload = {
    "status": "pass",
    "theorem": "a_discrete_support_bit_does_not_complete_the_nonzero_branch",
    "sequence_distances_to_labelled_zero": [str(x) for x in distances_to_limit],
    "completion_adds": ["z=0", "bit=1"],
    "live_support_repair": "uniform gap",
    "alternative_semantics": "provenance bit with labelled-zero states",
    "gapped_separation": str(delta),
    "decoder_costs_despite_constant_bit": [int(x) for x in decoder_costs],
    "scalar_defect_port_ceiling_respected": True,
    "theta_application_frozen": True,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "discrete-support-bit-completion.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
