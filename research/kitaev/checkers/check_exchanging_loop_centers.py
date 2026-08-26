import hashlib
import json
from pathlib import Path

import sympy as sp


x, l1, l2, q = sp.symbols("x l1 l2 q", real=True)

r1 = -x + l1
composite = sp.simplify(-r1 + l2)
assert composite == x + l2 - l1

center1 = l1 / 2
center2 = l2 / 2
assert sp.simplify((center2 - center1) * 2 - (l2 - l1)) == 0

# Common fixed point equations force equal displacements.
c = sp.symbols("c", real=True)
solutions = sp.solve([sp.Eq(c, -c + l1), sp.Eq(c, -c + l2)], [c, l2], dict=True)
assert solutions == [{c: l1 / 2, l2: l1}]

# Hostile pair r1(x)=-x, r2(x)=-x+2 generates translation by two.
hostile_delta = (l2 - l1).subs({l1: 0, l2: 2})
assert hostile_delta == 2
for repetitions in range(1, 9):
    assert x + repetitions * hostile_delta == x + 2 * repetitions

# Origin changes shift both centers equally and preserve their mismatch.
shifted_difference = sp.simplify((center2 + q) - (center1 + q))
assert shifted_difference == center2 - center1

payload = {
    "status": "pass",
    "theorem": "multiple_exchanging_loops_admit_bounded_safety_frame_only_when_centers_agree",
    "odd_loop": "r_i(x)=-x+ell_i",
    "odd_center": "ell_i/2",
    "two_odd_composite": "x -> x+ell_j-ell_i",
    "common_fixed_point_condition": "ell_i=ell_j for all odd loops",
    "bounded_orbit_condition": "all even translations vanish and all odd centers agree",
    "hostile_reflections": ["x -> -x", "x -> -x+2"],
    "hostile_composite": "x -> x+2",
    "center_mismatch_gauge_invariant": True,
    "theta_loop_generators_computed": False,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "exchanging-loop-centers.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
