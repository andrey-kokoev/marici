"""Exact audit of the invariant amplitude left by three-sector symmetry."""

from fractions import Fraction
import json
from pathlib import Path


def rank(rows: list[list[int]]) -> int:
    matrix = [[Fraction(value) for value in row] for row in rows]
    row = 0
    for column in range(len(matrix[0])):
        pivot = next((r for r in range(row, len(matrix)) if matrix[r][column]), None)
        if pivot is None:
            continue
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        scale = matrix[row][column]
        matrix[row] = [value / scale for value in matrix[row]]
        for other in range(len(matrix)):
            if other != row and matrix[other][column]:
                factor = matrix[other][column]
                matrix[other] = [a - factor * b for a, b in zip(matrix[other], matrix[row])]
        row += 1
    return row


difference_relations = [[1, -1, 0], [0, 1, -1]]
sum_relation = [1, 1, 1]
diagonal_witness = [1, 1, 1]
hostile_fixed_sum = 24 * sum(diagonal_witness)
hostile_k = 4 - hostile_fixed_sum // 24


def cyclic_average(vector: list[int]) -> list[Fraction]:
    mean = Fraction(sum(vector), 3)
    return [mean, mean, mean]


average_witness = cyclic_average([1, 2, 3])

checks = {
    "difference_relation_rank_is_two": rank(difference_relations) == 2,
    "difference_kernel_is_one_dimensional": 3 - rank(difference_relations) == 1,
    "diagonal_witness_satisfies_differences": all(sum(a * b for a, b in zip(row, diagonal_witness)) == 0 for row in difference_relations),
    "diagonal_witness_has_nonzero_total": sum(diagonal_witness) == 3,
    "symmetric_witness_gives_F_72": hostile_fixed_sum == 72,
    "symmetric_witness_restores_inaccessible_k_one": hostile_k == 1,
    "cyclic_average_is_diagonal": average_witness == [2, 2, 2],
    "cyclic_average_preserves_total": sum(average_witness) == 6,
    "symmetry_projector_does_not_kill_trivial_amplitude": average_witness != [0, 0, 0],
    "adding_sum_relation_has_rank_three": rank(difference_relations + [sum_relation]) == 3,
    "sum_relation_kills_diagonal_witness": sum(a * b for a, b in zip(sum_relation, diagonal_witness)) == 3,
    "modulus_four_requires_extra_amplitude_condition": sum(diagonal_witness) % 4 != 0,
}

result = {
    "work_package": "WP153",
    "title": "Trivial-representation amplitude obstruction",
    "domain": "central fixed-set Euler units f_i=chi(X^g_i)/24 in Z^3",
    "symmetry_relations": ["f_CP=f_-1", "f_-1=f_-CP"],
    "decomposition": "Z^3 = trivial diagonal amplitude plus two-dimensional difference sector",
    "classification": "three-sector symmetry kills differences but leaves the total fixed-point amplitude unauthorized",
    "selector": False,
    "rigidifier": "central-sector alignment",
    "physical_instrument": False,
    "smallest_exact_falsifier": "f=(1,1,1) obeys all equality relations but gives F=72 and k=1 at quotient Euler one",
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "all_passed": all(checks.values()),
}

output = Path(__file__).resolve().parents[1] / "results" / "wp153_trivial_representation_amplitude.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

