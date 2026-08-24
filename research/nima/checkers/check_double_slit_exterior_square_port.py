"""Exact exterior-square dictionary for the QND double-slit interface."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/double-slit-exterior-square-port.json"

c = sp.Rational(3, 5)
s = sp.Rational(4, 5)

# Rows are path occurrences L,R; columns are pointer occurrences 0,1.
# The global state is (|L,0> + |R>(c|0>+s|1>))/sqrt(2).
amplitude = sp.Matrix([[1, 0], [c, s]]) / sp.sqrt(2)
rho_path = sp.simplify(amplitude * amplitude.T)
rho_pointer = sp.simplify(amplitude.T * amplitude)

plucker = sp.simplify(amplitude.det())
path_det = sp.simplify(rho_path.det())
pointer_det = sp.simplify(rho_pointer.det())
visibility = sp.simplify(2 * abs(rho_path[0, 1]))
distinguishability = s

gates = {
    "global_state_is_normalized": sp.trace(rho_path) == 1,
    "local_determinant_is_squared_exterior_port": sp.simplify(
        path_det - plucker**2
    ) == 0,
    "both_local_restrictions_share_the_exterior_port": path_det == pointer_det,
    "lost_visibility_is_four_times_exterior_weight": sp.simplify(
        1 - visibility**2 - 4 * plucker**2
    ) == 0,
    "which_path_square_is_four_times_exterior_weight": sp.simplify(
        distinguishability**2 - 4 * plucker**2
    ) == 0,
    "complementarity_is_the_exterior_square_identity": sp.simplify(
        visibility**2 + distinguishability**2 - 1
    ) == 0,
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.double-slit-exterior-square-port.v1",
    "amplitude_matrix": [[str(value) for value in row] for row in amplitude.tolist()],
    "path_restriction": [[str(value) for value in row] for row in rho_path.tolist()],
    "pointer_restriction": [[str(value) for value in row] for row in rho_pointer.tolist()],
    "exterior_square_port": str(plucker),
    "exterior_weight": str(plucker**2),
    "local_determinant": str(path_det),
    "visibility": str(visibility),
    "distinguishability": str(distinguishability),
    "identity": "1 - V^2 = D^2 = 4*|wedge^2 amplitude|^2",
    "gates": gates,
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))

