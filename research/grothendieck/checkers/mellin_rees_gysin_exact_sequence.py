import json
from pathlib import Path

import sympy as sp


c = sp.symbols("c", nonzero=True)
checks = {}
exact = {}


def degree_matrix(order):
    """Multiplication by c*exp(y) on A_order in the monomial basis."""
    matrix = sp.zeros(order + 1)
    for column in range(order + 1):
        for row in range(column, order + 1):
            matrix[row, column] = c / sp.factorial(row - column)
    return matrix


for order in range(13):
    middle_dimension = order + 1
    left_dimension = order
    inclusion = sp.zeros(middle_dimension, left_dimension)
    for column in range(left_dimension):
        inclusion[column + 1, column] = 1
    evaluation = sp.zeros(1, middle_dimension)
    evaluation[0, 0] = 1

    checks[f"jet_{order}_complex"] = evaluation * inclusion == sp.zeros(
        1, left_dimension
    )
    checks[f"jet_{order}_left_injective"] = inclusion.rank() == left_dimension
    checks[f"jet_{order}_right_surjective"] = evaluation.rank() == 1
    checks[f"jet_{order}_exact_middle"] = (
        inclusion.rank() + evaluation.rank() == middle_dimension
    )

    degree_middle = degree_matrix(order)
    if order:
        degree_left = degree_matrix(order - 1)
        checks[f"jet_{order}_degree_square"] = (
            degree_middle * inclusion == inclusion * degree_left
        )
    checks[f"jet_{order}_boundary_naturality"] = (
        evaluation * degree_middle == c * evaluation
    )
    checks[f"jet_{order}_degree_invertible"] = sp.factor(
        degree_middle.det() - c ** middle_dimension
    ) == 0

    if order:
        truncate_middle = sp.zeros(order, order + 1)
        for index in range(order):
            truncate_middle[index, index] = 1
        truncate_left = sp.zeros(order - 1, order)
        for index in range(order - 1):
            truncate_left[index, index] = 1
        previous_inclusion = sp.zeros(order, order - 1)
        for index in range(order - 1):
            previous_inclusion[index + 1, index] = 1
        checks[f"jet_{order}_truncation_square"] = (
            truncate_middle * inclusion == previous_inclusion * truncate_left
        )
        checks[f"jet_{order}_truncation_surjective"] = (
            truncate_middle.rank() == order
        )

    exact[str(order)] = {
        "dimensions": [left_dimension, middle_dimension, 1],
        "inclusion_rank": inclusion.rank(),
        "evaluation_rank": evaluation.rank(),
        "degree_determinant": str(sp.factor(degree_middle.det())),
    }

result = {
    "schema": "marici.mellin_rees_gysin_exact_sequence.v1",
    "checks": checks,
    "exact": {"jets_0_through_12": exact},
}

if not all(checks.values()):
    raise SystemExit(json.dumps(result, indent=2))

output = Path("research/grothendieck/results/mellin_rees_gysin_exact_sequence.json")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
