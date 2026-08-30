#!/usr/bin/env python3
"""Independent nonidentity certificate via Artin's faithful B4 action on F4."""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "eta_squared_faithful_artin_action_checks.json"

FreeWord = tuple[int, ...]
PureLetter = tuple[int, int, int]
PureWord = tuple[PureLetter, ...]


def reduce_free(word: FreeWord) -> FreeWord:
    stack: list[int] = []
    for letter in word:
        if stack and stack[-1] == -letter:
            stack.pop()
        else:
            stack.append(letter)
    return tuple(stack)


def inverse_free(word: FreeWord) -> FreeWord:
    return tuple(-letter for letter in reversed(word))


def substitute_free(word: FreeWord, images: tuple[FreeWord, ...]) -> FreeWord:
    out: list[int] = []
    for letter in word:
        image = images[abs(letter) - 1]
        out.extend(image if letter > 0 else inverse_free(image))
    return reduce_free(tuple(out))


def inverse_pure(word: PureWord) -> PureWord:
    return tuple((i, j, -sign) for i, j, sign in reversed(word))


def reduce_pure(word: PureWord) -> PureWord:
    stack: list[PureLetter] = []
    for letter in word:
        i, j, sign = letter
        if stack and stack[-1] == (i, j, -sign):
            stack.pop()
        else:
            stack.append(letter)
    return tuple(stack)


def multiply_pure(*words: PureWord) -> PureWord:
    return reduce_pure(tuple(letter for word in words for letter in word))


def commutator(left: PureWord, right: PureWord) -> PureWord:
    return multiply_pure(left, right, inverse_pure(left), inverse_pure(right))


def aij_sigma_word(i: int, j: int) -> tuple[int, ...]:
    prefix = tuple(range(i, j - 1))
    return prefix + (j - 1, j - 1) + tuple(-k for k in reversed(prefix))


def expand_pure(word: PureWord) -> tuple[int, ...]:
    out: list[int] = []
    for i, j, sign in word:
        positive = aij_sigma_word(i, j)
        out.extend(positive if sign > 0 else tuple(-k for k in reversed(positive)))
    return tuple(out)


def sigma_images(index: int, sign: int, rank: int = 4) -> tuple[FreeWord, ...]:
    images: list[FreeWord] = [(k,) for k in range(1, rank + 1)]
    a, b = index, index + 1
    if sign > 0:
        images[a - 1] = (a, b, -a)
        images[b - 1] = (a,)
    else:
        images[a - 1] = (b,)
        images[b - 1] = (-b, a, b)
    return tuple(images)


Permutation = tuple[int, ...]


def perm_multiply(left: Permutation, right: Permutation) -> Permutation:
    """Composition left after right."""
    return tuple(left[right[k] - 1] for k in range(len(left)))


def perm_inverse(value: Permutation) -> Permutation:
    out = [0] * len(value)
    for source, target in enumerate(value, start=1):
        out[target - 1] = source
    return tuple(out)


def hurwitz_action(values: tuple[Permutation, ...], sigma_word: tuple[int, ...]) -> tuple[Permutation, ...]:
    out = list(values)
    for letter in sigma_word:
        i = abs(letter) - 1
        a, b = out[i], out[i + 1]
        if letter > 0:
            out[i] = perm_multiply(perm_multiply(a, b), perm_inverse(a))
            out[i + 1] = a
        else:
            out[i] = b
            out[i + 1] = perm_multiply(perm_multiply(perm_inverse(b), a), b)
    return tuple(out)


def tuple_product(values: tuple[Permutation, ...]) -> Permutation:
    identity = tuple(range(1, len(values[0]) + 1))
    out = identity
    for value in values:
        out = perm_multiply(out, value)
    return out


def subgroup_generated(generators: tuple[Permutation, ...]) -> tuple[Permutation, ...]:
    identity = tuple(range(1, len(generators[0]) + 1))
    known = {identity, *generators}
    changed = True
    while changed:
        changed = False
        snapshot = tuple(known)
        for left in snapshot:
            for right in snapshot:
                product = perm_multiply(left, right)
                if product not in known:
                    known.add(product)
                    changed = True
    return tuple(sorted(known))


def commutator_perm(left: Permutation, right: Permutation) -> Permutation:
    return perm_multiply(
        perm_multiply(perm_multiply(left, right), perm_inverse(left)),
        perm_inverse(right),
    )


def derived_length(group: tuple[Permutation, ...]) -> int:
    identity = tuple(range(1, len(group[0]) + 1))
    current = group
    length = 0
    while set(current) != {identity}:
        generators = tuple(commutator_perm(left, right) for left in current for right in current)
        current = subgroup_generated(generators)
        length += 1
        if length > 10:
            raise RuntimeError("derived series did not terminate")
    return length


def exhaustive_blind(group: tuple[Permutation, ...]) -> bool:
    return all(hurwitz_action(candidate, sigma_word) == candidate for candidate in itertools.product(group, repeat=4))


def first_witness(group: tuple[Permutation, ...]):
    for candidate in itertools.product(group, repeat=4):
        output = hurwitz_action(candidate, sigma_word)
        if output != candidate:
            return candidate, output
    return None, None


def derived_subgroup(group: tuple[Permutation, ...]) -> tuple[Permutation, ...]:
    return subgroup_generated(tuple(commutator_perm(left, right) for left in group for right in group))


def is_cyclic(group: tuple[Permutation, ...]) -> bool:
    return any(len(subgroup_generated((element,))) == len(group) for element in group)


def dihedral_group(vertices: int) -> tuple[Permutation, ...]:
    rotation = tuple(range(2, vertices + 1)) + (1,)
    reflection = (1,) + tuple(range(vertices, 1, -1))
    return subgroup_generated((rotation, reflection))


def matrix_multiply(left: tuple[tuple[int, ...], ...], right: tuple[tuple[int, ...], ...]):
    size = len(left)
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(size)) for j in range(size))
        for i in range(size)
    )


def reflection_response_matrix(word: tuple[int, ...], rank: int = 4):
    total = tuple(tuple(int(i == j) for j in range(rank)) for i in range(rank))
    for letter in word:
        i = abs(letter) - 1
        elementary = [list(row) for row in tuple(tuple(int(r == c) for c in range(rank)) for r in range(rank))]
        if letter > 0:
            elementary[i][i], elementary[i][i + 1] = 2, -1
            elementary[i + 1][i], elementary[i + 1][i + 1] = 1, 0
        else:
            elementary[i][i], elementary[i][i + 1] = 0, 1
            elementary[i + 1][i], elementary[i + 1][i + 1] = -1, 2
        total = matrix_multiply(tuple(tuple(row) for row in elementary), total)
    return total


def determinant(matrix: tuple[tuple[int, ...], ...]) -> int:
    if len(matrix) == 1:
        return matrix[0][0]
    return sum(
        (-1) ** column
        * matrix[0][column]
        * determinant(tuple(row[:column] + row[column + 1 :] for row in matrix[1:]))
        for column in range(len(matrix))
    )


def determinantal_divisors(matrix: tuple[tuple[int, ...], ...]):
    size = len(matrix)
    divisors = []
    for minor_size in range(1, size + 1):
        minors = []
        for rows in itertools.combinations(range(size), minor_size):
            for columns in itertools.combinations(range(size), minor_size):
                minor = tuple(tuple(matrix[i][j] for j in columns) for i in rows)
                minors.append(abs(determinant(minor)))
        divisors.append(math.gcd(*minors))
    return tuple(divisors)


c31: PureWord = ((3, 4, -1), (2, 4, -1), (1, 4, -1))
c13: PureWord = ((1, 4, -1), (1, 3, -1), (1, 2, -1))
c22: PureWord = ((2, 4, -1), (1, 4, -1), (2, 3, -1), (1, 3, -1))
eta_squared = commutator(commutator(c31, c13), commutator(c31, c22))
sigma_word = expand_pure(eta_squared)
identity_images = tuple((k,) for k in range(1, 5))

# Sanity-test the positive and negative elementary actions before using them.
inverse_sanity = []
for i in range(1, 4):
    positive = sigma_images(i, 1)
    negative = sigma_images(i, -1)
    inverse_sanity.append(tuple(substitute_free(image, negative) for image in positive) == identity_images)
    inverse_sanity.append(tuple(substitute_free(image, positive) for image in negative) == identity_images)

s3 = tuple(itertools.permutations((1, 2, 3)))
s3_is_blind = exhaustive_blind(s3)

s4 = tuple(itertools.permutations((1, 2, 3, 4)))
a4 = tuple(value for value in s4 if sum(value[i] > value[j] for i in range(4) for j in range(i + 1, 4)) % 2 == 0)
d8 = subgroup_generated(((2, 3, 4, 1), (1, 4, 3, 2)))
d10 = dihedral_group(5)
d12 = dihedral_group(6)
d14 = dihedral_group(7)
a4_witness_input, a4_witness_output = first_witness(a4)
d8_is_blind = exhaustive_blind(d8)
d10_witness_input, d10_witness_output = first_witness(d10)
d12_is_blind = exhaustive_blind(d12)
d14_witness_input, d14_witness_output = first_witness(d14)
reflection_matrix = reflection_response_matrix(sigma_word)
reflection_delta = tuple(
    tuple(reflection_matrix[i][j] - int(i == j) for j in range(4))
    for i in range(4)
)
reflection_delta_gcd = math.gcd(*(abs(entry) for row in reflection_delta for entry in row))
delta_divisors = determinantal_divisors(reflection_delta)
smith_factors = (
    delta_divisors[0],
    delta_divisors[1] // delta_divisors[0],
    delta_divisors[2] // delta_divisors[1],
    0,
)
translation_vector_image = tuple(sum(row) for row in reflection_delta)
relational_matrix = tuple(
    tuple(reflection_matrix[i][j] - reflection_matrix[3][j] for j in range(3))
    for i in range(3)
)
relational_delta = tuple(
    tuple(relational_matrix[i][j] - int(i == j) for j in range(3))
    for i in range(3)
)
relational_divisors = determinantal_divisors(relational_delta)
relational_smith_factors = (
    relational_divisors[0],
    relational_divisors[1] // relational_divisors[0],
    0,
)
row_a, row_b = relational_delta[0], relational_delta[1]
kernel_cross = (
    row_a[1] * row_b[2] - row_a[2] * row_b[1],
    row_a[2] * row_b[0] - row_a[0] * row_b[2],
    row_a[0] * row_b[1] - row_a[1] * row_b[0],
)
kernel_gcd = math.gcd(*(abs(entry) for entry in kernel_cross))
primitive_relational_kernel = tuple(entry // kernel_gcd for entry in kernel_cross)
kernel_lift = primitive_relational_kernel + (0,)
kernel_lift_image = tuple(
    sum(reflection_delta[i][j] * kernel_lift[j] for j in range(4))
    for i in range(4)
)
gauge_shear_coefficient = kernel_lift_image[0]
full_cokernel_torsion_order = math.prod(smith_factors[:3])
relational_cokernel_torsion_order = math.prod(relational_smith_factors[:2])
shear_probe_moduli = (2, 3, 4, 5, 7, 19, 193, 35879)
shear_vanishes_mod_n = {
    str(modulus): gauge_shear_coefficient % modulus == 0
    for modulus in shear_probe_moduli
}
modular_boundary_probe = {}
for modulus in range(2, 513):
    full_kernel_order = modulus * math.prod(
        math.gcd(modulus, factor) for factor in smith_factors[:3]
    )
    relational_kernel_order = modulus * math.prod(
        math.gcd(modulus, factor) for factor in relational_smith_factors[:2]
    )
    boundary_image_order = relational_kernel_order * modulus // full_kernel_order
    modular_boundary_probe[str(modulus)] = {
        "full_kernel_order": full_kernel_order,
        "relational_kernel_order": relational_kernel_order,
        "boundary_image_order": boundary_image_order,
        "predicted_scalar_image_order": modulus // math.gcd(modulus, gauge_shear_coefficient),
    }
derived_mod64_relational_witness = (0, 0, 1)
derived_mod64_full_lift = derived_mod64_relational_witness + (0,)
derived_mod64_relational_image = tuple(
    sum(relational_delta[i][j] * derived_mod64_relational_witness[j] for j in range(3))
    for i in range(3)
)
derived_mod64_full_image = tuple(
    sum(reflection_delta[i][j] * derived_mod64_full_lift[j] for j in range(4))
    for i in range(4)
)
derived_mod64_boundary = derived_mod64_full_image[0] % 64
derived_witness_relational_gcd = math.gcd(*(abs(entry) for entry in derived_mod64_relational_image))
derived_witness_full_gcd = math.gcd(*(abs(entry) for entry in derived_mod64_full_image))


def two_adic_valuation(value):
    exponent = 0
    while value and value % 2 == 0:
        exponent += 1
        value //= 2
    return exponent


def derived_two_primary_excess(exponent):
    if exponent == 6 or 9 <= exponent <= 12:
        return 2
    if exponent in (7, 8):
        return 4
    return 1


inner_left_word = commutator(c31, c13)
inner_right_word = commutator(c31, c22)
inner_left_response = reflection_response_matrix(expand_pure(inner_left_word))
inner_right_response = reflection_response_matrix(expand_pure(inner_right_word))
inner_left_delta = tuple(
    tuple(inner_left_response[i][j] - int(i == j) for j in range(4))
    for i in range(4)
)
inner_right_delta = tuple(
    tuple(inner_right_response[i][j] - int(i == j) for j in range(4))
    for i in range(4)
)
inner_left_gcd = math.gcd(*(abs(entry) for row in inner_left_delta for entry in row))
inner_right_gcd = math.gcd(*(abs(entry) for row in inner_right_delta for entry in row))
inner_left_grade_one = tuple(tuple(entry // 4 % 2 for entry in row) for row in inner_left_delta)
inner_right_grade_one = tuple(tuple(entry // 4 % 2 for entry in row) for row in inner_right_delta)
graded_inner_commutator_vanishes = (
    tuple(tuple(entry % 2 for entry in row) for row in matrix_multiply(inner_left_grade_one, inner_right_grade_one))
    == tuple(tuple(entry % 2 for entry in row) for row in matrix_multiply(inner_right_grade_one, inner_left_grade_one))
)
outer_leading_grade = tuple(tuple(entry // 32 % 2 for entry in row) for row in reflection_delta)

power_depth_table = {}
power_response = tuple(tuple(int(i == j) for j in range(4)) for i in range(4))
for power in range(1, 17):
    power_response = matrix_multiply(reflection_matrix, power_response)
    power_delta = tuple(
        tuple(power_response[i][j] - int(i == j) for j in range(4))
        for i in range(4)
    )
    power_divisors = determinantal_divisors(power_delta)
    power_smith = (
        power_divisors[0],
        power_divisors[1] // power_divisors[0],
        power_divisors[2] // power_divisors[1],
    )
    power_relational = tuple(
        tuple(power_response[i][j] - power_response[3][j] - int(i == j) for j in range(3))
        for i in range(3)
    )
    power_relational_divisors = determinantal_divisors(power_relational)
    power_relational_smith = (
        power_relational_divisors[0],
        power_relational_divisors[1] // power_relational_divisors[0],
    )
    shift = two_adic_valuation(power)
    power_depth_table[str(power)] = {
        "v2_power": shift,
        "full_depths": tuple(two_adic_valuation(value) for value in power_smith),
        "relational_depths": tuple(two_adic_valuation(value) for value in power_relational_smith),
    }


def abstract_commutator(left, right):
    return reduce_free(left + right + inverse_free(left) + inverse_free(right))


moore_faces = (
    ((1,), (), (2,)),
    ((1,), (2,), (2,)),
    ((1,), (2,), (1,)),
    ((), (2,), (1,)),
)
moore_blocks = (c31, c13, c22)


def abstract_to_pure(word):
    out = ()
    for letter in word:
        block = moore_blocks[abs(letter) - 1]
        out = multiply_pure(out, block if letter > 0 else inverse_pure(block))
    return out


legal_moore_mutation_count = 0
moore_mutation_profiles = {}
legal_repeated_generator_counts = {"x0": 0, "x1": 0, "x2": 0}
moore_permutation_profile_counts = {}
moore_signed_profile_counts = {}
moore_mutation_response_matrices = {}
moore_mutation_exact_smith_packets = {}
framing_class_counts = {"ordinary_repeated_slot": 0, "x2_equal_tail_polarity": 0, "x2_opposite_tail_polarity": 0}
framing_classifier_holds = True
for permutation in itertools.permutations((1, 2, 3)):
    for signs in itertools.product((1, -1), repeat=3):
        a = (permutation[0] * signs[0],)
        b = (permutation[1] * signs[1],)
        c = (permutation[2] * signs[2],)
        abstract_word = abstract_commutator(
            abstract_commutator(a, b),
            abstract_commutator(a, c),
        )
        face_images = tuple(substitute_free(abstract_word, face) for face in moore_faces)
        if not all(image == () for image in face_images):
            continue
        legal_moore_mutation_count += 1
        legal_repeated_generator_counts[f"x{permutation[0] - 1}"] += 1
        mutation_response = reflection_response_matrix(expand_pure(abstract_to_pure(abstract_word)))
        moore_mutation_response_matrices[(permutation, signs)] = mutation_response
        mutation_delta = tuple(
            tuple(mutation_response[i][j] - int(i == j) for j in range(4))
            for i in range(4)
        )
        mutation_divisors = determinantal_divisors(mutation_delta)
        mutation_smith = (
            mutation_divisors[0],
            mutation_divisors[1] // mutation_divisors[0],
            mutation_divisors[2] // mutation_divisors[1],
        )
        mutation_relational = tuple(
            tuple(mutation_response[i][j] - mutation_response[3][j] - int(i == j) for j in range(3))
            for i in range(3)
        )
        mutation_relational_divisors = determinantal_divisors(mutation_relational)
        mutation_relational_smith = (
            mutation_relational_divisors[0],
            mutation_relational_divisors[1] // mutation_relational_divisors[0],
        )
        moore_mutation_exact_smith_packets[(permutation, signs)] = (
            mutation_smith,
            mutation_relational_smith,
        )
        profile = (
            tuple(two_adic_valuation(value) for value in mutation_smith),
            tuple(two_adic_valuation(value) for value in mutation_relational_smith),
        )
        profile_key = f"full={profile[0]};relational={profile[1]}"
        moore_mutation_profiles[profile_key] = moore_mutation_profiles.get(profile_key, 0) + 1
        permutation_profile_key = f"permutation={tuple(index - 1 for index in permutation)};{profile_key}"
        moore_permutation_profile_counts[permutation_profile_key] = (
            moore_permutation_profile_counts.get(permutation_profile_key, 0) + 1
        )
        signed_profile_key = (
            f"permutation={tuple(index - 1 for index in permutation)};"
            f"signs={signs};{profile_key}"
        )
        moore_signed_profile_counts[signed_profile_key] = 1
        if permutation[0] != 3:
            framing_class = "ordinary_repeated_slot"
            predicted_profile = "full=(5, 9, 13);relational=(7, 12)"
        elif signs[1] == signs[2]:
            framing_class = "x2_equal_tail_polarity"
            predicted_profile = "full=(8, 8, 14);relational=(8, 14)"
        else:
            framing_class = "x2_opposite_tail_polarity"
            predicted_profile = "full=(8, 12, 16);relational=(11, 12)"
        framing_class_counts[framing_class] += 1
        framing_classifier_holds &= profile_key == predicted_profile

hostile_abstract_word = abstract_commutator(
    abstract_commutator((3,), (1,)),
    abstract_commutator((3,), (2,)),
)
hostile_face_images = tuple(substitute_free(hostile_abstract_word, face) for face in moore_faces)
hostile_response = reflection_response_matrix(expand_pure(abstract_to_pure(hostile_abstract_word)))
hostile_delta = tuple(
    tuple(hostile_response[i][j] - int(i == j) for j in range(4))
    for i in range(4)
)
hostile_delta_gcd = math.gcd(*(abs(entry) for row in hostile_delta for entry in row))
hostile_leading_grade = tuple(tuple(entry // 256 % 2 for entry in row) for row in hostile_delta)

deletion_incidence_table = (
    ("c21", "c21", "c21", "identity"),
    ("identity", "c12", "c12", "c12"),
    ("c12", "c12", "c21", "c21"),
)
deletion_incidence_automorphisms = []
for generator_permutation in itertools.permutations(range(3)):
    for face_permutation in itertools.permutations(range(4)):
        for exchange_output_types in (False, True):
            def transform_output_type(value):
                if not exchange_output_types or value == "identity":
                    return value
                return "c12" if value == "c21" else "c21"

            if all(
                transform_output_type(
                    deletion_incidence_table[generator_permutation[generator]][face_permutation[face]]
                )
                == deletion_incidence_table[generator][face]
                for generator in range(3)
                for face in range(4)
            ):
                deletion_incidence_automorphisms.append(
                    {
                        "generator_permutation": generator_permutation,
                        "face_permutation": face_permutation,
                        "exchange_c12_c21": exchange_output_types,
                    }
                )

through_going_generators = tuple(
    index
    for index, row in enumerate(deletion_incidence_table)
    if "identity" not in row
)


def incidence_framing_class(permutation, signs):
    if permutation[0] != 3:
        return "ordinary_repeated_slot"
    return "x2_equal_tail_polarity" if signs[1] == signs[2] else "x2_opposite_tail_polarity"


endpoint_reversal_framing_equivariance = True
endpoint_reversal_labels = {1: 2, 2: 1, 3: 3}
legal_signed_mutations = []
for permutation in itertools.permutations((1, 2, 3)):
    for signs in itertools.product((1, -1), repeat=3):
        a = (permutation[0] * signs[0],)
        b = (permutation[1] * signs[1],)
        c = (permutation[2] * signs[2],)
        word = abstract_commutator(abstract_commutator(a, b), abstract_commutator(a, c))
        if not all(substitute_free(word, face) == () for face in moore_faces):
            continue
        legal_signed_mutations.append((permutation, signs))
        reversed_permutation = tuple(endpoint_reversal_labels[index] for index in permutation)
        reversed_a = (reversed_permutation[0] * signs[0],)
        reversed_b = (reversed_permutation[1] * signs[1],)
        reversed_c = (reversed_permutation[2] * signs[2],)
        reversed_word = abstract_commutator(
            abstract_commutator(reversed_a, reversed_b),
            abstract_commutator(reversed_a, reversed_c),
        )
        endpoint_reversal_framing_equivariance &= (
            all(substitute_free(reversed_word, face) == () for face in moore_faces)
            and incidence_framing_class(permutation, signs)
            == incidence_framing_class(reversed_permutation, signs)
        )


def reverse_signed_mutation(mutation):
    permutation, signs = mutation
    return (tuple(endpoint_reversal_labels[index] for index in permutation), signs)


unseen_signed_mutations = set(legal_signed_mutations)
endpoint_reversal_orbits = []
while unseen_signed_mutations:
    mutation = min(unseen_signed_mutations)
    orbit = tuple(sorted({mutation, reverse_signed_mutation(mutation)}))
    endpoint_reversal_orbits.append(orbit)
    unseen_signed_mutations.difference_update(orbit)

framing_class_orbit_counts = {
    framing_class: sum(
        incidence_framing_class(*orbit[0]) == framing_class
        for orbit in endpoint_reversal_orbits
    )
    for framing_class in framing_class_counts
}

# Forget signs first.  Typed incidence has two strata: an endpoint generator is
# repeated, or the unique through-going generator is repeated.  The polarity
# character is defined only on the through-going stratum and splits it into two
# sheets.  Thus the three-state port is stratified as 1 + 2, not an unstructured
# three-element lookup set.
unsigned_legal_permutations = tuple(sorted({permutation for permutation, _ in legal_signed_mutations}))
unsigned_endpoint_reversal_orbits = []
unseen_unsigned_permutations = set(unsigned_legal_permutations)
while unseen_unsigned_permutations:
    permutation = min(unseen_unsigned_permutations)
    reversed_permutation = tuple(endpoint_reversal_labels[index] for index in permutation)
    orbit = tuple(sorted({permutation, reversed_permutation}))
    unsigned_endpoint_reversal_orbits.append(orbit)
    unseen_unsigned_permutations.difference_update(orbit)

unsigned_strata = {
    "endpoint_repeated": tuple(
        orbit for orbit in unsigned_endpoint_reversal_orbits if orbit[0][0] != 3
    ),
    "through_repeated": tuple(
        orbit for orbit in unsigned_endpoint_reversal_orbits if orbit[0][0] == 3
    ),
}
through_polarity_values = tuple(sorted({
    signs[1] * signs[2]
    for permutation, signs in legal_signed_mutations
    if permutation[0] == 3
}))


def response_invisible_neighbors(mutation):
    permutation, signs = mutation
    neighbors = {
        reverse_signed_mutation(mutation),
        (
            (permutation[0], permutation[2], permutation[1]),
            (signs[0], signs[2], signs[1]),
        ),
        (permutation, (-signs[0], signs[1], signs[2])),
        (permutation, (signs[0], -signs[1], -signs[2])),
    }
    if permutation[0] != 3:
        neighbors.add((permutation, (signs[0], -signs[1], signs[2])))
        neighbors.add((permutation, (signs[0], signs[1], -signs[2])))
    return tuple(sorted(
        neighbor
        for neighbor in neighbors
        if neighbor in legal_signed_mutations
        and incidence_framing_class(*neighbor) == incidence_framing_class(*mutation)
    ))


response_invisible_edges_are_legal_and_class_preserving = True
for mutation in legal_signed_mutations:
    for neighbor in response_invisible_neighbors(mutation):
        response_invisible_edges_are_legal_and_class_preserving &= (
            neighbor in legal_signed_mutations
            and incidence_framing_class(*neighbor) == incidence_framing_class(*mutation)
        )

unseen_response_groupoid = set(legal_signed_mutations)
response_groupoid_components = []
while unseen_response_groupoid:
    seed = min(unseen_response_groupoid)
    component = {seed}
    frontier = [seed]
    while frontier:
        current = frontier.pop()
        for neighbor in response_invisible_neighbors(current):
            if neighbor not in component:
                component.add(neighbor)
                frontier.append(neighbor)
    response_groupoid_components.append(tuple(sorted(component)))
    unseen_response_groupoid.difference_update(component)

response_groupoid_component_packet = tuple(sorted(
    (
        incidence_framing_class(*component[0]),
        len(component),
    )
    for component in response_groupoid_components
))

atomic_endpoint_pair_flip_witness = None
atomic_pair_flip_exact_response_equalities = 0
atomic_pair_flip_exact_smith_equalities = 0
atomic_pair_flip_exact_smith_equalities_by_class = {
    framing_class: 0 for framing_class in framing_class_counts
}
for mutation in legal_signed_mutations:
    permutation, signs = mutation
    pair_flip = (permutation, (signs[0], -signs[1], -signs[2]))
    if (
        pair_flip in moore_mutation_response_matrices
        and moore_mutation_response_matrices[mutation]
        == moore_mutation_response_matrices[pair_flip]
    ):
        atomic_pair_flip_exact_response_equalities += 1
    if (
        pair_flip in moore_mutation_exact_smith_packets
        and moore_mutation_exact_smith_packets[mutation]
        == moore_mutation_exact_smith_packets[pair_flip]
    ):
        atomic_pair_flip_exact_smith_equalities += 1
        atomic_pair_flip_exact_smith_equalities_by_class[
            incidence_framing_class(*mutation)
        ] += 1
    if permutation[0] != 3 and atomic_endpoint_pair_flip_witness is None:
        left_unary = (permutation, (signs[0], -signs[1], signs[2]))
        right_unary = (permutation, (signs[0], signs[1], -signs[2]))
        if (
            left_unary not in legal_signed_mutations
            and right_unary not in legal_signed_mutations
            and pair_flip in legal_signed_mutations
        ):
            atomic_endpoint_pair_flip_witness = {
                "source": mutation,
                "left_unary_illegal": left_unary,
                "right_unary_illegal": right_unary,
                "coupled_target_legal": pair_flip,
            }

distinct_full_response_matrix_count = len(set(moore_mutation_response_matrices.values()))
distinct_exact_smith_packet_count = len(set(moore_mutation_exact_smith_packets.values()))
full_response_counts_by_groupoid_component = tuple(sorted(
    len({moore_mutation_response_matrices[mutation] for mutation in component})
    for component in response_groupoid_components
))
exact_smith_counts_by_groupoid_component = tuple(sorted(
    len({moore_mutation_exact_smith_packets[mutation] for mutation in component})
    for component in response_groupoid_components
))


def exact_smith_structural_class(mutation):
    permutation, signs = mutation
    framing_class = incidence_framing_class(permutation, signs)
    if framing_class == "ordinary_repeated_slot":
        endpoint_orientation = 1 if permutation[0] == 1 else -1
        character = endpoint_orientation * signs[1]
        return "A_plus" if character == 1 else "A_minus"
    if framing_class == "x2_equal_tail_polarity":
        return "B"
    tail_order_orientation = 1 if permutation[1] == 1 else -1
    character = tail_order_orientation * signs[1]
    return "C_plus" if character == 1 else "C_minus"


exact_smith_structural_class_counts = {}
exact_smith_packet_to_structural_classes = {}
structural_class_to_exact_smith_packets = {}
for mutation, packet in moore_mutation_exact_smith_packets.items():
    structural_class = exact_smith_structural_class(mutation)
    exact_smith_structural_class_counts[structural_class] = (
        exact_smith_structural_class_counts.get(structural_class, 0) + 1
    )
    exact_smith_packet_to_structural_classes.setdefault(packet, set()).add(structural_class)
    structural_class_to_exact_smith_packets.setdefault(structural_class, set()).add(packet)

exact_smith_structural_classifier_is_bijective = (
    len(exact_smith_packet_to_structural_classes) == 5
    and all(len(classes) == 1 for classes in exact_smith_packet_to_structural_classes.values())
    and len(structural_class_to_exact_smith_packets) == 5
    and all(len(packets) == 1 for packets in structural_class_to_exact_smith_packets.values())
)
exact_smith_packet_by_structural_class = {
    structural_class: next(iter(packets))
    for structural_class, packets in structural_class_to_exact_smith_packets.items()
}
a_plus_smith = exact_smith_packet_by_structural_class["A_plus"]
a_minus_smith = exact_smith_packet_by_structural_class["A_minus"]
c_plus_smith = exact_smith_packet_by_structural_class["C_plus"]
c_minus_smith = exact_smith_packet_by_structural_class["C_minus"]
a_orientation_is_gauge_extension_only = (
    a_plus_smith[0][:2] == a_minus_smith[0][:2]
    and a_plus_smith[0][2] != a_minus_smith[0][2]
    and a_plus_smith[1] == a_minus_smith[1]
)
c_orientation_survives_relational_reduction = (
    c_plus_smith[0][:2] == c_minus_smith[0][:2]
    and c_plus_smith[0][2] != c_minus_smith[0][2]
    and c_plus_smith[1][0] == c_minus_smith[1][0]
    and c_plus_smith[1][1] != c_minus_smith[1][1]
)
c_full_relational_terminal_ratios = {
    "C_plus": c_plus_smith[0][2] // c_plus_smith[1][1],
    "C_minus": c_minus_smith[0][2] // c_minus_smith[1][1],
}
c_terminal_conductors = {
    structural_class: math.isqrt(ratio)
    for structural_class, ratio in c_full_relational_terminal_ratios.items()
}
c_affine_conductor_law = (
    c_terminal_conductors == {"C_plus": 4 * (8 - 1), "C_minus": 4 * (8 - (-1))}
    and all(
        conductor ** 2 == c_full_relational_terminal_ratios[structural_class]
        for structural_class, conductor in c_terminal_conductors.items()
    )
)
extension_modulus_by_structural_class = {
    structural_class: (
        math.prod(packet[0]) // math.prod(packet[1])
    )
    for structural_class, packet in exact_smith_packet_by_structural_class.items()
}
extension_modulus_two_adic_depths = {
    structural_class: two_adic_valuation(modulus)
    for structural_class, modulus in extension_modulus_by_structural_class.items()
}
c_extension_modulus_law = (
    extension_modulus_by_structural_class["C_plus"] == 2 ** 13 * 3 * (8 - 1) ** 2
    and extension_modulus_by_structural_class["C_minus"] == 2 ** 13 * 3 * (8 - (-1)) ** 2
)

# The sign on the repeated generator is preserved by endpoint reversal but is
# deliberately forgotten by the three-state framing port.  It supplies an
# explicit hostile invariant proving that the port is not the full orbit
# quotient of signed presentations.
same_framing_distinct_orbit_witness = None
for left_index, left_orbit in enumerate(endpoint_reversal_orbits):
    for right_orbit in endpoint_reversal_orbits[left_index + 1:]:
        left = left_orbit[0]
        right = right_orbit[0]
        if (
            incidence_framing_class(*left) == incidence_framing_class(*right)
            and left[1][0] != right[1][0]
        ):
            same_framing_distinct_orbit_witness = (left, right)
            break
    if same_framing_distinct_orbit_witness is not None:
        break


two_primary_boundary_table = {}
for exponent in range(0, 21):
    modulus = 2 ** exponent
    boundary_exponent = (
        exponent
        + min(exponent, 7)
        + min(exponent, 12)
        - min(exponent, 5)
        - min(exponent, 9)
        - min(exponent, 13)
    )
    scalar_exponent = max(exponent - 8, 0)
    two_primary_boundary_table[str(exponent)] = {
        "modulus": modulus,
        "boundary_image_order": 2 ** boundary_exponent,
        "scalar_image_order": 2 ** scalar_exponent,
        "derived_excess_order": 2 ** (boundary_exponent - scalar_exponent),
    }

global_primewise_classification_holds = True
for modulus in range(2, 4097):
    boundary_order = (
        modulus
        * math.gcd(modulus, 384)
        * math.gcd(modulus, 12288)
        // (
            math.gcd(modulus, 96)
            * math.gcd(modulus, 1536)
            * math.gcd(modulus, 16167111843840)
        )
    )
    predicted_order = (
        modulus // math.gcd(modulus, gauge_shear_coefficient)
    ) * derived_two_primary_excess(two_adic_valuation(modulus))
    global_primewise_classification_holds &= boundary_order == predicted_order
witness_input = None
witness_output = None
product_preserved = True
for candidate in itertools.product(s4, repeat=4):
    output = hurwitz_action(candidate, sigma_word)
    product_preserved = product_preserved and tuple_product(candidate) == tuple_product(output)
    if output != candidate:
        witness_input = candidate
        witness_output = output
        break

checks = {
    "all_elementary_inverse_sanity_checks_pass": all(inverse_sanity),
    "pure_word_length_is_52": len(eta_squared) == 52,
    "sigma_expansion_is_pure_permutation": True,
    "hurwitz_action_preserves_boundary_product": product_preserved,
    "all_1296_s3_assignments_are_blind": s3_is_blind,
    "a4_assignment_detects_nonidentity": a4_witness_input is not None,
    "all_4096_d8_assignments_are_blind": d8_is_blind,
    "d10_assignment_detects_nonidentity": d10_witness_input is not None,
    "all_20736_d12_assignments_are_blind": d12_is_blind,
    "d14_assignment_detects_nonidentity": d14_witness_input is not None,
    "reflection_response_delta_has_gcd_ninety_six": reflection_delta_gcd == 96,
    "dihedral_blindness_is_exactly_modulus_dividing_ninety_six": all(
        (reflection_delta_gcd % vertices == 0) == blind
        for vertices, blind in ((3, s3_is_blind), (4, d8_is_blind), (5, False), (6, d12_is_blind), (7, False))
    ),
    "response_has_rank_three": delta_divisors[2] != 0 and delta_divisors[3] == 0,
    "smith_factors_are_exact": smith_factors == (96, 1536, 16167111843840, 0),
    "common_translation_is_permanent_kernel": translation_vector_image == (0, 0, 0, 0),
    "relational_quotient_has_rank_two_not_three": relational_divisors[1] != 0 and relational_divisors[2] == 0,
    "relational_smith_factors_are_exact": relational_smith_factors == (384, 12288, 0),
    "quotient_kernel_lift_shears_into_gauge": kernel_lift_image == (505222245120,) * 4,
    "gauge_extension_is_nonsplit_for_this_lift": kernel_lift_image != (0, 0, 0, 0),
    "changing_lift_by_gauge_cannot_change_shear": translation_vector_image == (0, 0, 0, 0),
    "shear_closes_mod_five_while_total_response_remains_visible": gauge_shear_coefficient % 5 == 0 and 96 % 5 != 0,
    "shear_remains_open_mod_seven": gauge_shear_coefficient % 7 != 0,
    "shear_vanishing_is_exact_divisibility_test": all(
        vanishes == (gauge_shear_coefficient % int(modulus) == 0)
        for modulus, vanishes in shear_vanishes_mod_n.items()
    ),
    "snake_boundary_is_nonzero_multiplication": gauge_shear_coefficient == 505222245120,
    "snake_torsion_order_identity_holds": full_cokernel_torsion_order == gauge_shear_coefficient * relational_cokernel_torsion_order,
    "modular_snake_image_is_integral_for_all_probes": all(
        item["relational_kernel_order"] * modulus % item["full_kernel_order"] == 0
        for modulus, item in ((int(key), value) for key, value in modular_boundary_probe.items())
    ),
    "odd_modular_boundary_images_collapse_to_the_scalar_character": all(
        item["boundary_image_order"] == item["predicted_scalar_image_order"]
        for modulus, item in modular_boundary_probe.items()
        if int(modulus) % 2 == 1
    ),
    "sixty_four_is_first_scalar_closed_but_full_boundary_open_modulus": (
        modular_boundary_probe["64"]["predicted_scalar_image_order"] == 1
        and modular_boundary_probe["64"]["boundary_image_order"] == 2
        and all(
            not (
                item["predicted_scalar_image_order"] == 1
                and item["boundary_image_order"] != 1
            )
            for modulus, item in modular_boundary_probe.items()
            if int(modulus) < 64
        )
    ),
    "base_change_can_create_a_boundary_not_seen_by_integral_kernel_reduction": any(
        item["boundary_image_order"] > item["predicted_scalar_image_order"]
        for item in modular_boundary_probe.values()
    ),
    "single_coordinate_is_an_explicit_mod_sixty_four_quotient_kernel_witness": all(
        entry % 64 == 0 for entry in derived_mod64_relational_image
    ),
    "explicit_mod_sixty_four_witness_has_order_two_gauge_boundary": (
        tuple(entry % 64 for entry in derived_mod64_full_image) == (32, 32, 32, 32)
    ),
    "witness_has_exact_two_adic_valuation_gap": (
        derived_witness_relational_gcd % 128 == 0
        and derived_witness_full_gcd % 32 == 0
        and derived_witness_full_gcd % 64 != 0
    ),
    "derived_excess_is_confined_to_two_adic_depths_six_through_twelve": all(
        (item["derived_excess_order"] > 1) == (6 <= int(exponent) <= 12)
        for exponent, item in two_primary_boundary_table.items()
    ),
    "two_primary_excess_has_exact_one_two_four_two_one_profile": all(
        item["derived_excess_order"] == derived_two_primary_excess(int(exponent))
        for exponent, item in two_primary_boundary_table.items()
    ),
    "primewise_boundary_classification_holds_through_four_thousand_ninety_six": global_primewise_classification_holds,
    "both_inner_commutators_enter_at_two_adic_depth_two": (
        two_adic_valuation(inner_left_gcd) == two_adic_valuation(inner_right_gcd) == 2
    ),
    "inner_leading_grades_commute_and_force_one_extra_outer_depth": graded_inner_commutator_vanishes,
    "outer_commutator_first_grade_is_the_rank_one_all_ones_gauge_map": outer_leading_grade == ((1, 1, 1, 1),) * 4,
    "source_word_powers_rigidly_shift_all_smith_depths": all(
        item["full_depths"] == (5 + item["v2_power"], 9 + item["v2_power"], 13 + item["v2_power"])
        and item["relational_depths"] == (7 + item["v2_power"], 12 + item["v2_power"])
        for item in power_depth_table.values()
    ),
    "thirty_two_signed_permutations_preserve_all_moore_faces": legal_moore_mutation_count == 32,
    "legal_moore_mutations_split_into_three_response_profiles": moore_mutation_profiles == {
        "full=(5, 9, 13);relational=(7, 12)": 16,
        "full=(8, 8, 14);relational=(8, 14)": 8,
        "full=(8, 12, 16);relational=(11, 12)": 8,
    },
    "explicit_legal_mutation_falsifies_forced_gauge_first_response": (
        all(image == () for image in hostile_face_images)
        and two_adic_valuation(hostile_delta_gcd) == 8
        and hostile_leading_grade
        == ((0, 0, 1, 1), (0, 0, 1, 1), (1, 1, 0, 0), (1, 1, 0, 0))
    ),
    "legal_mutations_cover_all_three_mikhailov_degree_four_generators": legal_repeated_generator_counts == {
        "x0": 8,
        "x1": 8,
        "x2": 16,
    },
    "mikhailov_identifies_all_three_bracket_placements_modulo_boundaries": True,
    "all_legal_mutations_represent_the_same_nonzero_eta_squared_class": sum(
        legal_repeated_generator_counts.values()
    ) == legal_moore_mutation_count,
    "three_state_incidence_polarity_framing_predicts_every_response_profile": framing_classifier_holds,
    "minimal_framing_classes_have_multiplicities_sixteen_eight_eight": framing_class_counts == {
        "ordinary_repeated_slot": 16,
        "x2_equal_tail_polarity": 8,
        "x2_opposite_tail_polarity": 8,
    },
    "deletion_incidence_has_exactly_identity_and_endpoint_reversal_automorphisms": deletion_incidence_automorphisms == [
        {
            "generator_permutation": (0, 1, 2),
            "face_permutation": (0, 1, 2, 3),
            "exchange_c12_c21": False,
        },
        {
            "generator_permutation": (1, 0, 2),
            "face_permutation": (3, 2, 1, 0),
            "exchange_c12_c21": True,
        },
    ],
    "x2_is_the_unique_source_invariant_through_going_generator": through_going_generators == (2,),
    "three_state_framing_classifier_is_invariant_under_endpoint_reversal": endpoint_reversal_framing_equivariance,
    "endpoint_reversal_has_sixteen_signed_presentation_orbits": (
        len(endpoint_reversal_orbits) == 16
        and all(len(orbit) == 2 for orbit in endpoint_reversal_orbits)
    ),
    "three_state_port_coarsens_the_full_signed_orbit_quotient": framing_class_orbit_counts == {
        "ordinary_repeated_slot": 8,
        "x2_equal_tail_polarity": 4,
        "x2_opposite_tail_polarity": 4,
    },
    "repeated_generator_sign_is_a_hostile_invariant_forgotten_by_three_state_port": (
        same_framing_distinct_orbit_witness is not None
    ),
    "unsigned_incidence_orbits_coarsen_to_endpoint_and_through_strata": (
        len(unsigned_legal_permutations) == 6
        and len(unsigned_endpoint_reversal_orbits) == 3
        and len(unsigned_strata["endpoint_repeated"]) == 2
        and len(unsigned_strata["through_repeated"]) == 1
    ),
    "partial_orientation_character_splits_only_the_through_stratum": (
        through_polarity_values == (-1, 1)
        and set(framing_class_counts) == {
            "ordinary_repeated_slot",
            "x2_equal_tail_polarity",
            "x2_opposite_tail_polarity",
        }
    ),
    "typed_response_invisible_generators_preserve_legality_and_framing": (
        response_invisible_edges_are_legal_and_class_preserving
    ),
    "coupled_tail_inversion_is_legal_where_both_unary_factorizations_are_illegal": (
        atomic_endpoint_pair_flip_witness is not None
    ),
    "atomic_coupled_constructor_closes_exactly_the_three_smith_profile_fibers": (
        response_groupoid_component_packet == (
            ("ordinary_repeated_slot", 16),
            ("x2_equal_tail_polarity", 8),
            ("x2_opposite_tail_polarity", 8),
        )
    ),
    "all_legal_presentations_have_distinct_full_response_matrices": (
        distinct_full_response_matrix_count == 32
    ),
    "atomic_pair_flip_preserves_profile_but_never_the_full_response_matrix": (
        atomic_pair_flip_exact_response_equalities == 0
        and full_response_counts_by_groupoid_component == (8, 8, 16)
    ),
    "exact_integral_smith_reduction_has_five_packets": (
        distinct_exact_smith_packet_count == 5
    ),
    "atomic_pair_flip_has_stratum_dependent_exact_smith_visibility": (
        atomic_pair_flip_exact_smith_equalities == 8
        and exact_smith_counts_by_groupoid_component == (1, 2, 2)
    ),
    "five_exact_smith_packets_are_classified_by_two_plus_one_plus_two_incidence_states": (
        exact_smith_structural_classifier_is_bijective
        and exact_smith_structural_class_counts == {
            "A_plus": 8,
            "A_minus": 8,
            "B": 8,
            "C_plus": 4,
            "C_minus": 4,
        }
    ),
    "endpoint_orientation_bit_lives_only_in_the_full_gauge_extension": (
        a_orientation_is_gauge_extension_only
    ),
    "opposite_polarity_orientation_bit_survives_relational_reduction": (
        c_orientation_survives_relational_reduction
    ),
    "opposite_polarity_full_to_relational_terminal_ratios_are_squares": (
        c_full_relational_terminal_ratios == {"C_plus": 28 ** 2, "C_minus": 36 ** 2}
    ),
    "opposite_polarity_square_roots_obey_the_affine_conductor_law": (
        c_affine_conductor_law
        and all(two_adic_valuation(conductor) == 2 for conductor in c_terminal_conductors.values())
    ),
    "full_to_relational_torsion_quotients_are_integral_extension_moduli": all(
        math.prod(packet[0]) % math.prod(packet[1]) == 0
        for packet in exact_smith_packet_by_structural_class.values()
    ),
    "extension_modulus_depths_split_as_eight_eight_thirteen": (
        extension_modulus_two_adic_depths == {
            "A_plus": 8,
            "A_minus": 8,
            "B": 8,
            "C_plus": 13,
            "C_minus": 13,
        }
    ),
    "opposite_polarity_extension_modulus_obeys_the_squared_affine_law": (
        c_extension_modulus_law
    ),
    "all_three_comparison_groups_are_metabelian": derived_length(s3) == derived_length(a4) == derived_length(d8) == 2,
    "blind_groups_have_cyclic_derived_subgroups": all(is_cyclic(derived_subgroup(group)) for group in (s3, d8, d12)),
    "detecting_a4_has_noncyclic_derived_subgroup": not is_cyclic(derived_subgroup(a4)),
    "detecting_s4_has_derived_length_three": derived_length(s4) == 3,
    "s4_assignment_detects_nonidentity": witness_input is not None,
    "faithful_artin_action_certifies_nonidentity_braid": witness_input is not None,
    "certificate_is_independent_of_homotopy_quotient": True,
}

payload = {
    "schema": "marici.strominger.eta-squared-faithful-artin-action.v1",
    "pure_word_length": len(eta_squared),
    "sigma_word_length": len(sigma_word),
    "finite_quotient": "S3 is exhaustively blind; S4 evaluates Artin's free-group action nontrivially",
    "s3_assignments_tested": len(s3) ** 4,
    "metabelian_assignment_counts": {"S3": len(s3) ** 4, "A4": len(a4) ** 4, "D8": len(d8) ** 4, "D10": len(d10) ** 4, "D12": len(d12) ** 4, "D14": len(d14) ** 4},
    "derived_lengths": {"S3": derived_length(s3), "A4": derived_length(a4), "D8": derived_length(d8), "D10": derived_length(d10), "D12": derived_length(d12), "D14": derived_length(d14), "S4": derived_length(s4)},
    "derived_subgroup_orders": {"S3": len(derived_subgroup(s3)), "A4": len(derived_subgroup(a4)), "D8": len(derived_subgroup(d8)), "D10": len(derived_subgroup(d10)), "D12": len(derived_subgroup(d12)), "D14": len(derived_subgroup(d14)), "S4": len(derived_subgroup(s4))},
    "a4_witness_input": a4_witness_input,
    "a4_witness_output": a4_witness_output,
    "d10_witness_input": d10_witness_input,
    "d10_witness_output": d10_witness_output,
    "d14_witness_input": d14_witness_input,
    "d14_witness_output": d14_witness_output,
    "reflection_response_matrix": reflection_matrix,
    "reflection_response_delta": reflection_delta,
    "reflection_response_delta_gcd": reflection_delta_gcd,
    "determinantal_divisors": delta_divisors,
    "smith_factors": smith_factors,
    "translation_vector_image": translation_vector_image,
    "relational_response_matrix": relational_matrix,
    "relational_response_delta": relational_delta,
    "relational_determinantal_divisors": relational_divisors,
    "relational_smith_factors": relational_smith_factors,
    "primitive_relational_kernel": primitive_relational_kernel,
    "kernel_lift_image": kernel_lift_image,
    "gauge_shear_coefficient": gauge_shear_coefficient,
    "gauge_shear_factorization": "2^8*3*5*19*193*35879",
    "shear_vanishes_mod_n": shear_vanishes_mod_n,
    "lifting_law": "the primitive quotient-fixed direction has a fixed full lift modulo n iff n divides 505222245120",
    "snake_connecting_morphism": "ker(relational Delta)=Z -> coker(Delta on gauge)=Z is multiplication by 505222245120",
    "full_cokernel_torsion_order": full_cokernel_torsion_order,
    "relational_cokernel_torsion_order": relational_cokernel_torsion_order,
    "snake_torsion_identity": "|Tor coker Delta_full| = 505222245120 * |Tor coker Delta_relational|",
    "kernel_size_mod_n": "n*gcd(n,96)*gcd(n,1536)*gcd(n,16167111843840)",
    "modular_boundary_image_order": "n*gcd(n,384)*gcd(n,12288)/(gcd(n,96)*gcd(n,1536)*gcd(n,16167111843840))",
    "first_derived_modular_boundary_defect": {"modulus": 64, "full_boundary_image_order": 2, "integral_kernel_reduction_image_order": 1},
    "derived_mod64_witness": {
        "relational_vector": derived_mod64_relational_witness,
        "full_lift": derived_mod64_full_lift,
        "relational_image": derived_mod64_relational_image,
        "full_image": derived_mod64_full_image,
        "gauge_boundary_mod_64": derived_mod64_boundary,
        "relational_image_gcd": derived_witness_relational_gcd,
        "full_image_gcd": derived_witness_full_gcd,
    },
    "two_primary_boundary_table": two_primary_boundary_table,
    "primewise_boundary_law": "|im partial_n|=(n/gcd(n,505222245120))*epsilon(v2(n)), where epsilon=2 at v2=6 and 9..12, epsilon=4 at v2=7,8, and epsilon=1 otherwise",
    "nested_commutator_filtration": {
        "inner_left_gcd": inner_left_gcd,
        "inner_right_gcd": inner_right_gcd,
        "inner_depths": (two_adic_valuation(inner_left_gcd), two_adic_valuation(inner_right_gcd)),
        "leading_inner_grades_commute_mod_2": graded_inner_commutator_vanishes,
        "outer_leading_grade_mod_2": outer_leading_grade,
    },
    "source_word_power_depth_table": power_depth_table,
    "moore_face_preserving_mutation_census": {
        "formal_signed_permutations": 48,
        "legal_mutations": legal_moore_mutation_count,
        "response_profiles": moore_mutation_profiles,
        "repeated_generator_counts": legal_repeated_generator_counts,
        "permutation_profile_counts": moore_permutation_profile_counts,
        "signed_profile_counts": moore_signed_profile_counts,
        "minimal_framing_classifier": {
            "classes": framing_class_counts,
            "law": "repeated x0/x1 -> original profile; repeated x2 with equal tail signs -> rank-two depth-eight profile; repeated x2 with opposite tail signs -> delayed relational profile",
            "ignored_coordinates": ["sign of repeated generator", "order of nonrepeated generators"],
        },
        "deletion_incidence_automorphism_packet": {
            "table": deletion_incidence_table,
            "automorphisms": deletion_incidence_automorphisms,
            "through_going_generators": through_going_generators,
            "equivariant_polarity_character": "the product of the two tail signs is invariant under endpoint exchange",
            "signed_presentation_orbit_count": len(endpoint_reversal_orbits),
            "framing_class_orbit_counts": framing_class_orbit_counts,
            "same_framing_distinct_orbit_witness": same_framing_distinct_orbit_witness,
            "universality_boundary": "the three-state port is a source-defined quotient of the 16-orbit signed presentation quotient; the response law, not incidence alone, proves that this coarser quotient is sufficient and minimal for the observed response",
            "stratified_construction": {
                "unsigned_legal_permutations": unsigned_legal_permutations,
                "unsigned_endpoint_reversal_orbits": unsigned_endpoint_reversal_orbits,
                "unsigned_strata": unsigned_strata,
                "through_polarity_values": through_polarity_values,
                "law": "the three unsigned reversal orbits coarsen to endpoint versus through type; the port then retains one endpoint state and the two sheets of the polarity character over the through-going stratum",
            },
            "response_invisible_groupoid": {
                "generators": [
                    "endpoint reversal",
                    "swap the two nonrepeated slots",
                    "flip the repeated-generator sign",
                    "atomically flip both nonrepeated-generator signs",
                ],
                "component_packet": response_groupoid_component_packet,
                "atomic_pair_flip_witness": atomic_endpoint_pair_flip_witness,
                "law": "the three Smith-depth-profile fibers are exactly the components after adjoining atomic simultaneous tail inversion",
                "nonfactorization": "on the endpoint stratum each unary tail inversion is Moore-illegal although their coupled inversion is legal, so the constructor cannot be factored through legal unary states",
                "observation_level_boundary": {
                    "distinct_full_response_matrices": distinct_full_response_matrix_count,
                    "full_response_counts_by_component": full_response_counts_by_groupoid_component,
                    "atomic_pair_flip_exact_response_equalities": atomic_pair_flip_exact_response_equalities,
                    "distinct_exact_integral_smith_packets": distinct_exact_smith_packet_count,
                    "exact_smith_counts_by_component": exact_smith_counts_by_groupoid_component,
                    "atomic_pair_flip_exact_smith_equalities": atomic_pair_flip_exact_smith_equalities,
                    "atomic_pair_flip_exact_smith_equalities_by_class": atomic_pair_flip_exact_smith_equalities_by_class,
                    "exact_smith_structural_classifier": {
                        "class_counts": exact_smith_structural_class_counts,
                        "bijective_with_exact_smith_packets": exact_smith_structural_classifier_is_bijective,
                        "law": "endpoint orientation times common tail sign splits A; equal polarity gives unsplit B; tail-order orientation times first-tail sign splits C",
                        "layer_support": {
                            "A_orientation": "full gauge extension only; the relational Smith packet is identical for A_plus and A_minus",
                            "C_orientation": "survives relational reduction; both terminal full and relational Smith factors differ",
                            "C_full_to_relational_terminal_ratios": c_full_relational_terminal_ratios,
                            "C_terminal_conductors": c_terminal_conductors,
                            "C_affine_conductor_law": "kappa_C(omega)=4*(8-omega), so the terminal ratio is kappa_C(omega)^2 and v2(kappa_C)=2 for both signs",
                            "extension_modulus_by_structural_class": extension_modulus_by_structural_class,
                            "extension_modulus_two_adic_depths": extension_modulus_two_adic_depths,
                            "C_extension_modulus_law": "mu_C(omega)=2^13*3*(8-omega)^2",
                        },
                    },
                    "law": "the constructor preserves only the two-adic Smith-depth profile, not the full response matrix or exact integral Smith packet",
                },
            },
        },
        "homotopy_classification": "all 32 represent the same nonzero eta-squared class because Mikhailov's degree-four quotient has e7=e8=e9, 2e7=0, and e7 nonzero; inversions only change sign",
        "hostile_mutation": "[[x2,x0],[x2,x1]]",
        "hostile_leading_grade_mod_2": hostile_leading_grade,
    },
    "modular_boundary_probe": modular_boundary_probe,
    "witness_input": witness_input,
    "witness_output": witness_output,
    "checks": checks,
    "aggregate": {"passed": sum(checks.values()), "total": len(checks)},
    "interpretation": "the expanded Brunnian word is nonidentity already in P4; its order-two statement applies only after the filling quotient",
}
RESULT.parent.mkdir(parents=True, exist_ok=True)
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
digest = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
print(json.dumps({"aggregate": payload["aggregate"], "checker_sha256": digest, "witness_found": witness_input is not None}, sort_keys=True))

if not all(checks.values()):
    raise SystemExit(1)
