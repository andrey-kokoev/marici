import json
from pathlib import Path

import sympy as sp


checks = {}
exact = {}

for order in range(13):
    dimension = order + 1
    shift = sp.zeros(dimension)
    for row in range(1, dimension):
        shift[row, row - 1] = 1

    coefficients = sp.Matrix(sp.symbols(f"a0:{dimension}"))
    expected = sp.Matrix([0] + list(coefficients[:-1]))
    checks[f"jet_{order}_residue_shift"] = shift * coefficients == expected
    checks[f"jet_{order}_singular"] = shift.det() == 0
    checks[f"jet_{order}_nilpotent"] = shift ** dimension == sp.zeros(dimension)
    exact[str(order)] = {
        "dimension": dimension,
        "rank": shift.rank(),
        "determinant": str(shift.det()),
        "nilpotence_index_upper_bound": dimension,
    }

# A hostile cyclic shift is invertible but incorrectly wraps the terminal jet
# into the boundary residue instead of retaining the missing boundary class.
hostile = sp.zeros(4)
for row in range(1, 4):
    hostile[row, row - 1] = 1
hostile[0, 3] = 1
checks["hostile_cyclic_wrap_is_detected"] = hostile.det() != 0
checks["hostile_cyclic_wrap_changes_first_residue"] = hostile[0, 3] == 1

result = {
    "schema": "marici.exponent_gysin_shift_obstruction.v1",
    "checks": checks,
    "exact": {
        "jets_0_through_12": exact,
        "hostile_cyclic_determinant": str(hostile.det()),
    },
}

if not all(checks.values()):
    raise SystemExit(json.dumps(result, indent=2))

output = Path("research/grothendieck/results/exponent_gysin_shift_obstruction.json")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
