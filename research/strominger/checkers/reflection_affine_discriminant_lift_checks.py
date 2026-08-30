import json
from fractions import Fraction
from pathlib import Path


F = ((2, 7), (3, 7))
DET = -7


def matmul(a, b):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


def inverse_f_times(matrix):
    # F^-1 = [[-1,1],[3/7,-2/7]].
    inverse = ((Fraction(-1), Fraction(1)),
               (Fraction(3, 7), Fraction(-2, 7)))
    return matmul(matmul(inverse, matrix), F)


def integral(matrix):
    return all(entry.denominator == 1 for row in matrix for entry in row)


I = ((1, 0), (0, 1))
NEG_I = ((-1, 0), (0, -1))
X = ((0, 1), (1, 0))
NEG_X = ((0, -1), (-1, 0))

records = []
for name, action in (("I", I), ("-I", NEG_I), ("X", X), ("-X", NEG_X)):
    comparison = inverse_f_times(action)
    records.append({
        "action": name,
        "comparison": [[str(entry) for entry in row] for row in comparison],
        "integral_lift": integral(comparison),
    })

record_by_name = {record["action"]: record for record in records}

image_generator_mod_7 = (2, 3)
exchanged_generator_mod_7 = (3, 2)
same_projective_line = any(
    ((scalar * image_generator_mod_7[0]) % 7,
     (scalar * image_generator_mod_7[1]) % 7) == exchanged_generator_mod_7
    for scalar in range(1, 7)
)

gates = [
    DET == -7,
    record_by_name["I"]["integral_lift"],
    record_by_name["-I"]["integral_lift"],
    not record_by_name["X"]["integral_lift"],
    not record_by_name["-X"]["integral_lift"],
    record_by_name["X"]["comparison"] == [["-1", "0"], ["5/7", "1"]],
    not same_projective_line,
]

result = {
    "schema": "marici.strominger.reflection_affine_discriminant_lift.v1",
    "frame": F,
    "determinant": DET,
    "signed_coordinate_actions": records,
    "mod_7_image_line_generator": image_generator_mod_7,
    "exchange_image": exchanged_generator_mod_7,
    "exchange_preserves_image_line": same_projective_line,
    "physical_exchange_descends": False,
    "typed_conclusion": "no source-derived coefficient involution presently exists",
    "smallest_missing_constructor": "integral reflection lift or typed correspondence",
    "gates_passed": sum(gates),
    "gates_total": len(gates),
    "all_passed": all(gates),
}

output = Path(__file__).parents[1] / "results" / "reflection_affine_discriminant_lift_checks.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
print(json.dumps(result, indent=2))
raise SystemExit(0 if all(gates) else 1)
