import hashlib
import json
from pathlib import Path

import sympy as sp


x = sp.Integer(2)
root_sinh = sp.sqrt(x**2 - 1)

# Chebyshev identities at cosh(a)=2.
cosh_1 = x
cosh_2 = sp.chebyshevt(2, x)
cosh_3 = sp.chebyshevt(3, x)
cosh_4 = sp.chebyshevt(4, x)
sinh_1 = root_sinh * sp.chebyshevu(0, x)
sinh_2 = root_sinh * sp.chebyshevu(1, x)
sinh_3 = root_sinh * sp.chebyshevu(2, x)

assert (cosh_1, cosh_2, cosh_3, cosh_4) == (2, 7, 26, 97)
assert tuple(sp.simplify(v / sp.sqrt(3)) for v in (sinh_1, sinh_2, sinh_3)) == (1, 4, 15)

# At z=a+i*pi, odd shells acquire a minus sign and even shells a plus sign.
background_value = -cosh_1 + 4 * cosh_2 - cosh_3
background_derivative = -sinh_1 + 8 * sinh_2 - 3 * sinh_3
block_value = -cosh_3 + cosh_4
velocity = sp.simplify(-block_value / background_derivative)

assert background_value == 0
assert sp.simplify(background_derivative) == -14 * sp.sqrt(3)
assert block_value == 71
assert velocity == 71 * sp.sqrt(3) / 42
assert velocity > 0

payload = {
    "status": "pass",
    "theorem": "local_odd_even_dominance_does_not_compose_into_inward_divisor_transport",
    "cosh_a": "2",
    "background_coefficients_shells_1_to_3": [1, 4, 1],
    "background_zero": "exact",
    "background_derivative": "-14*sqrt(3)",
    "added_block_shells": [3, 4],
    "added_block_coefficients": [1, 1],
    "outer_even_dominates_inner_odd": True,
    "block_value_at_zero": "71",
    "zero_velocity": "71/(14*sqrt(3))",
    "motion": "outward",
    "context_free_dominance_implication": False,
    "required_repair": "control relative phase of block evaluation and background derivative",
    "source_cone_excluded": False,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "contextual-odd-even-dominance.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
