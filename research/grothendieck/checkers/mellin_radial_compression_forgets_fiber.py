import json
from pathlib import Path

import sympy as sp


# Minimal two-point norm-one fiber. Radial Mellin compression sums over the
# fiber; the antisymmetric angular mode survives in the source but vanishes
# under every radial character.
R = sp.Matrix([[1, 1]])
angular = sp.Matrix([1, -1])
radial = sp.Matrix([1, 1])
Q = R.T * R

checks = {
    "angular_mode_is_nonzero": angular != sp.zeros(2, 1),
    "radial_compression_kills_angular_mode": R * angular == sp.zeros(1, 1),
    "radial_mode_survives": R * radial != sp.zeros(1, 1),
    "radial_gram_is_not_faithful": Q.det() == 0,
    "angular_mode_is_radial_gram_null": Q * angular == sp.zeros(2, 1),
}

result = {
    "schema": "marici.grothendieck.mellin-radial-compression-forgets-fiber.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "interpretation": "Mellin characters depend only on the idele norm. Radial compression annihilates nontrivial norm-one fiber modes, so a post-Mellin Green form is not a full-source form.",
}

out = Path(__file__).parents[1] / "results" / "mellin_radial_compression_forgets_fiber.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
