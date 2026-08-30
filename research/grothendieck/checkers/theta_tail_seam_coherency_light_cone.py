import json
from pathlib import Path

import sympy as sp


a, b, c, d = sp.symbols("a b c d", real=True)
U = a + sp.I * b
V = c + sp.I * d
C = sp.expand(U * V)

S0 = sp.expand(U * sp.conjugate(U) + V * sp.conjugate(V))
S1 = sp.expand(C + sp.conjugate(C))
S2 = sp.expand(sp.I * (C - sp.conjugate(C)))
S3 = sp.expand(U * sp.conjugate(U) - V * sp.conjugate(V))

H = sp.Matrix(
    [
        [sp.expand(U * sp.conjugate(U)), C],
        [sp.conjugate(C), sp.expand(V * sp.conjugate(V))],
    ]
)

swap = {a: c, b: d, c: a, d: b}
checks = {
    "coherency_determinant_zero": sp.simplify(H.det()) == 0,
    "stokes_light_cone_identity": sp.simplify(S0**2 - S1**2 - S2**2 - S3**2) == 0,
    "even_coordinates_fixed_by_sheet_swap": all(
        sp.simplify(expr.xreplace(swap) - expr) == 0 for expr in (S0, S1, S2)
    ),
    "krein_coordinate_reversed_by_sheet_swap": sp.simplify(S3.xreplace(swap) + S3) == 0,
    "missing_magnitude_reconstructed": sp.simplify(S3**2 - (S0**2 - S1**2 - S2**2)) == 0,
}

result = {
    "schema": "marici.grothendieck.theta_tail_seam_coherency_light_cone.v1",
    "coherency_matrix": [[str(value) for value in row] for row in H.tolist()],
    "stokes_coordinates": {"S0": str(S0), "S1": str(S1), "S2": str(S2), "S3": str(S3)},
    "checks": checks,
    "fiber_after_even_observation": "two sheets distinguished by sign(S3), away from S3=0",
}

assert all(checks.values())
output = Path("research/grothendieck/results/theta_tail_seam_coherency_light_cone.json")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
