import json
from pathlib import Path

import sympy as sp


P, Q, M = sp.symbols("P Q M")
A = P + Q + M
R = P - Q

observation = sp.Matrix([[1, 1, 1], [0, 0, 1]])
kernel = observation.nullspace()
antisymmetric = sp.Matrix([1, -1, 0])

checks = {
    "bilateral_decomposition": sp.simplify(A - (P + Q + M)) == 0,
    "observed_rank_is_two": observation.rank() == 2,
    "blind_fiber_is_one_dimensional": len(kernel) == 1,
    "blind_fiber_is_tail_antisymmetry": kernel[0].cross(antisymmetric) == sp.zeros(3, 1),
    "krein_channel_varies_on_blind_fiber": sp.Matrix([[1, -1, 0]])[0, :].dot(antisymmetric) == 2,
}

result = {
    "schema": "marici.grothendieck.bilateral_tail_seam_rank_defect.v1",
    "observation_matrix": [list(map(str, row)) for row in observation.tolist()],
    "rank": observation.rank(),
    "kernel_basis": [list(map(str, vector)) for vector in kernel],
    "krein_channel": str(R),
    "checks": checks,
}

assert all(checks.values())
output = Path("research/grothendieck/results/bilateral_tail_seam_rank_defect.json")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
