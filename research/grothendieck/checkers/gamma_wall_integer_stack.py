import json
from pathlib import Path

import sympy as sp


j, c = sp.symbols("j c", positive=True)
a = sp.Rational(3, 2)
b = a * (j + sp.Rational(5, 4))
A = sp.Matrix([[j + sp.Rational(19, 4), -b], [1, 0]])


def stack_matrix(m):
    dimension = 2 * (m + 1) + 1
    matrix = sp.zeros(dimension)
    wall = dimension - 1
    for k in range(m + 1):
        row = 2 * k
        matrix[row : row + 2, row : row + 2] = A
        if k:
            matrix[row, row - 2] = k
            matrix[row, row - 1] = -a * k
    matrix[0, wall] = 1
    matrix[wall, wall] = c
    return matrix


checks = {}
determinants = {}
for m in range(11):
    matrix = stack_matrix(m)
    expected_dimension = 2 * m + 3
    expected_determinant = c * b ** (m + 1)
    checks[f"grade_{m}_dimension"] = matrix.rows == expected_dimension
    checks[f"grade_{m}_determinant"] = sp.factor(matrix.det() - expected_determinant) == 0

    coflag_ok = True
    for r in range(m + 1):
        retained = set(range(2 * r, 2 * (m + 1)))
        for column in retained:
            for row in range(matrix.rows):
                if row not in retained and matrix[row, column] != 0:
                    coflag_ok = False
    checks[f"grade_{m}_tail_coflag_invariant"] = coflag_ok
    tail_dimension = 2 * (m + 1)
    checks[f"grade_{m}_tail_subspace_invariant"] = all(
        matrix[matrix.rows - 1, column] == 0 for column in range(tail_dimension)
    )
    checks[f"grade_{m}_wall_quotient_scales_by_c"] = matrix[-1, -1] == c
    determinants[str(m)] = str(sp.factor(matrix.det()))

grade_nine = stack_matrix(9)
checks["grade_nine_dimension_21"] = grade_nine.rows == 21
checks["wall_shear_into_grade_zero"] = grade_nine[0, 20] == 1
checks["wall_scales_by_c"] = grade_nine[20, 20] == c

hostile = stack_matrix(2)
hostile[0:2, 0:2] = sp.Matrix([[j + sp.Rational(19, 4), b], [1, 0]])
hostile_expected = -c * b**3
checks["hostile_sign_reverses_orientation"] = sp.factor(hostile.det() - hostile_expected) == 0

result = {
    "schema": "marici.gamma_wall_integer_stack.v1",
    "checks": checks,
    "exact": {
        "dimension_formula": "2*m + 3",
        "determinant_formula": "c * ((3/2)*(j + 5/4))**(m + 1)",
        "grade_nine_shape": list(grade_nine.shape),
        "determinants_0_through_10": determinants,
        "hostile_grade_two_determinant": str(sp.factor(hostile.det())),
    },
}

if not all(result["checks"].values()):
    raise SystemExit(json.dumps(result, indent=2))

output = Path("research/grothendieck/results/gamma_wall_integer_stack.json")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
