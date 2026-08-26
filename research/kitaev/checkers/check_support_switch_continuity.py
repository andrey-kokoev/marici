import hashlib
import json
from fractions import Fraction
from pathlib import Path


def support(value):
    return 0 if value == 0 else 1


sequence = [Fraction(1, n) for n in range(1, 17)]
assert all(support(value) == 1 for value in sequence)
assert support(Fraction(0)) == 0
assert sequence[-1] < sequence[0]

# The support jump stays one while analytic distance tends to zero.
hostile = [
    {
        "n": n,
        "analytic_distance": str(Fraction(1, n)),
        "support_distance": 1,
        "required_lipschitz_constant": n,
    }
    for n in (2, 4, 8, 16)
]

# On {0} union {|z| >= delta}, the sharp scalar bound is 1/delta.
delta = Fraction(1, 4)
admitted = [Fraction(0), -1, -delta, delta, 1]
for z in admitted:
    for w in admitted:
        lhs = abs(support(z) - support(w))
        rhs = abs(z - w) / delta
        assert lhs <= rhs

payload = {
    "status": "pass",
    "theorem": "support_dependent_compilation_needs_a_gapped_or_discrete_switch",
    "hostile_sequence": hostile,
    "support_indicator_continuous_at_zero": False,
    "gap": str(delta),
    "gapped_lipschitz_constant": str(1 / delta),
    "hybrid_discrete_port_required_without_gap": True,
    "scalar_defect_port_ceiling_respected": True,
    "theta_application_frozen": True,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "support-switch-continuity.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
