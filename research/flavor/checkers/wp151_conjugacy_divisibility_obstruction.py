"""Exact conjugacy-class divisibility audit for B3 x CP of order 96."""

from itertools import permutations, product
from math import gcd
from functools import reduce
import json
from pathlib import Path


Matrix = tuple[int, ...]
Element = tuple[Matrix, int]


def signed_permutation_matrix(permutation: tuple[int, ...], signs: tuple[int, ...]) -> Matrix:
    entries = [0] * 9
    for row in range(3):
        entries[3 * row + permutation[row]] = signs[row]
    return tuple(entries)


def multiply_matrix(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        sum(left[3 * row + k] * right[3 * k + column] for k in range(3))
        for row in range(3)
        for column in range(3)
    )


def transpose(matrix: Matrix) -> Matrix:
    return tuple(matrix[3 * column + row] for row in range(3) for column in range(3))


def multiply(left: Element, right: Element) -> Element:
    return multiply_matrix(left[0], right[0]), (left[1] + right[1]) % 2


def inverse(element: Element) -> Element:
    return transpose(element[0]), element[1]


identity_matrix: Matrix = (1, 0, 0, 0, 1, 0, 0, 0, 1)
minus_identity: Matrix = (-1, 0, 0, 0, -1, 0, 0, 0, -1)
identity: Element = (identity_matrix, 0)
cp: Element = (identity_matrix, 1)
global_sign: Element = (minus_identity, 0)
global_sign_cp: Element = (minus_identity, 1)

signed_matrices = {
    signed_permutation_matrix(permutation, signs)
    for permutation in permutations(range(3))
    for signs in product((-1, 1), repeat=3)
}
elements = {(matrix, cp_bit) for matrix in signed_matrices for cp_bit in (0, 1)}


def conjugate(actor: Element, target: Element) -> Element:
    return multiply(multiply(actor, target), inverse(actor))


remaining = set(elements)
classes: list[set[Element]] = []
while remaining:
    representative = next(iter(remaining))
    conjugacy_class = {conjugate(actor, representative) for actor in elements}
    classes.append(conjugacy_class)
    remaining -= conjugacy_class

class_sizes = sorted(len(conjugacy_class) for conjugacy_class in classes)
nonidentity_sizes = [
    len(conjugacy_class)
    for conjugacy_class in classes
    if identity not in conjugacy_class
]
center = {
    element
    for element in elements
    if all(multiply(element, other) == multiply(other, element) for other in elements)
}
nonidentity_gcd = reduce(gcd, nonidentity_sizes)

# A conjugacy-invariant fixed-set assignment may put Euler value 24 on the
# singleton CP class and zero on every other nonidentity class.
hostile_fixed_sum = 24 * 1
hostile_k = (96 - hostile_fixed_sum) // 24

checks = {
    "signed_permutation_group_has_order_48": len(signed_matrices) == 48,
    "cp_doubled_group_has_order_96": len(elements) == 96,
    "inverse_contract_holds": all(multiply(element, inverse(element)) == identity for element in elements),
    "conjugacy_classes_partition_group": sum(class_sizes) == 96,
    "conjugacy_class_count_is_twenty": len(classes) == 20,
    "center_has_order_four": center == {identity, cp, global_sign, global_sign_cp},
    "four_singleton_classes_exist": class_sizes.count(1) == 4,
    "three_nonidentity_singleton_classes_exist": nonidentity_sizes.count(1) == 3,
    "nonidentity_class_size_gcd_is_one": nonidentity_gcd == 1,
    "class_symmetry_forces_no_mod24_divisibility": nonidentity_gcd % 24 != 0,
    "hostile_class_invariant_sum_is_24": hostile_fixed_sum == 24,
    "hostile_sum_breaks_modulus_four": hostile_k == 3 and hostile_k % 4 != 0,
}

result = {
    "work_package": "WP151",
    "title": "Conjugacy-divisibility obstruction",
    "group": "((Z2)^3 semidirect S3) times CP",
    "group_order": 96,
    "conjugacy_class_count": len(classes),
    "conjugacy_class_sizes": class_sizes,
    "center_order": len(center),
    "nonidentity_class_size_gcd": nonidentity_gcd,
    "classification": "conjugacy invariance cannot force F=0 mod 96; stronger geometric index data are required",
    "selector": False,
    "rigidifier": "conjugacy-class organization only",
    "physical_instrument": False,
    "smallest_exact_falsifier": "the central CP element is a singleton conjugacy class, allowing a class-invariant contribution F=24 and k=3",
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "all_passed": all(checks.values()),
}

output = Path(__file__).resolve().parents[1] / "results" / "wp151_conjugacy_divisibility_obstruction.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

