"""Hostile transport gate for extending the frozen C3 Tate bridge."""

import json
from pathlib import Path


weights = [-2, -1, 1, 1]

# For a constant row ell, ell*S(z)=ell as a Laurent-polynomial identity
# requires ell_i*(z^w_i-1)=0. Every nonzero weight forces ell_i=0.
constant_invariant_coordinates = [i for i, w in enumerate(weights) if w == 0]
generic_constant_invariant_dimension = len(constant_invariant_coordinates)
assert generic_constant_invariant_dimension == 0

# At the equal-energy fixed point z=1, S(1)=identity and the constraint
# disappears completely.
fixed_point_invariant_dimension = len(weights)
assert fixed_point_invariant_dimension == 4

result = {
    "schema": "marici.rs2.tate-bridge-transport-gate.v1",
    "cosmological_transition": {
        "matrix": "diag(z^-2,z^-1,z,z)",
        "weights": weights,
    },
    "generic_constant_projection": {
        "required_identity": "ell*S(z)=ell",
        "solution_dimension": generic_constant_invariant_dimension,
        "nonzero_solution_exists": False,
    },
    "fixed_point_z_1": {
        "transition": "identity",
        "solution_dimension": fixed_point_invariant_dimension,
        "selects_projection": False,
    },
    "verdict": (
        "The canonical Tate bridge is natural on the C3/D3 occurrence-label "
        "coinvariant, but it does not extend through the rank-four cosmological "
        "coefficient transport by any nonzero constant projection. A source-derived "
        "z-dependent localization or coefficient functional is required."
    ),
}

out = Path(__file__).parents[1] / "results" / "rs2-tate-bridge-transport-gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
