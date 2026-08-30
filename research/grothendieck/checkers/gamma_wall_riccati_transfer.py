import json
from pathlib import Path

import sympy as sp


j, q = sp.symbols("j q")
a = sp.Rational(3, 2)
R, Rm, S = sp.symbols("R Rm S", nonzero=True)

pearson_divided = (
    R * sp.Symbol("Rnext")
    - (j + sp.Rational(19, 4)) * R
    + a * (j + sp.Rational(5, 4))
    - q * S * (Rm - a)
)

Rnext = (
    j
    + sp.Rational(19, 4)
    - a * (j + sp.Rational(5, 4)) / R
    + q * S * (Rm - a) / R
)
riccati_residual = sp.simplify(
    pearson_divided.subs(sp.Symbol("Rnext"), Rnext)
)

Snext = S * Rm / R
companion_residual = sp.simplify(Snext * R - S * Rm)

wrong_Rnext = Rnext.subs(sp.Rational(19, 4), sp.Rational(9, 2))
wrong_residual = sp.factor(
    pearson_divided.subs(sp.Symbol("Rnext"), wrong_Rnext)
)

Rnext_symbol, Snext = sp.symbols("Rnext_symbol Snext", nonzero=True)
backward_denominator = (
    j
    + sp.Rational(19, 4)
    + q * Snext * (1 - a / Rm)
    - Rnext_symbol
)
backward_R = a * (j + sp.Rational(5, 4)) / backward_denominator
backward_S = Snext * backward_R / Rm
backward_R_residual = sp.simplify(
    Rnext.subs({R: backward_R, S: backward_S}) - Rnext_symbol
)
backward_S_residual = sp.simplify(backward_S * Rm - Snext * backward_R)

c, Ij, Wj = sp.symbols("c Ij Wj", positive=True)
endpoint_flux = c ** (j + sp.Rational(5, 4)) * (c - a) ** 2 * sp.exp(-c)
endpoint_scaling_residual = sp.simplify(
    endpoint_flux.subs(j, j + 1) - c * endpoint_flux
)
Ej = Wj / Ij
base_Rnext = (
    j
    + sp.Rational(19, 4)
    - a * (j + sp.Rational(5, 4)) / R
    + Ej / R
)
base_recurrence_residual = sp.simplify(
    R * base_Rnext
    - (j + sp.Rational(19, 4)) * R
    + a * (j + sp.Rational(5, 4))
    - Ej
)
Enext = c * Ej / R
wall_channel_residual = sp.simplify(Enext * R - c * Ej)

transfer_matrix = sp.Matrix(
    [
        [j + sp.Rational(19, 4), -a * (j + sp.Rational(5, 4)), 1],
        [1, 0, 0],
        [0, 0, c],
    ]
)
expected_determinant = a * (j + sp.Rational(5, 4)) * c
determinant_residual = sp.factor(transfer_matrix.det() - expected_determinant)
tail_minor = transfer_matrix.extract([0, 1], [0, 1]).det()
tail_minor_residual = sp.factor(tail_minor - a * (j + sp.Rational(5, 4)))
wall_column = transfer_matrix[:, 2]
expected_wall_column = sp.Matrix([1, 0, c])

result = {
    "schema": "marici.gamma_wall_riccati_transfer.v1",
    "checks": {
        "riccati_transfer_residual_zero": riccati_residual == 0,
        "companion_transfer_residual_zero": companion_residual == 0,
        "wrong_coefficient_residual_nonzero": wrong_residual != 0,
        "backward_R_inverse_residual_zero": backward_R_residual == 0,
        "backward_S_inverse_residual_zero": backward_S_residual == 0,
        "endpoint_flux_scales_by_c": endpoint_scaling_residual == 0,
        "base_recurrence_with_wall_channel": base_recurrence_residual == 0,
        "normalized_wall_channel_transfer": wall_channel_residual == 0,
        "linear_lift_determinant": determinant_residual == 0,
        "tail_bivector_scale": tail_minor_residual == 0,
        "wall_to_tail_shear": wall_column == expected_wall_column,
    },
    "exact": {
        "riccati_residual": str(riccati_residual),
        "companion_residual": str(companion_residual),
        "wrong_coefficient_residual": str(wrong_residual),
        "backward_R_residual": str(backward_R_residual),
        "backward_S_residual": str(backward_S_residual),
        "endpoint_flux": str(endpoint_flux),
        "endpoint_scaling_residual": str(endpoint_scaling_residual),
        "base_recurrence_residual": str(base_recurrence_residual),
        "wall_channel_residual": str(wall_channel_residual),
        "transfer_matrix": [[str(entry) for entry in row] for row in transfer_matrix.tolist()],
        "determinant": str(sp.factor(transfer_matrix.det())),
        "determinant_residual": str(determinant_residual),
        "tail_minor": str(sp.factor(tail_minor)),
        "tail_minor_residual": str(tail_minor_residual),
        "wall_column": [str(entry) for entry in wall_column],
    },
}

if not all(result["checks"].values()):
    raise SystemExit(json.dumps(result, indent=2))

output = Path("research/grothendieck/results/gamma_wall_riccati_transfer.json")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
