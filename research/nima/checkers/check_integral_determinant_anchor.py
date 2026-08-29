def determinant_2x2(matrix: tuple[tuple[int, int], tuple[int, int]]) -> int:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


orientation_preserving = ((0, -1), (1, 0))
orientation_reversing = ((0, 1), (1, 0))
nonunimodular = ((2, 0), (0, 1))

assert determinant_2x2(orientation_preserving) == 1
assert determinant_2x2(orientation_reversing) == -1
assert determinant_2x2(nonunimodular) == 2

# Relation <2e1> is not saturated: e1 is absent but 2e1 is present.
primitive_relation = (1, 0)
unsaturated_relation = (2, 0)
assert primitive_relation != unsaturated_relation
assert tuple(2 * value for value in primitive_relation) == unsaturated_relation

# Both span the same rational line, while only the primitive generator yields
# a torsion-free rank-one quotient.
rational_direction_primitive = (1, 0)
rational_direction_unsaturated = (unsaturated_relation[0] // 2, unsaturated_relation[1])
assert rational_direction_primitive == rational_direction_unsaturated
unsaturated_quotient_torsion_order = 2
saturated_quotient_torsion_order = 1
assert unsaturated_quotient_torsion_order != saturated_quotient_torsion_order

print("determinant +1: preserves integral orientation")
print("determinant -1: reverses integral orientation")
print("same rational relation: different integral torsion and primitivity")
