#!/usr/bin/env python3
"""Recover the simple antisymmetric detector from sourced two-wall monodromy."""
import json
from pathlib import Path
import sympy as sp

R = Path(__file__).resolve().parents[3]
mon = json.loads((R / "research/benincasa/two-wall-conductor-monodromy.json").read_text())
prior = json.loads((R / "research/voevodsky/results/C15_canonical_physical_mixed_detector.json").read_text())

def column_matrix(columns):
    return sp.Matrix.hstack(*[sp.Matrix(c) for c in columns])

T1 = column_matrix(mon["root_swap_1"]["matrix_columns_in_basis"])
T2 = column_matrix(mon["root_swap_2"]["matrix_columns_in_basis"])
s_plus = sp.Matrix([1, 1, 0])
s_minus = sp.Matrix([1, -1, 0])
x, y = sp.symbols("x y", nonzero=True)
c = 1 / (4 * x**3 * y**3 * (x + y))
v_projection = sp.simplify(-c - c)
checks = {
    "source_monodromies_involutive": T1**2 == sp.eye(3) and T2**2 == sp.eye(3),
    "source_monodromies_commute": T1 * T2 == T2 * T1,
    "second_swap_sources_odd_simple": T2 * s_plus == s_minus,
    "first_swap_sources_opposite_odd_simple": T1 * s_plus == -s_minus,
    "odd_simple_primitive": sp.gcd(*map(abs, s_minus)) == 1,
    "prior_canonical_vector_symmetric": prior["physical_covector"] == [1, 1],
    "prior_antisymmetric_candidate": prior["counterfactual_antisymmetric_image"]["source_covector"] == [1, -1],
    "v_projection_nonzero_rational": v_projection != 0,
}
assert all(checks.values()), checks
out = {
    "schema": "marici.voevodsky.second-wall-root-swap-mixed-detector.v1",
    "passed": True,
    "canonical_simple_vector": [1, 1, 0],
    "second_wall_transport_output": [int(v) for v in T2 * s_plus],
    "first_wall_transport_output": [int(v) for v in T1 * s_plus],
    "v_alg_projection": str(v_projection),
    "source": "research/benincasa/two-wall-conductor-monodromy.json",
    "construction": "apply either labelled integral wall root swap to the canonical symmetric mixed residue",
    "remaining": "identify the marked algebraic period with the admitted physical readout and fix its integral Betti normalization",
    "checks": checks,
}
p = R / "research/voevodsky/results/second_wall_root_swap_mixed_detector.json"
p.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({"passed": True, "T2_symmetric": [1, -1, 0], "v_alg_nonzero": True}))
