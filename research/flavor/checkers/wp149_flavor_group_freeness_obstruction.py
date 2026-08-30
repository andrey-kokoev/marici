"""Exact freeness audit for the natural order-96 flavor presentation group."""

from itertools import permutations, product
import json
from pathlib import Path


Vector = tuple[tuple[int, int], tuple[int, int], tuple[int, int]]
Element = tuple[tuple[int, int, int], tuple[int, int, int], int]


def act(element: Element, vector: Vector) -> Vector:
    permutation, signs, cp = element
    conjugated = tuple((real, -imag if cp else imag) for real, imag in vector)
    return tuple(
        (signs[i] * conjugated[permutation[i]][0], signs[i] * conjugated[permutation[i]][1])
        for i in range(3)
    )


elements = [
    (permutation, signs, cp)
    for permutation in permutations(range(3))
    for signs in product((-1, 1), repeat=3)
    for cp in (0, 1)
]
identity: Element = ((0, 1, 2), (1, 1, 1), 0)

collision_vector: Vector = ((1, 0), (1, 0), (2, 0))
zero_coordinate_vector: Vector = ((1, 0), (2, 0), (0, 0))
real_generic_vector: Vector = ((1, 0), (2, 0), (3, 0))
complex_generic_vector: Vector = ((1, 1), (2, 3), (4, 5))

transposition: Element = ((1, 0, 2), (1, 1, 1), 0)
third_sign_flip: Element = ((0, 1, 2), (1, 1, -1), 0)
cp_only: Element = ((0, 1, 2), (1, 1, 1), 1)


def stabilizer(vector: Vector) -> list[Element]:
    return [element for element in elements if act(element, vector) == vector]


checks = {
    "signed_permutation_order_is_48": 6 * 8 == 48,
    "cp_doubled_group_order_is_96": len(elements) == 96,
    "all_enumerated_elements_are_distinct": len(set(elements)) == 96,
    "identity_acts_trivially": act(identity, complex_generic_vector) == complex_generic_vector,
    "transposition_is_nonidentity": transposition != identity,
    "transposition_fixes_collision_locus": act(transposition, collision_vector) == collision_vector,
    "sign_flip_is_nonidentity": third_sign_flip != identity,
    "sign_flip_fixes_zero_coordinate_locus": act(third_sign_flip, zero_coordinate_vector) == zero_coordinate_vector,
    "cp_is_nonidentity": cp_only != identity,
    "cp_fixes_real_locus": act(cp_only, real_generic_vector) == real_generic_vector,
    "generic_complex_witness_has_trivial_stabilizer": stabilizer(complex_generic_vector) == [identity],
    "global_action_is_not_free": len(stabilizer(collision_vector)) > 1,
}

result = {
    "work_package": "WP149",
    "title": "Natural flavor-group freeness obstruction",
    "domain": "canonical linear action on three complex generation coordinates",
    "group": "((Z2)^3 semidirect S3) times CP",
    "group_order": 96,
    "classification": "order-96 source grammar with nonfree canonical action; fails WP148 covering gate",
    "selector": False,
    "rigidifier": "presentation symmetry only on this domain",
    "physical_instrument": False,
    "fixed_loci": [
        "generation-collision locus fixed by a transposition",
        "zero-coordinate locus fixed by a sign flip",
        "real locus fixed by CP",
    ],
    "smallest_exact_falsifier": "the nonidentity transposition (12) fixes the vector (1,1,2)",
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "all_passed": all(checks.values()),
}

output = Path(__file__).resolve().parents[1] / "results" / "wp149_flavor_group_freeness_obstruction.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

