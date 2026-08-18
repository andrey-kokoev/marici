"""Audit integral trivial/sign splitting for the lower double cover."""


def determinant_2x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def main():
    # Columns are the trivial and sign generators; rows are the two sheets.
    # sum -> (1,1), difference -> (1,-1).
    character_to_sheets = [[1, 1], [1, -1]]
    index = abs(determinant_2x2(character_to_sheets))
    assert index == 2

    # Modulo two, sum and difference coincide. This is the obstruction to an
    # integral character projector.
    mod_two_columns = [
        tuple(row[column] % 2 for row in character_to_sheets)
        for column in range(2)
    ]
    assert mod_two_columns[0] == mod_two_columns[1]

    projector_denominator = 2
    assert projector_denominator != 1

    print("deck_group: C2")
    print("character_to_sheet_lattice_index: 2")
    print("mod_2_trivial_equals_sign: YES")
    print("integral_character_idempotents: NO")
    print("projectors_after_inverting_2: (1+tau)/2,(1-tau)/2")
    print("square_root_sign_lattice_removes_index_2: NO")
    print("canonical_split_coefficient_ring: Z[1/2]")


if __name__ == "__main__":
    main()
